# 可迁移到因子挖掘的相邻方法

> 本文汇总 `adjacent` 路线收录的工作：它们不是因子挖掘论文，但已收录的因子挖掘工作直接借用，或可以借用它们的机制。逐篇内容见各速读卡。“迁移时要注意”一栏是本仓库的迁移分析，不是原论文的结论。

## 1. 对照

| 方法 | 原领域 | 迁移对应的问题 | 已收录工作中的借用 |
| --- | --- | --- | --- |
| [DSR](../../notes/cards/2019_DSR.md) | 符号回归 | P1 采样时约束，P4 只有终端奖励的策略梯度 | RiskMiner 的风险偏好优化与 DSR 的高分位更新同一思路 |
| [GFlowNet](../../notes/cards/2021_GFlowNet.md) | 分子等离散对象生成 | P3 代理奖励加少量真实评价，P4 离策略训练，P7 按奖励成比例采样 | AlphaSAGE 采用 GFlowNet 框架 |
| [Trajectory Balance](../../notes/cards/2022_TrajectoryBalance.md) | GFlowNet 训练目标 | P4 整条轨迹的信用分配，P7 更分散的样本 | AlphaSAGE 的训练损失 |
| [DeepMind AlphaEvolve](../../notes/cards/2025_DeepMind-AlphaEvolve.md) | 科学与算法发现中的代码演化 | P1 LLM 变异，P2 可读程序作为解，P3 评价级联，P7 质量-多样性程序库 | FactorEngine、CogAlpha 属同类 LLM 代码演化 |
| [GiGPO](../../notes/cards/2025_GiGPO.md) | 多轮 LLM 智能体强化学习 | P4 步骤级相对优势 | 未见借用；QuantEvolver、Alpha-R1 只用回合级 GRPO |
| [Tree-GRPO](../../notes/cards/2025_Tree-GRPO.md) | 多轮 LLM 智能体强化学习 | P3 共享前缀省预算，P4 由结果奖励构造过程信号 | 未见借用 |
| [Publication Bias](../../notes/cards/2022_PublicationBias.md) | 资产定价的发表偏差与多重检验 | P5 从一组候选 t 值估出收缩幅度与 FDR | 未见借用；与 QBX 的试验计数互补 |
| [Sequential Cauchy](../../notes/cards/2023_SequentialCauchy.md) | 多重检验 | P5 强 FWER 控制并指认个体显著项 | 未见借用；与 EvoQuantLab 的置换 p 值互补 |

## 2. 迁移点

### 2.1 只看高分尾部：DSR

DSR 把表达式生成看作只有终端奖励的强化学习，并指出标准策略梯度优化的是平均表现，而挖掘只需要最好的少数样本。批内奖励分位数作基线、只用高分尾部更新，是 RiskMiner 这类方法的直接来源。

迁移时要注意：在低信噪比的 IC 上，只追高分尾部更容易选中偶然的高分，需要配合独立的样本外检验（对应 P5）。

### 2.2 把“一批彼此不同的好因子”写成目标：GFlowNet 与 Trajectory Balance

GFlowNet 学习按奖励成比例采样，多样性来自训练目标本身，不必在最大化目标之外另加惩罚；它可以离策略训练，适合“代理奖励打分、只把多样批次送真实评价”的多轮流程。Trajectory Balance 用整条轨迹上的一个残差同时更新各步概率。自回归生成公式时后向概率恒为 1，损失化为 \((\log Z + \sum_t \log P_F - \log R)^2\)，与[生成器如何使用真实 IC](../generator_training_with_ic.md)中对 AlphaSAGE 的说明一致。

迁移时要注意：

- IC 要先变换成正奖励。
- 按 token 前缀生成时状态图是树。Trajectory Balance 论文第 4 节指出，树状态图上的 GFlowNet 等价于带熵正则的强化学习，因此与 PPO 比较时要统一熵设置。
- 因子池依赖的奖励会让目标分布不平稳，\(\log Z\) 追踪的是一个移动的目标。

### 2.3 LLM 代码演化的工程接口：DeepMind AlphaEvolve

“初始程序、可演化代码块、返回指标字典的评价函数”这套接口，以及先小规模初筛、再全量评价的评价级联，可以直接套用到代码因子挖掘上。

迁移时要注意：原论文的评价器多是可验证的确定性指标，回测 IC 却是带噪的样本内估计，长期爬山等于大量多重检验。样本外区间必须独立保留，代码因子还要做前视检查（对应 P5、P6）。

### 2.4 多轮智能体的步骤级信用：GiGPO 与 Tree-GRPO

两者都在不增加 critic 的前提下，把回合级结果奖励细化为步骤级信号。GiGPO 把跨轨迹重复出现的状态归为一组，Tree-GRPO 在分叉点比较兄弟子树。对多轮挖掘智能体（例如 AlphaPilot、AlphaDiverse），可以复用已完成的前缀，并用兄弟分支的 IC 差异做前缀级信用分配。

迁移时要注意：

- 深层公式前缀很少精确重复，智能体状态里还带反馈文本，“相同状态”可能需要用 AST 规范形或语义等价来定义。
- 因子挖掘的主要成本在叶节点回测；前缀共享能省多少，取决于中间轮次是否也调用评价。
- 低信噪比下，兄弟分支之间的 IC 差异需要树间基线兜底。

## 3. 未收录

- `Efficient Constant Optimization for Symbolic Regression with GPU-Accelerated Tree-Based Genetic Programming`（arXiv 2609.03352）：最小二乘残差目标、数据行独立的评价内核都与截面 IC 和时序、截面算子不匹配；“结构搜索与常数拟合分层”的思路已由 DSR 和 FactorEngine 覆盖。

### 2.5 把搜索规模纳入显著性：Publication Bias 与 Sequential Cauchy

这两篇不是因子挖掘方法，但直接回答“一批挖出来的因子有多少是真的”。Publication Bias 从一组候选的 t 值估出经验贝叶斯收缩幅度与预期错误发现比例，并给出“短窗口衰减是选择偏差的上界、长窗口衰减才是期望收益变化”的归因规则；Sequential Cauchy 只看 p 值、对相关结构不作参数假设，能强控制族错误率并指认具体哪个因子显著。

迁移时要注意：

- 两者都需要知道检验族有多大。挖掘流程中候选总数往往没有记录，这正是 QBX 试验计数要补的前提。
- 与 EvoQuantLab 的等预算区块置换相比，一个是解析估计、一个是重采样；后者不依赖对零假设的解析形式，但计算量更大。
- “提高因子入选门槛”不等于做了多重检验校正，“去掉流动性等风格暴露”也不等于消掉了数据窥探——Publication Bias 原文专门澄清了这两点。
