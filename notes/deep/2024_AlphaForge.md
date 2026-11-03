# AlphaForge 核心算法解读

> - 速读卡：[AlphaForge](../cards/2024_AlphaForge.md)。
> - 论文：AlphaForge: A Framework to Mine and Dynamically Combine Formulaic Alpha Factors，AAAI 2025。
> - 原文：[arXiv:2406.18394](https://arxiv.org/abs/2406.18394)
> - 阅读范围：PDF 全文 10 页，重点对应正文 Preliminary、Methodology、Experiments、Algorithm 1、Algorithm 2、公式 (1)-(5)、Table 1-3、Figure 1-3。
> - 官方代码补充范围：官方仓库 `README.md`、`train_AFF.py`、`combine_AFF.py`、`gan/network/`、`gan/dataset/collector.py`、`gan/utils/`、`alphagen/` 与 `alphagen_generic/` 中和 AlphaForge 主流程直接相关的实现。
> - 文档边界：本文解释论文算法与可直接从公式推出的性质；官方源码口径与论文不一致时单独标注，不改写论文结论。

## 1. 核心结论

AlphaForge 是一个两阶段公式 Alpha 框架：

1. Stage 1 使用 generator-predictor 结构挖掘公式 Alpha，并把满足预测能力和低相关要求的公式放入 Factor Zoo。
2. Stage 2 在每个交易日根据 Factor Zoo 中因子的近期表现动态筛选、重新赋权，生成当天的 Mega-Alpha。

核心链路为：

```text
随机公式样本 R
      │
      ▼
真实评价 fitness(x, Z, X, Y)
      │
      ▼
Predictor P 学习公式 one-hot -> fitness
      │
      ▼
冻结 P，训练 Generator G 最大化 P 的预测 fitness
      │
      ▼
Mask + Gumbel-Softmax 生成合法公式 one-hot
      │
      ▼
解析公式、真实评价、低相关筛选
      │
      ▼
Factor Zoo
      │
      ▼
每日用近期 IC / ICIR 等指标重筛 Top-N 因子
      │
      ▼
线性回归动态权重
      │
      ▼
Mega-Alpha 当日预测信号
```

论文最重要的思想不是单纯换一个生成器，而是把“挖出一批可解释、低相关的公式因子”和“随市场状态动态使用这些因子”拆成两个阶段。Stage 1 追求可执行的强因子库，Stage 2 处理因子有效性随时间变化的问题。

## 2. 问题定义与数据对象

论文设市场中有 `n` 只股票、`T` 个交易日。每个股票在每个交易日有 `m` 个原始特征，并可访问过去 `tau` 天滚动窗口数据。

单日输入可写为：

$$
X_t\in\mathbb R^{n\times m\tau}.
$$

标签为未来收益：

$$
y_t\in\mathbb R^n.
$$

一个公式 Alpha 是函数：

$$
f: X_t \mapsto v_t,\qquad v_t=f(X_t)\in\mathbb R^n.
$$

其中 `v_t` 是该公式在当天全部股票上的横截面因子值。

论文使用六个原始字段：

```text
open, high, close, low, volume, vwap
```

公式由 operands 和 operators 组成：

- operands：基础字段和可选常数；
- unary operators：例如 `abs`、`log`；
- binary operators：例如 `+`、`-`、`*`、`/`；
- time-series operators：例如 `Sum(volume, 5d)`。

论文沿用 AlphaGen 类 RPN 表示。公式树经后序遍历转成 Reverse Polish Notation，再编码成适合神经网络处理的 one-hot 矩阵。

| 符号 | 含义 |
| --- | --- |
| `D` | 可用 operator / feature token 的总数，论文没有明确常数 token 是否计入 |
| `S` | 公式最大长度 |
| `x in {0,1}^{D x S}` | 一个公式的 one-hot 矩阵 |
| `R={x_1,...,x_r}` | 已采样并评价过的公式样本库 |
| `Z={f_1,...,f_k}` | Factor Zoo，已入库的低相关强因子集合 |

## 3. 评价指标

论文正文显式定义 IC：

$$
IC(f,X,Y)
=
E_t[\rho(v_t,y_t)]
=
\frac{1}{T}\sum_{t=1}^{T}\rho(v_t,y_t),
\tag{1}
$$

其中 `rho(v_t, y_t)` 是某一横截面上因子值与未来收益的 Pearson correlation。

论文同时把 ICIR、RankIC、RankICIR 作为因子评价指标，但当前 PDF 正文只说明 RankIC 用于弥补 Pearson correlation 的不稳定，未给出 ICIR / RankICIR 的完整公式。后续复现时不能只凭正文唯一确定：

- ICIR 的有限日数门槛；
- Rank 的并列值处理；
- 横截面零方差和缺失值处理；
- 日度 IC 聚合时是否使用有效日等权。

## 4. Stage 1：Factor Mining Model

Stage 1 的目标是得到一组“强且相互低相关”的公式因子，称为 Factor Zoo。

### 4.1 Algorithm 1 主循环

Algorithm 1 的输入是行情与标签：

$$
X=\{X_t\},\qquad Y=\{y_t\}.
$$

输出是 Factor Zoo：

$$
Z=\{f_1,\ldots,f_k\}.
$$

算法步骤可以还原为：

1. 初始化 `Z = empty`。
2. 随机采样一批公式 one-hot 矩阵：

   $$
   R=\{x_1,\ldots,x_r\}.
   $$

3. 当 `|Z| < TargetFactorNum` 时重复：
   - 根据当前 Factor Zoo 计算样本库中每个公式的真实 fitness：

     $$
     R_{fitness}
     =
     \{\pi(x_1,Z,X,Y),\ldots,\pi(x_r,Z,X,Y)\}.
     $$

   - 训练 Predictor `P` 拟合 `x -> fitness`。
   - 在多个 generator epoch 中：
     - 采样两个 latent noise：

       $$
       z_1,z_2\sim N(0,1)^Q.
       $$

     - 经 Generator 和可微 mask 得到两个公式 one-hot：

       $$
       x_1=M(G(z_1)),\qquad x_2=M(G(z_2)).
       $$

     - 用 generator loss 更新 `G`。
     - 把 `x_1`、`x_2` 解析成公式。
     - 若新公式满足质量要求且不在 `Z` 中，则加入 Factor Zoo。
     - 将 `x_1`、`x_2` 加入样本库 `R`。

4. 当 Factor Zoo 达到目标数量后返回 `Z`。

论文伪代码中有一行 `theta_G <- theta_G || rand(), theta_P <- theta_P || rand()`。从语义看它表示在每轮重新训练前引入随机初始化或随机状态，但 `||` 的确切含义没有解释，不能唯一判断是完整重置、追加随机参数，还是公式排版残留。

### 4.2 Predictor：fitness surrogate

Predictor `P(x)` 输入一个公式 one-hot 矩阵，输出该公式的 fitness 预测值。它先于 Generator 训练，训练数据来自样本库 `R` 中所有已真实评价的公式。

论文给出的 Predictor loss 是 RMSE：

$$
L_P
=
\sqrt{
\frac{1}{n}
\sum_{i=1}^{n}
(P(x_i)-fitness(x_i))^2
}.
\tag{2}
$$

Predictor 的作用是把离散、稀疏、评价昂贵的公式 fitness 转化为可微 surrogate，使 Generator 可以通过梯度朝高分区域移动。

论文没有在 PDF 正文中披露 Predictor 网络结构、层数、hidden size、optimizer、batch size、训练 epoch、early stopping 或输入 padding 规则。

### 4.3 Generator：从 latent noise 到公式

Generator `G(z)` 输入 `Q` 维正态噪声：

$$
z\in\mathbb R^Q.
$$

输出是 `D x S` logit 矩阵。该 logit 经过 `M()` 变成公式 one-hot：

$$
x=M(G(z))\in\{0,1\}^{D\times S}.
$$

`M()` 同时包含两类机制：

- sequence rule mask：约束 token 序列满足公式语法；
- Gumbel-Softmax：把离散 token 采样做成可微近似。

论文强调 `M()` 保持 differentiability，因此 Generator 可以接收来自 Predictor 的梯度。

在 Predictor 训练完成后，冻结 `P`，Generator 先最小化：

$$
L_{Fitness}
=
-P(M(G(z))).
\tag{3}
$$

由于最小化负号，Generator 被训练为生成 Predictor 认为高 fitness 的公式。

### 4.4 Diversity loss

论文认为只最大化 Predictor 分数会导致 Generator 过早收敛到局部模式，因此加入 diversity loss。它用两个 latent noise 生成两组公式，并惩罚二者相似性。

最终 generator loss 写为：

$$
L_G
=
L_{Fitness}
+
L_{Diversity}
$$

$$
=
-P(x_1)
+
\lambda_{onehot}
\cdot
Similarity_{onehot}(f(z_1),f(z_2))
+
\lambda_{hidden}
\cdot
Similarity_{hidden}(f(z_1),f(z_2)).
\tag{4}
$$

这里有几个复现必须注意的细节：

- 公式中 `-P(x_1)` 只写了第一个样本，第二个样本主要用于 diversity；论文没有说明是否实际对 `x_1`、`x_2` 做对称平均。
- `Similarity_onehot` 没有给出具体计算式。
- `Similarity_hidden` 的 hidden representation 来源没有在 PDF 正文中定义。
- `lambda_onehot`、`lambda_hidden` 的取值在当前 PDF 中没有给出。
- Gumbel temperature、hard / soft 采样方式和 mask 逐步更新规则没有披露。

因此，论文能确定“用可微生成 + surrogate fitness + diversity 约束”这个目标结构，但不能唯一确定 Generator 的完整实现。

### 4.5 Fitness 函数与 Factor Zoo 准入

论文用 `pi(x,Z,X,Y)` 表示公式 one-hot `x` 在当前 Factor Zoo `Z` 下的真实 fitness：

$$
\pi(x,Z,X,Y)
=
\begin{cases}
|IC(f,X,Y)|,
&
f\text{ is valid and }\psi(f,Z,X,Y)<CORR'\\
0,
&
\text{otherwise}
\end{cases}
\tag{5}
$$

其中：

- `f=parse(x)`，表示从 one-hot 解析出的可执行公式；
- `Z` 是已有 Factor Zoo；
- `psi(f,Z,X,Y)` 是新公式与已有 Zoo 中各因子的最大绝对相关；
- `CORR'` 是人工设定的相关性阈值；
- 当 `|Z|=0` 时，`pi` 退化为 `|IC(f,X,Y)|`。

论文说明取绝对 IC 的原因是：负 IC 因子可以通过反向因子值变成正 IC 因子。

需要特别注意：正文文字说因子入库标准包含三方面：

1. IC；
2. ICIR；
3. 与已有库中因子的收益相关性。

但公式 (5) 只显式写了 `|IC|` 和 `psi<CORR'`，没有写 ICIR 阈值。Algorithm 1 中的 `qualified` 也没有展开。因此可以确认论文主张使用 IC/ICIR/相关性三类门槛，但当前 PDF 不能唯一还原这些门槛如何合并。

`pi` 会随 `Z` 变化而变化。也就是说，同一个公式在不同 Factor Zoo 状态下可能有不同 fitness，因为它与当前库的相关性不同。这是 AlphaForge 相比固定 objective 公式搜索的重要特征。

## 5. Stage 2：动态组合模型

Stage 2 解决的是 Factor Zoo 的使用问题。论文认为 Alpha 因子的有效性可能周期性失效、永久失效或反转，固定因子集合和固定权重难以及时适应市场变化。

### 5.1 Algorithm 2 主流程

Algorithm 2 输入：

- Factor Zoo：

  $$
  Z=\{f_1,\ldots,f_k\}
  $$

- 最大使用因子数 `N`；
- 数据集 `X`、`Y`。

输出是逐日预测：

$$
\hat Y=\{\hat y_t\}.
$$

主流程为：

1. 对每个交易日 `t`：
   - 初始化当日候选集合 `Z_t`。
   - 对 Zoo 中每个因子 `f` 计算近期表现：

     $$
     IC_t^\rho(f),\qquad ICIR_t^{\hat\rho}(f).
     $$

   - 若满足：

     $$
     IC_t^\rho(f)>IC'
     \quad\text{and}\quad
     ICIR_t^{\hat\rho}(f)>ICIR'
     $$

     则加入 `Z_t`。

   - 按 `IC_t^\rho(f)` 排序。
   - 选择 Top-N 因子：

     $$
     Z_t^{(N)}=TopN(Z_t).
     $$

   - 用这些因子拟合线性回归。
   - 用回归模型预测当前横截面，得到 `hat y_t`。

论文正文说明每个时点使用此前 `n` 天数据重新评估因子近期表现并拟合线性模型。因此复现时应将 Algorithm 2 中的 `LinearRegression(Z_t^{(N)}, y_t)` 理解为用可观测历史样本训练，再预测当前横截面；不能机械理解为使用当日未来标签拟合当日预测。

### 5.2 动态组合的含义

Stage 2 的动态性体现在两层：

- 因子集合动态：每天从固定 Factor Zoo 中筛选近期仍有效的一部分因子；
- 因子权重动态：每天用最新历史数据重新拟合线性回归权重。

论文强调组合模型偏向线性结构，原因是金融场景要求可解释，且非线性组合更容易在低信噪比金融数据中过拟合。

正文还提到可使用 ICIR、IC、RankIC 等近期指标进行重排，但 Algorithm 2 只显式写出 IC 和 ICIR。复现时要明确到底使用哪组指标。

### 5.3 组合阶段未披露细节

当前 PDF 没有给出以下实现细节：

- 近期窗口 `n` 的具体长度；
- `IC'`、`ICIR'`、`CORR'` 的数值；
- 线性回归是否包含截距；
- 因子值是否按日标准化；
- 目标 `y` 是否保留原值或标准化；
- 候选不足 `N` 时如何处理；
- 没有因子通过阈值时是否回退；
- 因子缺失值处理；
- 权重是否有约束；
- 交易成本是否进入组合训练目标。

这些缺口意味着论文足以还原动态组合主干，但不足以唯一复现实验代码。

## 6. 实验设置

### 6.1 数据与时间划分

论文主要使用 CSI300 和 CSI500 数据，因为两者覆盖中国 A 股市场较大市值范围，并且与被比较的相关工作保持一致。数据通过 Qlib 下载。

论文测试期为 2018-2022 年，并采用年度重训。第一个窗口明确写为：

| Split | 日期 |
| --- | --- |
| Train | 2010-01-01 至 2016-12-31 |
| Validation | 2017-01-01 至 2017-12-31 |
| Test | 2018-01-01 至 2018-12-31 |

后续年份按“测试年前一年作为 validation，并用新数据年度重训”的方式推进。论文没有在正文逐一列出 2019-2022 每个窗口的完整 train 范围。

### 6.2 标签

论文使用：

```text
Ref(VWAP, -21) / Ref(VWAP, -1) - 1
```

作为标签，并说明该标签更贴近真实交易场景。按 AlphaGen / AlphaForge 系列常见偏移记号理解，它表示使用未来第 1 日到未来第 21 日之间的 VWAP 收益，即大致 20 日持有收益。

复现时必须确认 `Ref` 的正负方向和数据可用边界，不能只复制字符串而忽略 future context。

### 6.3 对比方法

论文比较了三类公式方法：

| 方法 | 含义 |
| --- | --- |
| GP | 遗传规划，用 IC 作为优化目标 |
| DSO | Deep Symbolic Optimization，符号回归代表方法 |
| RL | AlphaGen 类强化学习公式因子集合生成 |

同时比较了三个机器学习模型：

| 方法 | 含义 |
| --- | --- |
| XGBoost | 梯度提升树 |
| LightGBM | 高效梯度提升框架 |
| MLP | 多层感知机 |

论文称为避免随机种子影响，每个模型重复运行 5 次。表中部分 deterministic baseline 未报告标准差。

### 6.4 主结果

Table 1 报告的核心结果如下，单位为百分比。

| 方法 | CSI300 IC | CSI300 RankIC | CSI500 IC | CSI500 RankIC |
| --- | ---: | ---: | ---: | ---: |
| XGB | 0.41 | 1.63 | 0.33 | 2.87 |
| MLP | 1.22 (0.16) | 1.75 (0.28) | 1.94 (0.11) | 3.31 (0.23) |
| LGBM | 0.84 | 1.85 | 1.75 | 3.81 |
| GP | 1.29 (0.44) | 2.72 (0.58) | 0.37 (0.76) | 2.34 (1.07) |
| DSO | 2.55 (0.69) | 3.88 (1.12) | 1.38 (0.57) | 4.56 (0.61) |
| RL | 2.09 (0.26) | 2.72 (0.42) | 1.91 (0.49) | 4.03 (0.62) |
| Static | 2.43 (0.57) | 3.67 (0.46) | 2.05 (0.29) | 4.48 (0.46) |
| Ours | 4.40 (0.56) | 5.89 (0.69) | 2.84 (0.58) | 5.57 (0.58) |

`Static` 是消融版本：使用 AlphaForge 的 factor mining model 生成 Alpha，但用类似 RL 的静态 Mega-Alpha 组合方式。`Ours` 是完整动态组合版本。这个对比说明：

- generator-predictor 挖掘模型本身相对 RL baseline 有增益；
- 动态组合进一步提升表现。

### 6.5 Factor pool size

论文将 pool size 设置为：

```text
1, 10, 20, 50, 100
```

并在 CSI300 上比较 IC。结果呈非单调关系，最高点出现在 pool size = 10。论文解释为动态组合每个时点只需要大约 10 个最相关的价格信息来源，继续扩大库可能带来边际收益下降。

这个结论需要谨慎理解：它支持“组合使用阶段不一定越多因子越好”，但不直接证明挖掘阶段永远只应保留 10 个因子，因为更大 Factor Zoo 仍可能为不同市场状态提供候选。

## 7. Case Study 与可解释性

论文用一个案例说明动态 factor timing：

- Generator 产生 100 个 Alpha 的 Factor Zoo；
- 组合模型每次最多使用 10 个因子；
- Day 1 和 Day 2 各选出 10 个因子；
- 两天只有 5 个因子重合；
- 同一个因子在不同日期的权重可能显著变化甚至变号。

例如，论文提到第 3 个因子在 Day 1 权重约为负值，而 Day 2 权重变为正值，说明同一公式可能在不同市场状态下承担不同作用。

论文还用 `S_log1p(ts_cov(high, volume, 20))` 解释公式可读性：该因子可理解为过去 20 天最高价与成交量趋势是否同步。论文认为，投资经理可以根据公式经济含义、权重方向和风险暴露做进一步判断。

另一个例子是 `-1 * ts_mean(volume, 20)`。论文指出它与市值风险暴露相关；若权重过大，组合可能偏向小市值股票，投资经理应识别并控制这种暴露。

这些案例的作用是说明公式 Alpha 相比黑盒模型更便于归因、风控和人工干预。

## 8. 回测与实盘证据

论文进行了模拟交易和实盘展示。

模拟交易设置：

- 时间：2018-01-01 至 2022-12-31；
- 股票池：CSI300；
- 框架：Qlib；
- 每日持有 Mega-Alpha 分数最高的 50 只股票；
- 等权持仓；
- 每日最多换 5 只股票，用于控制过高交易成本。

论文报告 AlphaForge 在五年模拟交易中取得最高净值表现。

实盘展示：

- 账户资金：300 万人民币；
- 股票池：CSI500；
- 时长：约 9 个月；
- 论文声称相对 CSI500 取得 21.68% 超额收益。

实盘结果是论文报告的外部证据，但当前 PDF 没有给出可复验的交易明细、成本模型、持仓约束、风险控制参数或审计口径，因此不能单独作为可复现算法定义。

## 9. 论文讨论中的重要边界

论文 Discussion 中有一个容易被忽略的点：尽管 Factor Zoo 增长会改变 mining objective，因为相关性惩罚依赖当前 `Z`，但 Generator 的训练目标仍主要是单个 Alpha 的 IC / fitness。

论文认为，未来可以探索把整批因子的 combined IC 作为 Generator 目标，以提高挖掘效率。这说明 AlphaForge 当前 Stage 1 并未直接优化完整 batch 的组合 IC，而是先挖单因子强度和低相关性，再交给 Stage 2 组合。

这与 AlphaGen 类方法不同：

- AlphaGen / RL baseline 更直接把组合 IC 边际贡献写入 reward；
- AlphaForge 用 surrogate model 学当前 Zoo 下的单公式 fitness，再通过 Stage 2 动态组合使用因子。

## 10. 复现时最关键的歧义与缺口：官方源码补全

本节只记录官方源码可确认的实现口径。源码与论文 Algorithm 1、Algorithm 2 或公式 (5) 不一致的点标注为“源码差异”，不等同于论文原文结论。

### 10.1 公式生成、action space 与 mask

官方源码确认公式使用 AlphaGen 类 RPN 栈表示，最大表达式长度为 `20`，实际 action space 大小为 `51`。`Null` token 不作为可采样 action；网络输出 action 再偏移成内部 token。

官方 action space 由以下部分组成：

- operators：`Inv`、`S_log1p`、`Add`、`Sub`、`Mul`、`Div`、`Pow`、`Ref`、`ts_mean`、`ts_sum`、`ts_std`、`ts_var`、`ts_max`、`ts_min`、`ts_med`、`ts_mad`、`ts_div`、`ts_pctchange`、`ts_delta`、`ts_wma`、`ts_ema`、`ts_cov`、`ts_corr`；
- features：`open`、`close`、`high`、`low`、`volume`、`vwap`；
- rolling windows / delta times：`1`、`5`、`10`、`20`、`30`、`40`、`50`；
- constants：`-30`、`-10`、`-5`、`-2`、`-1`、`-0.5`、`-0.01`、`0.01`、`0.5`、`1`、`2`、`5`、`10`、`30`；
- end token：`SEP`。

源码中也保留了一些未启用或与论文示例不同的 operator 定义，例如 `Abs`、`Sign`、`Log`、`CSRank`、`Greater`、`Less`、`ts_skew`、`ts_kurt`、`ts_rank`、`ts_ir` 等没有进入 AlphaForge 主训练配置。因此复现时应以主训练配置中的 action list 为准，而不是以所有 Python 类定义为准。

`ExpressionBuilder` 的 legality rule 是栈约束：

- terminal 合法条件是栈里只剩一个 featured expression；
- unary operator 要求栈顶是 featured expression；
- binary operator 要求至少两个元素，且不能把纯 `DeltaTime` 当作普通操作数；
- rolling operator 要求栈顶是 `DeltaTime`，其前一项或前两项是 featured expression；
- `DeltaTime` 只能接在 featured expression 后；
- `Constant` 可在空栈或 featured expression 后出现；
- `Feature` 不能紧跟 `DeltaTime`。

`NetM` 的 mask 实现有一个重要源码细节：每个位置先把非法 action 的 logit 设为极小值，再用 masked logit 的 `argmax` 更新 builder 前缀；随后 Generator 训练阶段再对 masked logit 调用 `F.gumbel_softmax(..., hard=True)` 得到硬 one-hot。也就是说，mask 递推使用的是 argmax 前缀，而最终 hard Gumbel 样本可能与该 argmax 前缀不同。这是源码行为，不是论文对 `M()` 的数学定义。

其它实现细节：

- Gumbel-Softmax 没有显式传入 temperature，使用 PyTorch 默认 `tau=1`，并采用 `hard=True`；
- 若某个样本生成 `SEP`，builder 会把后续 token 填成 `SEP`；
- duplicate 的主要判定是 token 序列字符串去重；
- 无效公式在 builder 解析或真实评价阶段被过滤或记为 0 分，不会仅凭 Predictor 分数直接进入 Zoo；
- `S_log1p` 的实现是 `sign(x) * log1p(abs(x))`；
- `ts_div` 的源码语义是当前值除以 `d` 日前值，不是除以滚动均值。

### 10.2 网络结构与训练预算

官方主流程使用 `NetP`、`NetG_DCGAN` 和 `NetM`。源码里存在其它 Generator 变体，但 `train_AFF.py` 主训练选择的是 DCGAN 版本。

Predictor `NetP` 的结构为：

```text
one-hot sequence
  -> permute to channel-first tensor
  -> Conv2d(n_actions -> 96, kernel=(1, 3))
  -> ReLU
  -> MaxPool2d(kernel=(1, 2))
  -> Conv2d(96 -> 128, kernel=(1, 4))
  -> ReLU
  -> flatten
  -> Linear(128 * 6 -> 256)
  -> Dropout(0.2)
  -> ReLU
  -> Linear(256 -> 1)
```

`NetP` 构造参数里有 `hidden`，但主结构实际使用固定 `256` hidden；源码没有把该参数作为通用 hidden size。Predictor 训练使用 weighted MSE，而不是公式 (2) 中写出的 RMSE；训练样本按 `train_test_split(test_size=0.2, random_state=42)` 切分，Adam learning rate 为 `1e-3`，batch size 为 `64`，最多 `100` epoch，early stopping patience 为 `10`。训练标签会按当前样本分数最大值缩放到大致 `0` 到 `100` 的区间；源码固定使用 `min_y=0`，没有按样本最小值平移。

Generator `NetG_DCGAN` 固定要求 `seq_len=20`，输入 latent noise 维度默认为 `100`，主要结构是：

```text
Normal(0, 1) latent z
  -> Linear(100 -> 6 * 384)
  -> reshape
  -> ConvTranspose / BatchNorm / ReLU blocks
  -> Conv / BatchNorm / ReLU blocks
  -> output logits with shape (batch, 20, n_actions)
```

源码中 `g_hidden=128` 传入构造函数，但 DCGAN 主干通道数固定为 `384/256/192/128/64`，并未按 `g_hidden` 缩放。Generator 训练默认 batch size 为 `256`，最多 `200` epoch，Adam learning rate 为 `1e-3`，early stopping patience 为 `10`，默认按生成候选的最大真实 score 选择 best state。源码在每轮 while 循环开始会重新初始化 `NetP` 和 `NetG` 的权重与 bias；但 BatchNorm running state 不是完整重置项，这属于源码实现细节。

Generator loss 的源码口径为：

- `loss_pred = -pred_1.mean()`，只用第一组 latent 样本的 Predictor 输出，第二组主要服务 diversity；
- one-hot similarity 先按 token 位置比较两组 hard one-hot，相似度超过阈值 `0.4` 的部分才进入惩罚，默认系数 `10`；
- hidden similarity 使用 `NetP` 中 `fc1` 后的 latent representation，cosine similarity 超过阈值 `0.4` 的部分才进入惩罚，默认系数 `10`；
- entropy loss 默认系数为 `0`，主流程不启用；
- 源码在 epoch 0 会评价候选并记录 best state，但只有 `epoch > 0` 时才执行 `backward()` 和 optimizer step，因此第 0 个 epoch 不更新 Generator。

源码差异：论文说 Predictor 训练后冻结 `P`，源码训练 Generator 时把 `NetP` 置为 `eval()`，optimizer 只更新 `NetG`，但并没有逐参数设置 `requires_grad=False`。这不改变 optimizer 更新对象，但会让 Autograd 仍构建穿过 Predictor 的梯度路径。

### 10.3 Fitness、准入与 Zoo 生命周期

官方源码的训练标签与论文一致，使用：

```text
Ref(vwap, -21) / Ref(vwap, -1) - 1
```

训练数据加载时使用 `raw=True`，价格字段会按 Qlib factor 还原，volume 会做缩放。表达式值和 target 在训练评价中按日做横截面标准化；`normalize_by_day` 会按日计算均值和标准差，并把 NaN 填成 0。

`get_metric()` 的源码口径是：

- 主 score 固定为 `abs(mean(IC))`；虽然函数参数保留 `metric_target`，内部又硬编码为 `ic`；
- ICIR 使用 `abs(mean(IC)) / std(IC)`，作为附加门槛参与入库；
- `batch_ret` 不是组合回测收益，而是以 `cov(factor, target) / var(factor)` 形式得到的日度 factor-return / slope-like 序列；
- 与已有 Zoo 的相关性检查使用候选 `batch_ret` 序列和 Zoo 中已保存 `ret_list` 的最大绝对相关；
- 若首日有限值覆盖不足 `0.8`，或首日唯一值比例不足 `0.01`，score 置 0；
- 非有限 IC、ICIR、return 类指标会被置 0。

默认 CLI / config 门槛为：

| 项 | 源码默认值 |
| --- | ---: |
| `zoo_size` | `100` |
| `corr_thresh` | `0.7` |
| `ic_thresh` | `0.03` |
| `icir_thresh` | `0.1` |

`filter_valid_blds()` 的入库筛选顺序是：先保留 `score > 0`，过滤 invalid，按 token 序列去重，按 score 降序排序；再要求 `score > ic_thresh`、`icir > icir_thresh`，并对本批候选之间的 `ret_list` 绝对相关做贪心去冗余。候选与已有 Zoo 的相关性主要已经体现在 `get_metric()` 得到的 score 中；每隔若干轮源码还会对整个 Zoo 重新执行一次过滤。

Zoo 生命周期的源码口径为：

- 初始随机收集约 `10000` 个候选；
- 每轮用当前候选和历史备份训练 Predictor，备份样本权重为 `1`，当前样本权重为 `2`；
- 每轮 Generator 训练后，合并训练中生成的候选和新采样候选，再进行真实评价与入库；
- 每轮结束还会追加一批随机探索候选，供下一轮使用；
- while 条件是 `len(zoo) < num_factors`，新增候选后不强制裁剪到刚好等于 `zoo_size`，因此最终 Zoo 数量可能超过目标数量。

源码没有持久保存“负 IC 因子应在后续整体取反”的独立方向字段；主 fitness 用 `abs(IC)`，但组合阶段直接使用表达式值计算近期 RankIC / RankICIR 和线性回归权重。

### 10.4 动态组合官方源码口径

`combine_AFF.py` 是官方 Stage 2 入口。它读取 Stage 1 保存的 final Zoo，按 `abs(score)` 排序，将表达式重新计算为因子张量；因子值默认按日标准化，target 不标准化。组合前会预计算每个因子的日度 IC、RankIC 和 `batch_ret`。

每日组合的核心实现为：

1. 对预测日 `cur`，使用 `shift = 21`，只取 `begin:cur-shift` 的历史区间计算近期表现和拟合线性回归；
2. 若 `window=inf`，历史起点为全样本起点；若使用有限 window，源码使用 `begin = cur - window - shift`，没有显式 clamp 到 0；
3. 对每个因子计算历史区间的 IC、ICIR、RankIC、RankICIR、return 和 return IR；
4. 按 `abs(RankICIR)` 降序排序；
5. 筛选 `RankIC > 0.02` 且 `RankICIR > 0.2` 的因子；
6. 若没有因子通过筛选，则回退到排序后的 top-1；
7. 最多取 `n_factors` 个因子，默认 README 示例为 `10`；
8. 将历史日期和股票截面展平成二维回归样本，在线性回归中显式加入常数列；
9. 用 `torch.linalg.lstsq` 求解 OLS，并对当日横截面预测。

源码差异：论文 Algorithm 2 写的是按 IC / ICIR 过滤并按 IC 排序；官方组合代码实际使用 RankIC / RankICIR，按 `abs(RankICIR)` 排序，并加入了空集合 top-1 fallback。源码没有加入权重非负、权重和、交易成本或换手约束；OLS 权重可以为负，是否使用某个因子由当日历史筛选决定。

另一个需要注意的细节是缺失值处理：拟合样本主要按 target 是否 finite 过滤，预测日因子值会用 `nan_to_num` 填 0；代码没有把组合阶段写成严格的投资组合优化器，它更接近每日横截面标签预测器。

### 10.5 数据切分、保存与 baseline 边界

官方 README 示例把 `train_end_year` 作为滚动训练结束年。例如 `train_end_year=2020` 时，训练区间为 2010-01-01 至 2020-12-31，validation 为 2021 年，test 为 2022 年。源码 `get_data_by_year()` 每次只构造一个 validation 年和一个 test 年；论文 2018-2022 的五年结果需要按年度滚动运行组合得到，而不是单次训练覆盖全部测试年。

源码还会为 validation / test 构造向前两年的 head data，用于满足滚动算子和未来标签上下文；全量数据范围则覆盖 train start 到 test end。公共文档中不应写官方代码 checkout 的本地绝对路径，也不应把本地 Qlib 数据目录写成算法定义。

保存口径：

- Stage 1 保存 builder pickle 和 CSV，final Zoo 文件名包含 `z_bld_zoo_final`；
- Stage 2 保存 validation 和 test 预测张量；
- 源码没有提供统一的 optimizer / RNG / dataloader checkpoint 复现包。

对比 baseline 方面，PDF 和官方主流程能确认 AlphaForge 自身的两阶段算法与主要实验入口，但不能从当前 PDF 唯一还原 DSO、GP、RL、MLP、XGBoost、LightGBM 的全部输入特征、超参和训练预算。后续复现实验需要单独标注 baseline 的代码依据或复现假设。

## 11. 阅读时最容易混淆的边界

1. Stage 1 的 Factor Zoo 是挖掘结果；Stage 2 的每日 Top-N 是使用阶段的动态子集。
2. Factor Zoo 可以有很多因子，但 Mega-Alpha 每天不一定使用全部因子。
3. 公式 (5) 的 fitness 明确写的是绝对 IC 和相关性门槛；正文文字还提到 ICIR，因此不能只按公式或只按文字还原。
4. `M()` 不是普通 softmax，它还承担公式语法 mask 和 Gumbel-Softmax 可微采样。
5. Predictor 是 surrogate，不替代真实评价；新生成公式仍需 parse、真实评价和准入。
6. Generator loss 中 diversity 是避免模式坍缩的关键，不是事后去重的替代品。
7. Algorithm 2 的线性回归必须按正文理解为使用历史数据预测当前，不能把当前未来收益泄露进当日预测。
8. `Static` 消融不是传统 RL baseline，而是 AlphaForge 挖掘 + 静态组合。
9. 论文的实盘展示不能替代可复现实验协议。
10. 当前 PDF 没有 supplementary hyperparameter 表；缺失实现细节应标注为源码依据或复现假设。
11. 官方源码补全的是实现事实；当它与论文 Algorithm 1、Algorithm 2 或公式 (5) 冲突时，不能反向改写论文结论。

## 12. 复现要点

从算法定位看，AlphaForge 的价值在于：

- 用可微 surrogate 引导离散公式搜索；
- 在 sparse fitness space 中通过 Generator 学习高分区域；
- 在生成目标中加入 diversity，避免公式同质化；
- 通过当前 Factor Zoo 相关性让 mining objective 随库状态变化；
- 将 Factor Zoo 挖掘与每日动态组合解耦。

复现时最关键的是保留以下语义：

1. 公式必须经过合法 mask / parse / 真实评价，不应只相信 Predictor。
2. Factor Zoo 准入必须同时考虑预测能力和与已有库的冗余。
3. 负 IC 公式的可用方向需要被显式处理，避免测试期按未来收益翻转。
4. Stage 2 只能使用预测日前可观测历史重筛与拟合。
5. 动态组合是训练后独立使用阶段，不应反向污染 Stage 1 的 Factor Zoo 定义。

当前 PDF 足以还原 AlphaForge 的两阶段算法主干、关键目标函数、Factor Zoo 语义、动态组合伪代码、实验数据划分、标签和主要证据；但不足以唯一还原官方实现的网络结构、超参、mask、ICIR 阈值、Zoo 更新和组合细节。补全这些内容时，应明确区分论文原文、官方源码依据和复现者自己的实现选择。
