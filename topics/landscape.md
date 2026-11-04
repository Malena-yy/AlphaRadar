# 因子挖掘研究全景：路线与阅读地图

本文面向公式化 Alpha 因子挖掘方向，梳理传统公式库、遗传/AutoML、RL/MCTS/GFlowNet、动态组合、LLM/Agent/RFT 等相关工作。相比纯时间线，本文采用“先总览、再按技术路线分组”的组织方式；每个分组内部大体按论文首次公开或会议发表时间排序。

调研结论：
1. 公式化因子挖掘的主战场已经从“单因子高 IC 搜索”转向“可执行、低冗余、样本外稳定、可组合的因子池维护”。
2. AlphaGen、RiskMiner、Alpha2、AlphaCFG、AlphaSAGE 等工作代表公式生成与结构化搜索主线；AlphaForge、Alpha-R1、AlphaGAT 等工作更偏向因子池筛选、启停和动态组合。
3. 语法、维度、金融语义和复杂度约束应尽量前置到生成阶段。只依赖生成后过滤，会浪费大量回测预算，也容易让策略学习到无效动作。
4. LLM/Agent 路线的价值不在于替代 RL/搜索器，而在于提供研究假设、结构变异、代码实现、评价摘要、经验记忆和 RFT 训练数据。
5. 相关工作普遍强调 DSL/AST 安全约束、严格时间切分、样本外评估、相关性去重和可复现诊断记录，这些工程约束与搜索算法本身同等重要。

目录结构：本文包含总览、路线脉络和分组导读，是对路线的综合分析，不是完整清单；全部收录工作见[论文索引](../INDEX.md)，逐篇内容见 [`notes/cards/`](../notes/cards/) 下的速读卡。

检索口径：优先纳入“显式公式/符号/DSL/代码形式 Alpha 或风险因子挖掘”的论文；对纯黑盒收益预测模型只在与公式挖掘框架强相关时纳入。每个条目保留论文链接，并补充对应 GitHub 开源仓库；若未发现官方仓库，则标注“未见官方开源”。作者单位优先采用论文 PDF、会议页面或官方项目页；若官方摘要页未展示单位，则统一写作“官方摘要页未展示单位信息；作者为/包含……”。本轮补检截至 2026-07-11，重点检索关键词包括 `formulaic alpha reinforcement learning`、`formulaic factor mining MCTS`、`alpha mining GFlowNet`、`alpha factor discovery reinforcement fine-tuning`、`LLM alpha mining evolutionary factor search` 和 `alpha factor screening reinforcement learning`。

## 1. 总览与阅读地图

本节先给出技术路线对比和三条演进主线，再按 RL 与 LLM/Agent 两条路线给出流程与脉络。第 2 节按路线分组导读；建议先读“三条演进主线”建立整体坐标，再看 2.2 RL 公式因子挖掘主线、2.3 因子池与动态组合，最后看 2.4 之后的 LLM 路线与评估方向。

### 技术路线总览

下表按表达空间、搜索策略、评估奖励、因子池与组合四个维度，对人工公式库、GP/AutoML、RL 策略搜索、结构化搜索以及 LLM/Agent/RFT 路线进行横向对比。

| 维度 | 人工公式库 | GP / AutoML | RL 策略搜索 | 结构化搜索 | LLM / Agent / RFT |
| --- | --- | --- | --- | --- | --- |
| 表达空间 | Alpha101 / 专家公式 | DSL / 树表达式 | RPN / token 轨迹 | AST / CFG / Program | DSL / AST / Code |
| 搜索策略 | 人工构造 / 规则筛选 | 进化搜索 / 层次扩展 | PPO / REINFORCE / IQN | MCTS / GFlowNet | Idea-Agent-Eval / GRPO |
| 评估奖励 | IC / RankIC / 相关性 | fitness / QD 多样性 | pool gain / IR / QCM / shaping | novelty / grammar / risk-seeking | DiCo / OOS / 反馈记忆 |
| 因子池与组合 | 低相关因子库 | 候选因子去冗余 | Factor Pool 更新 | 结构去重 / 多 mode | Factor DB / 轨迹-因子库 |

演进趋势：单因子 → 因子集合协同；序列 token → AST / Grammar / Program；Prompt 反馈 → 参数更新；静态池 → 动态组合。共同目标是持续发现高预测力、低冗余、可解释、可组合的公式因子集合。

### 三条演进主线

按时间横切 9 个分组，能看到三条主线在同时推进。它们不是三种并列的方法，而是对同一个目标的三种回答：怎样从巨大表达式空间里持续拿到一组可用的因子。每条主线下面按首次公开时间排列，括号中标出它对应的分组。

**主线一：优化单位从单条公式变成因子池。** 早期工作把“挖到一个高 IC 公式”当作终点：Alpha101（2016）固定一个人工库，AutoAlpha（2020）用层次化搜索提高搜索效率，AlphaGen（2023）第一次把奖励改成“新因子加入因子池后组合 IC 的边际贡献”。此后优化单位一路上移：RiskMiner（2024）在中间状态就用池内 MutIC 惩罚重复，AlphaForge（2024）把挖掘与使用拆成两段、使用阶段按近期表现动态定池，AlphaSAGE（2025）用 GFlowNet 让采样概率正比于奖励、天然覆盖多个模式。2026 年出现两种更彻底的做法：把因子池直接放进生成状态（AlphaPADI、AlphaPareto），以及把整个池当作生成和学习对象、用池对偏好训练（AlphaPADI，见 2.2）。同一时期，因子池维护也独立成了研究对象，例如 Alpha-R1 只做启停筛选、AlphaLedger 把扣费后的组合边际贡献做成账本（见 2.3）。这条主线的终点是一个问题：池级目标一旦进入训练，奖励就随池变化而不再平稳，于是引出主线二里的“补全状态”与“改变学习目标”。

**主线二：学习信号从外部反馈转向模型内部。** 公式挖掘的奖励只在完整公式生成后出现，且对生成的 token 不可微。早期做法是在外部构造更密集或更稳的信号：RiskMiner 给合法中间表达式即时奖励，TLRS 用专家子序列做轨迹级塑形，QFR 用信息比率压低短期波动，AlphaQCM 用回报分布方差做探索奖励。另一条路是让奖励变得可微：AlphaForge 训练预测器替代部分真实评价，同时把它的分数经 Gumbel-Softmax 回传给生成器（见 2.2）。LLM 路线重复了同一段历史，但速度更快：Alpha-GPT（2023）到 QuantaAlpha（2026）主要靠提示词与上下文循环，QuantEvolver（2026）开始用强化微调把评价反馈写进模型参数，AlphaPilot、AlphaDiverse 用 GRPO 训练多轮工具调用与分角色协作，AlphaLedger 用在线策略蒸馏把组合账本变成动作级监督（见 2.4、2.7）。这条主线的代价是把训练成本与模型依赖引入了挖掘流程，也带来了主线三要处理的问题：评价口径和证据链在训练流程里更容易不可追溯。

**主线三：评价从“报一个 IC”变成“可审计的证据链”。** 早期工作的结论主要是一张 IC 或回测表。随着搜索规模变大和 LLM 介入，两类风险被反复提出：一是搜索本身就是大量多重检验，二是泄漏与留存偏差让结果难以复核。应对手段逐步前移：AlphaEval（2025）用免回测的代理指标同时评价预测力、稳定性、逻辑与多样性；FactorBench（2026）把评价分成因子、池、扣费组合三层；QBX（2026）把时间可用性检查放进编译期、用内容身份去重并把试验次数记账（见 2.6）。在 LLM 路线内部，Auditing（2026）审计已留存项目的度量口径与留存偏差，EvoQuantLab（2026）用等预算置换把搜索规模计入显著性，AlphaMemo 与 AgenticFactorInvesting 分别从“经验复用的信用”和“准入闸门”两端控制选择偏差（见 2.9）。相邻方法里的 Publication Bias 与 Sequential Cauchy 提供了从一组候选直接估出收缩幅度与族错误率的工具。这条主线目前最薄的一环是：大多数挖掘工作仍不报告自己搜索了多少候选，而所有校正方法都需要这个前提。

三条主线交会在同一处：池视角让奖励依赖池状态，训练化让反馈进入模型参数，可审计性让搜索规模与数据边界暴露在评价之下。读一篇新工作时，可以沿这三条线各问一句——它的优化单位是什么、学习信号从哪里来、它的结论能否被独立复核——这比按方法标签归类更容易看出它真正前进了哪一步。

### 典型 RL 公式因子挖掘流程

本节基于 2.2、2.3 组的 AlphaGen、Synergistic RL、RiskMiner、Alpha2、QFR、AlphaQCM、TLRS、AlphaSAGE、AlphaCFG、AlphaForge、AlphaPROBE、Alpha-R1、AlphaGAT 和 EFS 等工作归纳，而不是只描述某一个 RL 公式生成器。强化学习与结构化搜索路线的共同起点是表达空间与生成约束：AlphaGen 使用 RPN token MDP，Alpha2 改为 program/register 构造并前置维度检查，AlphaCFG 用 α-Syn / α-Sem 和 CFG 将语法、语义、长度约束写入搜索空间，AlphaSAGE 则用 AST/prefix state 与 RGCN 编码公式结构。

候选公式搜索大致分为三类：AlphaGen、Synergistic RL 和 QFR 代表序列策略生成，围绕 PPO、REINFORCE、greedy baseline、replay buffer seed 和稳定性奖励改进 token 级生成；RiskMiner、Alpha2 和 AlphaCFG 代表树与文法搜索，用 MCTS、RL-guided MCTS、Tree-LSTM、grammar-aware search 和 risk-seeking 策略显式利用公式树结构；AlphaQCM 与 AlphaSAGE 代表回报分布建模和多样采样路线，用 IQN/QCM、GFlowNet、Trajectory Balance、structure-aware alignment 和 novelty reward 缓解奖励稀疏、非平稳和模式坍缩。

评价、准入和因子池反馈是这条路线区别于“单因子高 IC 搜索”的关键。AlphaGen 把组合 IC 边际贡献写入奖励并维护固定容量因子池，RiskMiner 用 MutIC 和合法中间表达式奖励控制重复与稀疏反馈，TLRS 用专家因子子序列 shaping 提供轨迹级监督，AlphaForge 将候选池扩展到动态 top-N 和 Mega-Alpha 组合，AlphaPROBE 保存 proposal 谱系用于去重和复盘，Alpha-R1 与 AlphaGAT 则提示后续可以在已有因子池上做 regime-aware 筛选、启停和动态权重。整体目标因此从“生成一个高分公式”转向“持续维护一组可执行、低冗余、样本外稳定、可组合的公式因子集合”。

### RL 公式因子挖掘路线脉络

RL 公式因子挖掘路线的核心问题不是“能否生成一个高 IC 公式”，而是如何在巨大离散表达式空间中稳定生成一组可执行、低冗余、样本外有效的因子。按技术演进看，相关工作大致形成以下主线：

| 方向 | 代表工作 | 解决的核心问题 | 调研启发 |
| --- | --- | --- | --- |
| 序列式 RL 生成 | AlphaGen、Synergistic RL、QFR | 将 RPN/DSL 公式生成建模为 token-level MDP；从 PPO 逐步反思到 REINFORCE 与稳定性奖励 | 保留公式生成环境，但要谨慎选择 policy loss；组合贡献、IR/ICIR 和 baseline 设计比单 IC 更关键 |
| 结构化搜索 | RiskMiner、Alpha2、AlphaCFG | 用 MCTS、program/register 表示、文法约束和维度检查利用公式树结构 | 将语法、维度和金融语义约束前置到生成阶段，减少非法表达式和无意义回测 |
| 奖励稠密化与分布视角 | RiskMiner、AlphaQCM、TLRS、AlphaSAGE | 缓解完整公式完成后才有奖励导致的稀疏、非平稳和模式坍缩 | 可把专家因子子结构、奖励分布方差、结构新颖性作为辅助奖励，而不是只做事后过滤 |
| 多样因子池采样 | AlphaForge、AlphaSAGE、AlphaPROBE、QuantEvolver | 从单因子最优转向高质量、多 mode、低相关候选池 | 因子池应保存结构、行为、谱系和组合贡献；新增因子准入看边际贡献而非孤立分数 |
| 生成后筛选/激活 | Alpha-R1、AlphaGAT | 不只挖因子，还要在市场状态变化时筛选、激活或动态组合 | regime-aware 筛选与动态权重更适合作为因子池使用阶段的问题，需与公式生成主线区分 |

### 典型 LLM/Agent 公式因子挖掘流程

本节基于 2.4 组的 Alpha-GPT、QuantAgent、AlphaAgent、Alpha-Jungle、RD-Agent(Q)、CogAlpha、QuantaAlpha、FactorMiner、FactorEngine、Hubble、EFS、QuantEvolver 和 Agora/SJS 等工作归纳，而不是给出一个脱离论文的通用 Agent 模板。LLM/Agent 路线的共同起点是研究输入与知识来源：Alpha-GPT 强调研究员想法、字段库和层次化 RAG，Automate Strategy Finding 与 FactorEngine 引入研报、文本、图像和专家因子，Hubble 使用 positive/negative RAG 控制学习与避让，QuantEvolver 则把 seed factors、时间窗口、因子家族和场景元数据组织成 task bank。

在生成侧，AlphaAgent、RD-Agent(Q)、CogAlpha、QuantaAlpha 和 Agora/SJS 分别展示了 idea/research agent、多智能体层级、diversified planning 和 agent-to-agent self-play 等假设规划方式；因子实现则可能落在 seed alpha、operator library、AST expression、Factor DSL、Python/program、Co-STEER 代码代理或 Factor Realizer 上。由于这些工作普遍面临代码执行、表达式错配和同质化风险，AlphaAgent、QuantaAlpha、CogAlpha、FactorEngine 和 Hubble 都把安全校验、一致性检查、复杂度约束、结构相似度、输出相关性或时间泄漏测试放入闭环中，而不是只在回测后事后筛选。

评价与反馈也来自这些论文的真实机制：Alpha-Jungle、Hubble、QuantEvolver 和 EFS 都强调 IC/RankIC、Sharpe、稳定性、换手、coverage、diversity、overfitting risk、family-aware scoring 或相关性去重等多维评价。回测结果之后通常进入三类自改进路径：QuantAgent、FactorMiner、Hubble 将结果沉淀为 signal knowledge base、experience memory、Factor DB 和诊断元数据；Alpha-Jungle、QuantaAlpha、FactorEngine、CogAlpha 把高质量轨迹用于 MCTS refinement、mutation、crossover、thinking evolution 或 program pool 搜索；QuantEvolver 则进一步把可执行评价转化为 RFT/GRPO 和 DiCo Reward，对 Miner LLM 做参数更新。

### 阅读边界与后续核查点

本文优先覆盖显式公式、符号表达式、DSL、AST 或代码形式的 Alpha / 风险因子挖掘工作。AlphaGAT、EFS、HRFT/IRFT 等条目与主线存在交集，但它们分别更偏动态组合、稀疏组合优化和高频风险因子生成，阅读时应避免把它们等同于日频公式 Alpha 生成 baseline。

后续维护时建议优先核查三类信息：第一，2025-2026 年新论文的版本、会议接收状态和官方仓库是否变化；第二，论文图是否与当前条目对应，避免使用早期草稿图或非官方复现图；第三，涉及 LLM/Agent 的工作是否提供可执行代码、数据切分和回测协议，否则只能作为方法思路参考，不宜直接作为可复现实验基线。

## 2. 分组导读

本节按技术路线分组，说明每组在解决什么、彼此是什么关系；每组只点名代表工作。全部收录工作、时间、会议和问题标注以[论文索引](../INDEX.md)为准。

### 2.1 公式库、遗传规划与 AutoML 基线

这一组工作定义了公式化 Alpha 的表达范式和早期自动搜索方式，是后续 RL/LLM 方法的算子库、种子库和 baseline 来源。

代表工作：[Alpha101](../notes/cards/2016_Alpha101.md)、[AutoAlpha](../notes/cards/2020_AutoAlpha.md)、[AlphaEvolve](../notes/cards/2021_AlphaEvolve.md)、[Warm Start GP](../notes/cards/2024_WarmStartGP.md)。

### 2.2 RL 公式因子挖掘主线

这一组是本文重点。它们直接把公式生成、结构化搜索、奖励塑形或多样采样建模为 RL/MCTS/GFlowNet 等策略搜索问题，核心目标是从巨大离散表达式空间中挖出可执行、低冗余、样本外稳健的因子集合。

代表工作：[AlphaGen](../notes/cards/2023_AlphaGen.md)、[Synergistic RL](../notes/cards/2024_SynergisticRL.md)、[RiskMiner](../notes/cards/2024_RiskMiner.md)、[Alpha2](../notes/cards/2024_Alpha2.md)、[QFR](../notes/cards/2024_QFR.md)、[AlphaQCM](../notes/cards/2025_AlphaQCM.md)、[TLRS](../notes/cards/2025_TLRS.md)、[AlphaSAGE](../notes/cards/2025_AlphaSAGE.md)、[AlphaCFG](../notes/cards/2026_AlphaCFG.md)。

把搜索历史显式持久化的另一支：多关系图（生成、结构、相关三类边）加 Pareto 选父（[CosmosAlpha](../notes/cards/2026_CosmosAlpha.md)），以及以整条研究轨迹为单位演化（[AlphaSeek](../notes/cards/2026_AlphaSeek.md)）。把先验做成中间表示、在生成期约束表达式的做法见 [AlphaLogics](../notes/cards/2026_AlphaLogics.md)。近期把“因子池视角”前移到生成端的做法：以整个池为生成单元并用扩散模型生成（[AlphaPADI](../notes/cards/2026_AlphaPADI.md)）、把池编码进策略状态（[AlphaPareto](../notes/cards/2026_AlphaPareto.md)）、把池级奖励转成池对偏好（[AlphaPADI](../notes/cards/2026_AlphaPADI.md)）。在训练信号层面，还有同前缀兄弟动作的局部蒸馏（[AlphaG-OPD](../notes/cards/2026_AlphaG-OPD.md)）与跨回合记忆加 SDE 回报评论家（[AlphaRJM](../notes/cards/2026_AlphaRJM.md)）。

### 2.3 因子池、动态组合与筛选

这一组不一定只关注“生成公式”本身，而是解决候选因子如何去重、动态加权、按市场状态启停，以及如何把因子挖掘结果接入下游投资目标。

代表工作：[AlphaForge](../notes/cards/2024_AlphaForge.md)、[AlphaGAT](../notes/cards/2025_AlphaGAT.md)、[EFS](../notes/cards/2025_EFS.md)、[Alpha-R1](../notes/cards/2025_Alpha-R1.md)、[AlphaPROBE](../notes/cards/2026_AlphaPROBE.md)、[AlphaLedger](../notes/cards/2026_AlphaLedger.md)、[GoAnt](../notes/cards/2026_GoAnt.md)。

### 2.4 LLM 驱动的因子生成

这一组把 LLM 当作想法生成器、公式实现器或结构变异算子：LLM 负责提出与改写表达式，搜索与评价往往仍由传统搜索器或回测循环完成。它们与 2.2 的 RL 主线不是替代关系，而是换了“谁提候选”这一步。

代表工作：[Alpha-GPT](../notes/cards/2023_Alpha-GPT.md)、[QuantAgent](../notes/cards/2024_QuantAgent.md)、[Alpha-GPT 2.0](../notes/cards/2024_Alpha-GPT2.md)、[LLM Strategy Finding](../notes/cards/2024_LLMStrategyFinding.md)、[AlphaAgent](../notes/cards/2025_AlphaAgent.md)、[Alpha-Jungle](../notes/cards/2025_Alpha-Jungle.md)、[CogAlpha](../notes/cards/2025_CogAlpha.md)、[QuantaAlpha](../notes/cards/2026_QuantaAlpha.md)、[FactorMiner](../notes/cards/2026_FactorMiner.md)、[Hubble](../notes/cards/2026_Hubble.md)、[LineageEvo](../notes/cards/2026_LineageEvo.md)、[TreEvo](../notes/cards/2025_TreEvo.md)、[AlphaMemo](../notes/cards/2026_AlphaMemo.md)、[AlphaLogics](../notes/cards/2026_AlphaLogics.md)、[AlphaSeek](../notes/cards/2026_AlphaSeek.md)、[CosmosAlpha](../notes/cards/2026_CosmosAlpha.md)、[EvoQuantLab](../notes/cards/2026_EvoQuantLab.md)、[AlphaRLM](../notes/cards/2026_AlphaRLM.md)、[AlphaSchema](../notes/cards/2026_AlphaSchema.md)、[AlphaDiverse](../notes/cards/2026_AlphaDiverse.md)。

### 2.5 LLM / Agent 的研究流程

这一组关注的是流程本身，而不是某种表达式表示：研究轨迹怎么组织、经验记忆存什么、评价预算怎么分配、多个智能体怎么分工。同一篇工作通常还会落在 2.4 或 2.2 的某条表示路线上。

代表工作：[RD-Agent(Q)](../notes/cards/2025_RD-Agent-Quant.md)（因子与模型双闭环）、[FactorEngine](../notes/cards/2026_FactorEngine.md)（程序池演化）、[QuantEvolver](../notes/cards/2026_QuantEvolver.md)（强化微调）、[AlphaPilot](../notes/cards/2026_AlphaPilot.md)、[AlphaLedger](../notes/cards/2026_AlphaLedger.md)、[AutoScientist-Quant](../notes/cards/2026_AutoScientist-Quant.md)、[X-Alpha](../notes/cards/2026_X-Alpha.md)、[AgonAlpha](../notes/cards/2026_AgonAlpha.md)、[Agora/SJS](../notes/cards/2026_Agora-SJS.md)、[EFS](../notes/cards/2025_EFS.md)、[Alpha-R1](../notes/cards/2025_Alpha-R1.md)、[AgenticFactorInvesting](../notes/cards/2026_AgenticFactorInvesting.md)。

### 2.6 表达空间扩展与风险因子生成

这一组与传统日频 Alpha 公式挖掘不完全同构，但对连续参数、符号-数值混合生成、高频风险因子和更宽表达空间有参考价值。

代表工作：[HRFT/IRFT](../notes/cards/2024_HRFT.md)（分钟高频风险因子）、[TextToAlpha](../notes/cards/2025_TextToAlpha.md)（季度披露文本，给出完整的文本到打分链路）、[MAPLE](../notes/cards/2026_MAPLE.md)（单模型多输出的神经 Alpha）、[Det-MASO](../notes/cards/2026_Det-MASO.md)（多智能体神经因子，智能体间相关矩阵惩罚）、[PRISM-VQ](../notes/cards/2026_PRISM-VQ.md)（离散隐因子，保留“载荷 × 因子”结构）、[GoAnt](../notes/cards/2026_GoAnt.md)（订单簿数据）。

### 2.7 基准与统一评测

这一组给出统一的数据、切分、指标或执行契约，用来横向比较多个挖掘方法。读者关心的是“怎么比”。

代表工作：[AlphaEval](../notes/cards/2025_AlphaEval.md)（免回测的代理指标）、[FactorBench](../notes/cards/2026_FactorBench.md)（因子 → 池 → 扣费组合三层）、[Look-Ahead-Bench](../notes/cards/2026_Look-Ahead-Bench.md)（LLM 前视偏差）、[MarketSenseAI](../notes/cards/2026_MarketSenseAI.md)（实时生成信号 + 零分布检验）。口径差异与已知会误导比较的情形见[评估口径对照](evaluation_protocol.md)。

### 2.8 审计、复现与泄漏检查

这一组审视证据链本身：结果怎么留存、指标口径是否一致、有没有做前视检查、试验次数记不记。读者关心的是“怎么证明”。它与 2.10 的显著性检验相邻。

代表工作：[Auditing LLM Alpha-Factor Mining](../notes/cards/2026_AuditingLLMAlpha.md)（留存偏差与指标来源）、[QBX](../notes/cards/2026_QBX.md)（编译期时间可用性、内容身份与试验账本）、[AgonAlpha](../notes/cards/2026_AgonAlpha.md)（独立上下文审稿与重跑否决）、[EvoQuantLab](../notes/cards/2026_EvoQuantLab.md)（冻结协议与等预算置换）。

### 2.9 LLM 挖掘的训练化与语义空间

这一组是 2.4 的最新变化：不再靠提示词循环反复试错，而是把经验写进模型参数、在显式的语义或机制空间里搜索，或对研究轨迹做后训练。

代表工作：[AlphaPilot](../notes/cards/2026_AlphaPilot.md)、[AlphaDiverse](../notes/cards/2026_AlphaDiverse.md)、[AlphaSchema](../notes/cards/2026_AlphaSchema.md)、[QuantEvolver](../notes/cards/2026_QuantEvolver.md)、[AlphaRLM](../notes/cards/2026_AlphaRLM.md)、[TreEvo](../notes/cards/2025_TreEvo.md)、[LineageEvo](../notes/cards/2026_LineageEvo.md)、[EvoQuantLab](../notes/cards/2026_EvoQuantLab.md)、[AutoScientist-Quant](../notes/cards/2026_AutoScientist-Quant.md)、[X-Alpha](../notes/cards/2026_X-Alpha.md)、[AgonAlpha](../notes/cards/2026_AgonAlpha.md)。

### 2.10 相邻方法

不是因子挖掘本身，但机制被已收录工作直接借用或可借用，例如 GFlowNet 的按奖励成比例采样、DSR 的风险寻求目标和多轮智能体的步骤级信用分配。逐篇见[可迁移的相邻方法](adjacent/transferable_methods.md)。

代表工作：[GFlowNet](../notes/cards/2021_GFlowNet.md)、[Trajectory Balance](../notes/cards/2022_TrajectoryBalance.md)、[DSR](../notes/cards/2019_DSR.md)、[GiGPO](../notes/cards/2025_GiGPO.md)、[Tree-GRPO](../notes/cards/2025_Tree-GRPO.md)、[DeepMind AlphaEvolve](../notes/cards/2025_DeepMind-AlphaEvolve.md)、[Publication Bias](../notes/cards/2022_PublicationBias.md)、[Sequential Cauchy](../notes/cards/2023_SequentialCauchy.md)。

### 2.11 过拟合控制与显著性检验

这一组与 2.6 相邻，但关注的是“挖出来的因子有多少是真的”：在搜索规模未知的情况下如何校正选择偏差、如何把搜索多重性计入显著性。它同时包含挖掘系统与可迁移的检验方法。

代表工作：[EvoQuantLab](../notes/cards/2026_EvoQuantLab.md)（等预算区块置换）、[AlphaMemo](../notes/cards/2026_AlphaMemo.md)（经验复用的选择偏差）、[AgenticFactorInvesting](../notes/cards/2026_AgenticFactorInvesting.md)（准入闸门与样本外冻结）、[Publication Bias](../notes/cards/2022_PublicationBias.md)（经验贝叶斯收缩与 FDR）、[Sequential Cauchy](../notes/cards/2023_SequentialCauchy.md)（强 FWER 控制）。
