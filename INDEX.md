# 论文索引

> 本文件由 `scripts/build_index.py` 根据 `papers.yaml` 生成，请勿手改。问题编号的含义见 README“出发点：因子挖掘面临的问题”，路线定义见 `taxonomy.yaml`。

共收录 43 篇（待筛 6，待写 5，速读 29，精读 3）。

## 1. 总表

按首次公开时间倒序。

| 时间 | 工作 | 一句话 | 问题 | 路线 | 链接 |
| --- | --- | --- | --- | --- | --- |
| 2026-10 | **QBX**（ICAIF 2026） | 面向 alpha 程序的编译器：以版本化算子注册表和带类型、时间可用性的 IR 定义可审计的候选空间。 | P1 P6 P10 | `evaluation` `formulaic` | [arXiv](https://arxiv.org/abs/2610.41689) · 待写 |
| 2026-10 | **FactorBench** | 组合视角的挖掘基准：在共享数据与评估契约下，横向比较九种自动挖掘方法产出的约五千个因子。 | P8 P10 | `evaluation` | [arXiv](https://arxiv.org/abs/2610.06947) · 待写 |
| 2026-10 | **Auditing LLM Alpha-Factor Mining**（ICAIF 2026 AI4F Workshop（非归档）） | 审计已留存项目的运行计数与结果保留方式，指出指标来源混用会让架构比较失效，并公开做全量再分析。 | P10 | `evaluation` | [arXiv](https://arxiv.org/abs/2610.29500) · 待写 |
| 2026-10 | **AlphaPilot** | 用强化学习训练多轮调用工具的 LLM 智能体：按市场描述提出公式、查询真实评价并维护因子池。 | — | `llm-agent` | [arXiv](https://arxiv.org/abs/2610.15488) · 待筛 |
| 2026-10 | **AlphaPADI** | 以因子池为条件的层次化离散扩散模型生成公式，把互补性纳入生成状态并支持多层结构改写。 | — | `formulaic` | [arXiv](https://arxiv.org/abs/2610.04959) · 待筛 |
| 2026-09 | **AlphaPareto**（NeurIPS 2026） | LLM 引导的多目标强化学习挖掘公式 Alpha，同时优化预测力与演变因子池的其它性质。 | — | `formulaic` | [arXiv](https://arxiv.org/abs/2609.34188) · 待筛 |
| 2026-09 | **AlphaDiverse** | 用多样化研究路径收集与后训练，把多智能体 Alpha 挖掘迁移到本地模型，缓解研究路径坍缩。 | — | `llm-agent` | [arXiv](https://arxiv.org/abs/2609.29014) · 待筛 |
| 2026-07 | **MAPLE** | 单次训练内生成多个低相关 Alpha：共享预测头、极端秩加权列表损失与显式相关性正则。 | — | `neural` `pool-combination` | [arXiv](https://arxiv.org/abs/2607.24131) · 待筛 |
| 2026-07 | **AlphaSchema** | 把交易语义组织成结构化 schema 空间，让 LLM 在显式的探索空间中挖掘 Alpha。 | — | `llm-agent` | [arXiv](https://arxiv.org/abs/2607.26642) · 待筛 |
| 2026-06 | **Agora/SJS** | 多智能体在密封评估下联合搜索交易信号与评价协议的自演化研究环境。 | P5 P6 | `llm-agent` | [arXiv](https://arxiv.org/abs/2606.29194) · [速读](notes/cards/2026_Agora-SJS.md) |
| 2026-05 | **QuantEvolver** | 用 RFT（GRPO + DiCo 奖励）把评价反馈写进轻量 LLM 参数，代替提示词循环。 | P1 P3 P4 P7 | `llm-agent` | [arXiv](https://arxiv.org/abs/2605.15412) · [代码](https://github.com/QuantLLM/QuantEvolver) · [速读](notes/cards/2026_QuantEvolver.md) |
| 2026-03 | **Hubble** | DSL / AST 安全沙箱加正负双通道 RAG 与因子家族感知评分，持久化全部诊断。 | P1 P7 P8 P9 P10 | `llm-agent` | [arXiv](https://arxiv.org/abs/2604.09601) · [速读](notes/cards/2026_Hubble.md) |
| 2026-03 | **FactorEngine**（ICDM 2026） | 图灵完备程序因子：LLM 演化宏观逻辑，贝叶斯优化微观参数，研报知识启动。 | P1 P2 P3 P6 | `llm-agent` | [arXiv](https://arxiv.org/abs/2603.16365) · [速读](notes/cards/2026_FactorEngine.md) |
| 2026-02 | **QuantaAlpha** | 把 LLM 挖掘过程视为可演化轨迹，对高质量轨迹做局部变异与交叉。 | P2 P7 | `llm-agent` | [arXiv](https://arxiv.org/abs/2602.07085) · [代码](https://github.com/QuantaAlpha/QuantaAlpha) · [速读](notes/cards/2026_QuantaAlpha.md) |
| 2026-02 | **FactorMiner** | 技能模块封装算子与评估协议，经验记忆记录应避开的高相关区域。 | P3 P7 P10 | `llm-agent` | [arXiv](https://arxiv.org/abs/2602.14670) · [速读](notes/cards/2026_FactorMiner.md) |
| 2026-02 | **AlphaPROBE** | 在因子谱系有向无环图上检索父节点，沿演化路径有偏地生成新因子。 | P1 P7 P8 | `formulaic` `pool-combination` | [arXiv](https://arxiv.org/abs/2602.11917) · [代码](https://github.com/gta0804/AlphaPROBE) · [速读](notes/cards/2026_AlphaPROBE.md) |
| 2026-01 | **Look-Ahead-Bench** | 衡量时点化 LLM 前视偏差的标准化基准，用跨市场状态的表现衰减区分真实预测与记忆。 | P6 | `evaluation` | [arXiv](https://arxiv.org/abs/2601.13770) · 待写 |
| 2026-01 | **AlphaCFG** | 用面向 alpha 的上下文无关文法约束语法、语义与长度，在其上做 RL 与 MCTS 搜索。 | P1 P7 | `formulaic` | [arXiv](https://arxiv.org/abs/2601.22119) · [代码](https://github.com/HanYang544/AlphaCFG) · [速读](notes/cards/2026_AlphaCFG.md) |
| 2025-12 | **Alpha-R1** | 用 SFT + GRPO 训练 LLM 按市场状态推理因子启停，做因子筛选。 | P5 P6 P8 P9 | `llm-agent` `pool-combination` | [arXiv](https://arxiv.org/abs/2512.23515) · [代码](https://github.com/FinStep-AI/Alpha-R1) · [速读](notes/cards/2025_Alpha-R1.md) |
| 2025-11 | **CogAlpha** | 七层 LLM 代理生成代码级 Alpha，经质量检查后做思考演化。 | P1 P2 P6 | `llm-agent` | [arXiv](https://arxiv.org/abs/2511.18850) · [速读](notes/cards/2025_CogAlpha.md) |
| 2025-09 | **AlphaSAGE**（ICLR 2026（Poster）） | AST + RGCN 编码公式结构，GFlowNet 按多信号奖励成比例采样多样因子。 | P4 P7 | `formulaic` | [arXiv](https://arxiv.org/abs/2509.25055) · [代码](https://github.com/BerkinChen/AlphaSAGE) · [速读](notes/cards/2025_AlphaSAGE.md) · [精读](notes/deep/2025_AlphaSAGE.md) |
| 2025-08 | **AlphaEval**（KDD 2026） | 面向公式 Alpha 挖掘的统一评估框架：以高效代理指标与回测相互对照，覆盖预测力、稳定性与稳健性。 | P10 | `evaluation` | [arXiv](https://arxiv.org/abs/2508.13174) · 待写 |
| 2025-07 | **TLRS** | 以专家因子子序列匹配做轨迹级奖励塑形，并用奖励中心化稳定训练。 | P4 | `formulaic` | [arXiv](https://arxiv.org/abs/2507.20263) · [速读](notes/cards/2025_TLRS.md) |
| 2025-07 | **EFS** | LLM 演化可执行的资产打分因子，用于只选 Top-m 资产的稀疏组合。 | P7 P8 | `llm-agent` `pool-combination` | [arXiv](https://arxiv.org/abs/2507.17211) · [速读](notes/cards/2025_EFS.md) |
| 2025-05 | **RD-Agent(Q)**（NeurIPS 2025） | 多智能体分别迭代因子与模型，用 Thompson 采样调度二者的联合优化。 | P7 P8 | `llm-agent` | [arXiv](https://arxiv.org/abs/2505.15155) · [代码](https://github.com/microsoft/RD-Agent) · [速读](notes/cards/2025_RD-Agent-Quant.md) |
| 2025-05 | **AlphaQCM**（ICML 2025） | 分布式强化学习估计奖励方差（QCM），作为非平稳稀疏奖励下的探索奖励。 | P4 | `formulaic` | [论文](https://openreview.net/forum?id=3sXMHlhBSs) · [代码](https://github.com/ZhuZhouFan/AlphaQCM) · [速读](notes/cards/2025_AlphaQCM.md) |
| 2025-05 | **Alpha-Jungle**（AAAI 2026） | LLM 驱动的 MCTS 逐步精炼公式，多维评价并规避高频子树。 | P1 P5 P7 P8 | `llm-agent` | [arXiv](https://arxiv.org/abs/2505.11122) · [速读](notes/cards/2025_Alpha-Jungle.md) |
| 2025-02 | **AlphaAgent**（KDD 2025） | 多智能体闭环，以 AST 原创性、假设一致性与复杂度正则对抗因子衰减。 | P2 P5 P7 P9 | `llm-agent` | [arXiv](https://arxiv.org/abs/2502.16789) · [代码](https://github.com/RndmVariableQ/AlphaAgent) · [速读](notes/cards/2025_AlphaAgent.md) |
| 2025 | **AlphaGAT**（IJCAI 2025） | CATimeMixer 生成神经 Alpha，再用 GAT + PPO 动态学习因子权重做组合选择。 | P2 P7 P8 | `neural` `pool-combination` | [论文](https://www.ijcai.org/proceedings/2025/834) · [速读](notes/cards/2025_AlphaGAT.md) · [精读](notes/deep/2025_AlphaGAT.md) |
| 2024-09 | **QFR**（IEEE Transactions on Signal Processing 2025） | 用带贪婪基线、无价值网络的 REINFORCE 替代 PPO，并以信息比率提升稳定性。 | P4 P9 | `formulaic` | [arXiv](https://arxiv.org/abs/2409.05144) · [速读](notes/cards/2024_QFR.md) |
| 2024-09 | **LLM Strategy Finding** | 从多模态财经材料抽取策略要素形成种子 Alpha，经多智能体评估后动态加权。 | P1 P8 | `llm-agent` | [arXiv](https://arxiv.org/abs/2409.06289) · [代码](https://github.com/kouzhizhuo/Automate-Strategy-Finding-with-LLM-in-Quant-investment) · [速读](notes/cards/2024_LLMStrategyFinding.md) |
| 2024-08 | **HRFT/IRFT**（WWW 2025（Industry Track）） | Transformer 以符号-数值混合词表端到端生成含常数的高频风险因子公式。 | P2 | `data-space` | [arXiv](https://arxiv.org/abs/2408.01271) · [代码](https://github.com/wencyxu/IRF-LLM-accepted-at-WWW25-) · [速读](notes/cards/2024_HRFT.md) |
| 2024-06 | **AlphaForge**（AAAI 2025） | 生成器-预测器挖掘因子，使用阶段按近期表现动态筛选并加权组合。 | P3 P4 P7 P8 P9 | `formulaic` `pool-combination` | [arXiv](https://arxiv.org/abs/2406.18394) · [代码](https://github.com/dulyhao/alphaforge) · [速读](notes/cards/2024_AlphaForge.md) · [精读](notes/deep/2024_AlphaForge.md) |
| 2024-06 | **Alpha2** | 把公式生成改为带寄存器的程序构造，搜索中做维度检查，由 RL 引导 MCTS。 | P1 P3 | `formulaic` | [arXiv](https://arxiv.org/abs/2406.16505) · [代码](https://github.com/x35f/alpha2) · [速读](notes/cards/2024_Alpha2.md) |
| 2024-02 | **RiskMiner**（ICAIF 2024） | 风险偏好 MCTS：合法中间表达式即时奖励，并惩罚与已有因子的重复。 | P1 P4 P7 P8 | `formulaic` | [arXiv](https://arxiv.org/abs/2402.07080) · [速读](notes/cards/2024_RiskMiner.md) |
| 2024-02 | **QuantAgent** | 内外双循环的自改进 LLM 智能体，持续积累交易信号知识库。 | P1 P4 | `llm-agent` | [arXiv](https://arxiv.org/abs/2402.03755) · [速读](notes/cards/2024_QuantAgent.md) |
| 2024-02 | **Alpha-GPT 2.0** | 把人在回路的 LLM 交互扩展到研究、建模、分析的完整量化研究流程。 | P1 P8 | `llm-agent` | [arXiv](https://arxiv.org/abs/2402.09746) · [速读](notes/cards/2024_Alpha-GPT2.md) |
| 2024-01 | **Synergistic RL**（ICOIN 2024） | 在 AlphaGen 上扩展算子与长窗口，并用优质种子公式引导探索。 | P1 P7 | `formulaic` | [arXiv](https://arxiv.org/abs/2401.02710) · [速读](notes/cards/2024_SynergisticRL.md) |
| 2023-07 | **Alpha-GPT**（EMNLP 2025（System Demonstrations）） | 人机交互的 LLM 因子挖掘：想法生成、公式实现与结果复盘，配合遗传规划搜索。 | P1 P2 | `llm-agent` | [arXiv](https://arxiv.org/abs/2308.00016) · [速读](notes/cards/2023_Alpha-GPT.md) |
| 2023-05 | **AlphaGen**（KDD 2023（ADS Track）） | 把 RPN 公式生成建模为 MDP，用因子池组合 IC 的边际贡献作为 PPO 奖励。 | P1 P3 P7 P8 | `formulaic` | [arXiv](https://arxiv.org/abs/2306.12964) · [代码](https://github.com/ICT-FinD-Lab/alphagen) · [速读](notes/cards/2023_AlphaGen.md) |
| 2021-03 | **AlphaEvolve**（SIGMOD 2021（Data Science and Engineering Track）） | AutoML 进化搜索，引入矩阵 / 向量算子与行业关系，并剪枝冗余表达式。 | P2 P3 P7 | `formulaic` | [arXiv](https://arxiv.org/abs/2103.16196) · [速读](notes/cards/2021_AlphaEvolve.md) |
| 2020-02 | **AutoAlpha** | 从低阶根基因逐层扩展的遗传规划，配合 PCA 近似的质量-多样性搜索。 | P1 P3 P7 | `formulaic` | [arXiv](https://arxiv.org/abs/2002.08245) · [速读](notes/cards/2020_AutoAlpha.md) |
| 2016-01 | **Alpha101**（Wilmott Magazine 2016） | 公开 101 个实盘使用过的公式 Alpha，是后续自动挖掘的基础因子库与基准。 | — | `formulaic` | [arXiv](https://arxiv.org/abs/1601.00991) · [速读](notes/cards/2016_Alpha101.md) |

## 2. 问题 × 工作矩阵

“●”表示该工作针对这个问题；末行是各问题的工作数。

| 工作 | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 | P10 |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| QBX | ● |   |   |   |   | ● |   |   |   | ● |
| FactorBench |   |   |   |   |   |   |   | ● |   | ● |
| Auditing LLM Alpha-Factor Mining |   |   |   |   |   |   |   |   |   | ● |
| AlphaPilot |   |   |   |   |   |   |   |   |   |   |
| AlphaPADI |   |   |   |   |   |   |   |   |   |   |
| AlphaPareto |   |   |   |   |   |   |   |   |   |   |
| AlphaDiverse |   |   |   |   |   |   |   |   |   |   |
| MAPLE |   |   |   |   |   |   |   |   |   |   |
| AlphaSchema |   |   |   |   |   |   |   |   |   |   |
| Agora/SJS |   |   |   |   | ● | ● |   |   |   |   |
| QuantEvolver | ● |   | ● | ● |   |   | ● |   |   |   |
| Hubble | ● |   |   |   |   |   | ● | ● | ● | ● |
| FactorEngine | ● | ● | ● |   |   | ● |   |   |   |   |
| QuantaAlpha |   | ● |   |   |   |   | ● |   |   |   |
| FactorMiner |   |   | ● |   |   |   | ● |   |   | ● |
| AlphaPROBE | ● |   |   |   |   |   | ● | ● |   |   |
| Look-Ahead-Bench |   |   |   |   |   | ● |   |   |   |   |
| AlphaCFG | ● |   |   |   |   |   | ● |   |   |   |
| Alpha-R1 |   |   |   |   | ● | ● |   | ● | ● |   |
| CogAlpha | ● | ● |   |   |   | ● |   |   |   |   |
| AlphaSAGE |   |   |   | ● |   |   | ● |   |   |   |
| AlphaEval |   |   |   |   |   |   |   |   |   | ● |
| TLRS |   |   |   | ● |   |   |   |   |   |   |
| EFS |   |   |   |   |   |   | ● | ● |   |   |
| RD-Agent(Q) |   |   |   |   |   |   | ● | ● |   |   |
| AlphaQCM |   |   |   | ● |   |   |   |   |   |   |
| Alpha-Jungle | ● |   |   |   | ● |   | ● | ● |   |   |
| AlphaAgent |   | ● |   |   | ● |   | ● |   | ● |   |
| AlphaGAT |   | ● |   |   |   |   | ● | ● |   |   |
| QFR |   |   |   | ● |   |   |   |   | ● |   |
| LLM Strategy Finding | ● |   |   |   |   |   |   | ● |   |   |
| HRFT/IRFT |   | ● |   |   |   |   |   |   |   |   |
| AlphaForge |   |   | ● | ● |   |   | ● | ● | ● |   |
| Alpha2 | ● |   | ● |   |   |   |   |   |   |   |
| RiskMiner | ● |   |   | ● |   |   | ● | ● |   |   |
| QuantAgent | ● |   |   | ● |   |   |   |   |   |   |
| Alpha-GPT 2.0 | ● |   |   |   |   |   |   | ● |   |   |
| Synergistic RL | ● |   |   |   |   |   | ● |   |   |   |
| Alpha-GPT | ● | ● |   |   |   |   |   |   |   |   |
| AlphaGen | ● |   | ● |   |   |   | ● | ● |   |   |
| AlphaEvolve |   | ● | ● |   |   |   | ● |   |   |   |
| AutoAlpha | ● |   | ● |   |   |   | ● |   |   |   |
| Alpha101 |   |   |   |   |   |   |   |   |   |   |
| **合计** | 17 | 8 | 8 | 8 | 4 | 6 | 18 | 13 | 5 | 6 |

## 3. 按路线

同一篇工作可以属于多条路线。

### 公式 / 符号因子挖掘（`formulaic`，17 篇）

公式库、遗传规划与 AutoML、RL / MCTS / GFlowNet / 文法搜索等显式公式、DSL、AST 形式的因子生成。

[Alpha101](notes/cards/2016_Alpha101.md)（2016-01） · [AutoAlpha](notes/cards/2020_AutoAlpha.md)（2020-02） · [AlphaEvolve](notes/cards/2021_AlphaEvolve.md)（2021-03） · [AlphaGen](notes/cards/2023_AlphaGen.md)（2023-05） · [Synergistic RL](notes/cards/2024_SynergisticRL.md)（2024-01） · [RiskMiner](notes/cards/2024_RiskMiner.md)（2024-02） · [Alpha2](notes/cards/2024_Alpha2.md)（2024-06） · [AlphaForge](notes/cards/2024_AlphaForge.md)（2024-06） · [QFR](notes/cards/2024_QFR.md)（2024-09） · [AlphaQCM](notes/cards/2025_AlphaQCM.md)（2025-05） · [TLRS](notes/cards/2025_TLRS.md)（2025-07） · [AlphaSAGE](notes/cards/2025_AlphaSAGE.md)（2025-09） · [AlphaCFG](notes/cards/2026_AlphaCFG.md)（2026-01） · [AlphaPROBE](notes/cards/2026_AlphaPROBE.md)（2026-02） · AlphaPareto（2026-09） · AlphaPADI（2026-10） · QBX（2026-10）

### LLM / Agent 因子挖掘（`llm-agent`，19 篇）

以大语言模型或智能体完成假设生成、公式或代码实现、经验记忆、评价反馈和 RFT 的因子挖掘。

[Alpha-GPT](notes/cards/2023_Alpha-GPT.md)（2023-07） · [Alpha-GPT 2.0](notes/cards/2024_Alpha-GPT2.md)（2024-02） · [QuantAgent](notes/cards/2024_QuantAgent.md)（2024-02） · [LLM Strategy Finding](notes/cards/2024_LLMStrategyFinding.md)（2024-09） · [AlphaAgent](notes/cards/2025_AlphaAgent.md)（2025-02） · [Alpha-Jungle](notes/cards/2025_Alpha-Jungle.md)（2025-05） · [RD-Agent(Q)](notes/cards/2025_RD-Agent-Quant.md)（2025-05） · [EFS](notes/cards/2025_EFS.md)（2025-07） · [CogAlpha](notes/cards/2025_CogAlpha.md)（2025-11） · [Alpha-R1](notes/cards/2025_Alpha-R1.md)（2025-12） · [FactorMiner](notes/cards/2026_FactorMiner.md)（2026-02） · [QuantaAlpha](notes/cards/2026_QuantaAlpha.md)（2026-02） · [FactorEngine](notes/cards/2026_FactorEngine.md)（2026-03） · [Hubble](notes/cards/2026_Hubble.md)（2026-03） · [QuantEvolver](notes/cards/2026_QuantEvolver.md)（2026-05） · [Agora/SJS](notes/cards/2026_Agora-SJS.md)（2026-06） · AlphaSchema（2026-07） · AlphaDiverse（2026-09） · AlphaPilot（2026-10）

### 神经 / 隐式因子（`neural`，2 篇）

深度网络直接输出 alpha 信号或端到端学习因子表示，输出不是可解释公式。

[AlphaGAT](notes/cards/2025_AlphaGAT.md)（2025） · MAPLE（2026-07）

### 因子池与组合（`pool-combination`，6 篇）

候选因子准入、去冗余、筛选启停、动态加权和面向下游投资目标的组合。

[AlphaForge](notes/cards/2024_AlphaForge.md)（2024-06） · [AlphaGAT](notes/cards/2025_AlphaGAT.md)（2025） · [EFS](notes/cards/2025_EFS.md)（2025-07） · [Alpha-R1](notes/cards/2025_Alpha-R1.md)（2025-12） · [AlphaPROBE](notes/cards/2026_AlphaPROBE.md)（2026-02） · MAPLE（2026-07）

### 评估与稳健性（`evaluation`，5 篇）

因子评价口径、衰减、拥挤、样本外稳健性、基准数据集与评估框架。

AlphaEval（2025-08） · Look-Ahead-Bench（2026-01） · Auditing LLM Alpha-Factor Mining（2026-10） · FactorBench（2026-10） · QBX（2026-10）

### 数据与表达空间（`data-space`，1 篇）

算子空间、高频 / 分钟频数据、另类数据（文本、新闻等）和表达空间扩展。

[HRFT/IRFT](notes/cards/2024_HRFT.md)（2024-08）

### 可借鉴的相邻方法（`adjacent`，0 篇）

不是因子挖掘本身，但机制可迁移的方法，例如 Agentic RL 的信用分配与 advantage 设计。

_暂无收录，待补检。_
