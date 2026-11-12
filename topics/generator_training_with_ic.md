# 公式因子挖掘的三类训练方法

> 本文以 AlphaGen 的策略梯度、AlphaForge 的可微代理生成与 AlphaSAGE 的轨迹平衡为例，比较真实因子 IC 如何进入训练。文献版本、实验与披露边界见各篇笔记；不据此概括所有强化学习或生成方法。

## 1. 共同约束

三类方法最终都生成离散公式。真实 IC 由公式在行情面板上求值后与未来收益标签计算，无法经离散 token 选择直接反传到生成器参数。合法中间表达式也可能被评价；困难在于信用分配与离散选择，不是所有方法都只能在最终一步得到反馈。

真实 IC 分别用于奖励、Predictor 的监督标签和轨迹平衡的终端目标。策略梯度通常提高期望回报，风险寻求方法另强调高分尾部；可微代理优化预测评分，GFlowNet 则以奖励比例分布为目标。

训练奖励与准入条件需分别说明。相关性可以用于入库门槛，也可以连续影响奖励；AlphaForge 的 fitness 已包含合法性与相关性条件，AlphaSAGE 的新颖性项也进入终端奖励，不能把所有池规则都视为训练之后的筛选。

## 2. 对照

| 对照项 | 策略梯度（以 AlphaGen 为例） | AlphaForge | AlphaSAGE |
| --- | --- | --- | --- |
| 生成方式 | 从空序列逐步采样 token | 由噪声一次生成整条公式的 token 分布 | 从空序列逐步采样 token |
| 真实 IC 的角色 | 组合 IC 变化形成奖励，进入回报或优势估计 | 评价公式，监督 Predictor 拟合 fitness | 合成正终端奖励 R，以 log R 作为 Trajectory Balance 的匹配目标 |
| 梯度路径 | 回报或优势加权的 log pi(a_t given s_t) 梯度；PPO 另有概率比与裁剪 | Predictor 的分数经 Gumbel-Softmax 近似回到 Generator | 轨迹残差对 log P_F、log P_B 与 log Z 的梯度 |
| 生成器学到的对象 | 提高期望回报；不保证只采样一个最优公式 | 提高 Predictor 认为的 fitness，并用多样性损失拉开样本 | 以完整公式的采样概率正比于 R 为目标，成立依赖奖励与优化条件 |

## 3. 强化学习

AlphaGen 将公式生成建模为序列决策：状态是已有 token，动作是下一符号，主要组合奖励在完整公式生成后计算。RiskMiner 则评价合法中间表达式；两者都不通过真实 IC 对离散选择直接求导。

策略梯度不穿过 IC。简化的 REINFORCE 更新方向为 `E[(return - baseline) * grad_theta log pi_theta(trajectory)]`；正、负优势分别提供提高、降低对应轨迹对数概率的方向，但参数共享与批内聚合会影响最终变化。PPO 另使用裁剪的概率比目标。QFR 针对中间状态价值估计偏差提出无价值网络的 REINFORCE 与贪婪基线，这是该论文的论证，不表示价值网络在所有公式任务中都不可用。

奖励具体写什么，要和训练机制分开看。

- AlphaGen 论文把新因子加入当前池后、线性组合 IC 的提升作为回报。池子一变，同一条公式的奖励就变。
- 另一种条件性设计是 `reward = abs(IC)`，不通过相关性门槛时置零。若如此定义，过滤决定奖励是否为零；连续相关性惩罚则是不同目标。这不是所有强化学习方法的共同设定。

## 4. AlphaForge

AlphaForge 不沿 token 逐步接收终端奖励。Generator 从高斯噪声输出整条公式每个位置的 logits。语法 mask 和 Gumbel-Softmax 把 logits 变成可微的 token 分布，因此生成器参数到公式表示之间有梯度。

真实 IC 仍在梯度路径之外。论文先用已评价公式训练 Predictor，拟合满足合法性与相关性条件时取绝对 IC、否则为零的 fitness：

```text
L_P = sqrt((1/n) * sum_i (P(x_i) - fitness(x_i))^2)
```

然后冻结 Predictor，让 Generator 最大化预测分数，并惩罚两次采样过于相似：

```text
L_G = -P(x_1) + L_Diversity
```

两者交替训练：训练 Predictor 时使用真实标签；训练 Generator 时固定 Predictor 参数，梯度仍穿过 Predictor 回到 Generator。新公式经过真实评价后扩充评分样本，只有满足准入条件的公式才进入 Factor Zoo；评分样本集与准入库是不同集合。

## 5. AlphaSAGE

AlphaSAGE 也从空公式逐步采样 token。当前部分公式先还原成抽象语法树，RGCN 按操作数、窗口等关系编码，线性头给出下一个 token 的概率。网络输入是这条部分公式，不是行情面板。行情只在公式结束后用于计算奖励。

终端奖励是

```text
R = R_IC + lambda(T) * R_SA + eta(T) * (1 - max abs(IC_mutual))
```

R_IC 先计算每日截面 Pearson 相关系数，再对跨日均值取绝对值，即 `abs(mean_d Corr(alpha(X_d), y_d))`（原文式 12）；它不同于逐日绝对 IC 的均值。R_SA 衡量结构近邻的历史行为一致性，新颖性按与已有因子的最大绝对互相关连续减分；辅助项权重随训练进度变化（原文式 12–14）。R 是训练奖励，不是股票收益本身。

Trajectory Balance 的目标是

```text
P(alpha) = R(alpha) / Z
Z = sum_over_all_terminal_formulas R(alpha)
```

论文的轨迹平衡损失比较前向概率、反向概率与终端奖励（式 6）：

```text
residual = log Z_theta
         + sum_t log P_F(s_t given s_(t-1))
         - log R(s_n)
         - sum_t log P_B(s_(t-1) given s_t)
L_TB = residual^2
```

在标准 TB 中，终端奖励作为给定匹配目标，梯度经过模型概率与总流量参数，不对离散采样或历史 IC 求导。P_F、P_B 与 Z_theta 共同决定路径残差；不能只根据残差符号断言每个动作概率都会同向变化。AlphaSAGE 另加入前向动作熵正则，鼓励保持探索（式 15–16）。

标准 TB 可在同一次损失更新中联合学习前向策略、后向策略与 log Z；也允许固定合法的后向策略。若完整 token 前缀状态只有唯一前驱，则 P_B=1，反向项恒为零。AlphaSAGE 正文将前向与反向策略写为学习对象，但未充分展开反向策略的实现、参数共享及更新细节，不能用树状图的简化补全。绝对 IC 为非负量；总奖励在零 IC、退化截面等边界下如何满足 log R 所需的严格正值，仍未完整说明。

奖励比例采样是训练目标，其成立需要相应的轨迹覆盖与优化条件；新颖性参照和辅助权重变化会使目标移动。池筛选与后续动态组合是不同机制，详细范围见[AlphaSAGE 精读](../notes/deep/2025_AlphaSAGE.md)。


## 6. 阅读边界

- 论文依据分别见[AlphaGen](../notes/cards/2023_AlphaGen.md)、[QFR](../notes/cards/2024_QFR.md)、[AlphaForge](../notes/deep/2024_AlphaForge.md) 和 [AlphaSAGE v3](../notes/deep/2025_AlphaSAGE.md)；一般 TB 的条件见[原方法笔记](../notes/cards/2022_TrajectoryBalance.md)。
- 各论文的标签、股票池、算子表和池容量不同；本文只比较训练机制，不比较实验结果。
- AlphaForge 与 AlphaSAGE 的后续动态组合与生成器训练分阶段；AlphaGen 的池组合优化则参与训练奖励计算，不能把三者都概括为“组合不参与生成训练”。
