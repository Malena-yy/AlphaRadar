# AlphaSAGE 核心算法解读

> - 速读卡：[AlphaSAGE](../cards/2025_AlphaSAGE.md)。
> - 论文：AlphaSAGE: Structure-Aware Alpha Mining via GFlowNets for Robust Exploration，ICLR 2026 conference paper。
> - 原文：[arXiv:2509.25055](https://arxiv.org/abs/2509.25055)
> - 分析范围：PDF 全文 28 页，覆盖正文第 1-5 节、Appendix A-F、Algorithm 1、Table 1-13、公式 (1)-(45)。
> - 源码依据：官方仓库 `README.md`、`train_gfn.py`、`run_adaptive_combination.py`、`src/alpha_gfn/`、`src/alphagen/data/`、`src/alphagen/models/alpha_pool.py`、`src/alphagen/utils/`、`src/alphagen_qlib/`。
> - 文档边界：本文解释论文算法与可直接从公式推出的性质；官方源码口径与论文不一致时单独标注，不改写论文结论。

## 1. 核心结论

AlphaSAGE 是面向公式化 Alpha 的结构感知生成框架。它不是直接训练一个资产组合策略，而是学习一个能够采样高质量、多样化公式 Alpha 的生成分布。

核心链路为：

```text
部分公式 AST 状态
        │
        ▼
RGCN 编码 AST 结构
        │
        ▼
GFlowNet forward policy 采样下一 token / SEP
        │
        ▼
完整合法公式 alpha
        │
        ▼
在历史截面数据上计算 alpha 输出
        │
        ▼
RIC + RSA + RNOV + entropy
        │
        ▼
Trajectory Balance 更新生成分布
        │
        ▼
高 reward、多样化 alpha pool
        │
        ▼
动态筛选与线性组合 Mega-Alpha
```

论文的三个核心创新是：

1. 用 RGCN 编码公式 AST，而不是只用 RPN / token 序列。
2. 用 GFlowNet 学习 `P_theta(alpha) proportional to R(alpha)` 的采样分布，目标是覆盖多个高 reward 模式，而不是像普通 RL 那样只逼近单一最优公式。
3. 用多维 reward 缓解稀疏终端反馈：预测能力 `R_IC`、结构-行为对齐 `R_SA`、新颖性 `R_NOV`，再加 action-level entropy regularization。

训练结束后，论文使用类似 AlphaForge 的动态重筛和线性回归组合方式，将候选 alpha library 转成时间变化的 Mega-Alpha。

### 针对的问题

对应 README 中的 P1-P10，本文涉及的机制如下；实验证据见第 11 节，消融见第 11.4 节。

- **P4 学习信号稀疏、延迟且不可微**：不最大化期望奖励，而是用 Trajectory Balance 让完整公式的采样概率正比于奖励（第 6 节）；奖励由预测性能、结构对齐和新颖性三项组成（第 5 节）。
- **P7 因子同质化与冗余**：新颖性奖励惩罚与已有高质量 alpha 高相关的候选（第 5.3 节），配合按奖励成比例的采样覆盖多个高奖励模式；附录对多样性作用的证明见第 12 节。

## 2. 问题定义

论文将单日市场输入写为：

$$
X_d \in \mathbb R^{N \times M},
$$

其中 `N` 是股票数，`M` 是特征数。一个公式 Alpha 是函数：

$$
\alpha: X_d \mapsto z_d,\qquad z_d=\alpha(X_d)\in\mathbb R^N.
$$

`z_d` 是该 alpha 在当天所有股票上的横截面预测信号，`y_d in R^N` 是未来收益或趋势标签。

论文指出已有 RL 公式挖掘常把目标写成“向当前池 `F` 加入一个 alpha 后，组合模型 IC 的边际提升”：

$$
R(\alpha|F)=IC(c(X;F\cup\{\alpha\}))-IC(c(X;F)).
$$

这个目标的问题是：

- reward 会随 `F` 更新而变化，MDP 非平稳；
- 搜索沿单一路径贪心构造组合，容易模式坍缩；
- 不直接学习全局高质量公式分布。

AlphaSAGE 改写为学习全局生成分布：

$$
P_\theta(\alpha)\propto R(\alpha),\qquad \alpha\in \mathcal X.
$$

这意味着生成器应按 reward 大小采样一批不同的高质量 alpha，而不是只返回一个最大 reward 公式。

## 3. Alpha 生成：状态、动作与 Early Stop

### 3.1 状态与动作

AlphaSAGE 把公式生成建模为 DAG 上的轨迹：

$$
\tau=(s_0\rightarrow s_1\rightarrow\cdots\rightarrow s_n=\alpha).
$$

论文定义：

| 对象 | 含义 |
| --- | --- |
| `s_0` | 空公式状态 |
| `s_t` | 部分构造的 AST |
| terminal state | 完整、合法的 AST，即一个可评价公式 alpha |
| action | 向当前 partial AST 的 open leaf 加入 operator、feature 或其它 token |
| invalid action mask | 根据当前状态屏蔽语法非法动作 |
| SEP | 结束生成并尝试把当前状态转为完整公式 |

只有完整合法轨迹才进入 reward 计算和 TB loss。

### 3.2 Early Stop 机制

为避免公式无限增长或达到最大长度后被强制截断为非法状态，论文引入 early stop。若当前状态已经构成合法表达式，则停止概率为：

$$
p=\frac{Len(s_t)}{MaxLen}.
\tag{4}
$$

因此公式越长，越倾向于结束。这个机制的直观作用是：

- 短公式仍有机会继续扩展；
- 长公式逐渐提高停止概率；
- `MaxLen` 既控制搜索空间，也控制 early stop 阈值。

需要注意一个伪代码细节：Algorithm 1 第 6-9 行写作 `if rand() >= p_es(s_t) then a_t <- SEP else sample action`。若 `rand()` 是 `[0,1]` 均匀随机数，这会让停止概率变为 `1-p`，与公式 (4) 的“停止概率为 p”相反。论文没有解释这个符号差异，复现时不能同时机械接受二者。

## 4. RGCN 结构编码

### 4.1 为什么不用纯序列

论文认为 RPN / token 序列会弱化公式的层次结构。例如二元运算、时序窗口、特征输入之间的关系并不是普通相邻 token 关系。AlphaSAGE 先将公式解析为 AST：

$$
T_\alpha=(V_\alpha,E_\alpha),
$$

其中节点是 operator、feature 或时间窗口等元素，边表示计算依赖。

### 4.2 六类关系

Appendix C.2 给出 RGCN 的六类关系：

| 编号 | 关系 |
| --- | --- |
| 1 | Unary operator 与 operand |
| 2 | Commutative operator 与 operands |
| 3 | Non-commutative operator 与 left operand |
| 4 | Non-commutative operator 与 right operand |
| 5 | Rolling operator 与 feature operand |
| 6 | Rolling operator 与 time operand |

这个关系集合的重要性在于：`Sub(a,b)` 与 `Sub(b,a)` 的左右边不同，`TsMean(close,20)` 的 feature 和 window 也不是同类输入。

### 4.3 RGCN 更新与图级 readout

RGCN 第 `l` 层的节点更新为：

$$
h_v^{(l)}
=
ReLU
\left(
\sum_{r\in R}
\sum_{u\in N_r(v)}
\frac{1}{c_{v,r}}W_r^{(l)}h_u^{(l-1)}
+
W_0^{(l)}h_v^{(l-1)}
\right).
\tag{7}
$$

其中：

- `R` 是关系类型集合；
- `N_r(v)` 是通过关系 `r` 连接到 `v` 的邻居；
- `c_{v,r}` 是归一化常数，论文举例为 `|N_r(v)|`；
- `W_r` 是关系特定参数；
- `W_0` 是 self-loop 参数。

公式 embedding 使用 max pooling：

$$
e_\alpha=
MaxPooling\left(\{h_v^{(L)}\}_{v\in V_\alpha}\right).
\tag{8}
$$

论文主配置使用 2 层 RGCN，hidden dimension 为 128。

## 5. 多维 Reward

AlphaSAGE 的完整 reward 是：

$$
R(\alpha,T)=R_{IC}(\alpha)+\lambda(T)R_{SA}(\alpha)+\eta(T)R_{NOV}(\alpha).
\tag{14}
$$

三个项分别对应预测能力、结构-行为对齐和新颖性。

### 5.1 Terminal Performance Reward：`R_IC`

论文将 `R_IC` 定义为 alpha 输出与未来标签的横截面 IC：

$$
R_{IC}(\alpha)=IC(\alpha,y)
=
E_d
\left[
\frac{Cov(\alpha(X_d),y_d)}
{\sqrt{Var(\alpha(X_d))\cdot Var(y_d)}}
\right].
\tag{12}
$$

Appendix D.1 又说明报告 IC / RankIC 时使用绝对值，因为公式方向可以翻转。这里存在一个实现上必须明确的边界：

- 主文 Eq. 12 写的是 signed IC；
- Appendix 的 reporting convention 使用 absolute IC；
- TB loss 中有 `log R`，所以实际训练 reward 必须非负并处理零值。

论文没有在正文中给出如何对负 IC、零方差或全缺失截面做数值保护。

### 5.2 Structure-Aware Reward：`R_SA`

`R_SA` 的目标是让“结构 embedding 相近”的公式在历史行为上也相近。

论文令 `Z_i in R^{D x N}` 表示 alpha `i` 在 `D` 个交易日、`N` 只股票上的横截面标准化输出，`Z_i(d)` 是第 `d` 天的横截面向量。行为距离为：

$$
d_{behav}(\alpha_i,\alpha_j)
=
\frac{1}{D}\sum_{d=1}^D
\left(Z_i(d)-Z_j(d)\right)^2.
\tag{9}
$$

从形状看，右侧需要进一步聚合股票维度才能得到标量距离；论文没有写明是横截面均值、求和还是其它归约。复现时必须显式选择。

然后在 embedding 空间找 `K` 个最近邻：

$$
w_{ij}
=
\frac{
\exp(-\|e_{\alpha_i}-e_{\alpha_j}\|^2)
}{
\sum_{k\in N_K(\alpha_i)}
\exp(-\|e_{\alpha_i}-e_{\alpha_k}\|^2)
},
\qquad j\in N_K(\alpha_i).
\tag{10}
$$

最终：

$$
R_{SA}(\alpha_i)
=
\exp
\left(
-
\sum_{j\in N_K(\alpha_i)}
w_{ij}\cdot d_{behav}(\alpha_i,\alpha_j)
\right).
\tag{11}
$$

因此：

- embedding 近邻行为越相似，`R_SA` 越接近 1；
- embedding 近邻行为差异越大，`R_SA` 越小；
- 该项不是直接最大化 IC，而是训练结构 embedding 与输出行为一致。

### 5.3 Novelty Reward：`R_NOV`

新颖性 reward 用已发现的高质量 alpha library `F_known` 作为参照：

$$
R_{NOV}(\alpha)
=
1-
\max_{\alpha'\in F_{known}}
|IC(\alpha,\alpha')|.
\tag{13}
$$

它惩罚与已有高质量 alpha 高相关的候选。这里的 IC 是 alpha 与 alpha 之间的横截面相关，而不是 alpha 与收益标签之间的相关。

`R_NOV` 的关键作用是避免 alpha pool 被一批近似重复的公式占满。

### 5.4 Reward 权重调度

论文使用随训练进度衰减的权重：

$$
\lambda(T)=
\left(1-\frac{T}{T_{anneal}}\right)\lambda_{max},
$$

$$
\eta(T)=
\left(1-\frac{t}{T_{anneal}}\right)\eta_{max}.
$$

正文对第一个权重用 `T`，第二个用 `t`，符号不完全一致。语义上二者都是训练进度调度：前期更多鼓励结构学习和 novelty，后期降低辅助 reward 权重，让预测表现占主导。

Appendix E.3 对比 constant、linear decay、exponential decay，报告 linear decay 最好，exponential decay 接近，constant 较弱。

## 6. GFlowNet 训练目标

GFlowNet 的目标是让完整公式的采样概率与 reward 成比例：

$$
P(\alpha)
=
\sum_{\tau:s_n=\alpha}P_F(\tau)
=
\frac{R(\alpha)}{Z},
\tag{5}
$$

其中：

$$
Z=\sum_{\alpha'\in\mathcal X}R(\alpha')
$$

是 partition function，对应可学习总流量。

论文采用 Trajectory Balance loss：

$$
L_{TB}(\tau)=
\left(
\log Z_\theta
+
\sum_{t=1}^{n}\log P_F(s_t|s_{t-1};\theta)
-
\log R(s_n)
-
\sum_{t=1}^{n}\log P_B(s_{t-1}|s_t;\theta)
\right)^2.
\tag{6}
$$

其中：

- `P_F` 是 forward policy；
- `P_B` 是 backward policy；
- `Z_theta` 是可学习标量；
- loss 在完整轨迹上计算。

论文正文提到 forward / backward policies，但 Algorithm 1 主要展示 forward sampling 和 terminal reward 计算，没有详细说明 backward policy 的参数化、采样或固定方式。

## 7. Entropy Regularization

论文为避免 premature convergence，在 action 级加入 entropy bonus：

$$
L_{ENT}
=
-
E_{\tau\sim P_F(\tau;\theta)}
\left[
\sum_{t=0}^{n-1}
H(\pi_\theta(\cdot|s_t))
\right].
\tag{15}
$$

因为 `L_ENT` 带负号，最小化时加入正系数会鼓励更高 entropy。

最终目标写作：

$$
L_{final}
=
E_{\tau\sim P_F(\tau;\theta)}[L_{TB}(\tau)]
+\beta L_{ENT}.
\tag{16}
$$

Algorithm 1 中，对一条 terminal trajectory：

1. 用 `B_prob` 保存各步 action distribution；
2. 结束时计算 `R_IC`、`R_NOV`、`R_SA`；
3. 组合总 reward；
4. 若通过阈值则加入 alpha pool，并保存 terminal embedding；
5. 用 `B_prob` 和 reward 计算 TB loss；
6. 加 entropy regularizer；
7. 更新 GFlowNet 参数；
8. 重置状态和概率 buffer。

论文没有给出 `PassThreshold(R)` 的具体阈值或 pool 替换规则。

## 8. 公式搜索空间

Appendix C.3 的 Table 3 给出原始特征和可用算子。

基础特征：

```text
Open, Close, High, Low, Vwap, Volume
```

算子按类别包括：

| 类别 | 算子 |
| --- | --- |
| Unary | Abs, Slog1p, Inv, Sign, Log |
| Cross-sectional | Rank |
| Binary | Add, Sub, Mul, Div, Pow, Greater, Less |
| Time-series unary | Ref, TsMean, TsSum, TsStd, TsIr, TsMinMaxDiff, TsMaxDiff, TsMinDiff, TsVar, TsSkew, TsKurt, TsMax, TsMin, TsMed, TsMad, TsRank, TsDelta, TsDiv, TsPctChange, TsWMA, TsEMA |
| Time-series binary | TsCov, TsCorr |

重要语义：

- `Greater` / `Less` 是逐元素 0/1 比较；
- `Ref` 是 `d` 日前取值；
- `TsDiv` 是当前值除以 `d` 日前值；
- `TsCov` / `TsCorr` 是两个输入在过去 `d` 日窗口上的滚动协方差 / Pearson 相关；
- `epsilon` 只用于数值稳定。

论文没有在 Table 3 中给出 window 候选集合，但 Table 4 指定 `Max Length = 20`。

## 9. Alpha Combination 与组合评价

论文第 3.5 节说明组合阶段沿用 AlphaForge 思路：

- 不固定静态 alpha 集；
- 在每个 period 根据近期有效性动态重筛 alpha；
- 使用简单线性回归重新赋权；
- 得到时间变化的 Mega-Alpha。

Appendix B.1 给出线性组合的通用形式：

$$
s_{i,t}
=
\sum_{k=1}^{K}w_k z^{(k)}_{i,t}.
\tag{17}
$$

同时列出一个带 L2、L1、权重和稀疏约束的正则化目标：

$$
\min_w
\sum_t
\|y_{t+\Delta}-Z_tw\|_2^2
+\lambda_2\|w\|_2^2
+\lambda_1\|w\|_1
$$

with constraints：

$$
\mathbf 1^\top w=1,\qquad \|w\|_0\le s.
\tag{18}
$$

但论文没有明确这就是实验中动态组合的完整实现，也没有给出 rolling window、回归目标、候选筛选阈值、换仓频率、缺失值处理或交易成本细节。复现论文组合效果时必须单独确认这些实现口径。

## 10. 评价指标与回测口径

Appendix D.1 定义了两类指标：

| 类型 | 指标 |
| --- | --- |
| Correlation metrics | IC, ICIR, RankIC, RankICIR |
| Portfolio metrics | Annualized Return, Maximum Drawdown, Sharpe Ratio |

论文表格中有时用 `RIC` 表示 RankIC，用 `RICIR` 表示 RankICIR。不要把这里的 `RIC` 与 reward 项 `R_IC` 混淆。

关键定义：

$$
\rho_d
=
\frac{
Cov(\alpha(X_d),y_d)
}{
\sqrt{Var(\alpha(X_d))Var(y_d)}
}.
\tag{27}
$$

$$
ICIR=
\frac{E_d[\rho_d]}{\sqrt{Var_d(\rho_d)}}.
\tag{29}
$$

RankIC 用 alpha 和 label 的横截面 rank 后再计算 Pearson correlation。

组合指标：

$$
AR=K\cdot E_d[R_d],
\tag{32}
$$

$$
MDD
=
-
\max_t
\left(
1-\frac{W_t}{\max_{u\le t}W_u}
\right),
\tag{33}
$$

$$
SR=
\frac{
\sqrt K E_d[R_d-r_{f,d}]
}{
\sqrt{Var_d(R_d-r_{f,d})}
}.
\tag{34}
$$

论文设置 `r_f = 0`。报告 convention 说明 IC / RankIC 使用绝对值，因为 alpha 方向可以反转。

回测持仓规则：

- 中国市场：Appendix D.1 明确写 CSI300/CSI500 每日买入 top 20% 股票，持有 20 日，只做多。正文和 Table 1 同时报告 CSI1000，但 Appendix 对 CSI1000 的组合规则没有单独展开。
- S&P500：每日买入 top 10%，卖空 bottom 10%，20 日后平仓，是 long-short 组合。

## 11. 实验设置与主要证据

### 11.1 数据划分

论文使用中国市场 CSI300、CSI500、CSI1000，以及美国市场 S&P500。

| 市场 | Train | Validation | Test |
| --- | --- | --- | --- |
| 中国市场 | 2010-01-01 至 2020-12-31 | 2021-01-01 至 2021-12-31 | 2022-01-01 至 2024-12-31 |
| S&P500 | 2010-01-01 至 2016-12-31 | 2017-01-01 至 2017-12-31 | 2018-01-01 至 2020-12-31 |

论文脚注说明美国市场数据因数据源限制截至 2020-12-31。

### 11.2 AlphaSAGE 超参数

Appendix D.2 Table 4 给出主配置：

| 参数 | 值 |
| --- | ---: |
| Max Length | 20 |
| Hidden Dim | 128 |
| Encoder Layer | 2 |
| Entropy Coef | 0.01 |
| Learning Rate | 0.0001 |
| SA Weight | 1.0 |
| NOV Weight | 0.3 |
| Pool Capacity | 50 |
| Episodes | 10000 / 20000 |

`10000/20000` 未在表内解释对应哪个市场或哪个实验设置。

### 11.3 Overall Performance

Table 1 报告 AlphaSAGE 在 CSI300、CSI500、CSI1000、S&P500 上整体优于多数 baseline，尤其在 ICIR、RankICIR 和 portfolio metrics 上有明显优势。

阅读时需要注意一个细节：正文称 AlphaSAGE 在所有 correlation metrics 上排名第一，但 Table 1 中 CSI1000 的 RankIC / RankICIR 有其它方法数值不低于 AlphaSAGE。写实验结论时应以表格逐项核对，不宜概括成“所有市场所有指标无例外第一”。

### 11.4 Ablation Study

Table 2 在 CSI300 上逐步加入组件：

| 配置 | 核心含义 | 结果趋势 |
| --- | --- | --- |
| Plain GFlowNet | 无 ES、GNN、SA、NOV、ENT | 基础结果较弱 |
| + ES | 只有 early stop | 结果反而更差，说明 ES 需要更强 encoder 配合 |
| + GNN | 换成结构 encoder | 最大单项提升 |
| + SA | 加结构-行为 reward | 改善排序稳定性和回撤 |
| + NOV | 加 novelty | 降低冗余，提升信号和 tradability |
| + ENT | 加 entropy | 最优整体结果 |

Table 10 又对比 RL / GFlowNet 与有无 proposed components：没有结构组件时 GFlowNet 甚至弱于 RL；加入 RGCN + composite reward 后 GFlowNet 最好。这说明论文贡献不是“只换成 GFlowNet”，而是 GFlowNet 与结构感知 reward/encoder 的组合。

### 11.5 Sensitivity 与 Scalability

Appendix E 给出若干实用结论：

- Training steps：GFlowNet 比 PPO 更快达到较高 plateau，振荡更小。
- Candidate pool size：小到中等容量提升很快，之后收益趋于饱和。
- MaxLen：`20` 最优；过短限制表达能力，过长引入噪声并增加优化难度。
- Encoder layers：2 层最好，3/4 层略弱，论文解释为可能有 over-smoothing 和优化难度。
- Hidden dim：128 最好，64 欠拟合，256 无明显收益且略伤 OOS。
- Reward schedule：linear decay 最好，exponential decay 接近，constant 较弱。
- Encoder architecture：RGCN 优于同等预算下的 Transformer sequence encoder。
- Runtime：论文报告 AlphaSAGE 在 CSI300/CSI500/S&P500/CSI1000 上训练耗时低于 AlphaGen、AlphaQCM、AlphaForge；主耗时仍来自候选公式在历史面板上的求值。

## 12. Diversity 证明的作用

Appendix F 不是 GFlowNet 正确性证明，而是解释“低相关 alpha 为什么让线性组合更稳定”。

设标准化 alpha 矩阵：

$$
F=[\alpha_1,\ldots,\alpha_N]\in\mathbb R^{T\times N},
$$

$$
\Sigma=\frac{1}{T}F^\top F,\qquad
g=\frac{1}{T}F^\top y.
\tag{35}
$$

OLS 估计：

$$
\hat\beta=\Sigma^{-1}g.
$$

若噪声方差为 `sigma^2`，则：

$$
Var(\hat\beta)=\frac{\sigma^2}{T}\Sigma^{-1},
$$

$$
tr Var(\hat\beta)
=
\frac{\sigma^2}{T}
\sum_{i=1}^{N}\frac{1}{\lambda_i}.
\tag{36}
$$

当 alpha 之间高度相关时，`Sigma` 的小特征值变小，`Sigma^{-1}` 放大估计方差。两 alpha 情况下：

$$
\Sigma=
\begin{bmatrix}
1 & \rho \\
\rho & 1
\end{bmatrix},
\qquad
\kappa_2(\Sigma)=\frac{1+\rho}{1-\rho}.
\tag{40}
$$

当 `rho -> 1`，方差和条件数都会爆炸。等相关矩阵中，off-diagonal correlation `rho` 会通过 `(N-1)/(1-rho)` 项放大总方差。

Corollary F.2 说明 ridge penalty 可以降低方差：

$$
tr Var(\hat\beta_\lambda)
=
\frac{\sigma^2}{T}
\sum_{i=1}^{N}
\frac{1}{\lambda_i+\lambda}.
\tag{45}
$$

但论文强调，显式提升 alpha diversity 是直接改善谱性质，ridge 只是用 shrinkage 代理控制方差。这为 `R_NOV` 和低 mutual correlation 目标提供理论动机。

## 13. 论文未披露或存在歧义的复现细节：官方源码补全

本节只记录官方源码能确认的实现口径。若源码与论文公式或文字不一致，以下写为“官方源码口径”或“源码差异”，不把它改写成论文原文结论。

### 13.1 生成与语法

官方源码没有显式维护“open leaf 遍历顺序”，而是用 RPN 前缀和栈式 `ExpressionBuilder` 构造表达式：

- action 列表顺序为 `BEG`、全部 operator、全部 feature、全部 time window、全部 constant、`SEP`；`BEG` 只作为初始状态 token，不在 forward mask 中开放采样。
- 状态是长度为 `MAX_EXPR_LENGTH=20` 的整数向量；初始状态为 `BEG` 加 padding `-1`，sink state 是全 `SEP` token。
- 普通 action 被采样后追加到第一个 padding 位置；采样 `SEP` 时直接转入 sink state。
- 表达式构造按 RPN 栈执行：operator 从栈顶弹出所需参数，反转后构造成 AST；最终栈中只有一个 `is_featured=True` 的表达式时才是合法 terminal。
- 单个 feature 已满足 terminal 条件；单个 constant 不满足，因为它不是 `featured` 表达式。

官方源码的 action legality 规则为：

| action 类型 | 官方源码合法条件 |
| --- | --- |
| Unary operator | 栈内参数数足够，且栈顶表达式 `is_featured=True`。 |
| Binary operator | 栈内参数数足够，左右两侧至少一侧 `is_featured=True`，且两侧都不是 `DeltaTime`。 |
| Rolling operator | 栈顶是 `DeltaTime`，前一个元素 `is_featured=True`。 |
| Pair rolling operator | 栈顶是 `DeltaTime`，前两个元素都 `is_featured=True`。 |
| DeltaTime | 栈非空，且栈顶 `is_featured=True`。 |
| Constant | 栈为空，或栈顶 `is_featured=True`。 |
| Feature | 只禁止紧跟在 `DeltaTime` 后面。 |
| SEP | 若长度未满，只有当前 builder 已合法才开放；若长度已满，源码会开放 SEP。 |

这补全了论文没有展开的 invalid action mask。对应地，源码没有单独实现 `PassThreshold(R)`；pool admission 由相关性门槛、容量和候选 IC 排名决定。

Early stop 的源码实现也不是直接按 Eq. 4 抽样 `SEP`。当当前状态已合法且 `SEP` 开放时，源码计算：

$$
p_{drop}=\text{mask\_dropout\_prob}\cdot\frac{Len(s_t)}{MaxLen}.
$$

若随机触发该事件，则把所有非 `SEP` 的合法 action mask 掉，从而强制结束；否则 `SEP` 只是合法 action 之一，仍由 forward policy 采样。官方 README 的主命令使用 `mask_dropout_prob=1.0`，而 argparse 默认值是 `0.5`。

还需要注意一个源码边界：满长状态只额外开放 `SEP`，但并不会主动关闭此前根据栈规则判定为合法的普通 action；若普通 action 在满长时被采样，`step()` 因没有 padding 位置而不会写入新 token。这与论文“达到 MaxLen 后避免非法强制截断”的叙述并不完全一致。

### 13.2 GFlowNet

官方源码使用外部 `gfn` 包的 `Sampler`、`DiscretePolicyEstimator` 和 `TBGFlowNet`，再用 `EntropyTBGFlowNet` 加 entropy 项：

- forward policy 为 `SequenceEncoder + pf_head`，输出维度是环境 action 数。
- backward policy 为 `SequenceEncoder + pb_head`，输出维度是 `n_actions - 1`，即不预测 exit action。
- 环境类中 `backward_step()` 未实现；TB 中 backward log-prob 的具体状态回溯由外部 `gfn` 包处理，官方仓库自身没有展开。
- 每个 episode 采样 `n_trajectories=1`；`update_freq` 不是并行采样 batch，而是把多条单轨迹 loss 累积后再做一次 optimizer step。
- 训练尾部若不足一个 `update_freq`，官方训练循环没有显式 flush pending loss。
- `save_estimator_outputs = entropy_coef > 0`；entropy 直接使用 sampler 保存的 forward estimator logits。

源码中的 entropy loss 为：

$$
L=(scores+\log Z)^2_{mean}-\text{entropy\_coef}\cdot H_{trajectory}.
$$

这里的 `scores` 来自父类 `TBGFlowNet`，包含 forward log-prob、backward log-prob 与 reward 的 TB 项；`entropy_temperature` 只用于 entropy 计算中的 logits 缩放，不改变 forward policy 的采样分布。

`log R` 的数值保护在环境 reward 中完成：若表达式非法、越界或 reward 计算为 0，最终返回值仍取：

$$
\max(R,\exp(-10)).
$$

因此 TB loss 总能取到正 reward。`R_IC` 在源码中使用 `abs(IC)`，这也解释了 signed IC 为负时如何进入训练 reward。

Reward 权重调度方面，官方源码把论文中的 `SA` 称为 `ssl_weight`，把 novelty 称为 `nov_weight`，并用 PyTorch scheduler 做 `linear`、`exponential` 或 `polynomial` 衰减。README 主命令使用 `ssl_weight=1.0`、`nov_weight=0.3`、`weight_decay_type=linear`、`final_weight_ratio=0.0`、`n_episodes=10000`；argparse 默认值则是 `ssl_weight=0.5`、`nov_weight=0.5`、`n_episodes=1000`。

### 13.3 RGCN 与 RSA

官方源码的 `SequenceEncoder` 支持 `transformer`、`lstm`、`gnn` 三种 encoder；README 主命令使用 `encoder_type=gnn`，但 argparse 默认值是 `lstm`。

GNN 模式的图构建口径为：

- 节点初始特征来自 action id 的共享 `nn.Embedding`。
- padding `-1` 会被去掉，但 `BEG` 会作为一个真实节点进入图；在完整 RPN 表达式中它通常是孤立节点。
- 边方向为 child -> operator。
- 六类 relation 的源码编号为：`0` unary operand、`1` commutative operand、`2` non-commutative left operand、`3` non-commutative right operand、`4` rolling feature operand、`5` rolling time operand。
- 非交换二元算子的左右关系由 RPN pop 顺序恢复：第一次 pop 是右操作数，第二次 pop 是左操作数。
- rolling 与 pair rolling 中，`DeltaTime` 归为 time relation，其它输入统一归为 feature relation。

论文 Eq. 8 明确写 `MaxPooling`，但官方源码实际调用 `global_mean_pool`。因此，“RGCN 使用 max pooling”是论文结论；“官方实现使用 mean pooling，并且 BEG 节点参与 pooling”是源码补全出的差异。

官方源码没有对交换表达式做 canonicalization。`Add(a,b)` 与 `Add(b,a)` 是否被视为同一结构，主要由生成顺序、字符串和相关性准入间接处理，而不是 AST 规范化处理。

`R_SA` 的源码实现口径为：

- 默认 `ssl_k=3`、`ssl_tau=0.1`。
- 候选 embedding 与 pool 中已存 embedding 计算 L2 距离，距离小于 `1e-6` 的对象被当作 self-like embedding 排除。
- similarity weight 为 `softmax(-dist^2 / ssl_tau)`。
- 行为距离先使用日度标准化后的因子值，计算 `(query_value - neighbor_value)^2`，再按股票维度均值、按日期均值，得到标量 MSE。
- `R_SA = exp(-weighted_consistency_loss)`。
- pool size 小于等于 1、没有 embedding 或没有邻居时，`R_SA` 返回 0。

这里补全了论文 Eq. 9 未写明的股票维度归约方式：官方源码采用“先日内股票均值，再跨日均值”。但源码的日度标准化会把 NaN 填 0，因此这个行为距离不是严格的 pairwise-finite MSE。

另一个实现细节是：环境在 reward 计算中用 `torch.no_grad()` 生成 terminal embedding；embedding 作为 pool 状态保存，源码没有在 encoder 参数更新后刷新既有 pool embedding。

### 13.4 数据、标签与评价

官方训练脚本中的标签为：

$$
y_t=\frac{close_{t+20}}{close_t}-1,
$$

对应代码表达式 `Ref(close, -20) / close - 1`。`StockData` 默认读取 qlib 字段 `open, close, high, low, volume, vwap`，默认 `max_backtrack_days=100`、`max_future_days=30`；日频 raw 模式下价格字段会乘复权因子、volume 会按复权因子和缩放项调整，但 GFlowNet 训练脚本没有打开 raw 模式。

官方 `train_gfn.py` 的日期在源码中硬编码为：

- train data：`2010-01-01` 至 `2016-12-31`；
- logger test data：`2018-01-01` 至 `2020-12-31`。

这与论文表中中国市场 `2010-2020 / 2021 / 2022-2024` 的划分不完全一致。官方 adaptive combination 脚本则通过 `train_end_year` 推导验证和测试区间；默认 `train_end_year=2020` 时，validation 是 2021 年，test 是 2022-2024 年，更接近论文中国市场划分。

IC / RankIC 数值处理口径为：

- 因子和 target 先按日做横截面标准化；
- 标准化中的 NaN 在输出中填 0；
- Pearson 相关按日计算后，NaN 相关再填 0；
- 零方差截面通过把过小 std product 置为 1 避免除零；
- 源码没有显式最小横截面样本数门槛。

官方 `AlphaPoolGFN` 的 reward 与 pool admission 口径为：

- `R_IC = abs(mean_daily_Pearson_IC)`。
- mutual IC 先逐 pool 因子计算 mean daily Pearson，再取绝对值。
- `R_NOV = 1 - max(abs(mutual_IC))`；空池时为 1。
- 默认 pool 相关性准入门槛为 `ic_mut_threshold=0.3`。
- pool 未满时，候选只有在最大绝对 mutual IC 不超过 0.3 时才入池。
- pool 已满时，候选还必须 `abs(IC)` 高于当前池内最低 `single_ic`，才会先加入再弹出最低 `single_ic` 的因子。
- 成功评价但未通过准入的候选仍可能把 `abs(IC)` 和 novelty 作为训练 reward 返回；无法评价或强相关到 `_calc_ics` 早停的候选返回 0 类 reward，再由环境的 `exp(-10)` 下限进入 TB。

官方 adaptive combination 脚本补全了论文第 3.5 节没有写明的组合细节：

- 组合标签同样默认为 `Ref(close, -label_days) / close - 1`，`label_days=20`。
- 每个预测日只使用 `cur - (label_days + 1)` 之前的历史指标，源码注释认为这是为了避免 look-ahead bias。
- 候选筛选使用历史 `abs(RIC) > threshold_ric` 且 `abs(RICIR) > threshold_ricir`，默认阈值分别是 `0.015` 和 `0.15`。
- 若没有因子过阈值，回退为按 `abs(RICIR)` 选 top 1。
- 每日最多取 `n_factors` 个候选；README 示例为 20，argparse 默认值为 10。
- 回归样本把历史日期和股票截面展平，只按 target finite 过滤样本。
- 预测前会对当日 factor 暴露 `nan_to_num`，并尝试用 SVD/QR 启发式删除线性相关列和行。
- 线性模型使用 `torch.linalg.lstsq`，并显式加入截距项；`ridge_alpha`、`corr_threshold`、`use_vif` 等参数在主路径中没有实际进入回归目标。
- `window='inf'` 时使用扩展窗口；有限 window 时使用滚动历史窗口。

组合评价中的 portfolio return 口径也由代码补全：`batch_ret` 每日取 factor 值最高的 top 20% 股票，计算其平均未来收益；源码同时计算了 bottom index 但没有用于 long-short 收益。`get_tensor_metrics()` 又把日收益除以 `label_days`，并用 `mean(ret_s) * len(ret_s) / 3` 作为 `ret`，MDD 使用 `1 + cumsum(ret)` 路径。以上是官方源码评价实现，不是论文 Appendix D.1 中全部市场 portfolio protocol 的完整可移植定义。

### 13.5 搜索空间、超参与 checkpoint

官方源码将 Table 3 未列出的 window 和 constant 补齐为：

```text
DELTA_TIMES = [10, 20, 30, 40, 50]
CONSTANTS = [-30., -10., -5., -2., -1., -0.5, -0.01, 0.01, 0.5, 1., 2., 5., 10., 30.]
```

源码中还存在两个算子语义差异：

- 论文 Table 3 把 `Greater` / `Less` 描述为逐元素比较，官方源码实现为逐元素 `max` / `min`。
- 论文 Table 3 把 `TsDiv(x,d)` 描述为当前值除以 `d` 日前值，官方源码实现为当前值除以过去窗口均值。

这两点会直接影响可复现实验的公式语义，不能只按名称等同。

官方 README 的 GFlowNet 主命令补全了 Table 4 之外的一组常用运行参数：

| 参数 | README 主命令 |
| --- | ---: |
| `pool_capacity` | 50 |
| `update_freq` | 64 |
| `n_episodes` | 10000 |
| `encoder_type` | `gnn` |
| `entropy_coef` | 0.01 |
| `entropy_temperature` | 1.0 |
| `mask_dropout_prob` | 1.0 |
| `ssl_weight` | 1.0 |
| `nov_weight` | 0.3 |
| `weight_decay_type` | `linear` |
| `final_weight_ratio` | 0.0 |

源码 checkpoint 也比论文更具体：`logger.save_checkpoint()` 每 `log_freq` 写出一个模型 state dict 和一个 pool JSON。pool JSON 只包含表达式、weights 和 reward 记录；训练脚本没有保存 optimizer、RNG、backward head、`logZ` 或完整数据/config 兼容信息。

因此，论文足以还原 AlphaSAGE 的算法主干、reward 设计、搜索空间类别、关键超参和评价口径；官方源码进一步补齐了 token 编码、RPN mask、window/constant 集合、reward 下限、pool 准入、RSA 归约、batch 更新和动态组合细节。但源码也暴露出若干与论文不一致或不完整的实现点，复现时必须把“论文语义”“官方源码事实”和“复现实现选择”分开记录。

## 14. 阅读时最容易混淆的边界

1. `R_IC` 是 reward 项，`RIC` 在结果表里常表示 RankIC。
2. `R_SA` 不直接奖励高收益，而是奖励结构 embedding 与历史行为的一致性。
3. `R_NOV` 比较的是 alpha 与已有 alpha 的相关性，不是与 label 的相关性。
4. GFlowNet 学的是 alpha 分布，不是单一公式的贪心最优策略。
5. RGCN 的节点是公式 AST 元素，不是股票或因子池中的 alpha。
6. 训练后的动态组合是独立组合阶段，不是 GFlowNet 生成动作的一部分。
7. Appendix F 证明 diversity 能稳定线性估计，但不证明 `R_NOV` 本身必然生成最优组合。
8. 官方源码补全的是实现事实；当它与论文公式冲突时，不能反向改写论文结论。

从算法定位看，AlphaSAGE 的价值在于把“结构感知公式表示、reward-proportional 多模式采样、预测/结构/新颖性联合 reward、低冗余 alpha library、动态线性组合”连成一个公式 Alpha 挖掘框架。复现时最关键的是保留 GFlowNet 采样目标、AST/RGCN 结构语义、三项 reward 的计算口径，以及组合评价与挖掘 reward 之间的边界。
