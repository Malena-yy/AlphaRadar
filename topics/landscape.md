# 因子挖掘研究全景：路线与阅读地图

本文面向公式化 Alpha 因子挖掘方向，梳理传统公式库、遗传/AutoML、RL/MCTS/GFlowNet、动态组合、LLM/Agent/RFT 等相关工作。相比纯时间线，本文采用“先总览、再按技术路线分组”的组织方式；每个分组内部大体按论文首次公开或会议发表时间排序。

调研结论：
1. 公式化因子挖掘的主战场已经从“单因子高 IC 搜索”转向“可执行、低冗余、样本外稳定、可组合的因子池维护”。
2. AlphaGen、RiskMiner、Alpha2、AlphaCFG、AlphaSAGE 等工作代表公式生成与结构化搜索主线；AlphaForge、Alpha-R1、AlphaGAT 等工作更偏向因子池筛选、启停和动态组合。
3. 语法、维度、金融语义和复杂度约束应尽量前置到生成阶段。只依赖生成后过滤，会浪费大量回测预算，也容易让策略学习到无效动作。
4. LLM/Agent 路线的价值不在于替代 RL/搜索器，而在于提供研究假设、结构变异、代码实现、评价摘要、经验记忆和 RFT 训练数据。
5. 相关工作普遍强调 DSL/AST 安全约束、严格时间切分、样本外评估、相关性去重和可复现诊断记录，这些工程约束与搜索算法本身同等重要。

目录结构：本文包含总览、路线脉络和各分组导读；逐篇内容见 [`notes/cards/`](../notes/cards/) 下的速读卡，结构化元数据统一登记在 [`papers.yaml`](../papers.yaml)。

检索口径：优先纳入“显式公式/符号/DSL/代码形式 Alpha 或风险因子挖掘”的论文；对纯黑盒收益预测模型只在与公式挖掘框架强相关时纳入。每个条目保留论文链接，并补充对应 GitHub 开源仓库；若未发现官方仓库，则标注“未见官方开源”。作者单位优先采用论文 PDF、会议页面或官方项目页；若官方摘要页未展示单位，则统一写作“官方摘要页未展示单位信息；作者为/包含……”。本轮补检截至 2026-07-11，重点检索关键词包括 `formulaic alpha reinforcement learning`、`formulaic factor mining MCTS`、`alpha mining GFlowNet`、`alpha factor discovery reinforcement fine-tuning`、`LLM alpha mining evolutionary factor search` 和 `alpha factor screening reinforcement learning`。

## 1. 总览与阅读地图

本节先给出技术路线对比、RL 公式因子挖掘闭环、RL 路线演进表和 LLM/Agent 闭环。后续论文条目按路线分组展开，重点阅读顺序建议为：先看第 3 节 RL 公式因子挖掘主线，再看第 4 节因子池/组合/筛选，最后看第 5 节 LLM/Agent/RFT 如何补充搜索与反馈机制。

### 技术路线总览

下表按表达空间、搜索策略、评估奖励、因子池与组合四个维度，对人工公式库、GP/AutoML、RL 策略搜索、结构化搜索以及 LLM/Agent/RFT 路线进行横向对比。

| 维度 | 人工公式库 | GP / AutoML | RL 策略搜索 | 结构化搜索 | LLM / Agent / RFT |
| --- | --- | --- | --- | --- | --- |
| 表达空间 | Alpha101 / 专家公式 | DSL / 树表达式 | RPN / token 轨迹 | AST / CFG / Program | DSL / AST / Code |
| 搜索策略 | 人工构造 / 规则筛选 | 进化搜索 / 层次扩展 | PPO / REINFORCE / IQN | MCTS / GFlowNet | Idea-Agent-Eval / GRPO |
| 评估奖励 | IC / RankIC / 相关性 | fitness / QD 多样性 | pool gain / IR / QCM / shaping | novelty / grammar / risk-seeking | DiCo / OOS / 反馈记忆 |
| 因子池与组合 | 低相关因子库 | 候选因子去冗余 | Factor Pool 更新 | 结构去重 / 多 mode | Factor DB / 轨迹-因子库 |

演进趋势：单因子 → 因子集合协同；序列 token → AST / Grammar / Program；Prompt 反馈 → 参数更新；静态池 → 动态组合。共同目标是持续发现高预测力、低冗余、可解释、可组合的公式因子集合。

### 典型 RL 公式因子挖掘流程

本节基于第 3、4 节已收集的 AlphaGen、Synergistic RL、RiskMiner、Alpha2、QFR、AlphaQCM、TLRS、AlphaSAGE、AlphaCFG、AlphaForge、AlphaPROBE、Alpha-R1、AlphaGAT 和 EFS 等工作归纳，而不是只描述某一个 RL 公式生成器。强化学习与结构化搜索路线的共同起点是表达空间与生成约束：AlphaGen 使用 RPN token MDP，Alpha2 改为 program/register 构造并前置维度检查，AlphaCFG 用 α-Syn / α-Sem 和 CFG 将语法、语义、长度约束写入搜索空间，AlphaSAGE 则用 AST/prefix state 与 RGCN 编码公式结构。

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

本节基于第 5 节已收集的 Alpha-GPT、QuantAgent、AlphaAgent、Alpha-Jungle、RD-Agent(Q)、CogAlpha、QuantaAlpha、FactorMiner、FactorEngine、Hubble、EFS、QuantEvolver 和 Agora/SJS 等工作归纳，而不是给出一个脱离论文的通用 Agent 模板。LLM/Agent 路线的共同起点是研究输入与知识来源：Alpha-GPT 强调研究员想法、字段库和层次化 RAG，Automate Strategy Finding 与 FactorEngine 引入研报、文本、图像和专家因子，Hubble 使用 positive/negative RAG 控制学习与避让，QuantEvolver 则把 seed factors、时间窗口、因子家族和场景元数据组织成 task bank。

在生成侧，AlphaAgent、RD-Agent(Q)、CogAlpha、QuantaAlpha 和 Agora/SJS 分别展示了 idea/research agent、多智能体层级、diversified planning 和 agent-to-agent self-play 等假设规划方式；因子实现则可能落在 seed alpha、operator library、AST expression、Factor DSL、Python/program、Co-STEER 代码代理或 Factor Realizer 上。由于这些工作普遍面临代码执行、表达式错配和同质化风险，AlphaAgent、QuantaAlpha、CogAlpha、FactorEngine 和 Hubble 都把安全校验、一致性检查、复杂度约束、结构相似度、输出相关性或时间泄漏测试放入闭环中，而不是只在回测后事后筛选。

评价与反馈也来自这些论文的真实机制：Alpha-Jungle、Hubble、QuantEvolver 和 EFS 都强调 IC/RankIC、Sharpe、稳定性、换手、coverage、diversity、overfitting risk、family-aware scoring 或相关性去重等多维评价。回测结果之后通常进入三类自改进路径：QuantAgent、FactorMiner、Hubble 将结果沉淀为 signal knowledge base、experience memory、Factor DB 和诊断元数据；Alpha-Jungle、QuantaAlpha、FactorEngine、CogAlpha 把高质量轨迹用于 MCTS refinement、mutation、crossover、thinking evolution 或 program pool 搜索；QuantEvolver 则进一步把可执行评价转化为 RFT/GRPO 和 DiCo Reward，对 Miner LLM 做参数更新。

### 阅读边界与后续核查点

本文优先覆盖显式公式、符号表达式、DSL、AST 或代码形式的 Alpha / 风险因子挖掘工作。AlphaGAT、EFS、HRFT/IRFT 等条目与主线存在交集，但它们分别更偏动态组合、稀疏组合优化和高频风险因子生成，阅读时应避免把它们等同于日频公式 Alpha 生成 baseline。

后续维护时建议优先核查三类信息：第一，2025-2026 年新论文的版本、会议接收状态和官方仓库是否变化；第二，论文图是否与当前条目对应，避免使用早期草稿图或非官方复现图；第三，涉及 LLM/Agent 的工作是否提供可执行代码、数据切分和回测协议，否则只能作为方法思路参考，不宜直接作为可复现实验基线。

## 2. 公式库、遗传规划与 AutoML 基线

这一组工作定义了公式化 Alpha 的表达范式和早期自动搜索方式，是后续 RL/LLM 方法的算子库、种子库和 baseline 来源。

- [Alpha101](../notes/cards/2016_Alpha101.md)（2016.01）：101 Formulaic Alphas
- [AutoAlpha](../notes/cards/2020_AutoAlpha.md)（2020.04（arXiv v2；v1 为 2020.02））：AutoAlpha: an Efficient Hierarchical Evolutionary Algorithm for Mining Alpha Factors in Quantitative Investment
- [AlphaEvolve](../notes/cards/2021_AlphaEvolve.md)（2021.04（SIGMOD 2021 / arXiv v2））：AlphaEvolve: A Learning Framework to Discover Novel Alphas in Quantitative Investment

## 3. RL 公式因子挖掘主线

这一组是本文重点。它们直接把公式生成、结构化搜索、奖励塑形或多样采样建模为 RL/MCTS/GFlowNet 等策略搜索问题，核心目标是从巨大离散表达式空间中挖出可执行、低冗余、样本外稳健的因子集合。

- [AlphaGen](../notes/cards/2023_AlphaGen.md)（2023.05（KDD 2023））：Generating Synergistic Formulaic Alpha Collections via Reinforcement Learning
- [Synergistic RL](../notes/cards/2024_SynergisticRL.md)（2024.01（arXiv v1；v2 为 2024.07））：Synergistic Formulaic Alpha Generation for Quantitative Trading based on Reinforcement Learning
- [RiskMiner](../notes/cards/2024_RiskMiner.md)（2024.02（arXiv；ICAIF 2024 相关工作））：RiskMiner: Discovering Formulaic Alphas via Risk Seeking Monte Carlo Tree Search
- [Alpha2](../notes/cards/2024_Alpha2.md)（2024.06）：Alpha2: Discovering Logical Formulaic Alphas using Deep Reinforcement Learning
- [QFR](../notes/cards/2024_QFR.md)（2024.09（arXiv v1；v3 为 2025.06））：QuantFactor REINFORCE: Mining Steady Formulaic Alpha Factors with Variance-bounded REINFORCE
- [AlphaQCM](../notes/cards/2025_AlphaQCM.md)（2025.05（ICML 2025 poster））：AlphaQCM: Alpha Discovery with Distributional Reinforcement Learning
- [TLRS](../notes/cards/2025_TLRS.md)（2025.07（arXiv v1））：Learning from Expert Factors: Trajectory-level Reward Shaping for Formulaic Alpha Mining
- [AlphaSAGE](../notes/cards/2025_AlphaSAGE.md)（2025.09（arXiv v1；v3 为 2026.05））：AlphaSAGE: Structure-Aware Alpha Mining via GFlowNets for Robust Exploration；[精读](../notes/deep/2025_AlphaSAGE.md)
- [AlphaCFG](../notes/cards/2026_AlphaCFG.md)（2026.01（arXiv v1））：Alpha Discovery via Grammar-Guided Learning and Search

## 4. 因子池、动态组合与筛选

这一组不一定只关注“生成公式”本身，而是解决候选因子如何去重、动态加权、按市场状态启停，以及如何把因子挖掘结果接入下游投资目标。

- [AlphaForge](../notes/cards/2024_AlphaForge.md)（2024.06（arXiv v1；AAAI 2025））：AlphaForge: A Framework to Mine and Dynamically Combine Formulaic Alpha Factors；[精读](../notes/deep/2024_AlphaForge.md)
- [AlphaGAT](../notes/cards/2025_AlphaGAT.md)（2025（IJCAI 2025，Proceedings pages 7500-7508））：AlphaGAT: A Two-Stage Learning Approach for Adaptive Portfolio Selection；[精读](../notes/deep/2025_AlphaGAT.md)
- [EFS](../notes/cards/2025_EFS.md)（2025.07（arXiv v1））：EFS: Evolutionary Factor Searching for Sparse Portfolio Optimization Using Large Language Models
- [Alpha-R1](../notes/cards/2025_Alpha-R1.md)（2025.12（arXiv v1））：Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning
- [AlphaPROBE](../notes/cards/2026_AlphaPROBE.md)（2026.02（arXiv v1））：AlphaPROBE: Alpha Mining via Principled Retrieval and On-graph biased evolution

## 5. LLM、Agent 与 RFT 因子挖掘

这一组工作把 LLM 用作想法生成器、公式实现器、代码代理、评价总结器、经验记忆或可微调策略。它们与第 3 节的 RL 主线并不是替代关系，更适合为公式搜索提供上游假设、结构变异、反馈压缩和长期经验沉淀。

- [Alpha-GPT](../notes/cards/2023_Alpha-GPT.md)（2023.07（arXiv））：Alpha-GPT: Human-AI Interactive Alpha Mining for Quantitative Investment
- [QuantAgent](../notes/cards/2024_QuantAgent.md)（2024.02）：QuantAgent: Seeking Holy Grail in Trading by Self-Improving Large Language Model
- [Alpha-GPT 2.0](../notes/cards/2024_Alpha-GPT2.md)（2024.02）：Alpha-GPT 2.0: Human-in-the-Loop AI for Quantitative Investment
- [LLM Strategy Finding](../notes/cards/2024_LLMStrategyFinding.md)（2024.09）：Automate Strategy Finding with LLM in Quant Investment
- [AlphaAgent](../notes/cards/2025_AlphaAgent.md)（2025.02（arXiv v1；KDD 2025））：AlphaAgent: LLM-Driven Alpha Mining with Regularized Exploration to Counteract Alpha Decay
- [Alpha-Jungle](../notes/cards/2025_Alpha-Jungle.md)（2025.05（arXiv v1；v3 为 2025.11；AAAI 2026））：Navigating the Alpha Jungle: An LLM-Powered MCTS Framework for Formulaic Factor Mining
- [RD-Agent(Q)](../notes/cards/2025_RD-Agent-Quant.md)（2025.05（arXiv v1；NeurIPS 2025））：R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization
- [CogAlpha](../notes/cards/2025_CogAlpha.md)（2025.11（arXiv v1；v3 为 2026.04））：Cognitive Alpha Mining via LLM-Driven Code-Based Evolution
- [QuantaAlpha](../notes/cards/2026_QuantaAlpha.md)（2026.02（arXiv v1；v3 为 2026.05））：QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining
- [FactorMiner](../notes/cards/2026_FactorMiner.md)（2026.02（arXiv v1））：FactorMiner: A Self-Evolving Agent with Skills and Experience Memory for Financial Alpha Discovery
- [FactorEngine](../notes/cards/2026_FactorEngine.md)（2026.03（arXiv v1；v2 为 2026.04））：FactorEngine: A Program-level Knowledge-Infused Factor Mining Framework for Quantitative Investment
- [Hubble](../notes/cards/2026_Hubble.md)（2026.03（arXiv v1；v2 为 2026.04））：Hubble: An LLM-Driven Agentic Framework for Safe, Diverse, and Reproducible Alpha Factor Discovery
- [QuantEvolver](../notes/cards/2026_QuantEvolver.md)（2026.05（arXiv v1））：From Feedback Loops to Policy Updates: Reinforcement Fine-Tuning for LLM-Based Alpha Factor Discovery
- [Agora/SJS](../notes/cards/2026_Agora-SJS.md)（2026.06（arXiv v1））：AI Trading's Alpha Singularity: Emergent Market Reasoning through Agent-to-Agent Self-Evolution

## 6. 表达空间扩展与风险因子生成

这一组与传统日频 Alpha 公式挖掘不完全同构，但对连续参数、符号-数值混合生成、高频风险因子和更宽表达空间有参考价值。

- [HRFT/IRFT](../notes/cards/2024_HRFT.md)（2024.08（arXiv v1；WWW Companion 2025））：HRFT: Mining High-Frequency Risk Factor Collections End-to-End via Transformer
