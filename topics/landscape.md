# 因子挖掘研究全景：路线与阅读地图

本文以显式公式、符号、DSL 和代码因子挖掘为主，纳入因子表示与组合机制相关的神经方法。先比较表达、搜索、学习与评价，再给出分组导读；全部工作及单篇证据见[论文索引](../INDEX.md)。分组可以交叉，不表示互斥分类或方法排名。

主要观察：

1. 单因子质量、池内互补性与下游组合是不同优化单位。AlphaGen 把组合贡献用于公式生成；AlphaPADI 直接生成整池；AlphaForge 同时包含代理生成与动态组合，不能只归为筛选器。
2. RL、MCTS、GFlowNet 和 LLM 描述不同层面的机制。结构表示、候选提议器、训练目标与流程编排可以组合；使用 LLM 不意味着候选一定由 LLM 提出。
3. 生成时约束可以减少形式非法候选，但不能替代实现后的数值、时间可用性与样本外检查。
4. 提示反馈、结构化记忆与参数训练是不同的经验利用方式。采用强化微调还需计入种子生成、训练和推理的总成本。
5. 搜索效率、预测表现与证据可复核性需要分别评价；高 IC、低相关或代码公开均不足以单独证明组合有效性。

## 1. 总览与阅读地图

比较一篇工作时，先确定优化单位、候选来源、学习信号与评价协议。第 2 节提供各类代表工作；训练、算子与实验口径的详细比较分别见[训练机制](generator_training_with_ic.md)、[算子空间](operator_space.md)与[评估口径](evaluation_protocol.md)。

### 技术路线总览

下表列出机制组合的代表，不把表示方式与搜索算法一一绑定。RPN 是逆波兰表示，AST 是抽象语法树，DSL 是领域特定语言；同一表示可以由不同提议器搜索。

| 方法类型 | 表达与候选来源 | 学习或选择依据 | 池与下游使用 |
| --- | --- | --- | --- |
| 人工公式库 | 人工定义公式，如 Alpha101 | 原论文的信号与持仓统计；后续研究可用其作固定参照 | 固定库不等于经过统一协议优化的组合 |
| GP / AutoML | 树或类型化程序；变异、交叉、层次扩展 | 候选 fitness、相似度与质量-多样性选择 | 搜索种群、交付池和组合使用集需区分 |
| RL 与树搜索 | RPN、寄存器程序或文法；策略采样与 MCTS | 组合贡献、终端或中间奖励；策略梯度或回报分布学习 | 池可参与奖励与状态，也可只作准入过滤 |
| GFlowNet | 逐步构造离散对象，如 AlphaSAGE 的部分公式 | 奖励比例分布目标与轨迹平衡约束 | 多模式采样不自动保证池内行为低相关 |
| 可微代理生成 | AlphaForge 从噪声生成公式表示 | Predictor 拟合真实 fitness，为 Generator 提供梯度 | 真实评价后入库，使用阶段动态筛选与拟合 |
| LLM / Agent | 提出假设、实现或改写公式、代码；也可只做评价与调度 | 提示反馈、记忆、演化选择或强化微调 | 池、轨迹与记忆承担不同角色，须逐篇区分 |
| 神经因子 | 网络学习隐式信号、离散表示或条件载荷 | 收益预测、重构与去相关等目标，依论文而定 | 联合训练与分阶段组合均存在，不能一概视为端到端 |

### 三条演进主线

以下归纳三个相互关联的方向。年份标识代表工作的首次公开时间，用于定位脉络；这些方向并存，不表示旧方法已被替代。

**主线一：优化单位扩展到因子池与组合。** Alpha101（2016）提供固定人工库，AutoAlpha（2020）用层次化搜索提高候选发现效率，AlphaGen（2023）把新因子入池后的组合 IC 边际贡献作为奖励。RiskMiner（2024）在中间奖励中惩罚与池内因子的重复；AlphaForge（2024）将代理生成与动态组合分开；AlphaSAGE（2025）以奖励比例采样目标配合新颖性奖励。AlphaPareto（2026）把池编码进策略状态，AlphaPADI（2026）进一步以整个池为生成与偏好学习对象（见 2.2）。使用阶段则有 Alpha-R1 的启停筛选与 AlphaLedger 的扣费组合边际贡献账本（见 2.3）。当池影响候选奖励时，状态表示与目标变化需一起考虑。

**主线二：反馈进入不同层次的学习与记忆。** 离散公式的真实 IC 无法经 token 选择直接反传。RiskMiner 的中间评价、TLRS 的专家子序列塑形、QFR 的贪婪基线与信息比率、AlphaQCM 的累积回报分布方差，分别改变反馈密度、方差或探索。AlphaForge 训练可微 Predictor，其分数经 Gumbel-Softmax 近似回传到 Generator，真实 IC 仍在梯度路径之外（见 2.3）。LLM 工作中，Alpha-GPT 与 QuantaAlpha 利用提示和搜索反馈；QuantEvolver、AlphaPilot、AlphaDiverse 用强化微调更新模型参数，AlphaLedger 用在线策略蒸馏提供动作监督（见 2.9）；AlphaMemo 则更新编辑信用记忆，不训练策略参数。这些机制需按决策对象与总成本比较。

**主线三：评价覆盖选择过程与证据链。** 反复评价与择优会引入选择偏差，时间泄漏与结果留存又影响证据可信度。AlphaEval（2025）提出免回测的多维代理指标；FactorBench（2026）分因子、池和扣费组合三层评价；QBX（2026）将时间可用性检查、内容身份和试验记录前置（见 2.7、2.8）。Auditing LLM Alpha-Factor Mining 审视指标总体与留存偏差；EvoQuantLab 提出等预算置换的搜索赢家诊断，但其 v2 未给出完整置换配置与校准产物。相邻方法中，Publication Bias 在发表选择模型下估计收缩与方向错误风险，Sequential Cauchy 在有效 p 值和分布假设下控制族错误率。账本、搜索诊断与候选族推断的分工见[搜索规模与过拟合校正](search_multiplicity.md)。

### 搜索与使用的边界

| 环节 | 非 LLM 生成与组合中的例子 | LLM / Agent 中的例子 | 比较要点 |
| --- | --- | --- | --- |
| 输入与表示 | AlphaGen 的 RPN、Alpha2 的寄存器程序、AlphaCFG 的文法 | Alpha-GPT 的研究想法与字段检索、AlphaSchema 的交易语义计划 | 输入数据与约束是否相同；计划空间与实现空间分开说明 |
| 候选提议 | 策略逐步采样、MCTS 展开、GFlowNet 构造 | LLM 改写代码或思路树；AlphaSchema 在模型外采样计划 | 谁提出候选，谁只负责实现、评价或分配预算 |
| 评价与反馈 | AlphaGen 的组合奖励、RiskMiner 的中间评价、AlphaQCM 的探索奖励 | Hubble 的家族评分与检索、AlphaMemo 的编辑信用、QuantEvolver 的强化微调 | 评价对象、奖励依赖的状态、反馈是否写入参数 |
| 下游使用 | AlphaForge 的动态筛选与拟合、AlphaGAT 的图强化学习组合 | Alpha-R1 的因子启停、EFS 的稀疏组合 | 生成模块是否参与组合训练；使用原生还是共同组合器 |

神经表示与组合也可能分阶段学习。[AlphaGAT](../notes/deep/2025_AlphaGAT.md) 先监督训练因子表示，再训练组合策略；其算法不能概括为两个模块端到端联合优化。HRFT/IRFT 的高频风险因子、CAVB 的隐因子重构与收益预测，与日频公式 alpha 有不同对象与证据口径，比较前需明确这些边界。

## 2. 分组导读

本节按技术路线分组，说明每组在解决什么、彼此是什么关系；每组只点名代表工作。全部收录工作、时间、会议和问题标注以[论文索引](../INDEX.md)为准。

### 2.1 公式库、遗传规划与 AutoML 基线

这一组工作定义了公式化 Alpha 的表达范式和早期自动搜索方式，是后续 RL/LLM 方法的算子库、种子库和 baseline 来源。

代表工作：[Alpha101](../notes/cards/2016_Alpha101.md)、[AutoAlpha](../notes/cards/2020_AutoAlpha.md)、[AlphaEvolve](../notes/cards/2021_AlphaEvolve.md)、[Warm Start GP](../notes/cards/2024_WarmStartGP.md)。

### 2.2 RL、结构化搜索与池生成

这一组通过策略学习、树搜索或生成模型探索离散表达式空间；分别关注信用分配、结构约束、采样分布与池级目标。

代表工作：[AlphaGen](../notes/cards/2023_AlphaGen.md)、[Synergistic RL](../notes/cards/2024_SynergisticRL.md)、[RiskMiner](../notes/cards/2024_RiskMiner.md)、[Alpha2](../notes/cards/2024_Alpha2.md)、[QFR](../notes/cards/2024_QFR.md)、[AlphaQCM](../notes/cards/2025_AlphaQCM.md)、[TLRS](../notes/cards/2025_TLRS.md)、[AlphaSAGE](../notes/cards/2025_AlphaSAGE.md)、[AlphaCFG](../notes/cards/2026_AlphaCFG.md)。

池级生成的代表是 [AlphaPADI](../notes/cards/2026_AlphaPADI.md)：在池上下文中做层次化离散扩散，将池级奖励转成池对偏好。[AlphaPareto](../notes/cards/2026_AlphaPareto.md) 把池编码进 PPO 状态并采用多目标奖励。训练信号的扩展还包括同前缀兄弟动作的局部蒸馏（[AlphaG-OPD](../notes/cards/2026_AlphaG-OPD.md)）与跨回合记忆加 SDE 回报评论家（[AlphaRJM](../notes/cards/2026_AlphaRJM.md)）。

### 2.3 因子池、动态组合与筛选

这一组不一定只关注“生成公式”本身，而是解决候选因子如何去重、动态加权、按市场状态启停，以及如何把因子挖掘结果接入下游投资目标。

代表工作：[AlphaForge](../notes/cards/2024_AlphaForge.md)、[AlphaGAT](../notes/cards/2025_AlphaGAT.md)、[EFS](../notes/cards/2025_EFS.md)、[Alpha-R1](../notes/cards/2025_Alpha-R1.md)、[AlphaPROBE](../notes/cards/2026_AlphaPROBE.md)、[AlphaLedger](../notes/cards/2026_AlphaLedger.md)、[GoAnt](../notes/cards/2026_GoAnt.md)。

### 2.4 LLM 驱动的因子生成

这一组把 LLM 当作想法生成器、公式实现器或结构变异算子：LLM 负责提出与改写表达式，搜索与评价往往仍由传统搜索器或回测循环完成。它们与 2.2 的 RL 主线不是替代关系，而是换了“谁提候选”这一步。

代表工作：[Alpha-GPT](../notes/cards/2023_Alpha-GPT.md)、[QuantAgent](../notes/cards/2024_QuantAgent.md)、[Alpha-GPT 2.0](../notes/cards/2024_Alpha-GPT2.md)、[LLM Strategy Finding](../notes/cards/2024_LLMStrategyFinding.md)、[AlphaAgent](../notes/cards/2025_AlphaAgent.md)、[Alpha-Jungle](../notes/cards/2025_Alpha-Jungle.md)、[CogAlpha](../notes/cards/2025_CogAlpha.md)、[QuantaAlpha](../notes/cards/2026_QuantaAlpha.md)、[FactorMiner](../notes/cards/2026_FactorMiner.md)、[Hubble](../notes/cards/2026_Hubble.md)、[LineageEvo](../notes/cards/2026_LineageEvo.md)、[TreEvo](../notes/cards/2025_TreEvo.md)、[AlphaMemo](../notes/cards/2026_AlphaMemo.md)、[AlphaLogics](../notes/cards/2026_AlphaLogics.md)、[AlphaSeek](../notes/cards/2026_AlphaSeek.md)、[CosmosAlpha](../notes/cards/2026_CosmosAlpha.md)、[AlphaRLM](../notes/cards/2026_AlphaRLM.md)、[AlphaSchema](../notes/cards/2026_AlphaSchema.md)、[AlphaDiverse](../notes/cards/2026_AlphaDiverse.md)。

### 2.5 LLM / Agent 的研究流程

这一组关注的是流程本身，而不是某种表达式表示：研究轨迹怎么组织、经验记忆存什么、评价预算怎么分配、多个智能体怎么分工。同一篇工作通常还会落在 2.4 或 2.2 的某条表示路线上。

代表工作：[RD-Agent(Q)](../notes/cards/2025_RD-Agent-Quant.md)（因子与模型双闭环）、[EvoQuantLab](../notes/cards/2026_EvoQuantLab.md)（类型化 GP 快循环与协议诊断慢循环，见[精读](../notes/deep/2026_EvoQuantLab.md)）、[FactorEngine](../notes/cards/2026_FactorEngine.md)（程序池演化）、[QuantEvolver](../notes/cards/2026_QuantEvolver.md)（强化微调）、[AlphaPilot](../notes/cards/2026_AlphaPilot.md)、[AlphaLedger](../notes/cards/2026_AlphaLedger.md)、[AutoScientist-Quant](../notes/cards/2026_AutoScientist-Quant.md)、[X-Alpha](../notes/cards/2026_X-Alpha.md)、[AgonAlpha](../notes/cards/2026_AgonAlpha.md)、[Agora/SJS](../notes/cards/2026_Agora-SJS.md)、[EFS](../notes/cards/2025_EFS.md)、[Alpha-R1](../notes/cards/2025_Alpha-R1.md)、[AgenticFactorInvesting](../notes/cards/2026_AgenticFactorInvesting.md)。

### 2.6 表达空间扩展与风险因子生成

这一组与传统日频 Alpha 公式挖掘不完全同构，但对连续参数、符号-数值混合生成、高频风险因子和更宽表达空间有参考价值。

代表工作：[HRFT/IRFT](../notes/cards/2024_HRFT.md)（分钟高频风险因子）、[TextToAlpha](../notes/cards/2025_TextToAlpha.md)（季度披露文本，给出完整的文本到打分链路）、[MAPLE](../notes/cards/2026_MAPLE.md)（单模型多输出的神经 Alpha）、[Det-MASO](../notes/cards/2026_Det-MASO.md)（多智能体神经因子，智能体间相关矩阵惩罚）、[PRISM-VQ](../notes/cards/2026_PRISM-VQ.md)（离散隐因子，保留“载荷 × 因子”结构）、[CAVB](../notes/cards/2025_CAVB.md)（对抗变分隐因子与分位条件载荷，区分重构和历史因子均值预测）、[GoAnt](../notes/cards/2026_GoAnt.md)（订单簿数据）。

### 2.7 基准与统一评测

这一组给出统一的数据、切分、指标或执行契约，用来横向比较多个挖掘方法。读者关心的是“怎么比”。

代表工作：[AlphaEval](../notes/cards/2025_AlphaEval.md)（免回测的代理指标）、[FactorBench](../notes/cards/2026_FactorBench.md)（因子 → 池 → 扣费组合三层）、[Look-Ahead-Bench](../notes/cards/2026_Look-Ahead-Bench.md)（LLM 前视偏差）、[MarketSenseAI](../notes/cards/2026_MarketSenseAI.md)（实时生成信号 + 零分布检验）。口径差异与已知会误导比较的情形见[评估口径对照](evaluation_protocol.md)。

### 2.8 审计、复现与泄漏检查

这一组审视证据链本身：结果怎么留存、指标口径是否一致、有没有做前视检查、试验次数记不记。读者关心的是“怎么证明”。它与 2.11 的显著性检验相邻。

代表工作：[Auditing LLM Alpha-Factor Mining](../notes/cards/2026_AuditingLLMAlpha.md)（留存偏差与指标来源）、[QBX](../notes/cards/2026_QBX.md)（编译期时间可用性、内容身份与试验账本）、[AgonAlpha](../notes/cards/2026_AgonAlpha.md)（独立上下文审稿与重跑否决）、[EvoQuantLab](../notes/cards/2026_EvoQuantLab.md)（冻结协议与等预算置换）。

### 2.9 LLM 挖掘的训练化与语义空间

这一组区分参数训练与搜索表示。前者把评价反馈写入模型参数，后者显式组织想法、语义计划或演化轨迹；采用结构化表示不意味着进行了模型训练。

- 参数训练：[QuantEvolver](../notes/cards/2026_QuantEvolver.md)（GRPO 与 DiCo 奖励）、[AlphaPilot](../notes/cards/2026_AlphaPilot.md)（多轮工具调用）、[AlphaDiverse](../notes/cards/2026_AlphaDiverse.md)（分角色联合 GRPO）、[AlphaLedger](../notes/cards/2026_AlphaLedger.md)（在线策略蒸馏）。
- 表示与搜索：[AlphaSchema](../notes/cards/2026_AlphaSchema.md)（模型外的语义计划搜索）、[TreEvo](../notes/cards/2025_TreEvo.md)（思路树演化）、[LineageEvo](../notes/cards/2026_LineageEvo.md)（谱系演化）、[CosmosAlpha](../notes/cards/2026_CosmosAlpha.md)（多关系图与 Pareto 选父）、[AlphaSeek](../notes/cards/2026_AlphaSeek.md)（研究轨迹演化）、[AlphaLogics](../notes/cards/2026_AlphaLogics.md)（先验中间表示）。

### 2.10 相邻方法

不是因子挖掘本身，但机制被已收录工作直接借用或可借用，例如 GFlowNet 的按奖励成比例采样、DSR 的风险寻求目标和多轮智能体的步骤级信用分配。逐篇见[可迁移的相邻方法](adjacent/transferable_methods.md)。

代表工作：[GFlowNet](../notes/cards/2021_GFlowNet.md)、[Trajectory Balance](../notes/cards/2022_TrajectoryBalance.md)、[DSR](../notes/cards/2019_DSR.md)、[GiGPO](../notes/cards/2025_GiGPO.md)、[Tree-GRPO](../notes/cards/2025_Tree-GRPO.md)、[DeepMind AlphaEvolve](../notes/cards/2025_DeepMind-AlphaEvolve.md)、[Publication Bias](../notes/cards/2022_PublicationBias.md)、[Sequential Cauchy](../notes/cards/2023_SequentialCauchy.md)。

### 2.11 过拟合控制与显著性检验

这一组与 2.8 相邻，关注选择偏差诊断与显著性推断。经验信用校正、搜索赢家检验与候选族错误率控制有不同对象，不能据其一推断交付因子均有效。

代表工作：[EvoQuantLab](../notes/cards/2026_EvoQuantLab.md)（等预算区块置换）、[AlphaMemo](../notes/cards/2026_AlphaMemo.md)（经验复用的选择偏差）、[AgenticFactorInvesting](../notes/cards/2026_AgenticFactorInvesting.md)（准入闸门与样本外冻结）、[Publication Bias](../notes/cards/2022_PublicationBias.md)（经验贝叶斯收缩与 FDR）、[Sequential Cauchy](../notes/cards/2023_SequentialCauchy.md)（满足假设时的渐近强 FWER 控制）。
