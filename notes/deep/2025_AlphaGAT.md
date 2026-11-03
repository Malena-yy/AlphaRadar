# AlphaGAT 核心算法解读

> - 速读卡：[AlphaGAT](../cards/2025_AlphaGAT.md)。
> - 论文：AlphaGAT: A Two-Stage Learning Approach for Adaptive Portfolio Selection，IJCAI 2025。
> - 原文：[IJCAI 2025 Proceedings 834](https://www.ijcai.org/proceedings/2025/834)
> - 阅读范围：PDF 全文 9 页，重点对应论文第 3、4、5 节以及公式 (1)–(10)、Algorithm 1、Table 1–4。
> - 文档边界：本文解释论文算法；论文未披露的细节单独列出，不作推断。

## 1. 核心结论

AlphaGAT 不是公式 Alpha 挖掘算法，而是一个两阶段神经因子与组合优化方法：

1. Stage I 使用监督学习模型 CATimeMixer，把过去行情转换为一组具有横截面预测能力、且彼此尽量低冗余的神经 Alpha。
2. Stage II 把每个 Alpha 当作图节点，用 GAT 建模因子之间的关系，通过 PPO 动态调整因子权重，再由加权信号选择 Top-G 资产。

其核心数据流为：

```text
过去 k 期、m 个资产、d 个行情字段
            │
            ▼
多尺度平均池化 → 趋势/季节分解
            │
            ▼
Trend 自上而下 Conv1D
Seasonal 自下而上 Conv1D
            │
            ▼
跨资产 Multi-Head Attention
            │
         堆叠 3 层
            ▼
n 个神经 Alpha：Z_t ∈ R^(n×m)
            │
            ▼
以 Alpha 为节点构造完全图
            │
            ▼
GAT → 动态因子权重 q_t
            │
            ▼
资产信号 v_t = q_t^T Z_t
            │
            ▼
Top-G 资产 + 资产内 softmax
            │
            ▼
组合收益、交易成本 → PPO 更新
```

需要特别区分两种关系建模：

- Stage I 的 Multi-Head Attention 在资产之间传播信息；
- Stage II 的 GAT 在 Alpha 因子之间传播信息。

### 针对的问题

对应 README 中的 P1-P10，本文涉及的机制如下；各模块的实验证据见第 9 节。

- **P2 表达能力与可解释性的权衡**：Stage I 由 CATimeMixer 直接输出神经 Alpha，不经过公式表达（第 3 节），输出不是可读的公式。
- **P7 因子同质化与冗余**：Stage I 损失惩罚因子间协方差矩阵非对角项的绝对值（第 4.2 节）；论文文字说降低相关性，公式惩罚的是协方差。
- **P8 挖掘目标与实际使用脱节**：Stage II 用 GAT 策略网络和 PPO 动态学习因子权重（第 5、7 节），奖励是扣除交易成本后的组合收益（第 6 节）。

## 2. 问题定义与张量含义

论文第 3.1 节定义：

- `m`：资产数量；
- `d`：单个资产的基础行情特征数量；
- `k`：历史观察窗口长度；
- `n`：Alpha 因子数量；
- `T`：训练时间样本数量。

单个时点 `t` 的全部资产特征为：

$$
X_t\in\mathbb R^{m\times d}.
$$

模型在时点 `t` 使用此前 `k` 期数据：

$$
\mathbf X_t=
\{X_{t-k},\ldots,X_{t-1}\}
\in\mathbb R^{k\times m\times d}.
$$

历史窗口截止于 `t-1`。按照论文时间记号，模型使用此前可观测行情形成 `t` 期信号。

一个 Alpha 函数产生全部资产上的横截面暴露：

$$
z_t=f(\mathbf X_t)\in\mathbb R^m.
$$

同时产生 `n` 个 Alpha 后得到：

$$
Z_t=
\begin{bmatrix}
Z_t^1\\
\vdots\\
Z_t^n
\end{bmatrix}
\in\mathbb R^{n\times m}.
$$

| 对象 | 形状 | 含义 |
| --- | --- | --- |
| $\mathbf X_t$ | $k\times m\times d$ | 历史行情窗口 |
| $Z_t^i$ | $m$ | 第 `i` 个 Alpha 在全部资产上的暴露 |
| $Z_t$ | $n\times m$ | 全部神经 Alpha |
| $q_t$ | $n$ | 动态因子权重 |
| $v_t$ | $m$ | 聚合后的资产交易信号 |
| $w_t$ | $m$ | 最终资产组合权重 |

论文实验使用 8 个原始字段：

```text
open, close, high, low, volume, vwap, turn, chg
```

实验中的历史窗口长度为 30，Alpha 数量为 64。

## 3. Stage I：CATimeMixer 神经 Alpha 生成

Stage I 的目标不是直接预测资产组合权重，而是生成：

1. 对未来资产变动具有横截面预测能力的 Alpha；
2. 彼此尽量不冗余的 Alpha。

### 3.1 多尺度下采样

CATimeMixer 首先使用平均池化将原始历史窗口转换为多个尺度：

$$
\{X_t^0,X_t^1,\ldots,X_t^L\}.
$$

第 `i` 个尺度的形状为：

$$
X_t^i
\in
\mathbb R^{
\left\lfloor k/2^i\right\rfloor
\times m\times d}.
$$

因此：

- `i=0` 是最细时间尺度；
- `i` 越大，序列越短、尺度越粗；
- 粗尺度偏向宏观趋势；
- 细尺度保留更多局部波动。

论文文字称其为 `L` 个尺度，但索引写成 `0,...,L`，按公式实际上得到 `L+1` 个层级。论文没有给出实验使用的具体尺度数 `L`。

### 3.2 趋势与季节项分解

每个尺度被分解为趋势项和季节项：

$$
X_t^i\longrightarrow\left(Tr_t^i,Se_t^i\right),
$$

其中：

- $Tr_t^i$：趋势项；
- $Se_t^i$：季节项或较高频的变化项。

这一思路来自 TimeMixer 的“先分解、再沿不同方向混合多尺度信息”。但 AlphaGAT 论文没有写明：

- 使用移动平均还是频域分解；
- 分解窗口长度；
- 序列边界填充方式；
- 分解算子的具体计算式。

因此只能确认论文使用 trend/seasonal decomposition，不能仅依据本文确定其精确实现。

### 3.3 Trend：自上而下的 Conv1D 混合

趋势信息由粗尺度向细尺度传递：

$$
\widehat{Tr}_t^i
=
\operatorname{TopDownConv1D}
\left(
Tr_t^{i+1},\ldots,Tr_t^L
\right).
\tag{1}
$$

粗尺度中的宏观趋势被用来补充更细尺度的趋势表示。Figure 2 展示的是渐进式结构：

```text
粗尺度 context
    │
   MLP
    │
与当前更细尺度趋势 Concat
    │
  Conv1D
    │
作为下一层 context 继续向细尺度传播
```

Figure 2 中使用了单词 `Contact`，结合连接结构应理解为 `Concat`。模型不是一次性拼接全部原始尺度，而是把上一尺度的混合结果逐级向细尺度传递。

### 3.4 Seasonal：自下而上的 Conv1D 混合

季节项采用相反方向：

$$
\widehat{Se}_t^i
=
\operatorname{BottomUpConv1D}
\left(
Se_t^0,\ldots,Se_t^{i-1}
\right).
\tag{1}
$$

细尺度中更丰富的局部变化被逐级补充到粗尺度：

```text
细尺度 seasonal
    │
   MLP
    │
与当前更粗尺度 seasonal Concat
    │
  Conv1D
    │
继续向粗尺度传播
```

两个方向的作用可以概括为：

- Trend：coarse-to-fine，向细尺度补充宏观趋势；
- Seasonal：fine-to-coarse，向粗尺度补充局部变化。

更新后的 $\widehat{Tr}_t^i$ 与 $\widehat{Se}_t^i$ 被组合为尺度 `i` 的特征 $H_t^i$。正文只使用 `combined` 描述这一操作，Figure 1 画有加号，但没有单独写出究竟采用逐元素相加、拼接还是带映射的融合公式。

### 3.5 跨资产注意力

前面的 Conv1D 主要提取单个资产的多尺度时间特征，没有显式交换不同资产的信息。

尺度 `i` 上全部资产的表示写为：

$$
H_t^i=
\{H_t^{i0},\ldots,H_t^{im}\}.
$$

CATimeMixer 把资产作为 Multi-Head Attention 的 token：

$$
E_t^i
=
\operatorname{MHA}
\left(
H_t^{i0},\ldots,H_t^{im}
\right).
$$

这一注意力的交互轴是资产轴，不是因子轴。它用于提取资产之间的横截面关系，例如共同趋势或相反变化。

### 3.6 三层反馈式结构

CATimeMixer 由 3 个相同层堆叠。每层的 Multi-Head Attention 输出 $E_t^i$ 会反馈为下一层的输入 $X_t^i$。

因此模型不是仅在输出端执行一次资产注意力，而是在每层中交替执行：

$$
\text{多尺度时间建模}
\rightarrow
\text{资产关系建模}
\rightarrow
\text{多尺度时间建模}
\rightarrow\cdots
$$

实验使用的隐藏表示维度为 `c=512`。

### 3.7 多尺度 Alpha 输出头

各尺度的输出分别经 MLP 映射到统一的 Alpha 空间，然后跨尺度求和：

$$
Z_t
=
\sum_{i=0}^{L}
\operatorname{MLP}(E_t^i).
$$

最终输出：

$$
Z_t\in\mathbb R^{n\times m},\qquad n=64.
$$

这 64 个 Alpha 是神经网络输出通道，不是可读取或执行的公式表达式。

论文没有说明不同尺度的时间长度如何在输出头中对齐，以及每个尺度如何压缩为时点 `t` 的单个 Alpha 输出。

## 4. Stage I 损失函数

为避免论文同时使用 `i`、`n` 表示不同对象造成混淆，本节重新约定：

- `a` 表示资产；
- `r,s` 表示 Alpha 因子；
- `m` 表示资产数；
- `n` 表示因子数。

这一重命名不改变原公式语义。

### 4.1 IC 预测损失

对时间 `t` 和因子 `r`，计算该因子与真实资产变动 $y_t$ 的横截面 Pearson IC：

$$
IC_{t,r}
=
\frac{
\sum_{a=1}^m
(z_{t,a}^{r}-\bar z_t^r)
(y_{t,a}-\bar y_t)
}{
\sqrt{\sum_{a=1}^m(z_{t,a}^{r}-\bar z_t^r)^2}
\sqrt{\sum_{a=1}^m(y_{t,a}-\bar y_t)^2}
}.
$$

训练损失为负平均 IC：

$$
L_{\mathrm{IC}}
=
-\frac{1}{nT}
\sum_{t=1}^{T}
\sum_{r=1}^{n}
IC_{t,r}.
\tag{3}
$$

因此：

- 正 IC 会降低损失；
- 负 IC 会增大损失；
- 优化对象是每个时点上的资产横截面相关性；
- 它不是均方预测误差；
- 它也不是最大化 $|IC|$，Alpha 方向必须为正向。

论文只把 $y_t$ 称为 `future price movement` 或 `true return`，没有明确收益计算公式和预测期限。

### 4.2 协方差多样性损失

为了减少不同 Alpha 的冗余，论文引入：

$$
L_{\mathrm{cov}}
=
\frac{1}{n^2T}
\sum_{t=1}^{T}
\sum_{r=1}^{n}
\sum_{\substack{s=1\\s\neq r}}^{n}
|C_{rs,t}|.
\tag{4}
$$

$C_{rs,t}$ 表示因子 `r` 和 `s` 的协方差。结合 $Z_t\in\mathbb R^{n\times m}$ 和逐时点求和，公式表达的自然维度是每个时点在资产横截面上计算因子协方差。但论文没有定义协方差估计式、样本分母和缺失资产处理。

公式有以下重要性质：

1. 惩罚的是 covariance，而不是 correlation。论文文字使用“降低相关性”，但公式明确写的是协方差。
2. 分母是 $n^2T$，不是 $n(n-1)T$。
3. $C_{rs}$ 和 $C_{sr}$ 都进入求和，每个非对角对称项会被计算两次。
4. 使用绝对值，因此正协方差和负协方差都会被惩罚；该项追求低线性依赖，而不是鼓励负相关因子。
5. 协方差具有尺度敏感性。若所有 Alpha 输出乘以 $\epsilon>0$，IC 理论上不变，而协方差损失缩小为 $\epsilon^2$ 倍。因此该目标存在压缩 Alpha 输出幅度的尺度退化倾向，论文没有讨论相应的输出尺度约束。

### 4.3 总损失

Stage I 的总损失为：

$$
L=L_{\mathrm{IC}}+\lambda L_{\mathrm{cov}}.
\tag{5}
$$

论文实验设置：

$$
\lambda=0.1.
$$

Stage I 使用 Adam，学习率为 $10^{-3}$。

## 5. Stage II：从 Alpha 图到投资组合

Stage II 不再直接读取原始市场特征，而是使用 Stage I 生成的 Alpha：

$$
s_t=Z_t.
$$

Algorithm 1 先加载已训练的 Stage I 模型 $M$，随后只写明更新策略参数 $\theta$ 和价值网络参数 $\phi$。按论文描述，Stage II 把 $M$ 作为固定 Alpha 生成器，没有给出联合端到端更新步骤。

### 5.1 因子完全图

Stage II 构造一个包含 `n` 个节点的完全图：

- 节点 `i` 是第 `i` 个 Alpha；
- 节点特征是 $Z_t^i\in\mathbb R^m$，即该 Alpha 在全部资产上的当前暴露；
- 每个因子节点与所有其他因子节点相连。

因此这里的图节点不是股票。股票关系已经在 Stage I 的跨资产注意力中处理，Stage II 的 GAT 处理的是因子关系。

### 5.2 GAT 注意力系数

论文公式 (7) 对因子 `i,j` 计算：

$$
e_{ij}
=
\operatorname{LeakyReLU}
\left(
\vec a^\top
[WZ_t^i\,\Vert\,WZ_t^j]
\right),
\tag{7}
$$

其中 $\Vert$ 表示拼接。

对因子 `i` 的全部邻居进行 softmax：

$$
\alpha_{ij}
=
\frac{\exp(e_{ij})}
{\sum_{k=1}^{n}\exp(e_{ik})}.
\tag{8}
$$

所以：

$$
\sum_j\alpha_{ij}=1.
$$

论文随后写出邻居聚合：

$$
h_i
=
\sigma
\left(
\sum_{j=1}^{n}
\alpha_{ij}Wh_j
\right).
\tag{9}
$$

公式 (9) 存在符号不一致：$h_i$ 正在被定义，右侧却已使用 $h_j$，而公式 (7) 的节点输入是 $Z_t^j$。全文能确定的是“对因子节点表示进行注意力加权聚合”，但不能仅凭本文判断 $h_j$ 是前一层表示还是排版笔误。

论文说明使用多头注意力，但没有给出：

- GAT 层数；
- 注意力头数；
- 每头维度；
- 多头结果采用拼接还是平均；
- 是否显式加入 self-loop。

### 5.3 GAT 输出因子权重

每个因子表示经过线性映射和因子维 softmax：

$$
q_t^i
=
\frac{
\exp(W_oh_i+b_o)
}{
\sum_{k=1}^{n}
\exp(W_oh_k+b_o)
}.
\tag{10}
$$

因此：

$$
q_t^i>0,
\qquad
\sum_iq_t^i=1.
$$

这使得因子组合是凸组合：

- 不能直接给某个因子负权重；
- 不能直接翻转因子方向；
- 但单个神经 Alpha 在不同资产上的暴露本身仍可正可负。

### 5.4 因子权重转为资产信号

论文写作：

$$
v_t=q_t*Z_t.
$$

原文没有定义 `*`。从维度看，要从 $q_t\in\mathbb R^n$ 和 $Z_t\in\mathbb R^{n\times m}$ 得到 $m$ 维资产信号，只能沿因子维加权求和：

$$
v_{t,a}
=
\sum_{r=1}^{n}
q_t^rZ_{t,a}^r,
$$

即：

$$
v_t=q_t^\top Z_t\in\mathbb R^m.
$$

这是基于论文张量维度的消歧，不是正文明确写出的矩阵乘法符号。

### 5.5 Top-G 资产与最终权重

令 $\mathcal G_t$ 为 $v_t$ 中信号最高的 `G` 个资产。最终资产权重为：

$$
w_{t,a}
=
\begin{cases}
\dfrac{\exp(v_{t,a})}
{\sum_{j\in\mathcal G_t}\exp(v_{t,j})},
&a\in\mathcal G_t,\\[8pt]
0,
&a\notin\mathcal G_t.
\end{cases}
\tag{6}
$$

由公式可确定该组合：

- 只持有 Top-G 资产；
- 权重非负；
- 权重总和为 1；
- 没有显式现金仓位；
- 没有空头；
- 即使 Top-G 信号全部为负，softmax 仍会满仓持有这些资产。

论文没有给出具体的 `G`，仅凭论文无法原样复现实验的资产集中度。

## 6. MDP、组合收益和交易成本

论文第 3.2 节定义价格相对向量：

$$
p_{t,a}
=
\frac{\operatorname{close}_{t,a}}
{\operatorname{close}_{t-1,a}}.
$$

未扣交易成本的组合净收益为：

$$
\widetilde r_t=w_t^\top p_t-1.
$$

若交易成本比例为 $c_t$，最终 reward 为：

$$
r_t
=
(\widetilde r_t+1)(1-c_t)-1.
$$

等价于：

$$
r_t
=
(w_t^\top p_t)(1-c_t)-1.
$$

这不是简单的 $\widetilde r_t-c_t$，而是对组合总值乘以 $(1-c_t)$。

论文实验给出的交易费率为 `0.25%`，但没有定义 $c_t$ 如何由新旧权重或换手率计算。因此费率是论文明确参数，具体换手成本计算式不是论文明确内容。

## 7. PPO 训练流程及论文缺口

Algorithm 1 给出的 Stage II 训练流程为：

1. 初始化策略网络 $\pi_\theta$ 和价值网络 $v_\phi$；
2. 初始化缓冲区 $D$；
3. 加载 Stage I 模型 $M$；
4. 每个 episode 初始化市场状态；
5. 计算 $Z_t=M(X_t)$；
6. 采样动作 $a_t\sim\pi_\theta(a_t\mid Z_t)$；
7. 执行动作并取得 reward 和下一期行情；
8. 计算 $Z_{t+1}=M(X_{t+1})$；
9. 保存 $(Z_t,a_t,r_t,Z_{t+1})$；
10. episode 结束后计算优势 $\widehat A_t$；
11. 用梯度下降更新 $\theta$ 和 $\phi$。

论文没有给出 PPO 的实际损失和训练参数，包括：

- 动作概率分布；
- old/new action log-prob；
- PPO clipped surrogate objective；
- clip range；
- 折扣因子 $\gamma$；
- GAE 参数；
- value loss；
- entropy bonus；
- minibatch size；
- PPO epoch 数；
- episode 数量；
- buffer 的清空和复用边界。

此外存在一个关键不一致：

- Algorithm 1 写 $a_t\sim\pi_\theta(\cdot\mid Z_t)$，动作由随机策略采样；
- 公式 (10) 直接通过 softmax 产生确定性的 $q_t$。

论文没有解释如何从确定性的 GAT softmax 输出构造 PPO 所需的随机策略与 action log-prob。因此只能确定作者使用 PPO 优化 GAT 因子权重策略，不能从本文唯一恢复具体 PPO 实现。

## 8. AlphaGAT 的自适应机制

AlphaGAT 没有显式的牛市、熊市或 regime 分类器，也没有单独的市场状态标签。

它的自适应来自：

1. 每个时点根据最近 30 期行情重新生成 $Z_t$；
2. GAT 根据当前 Alpha 暴露和因子间关系重新计算注意力；
3. 得到随时间变化的 $q_t$；
4. $q_t$ 改变资产综合信号 $v_t$；
5. Top-G 集合和最终组合权重随之变化；
6. PPO 通过组合收益与交易成本反馈训练这一映射。

其策略学习对象可以概括为：

$$
Z_t\longmapsto q_t\longmapsto w_t.
$$

GAT 图本身没有时间边。时间信息主要由 Stage I 的历史窗口编码，GAT 的动态性来自每个时点重新计算因子图注意力。

## 9. 实验如何支持各模块

### 9.1 Stage I 架构消融

Table 4 比较：

- TimeMixer；
- CTimeMixer：加入 Conv1D；
- ATimeMixer：加入跨资产注意力；
- CATimeMixer：同时使用 Conv1D 和跨资产注意力。

CATimeMixer 报告结果为：

| 市场 | IC | RankIC |
| --- | ---: | ---: |
| DJIA | 0.026 | 0.027 |
| HSI | 0.022 | 0.023 |
| CSI | 0.014 | 0.016 |
| CRYPTO | 0.039 | 0.038 |

四个数据集上，CATimeMixer 报告的 IC 和 RankIC 均高于基础 TimeMixer，支持“多尺度 Conv1D 与跨资产注意力结合”的有效性。

不过 Table 4 没有单独移除 $L_{\mathrm{cov}}$，因此不能独立量化协方差损失带来的提升。

### 9.2 GAT 与 RL 消融

Table 3 比较：

- `ours`：GAT + RL；
- `MLP`：用 MLP 替换 GAT，但保留 RL；
- `rand`：随机因子权重；
- `top-IC`：依据上一期 IC 的权重规则；
- `equal`：等权因子组合。

累计财富结果为：

| 方法 | DJIA | HSI | CSI | CRYPTO |
| --- | ---: | ---: | ---: | ---: |
| AlphaGAT | 1.428 | 1.359 | 1.239 | 3.288 |
| MLP | 1.357 | 1.277 | 1.139 | 2.691 |
| random | 1.182 | 1.132 | 1.085 | 1.909 |
| top-IC | 1.228 | 1.167 | 1.114 | 1.766 |
| equal | 1.241 | 1.173 | 1.104 | 1.639 |

这组结果支持：

- 动态 RL 权重优于随机、等权和简单 IC 规则；
- 同样使用 RL 时，GAT 通常优于 MLP，说明因子关系建模具有价值。

但不能把结果概括成“GAT 在每个指标都优于 MLP”。例如 DJIA 的 Calmar Ratio 中，MLP 为 `1.732`，AlphaGAT 为 `1.507`。

正文对 `top-IC` 的描述为“根据上一期 IC 分配随机权重”，规则表述本身不够清楚，无法从论文恢复精确计算过程。

### 9.3 总体结果边界

Table 1 中 AlphaGAT 在多数市场和指标上领先，但不是所有指标都领先。例如 CRYPTO 的 Calmar Ratio 为：

$$
\operatorname{CR}_{\text{FinRL-Meta}}=4.120
>
\operatorname{CR}_{\text{AlphaGAT}}=3.661.
$$

因此更准确的表述是：AlphaGAT 在论文报告的大多数市场和指标上领先，而不是无例外地全面超过所有基线。

## 10. 论文明确给出的实验参数

| 项目 | 论文值 |
| --- | ---: |
| 原始特征数 | 8 |
| 历史窗口 | 30 |
| 神经 Alpha 数量 | 64 |
| CATimeMixer 堆叠层数 | 3 |
| 隐藏维度 `c` | 512 |
| Stage I 优化器 | Adam |
| Stage I 学习率 | $10^{-3}$ |
| 协方差权重 $\lambda$ | 0.1 |
| Stage II 算法 | PPO |
| Stage II 学习率 | $5\times10^{-4}$ |
| 交易费率 | 0.25% |
| RL 实验次数 | 5 个不同随机种子 |
| 超参数选择 | validation 调优、test 报告 |

数据划分为：

| 数据集 | 资产数 | Train | Validation | Test |
| --- | ---: | --- | --- | --- |
| DJIA | 29 | 2010-01 至 2020-09 | 2020-09 至 2022-01 | 2022-01 至 2023-06 |
| HSI | 56 | 2010-01 至 2020-09 | 2020-09 至 2022-01 | 2022-01 至 2023-06 |
| CSI | 98 | 2010-01 至 2020-09 | 2020-09 至 2022-01 | 2022-01 至 2023-06 |
| CRYPTO | 18 | 2018-01 至 2023-01 | 2023-01 至 2023-09 | 2023-09 至 2024-04 |

论文还说明因缺失数据排除了一些公司，但没有提供完整排除名单和动态成分处理方法。

## 11. 论文未披露、复现时不能擅自猜测的细节

### 11.1 Stage I

- 多尺度数量 `L`；
- trend/seasonal decomposition 的具体算法和参数；
- Conv1D kernel、通道、stride、padding 和激活函数；
- MHA 头数、投影维度和 mask；
- trend/seasonal 的精确融合运算；
- 多尺度输出的时间对齐和压缩方式；
- true return 标签公式与预测期限；
- 协方差估计分母及无效截面处理；
- 输入归一化、缺失值和退化因子处理；
- Stage I batch size、epoch 数、梯度裁剪和早停规则。

### 11.2 Stage II

- GAT 层数、头数、隐藏维度和 self-loop；
- 公式 (9) 中 $h_j$ 的准确含义；
- PPO 动作分布及确定性 $q_t$ 与随机动作的对应关系；
- clipped objective、GAE、折扣因子、entropy/value 系数；
- rollout、minibatch、PPO epoch 和 episode 数量；
- Top-G 的具体 `G`；
- $c_t$ 与换手率的映射；
- 初始组合权重、停牌和缺失资产处理；
- 训练期、验证期和测试期之间的模型选择与恢复细节。

这些缺失项意味着论文足以还原 AlphaGAT 的算法思想、主要张量流、Stage I 目标函数和 Stage II 组合映射，但不足以唯一复现全部实验实现。任何补全方案都应明确标注为成熟算法标准实现或复现假设，而不能写成论文原文设定。

## 12. 阅读时最容易混淆的四个边界

1. AlphaGAT 生成的是神经 Alpha，不是公式 Alpha。
2. Stage I 的 attention 建模资产关系，Stage II 的 GAT 建模因子关系。
3. PPO 的 action 是因子权重，不是直接的资产权重；资产权重还要经过因子加权、Top-G 和 softmax。
4. 论文文字说降低因子相关性，但公式实际惩罚的是原始 Alpha 暴露的 covariance。

从算法定位看，AlphaGAT 的主要价值不是搜索新的可解释表达式，而是把“神经因子生成、因子去冗余、动态因子启停和最终组合决策”连接成一个两阶段投资策略。
