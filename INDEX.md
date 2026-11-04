# 论文索引

> 本文件由 `scripts/build_index.py` 根据 `papers.yaml` 和速读卡生成，请勿手改。问题编号的含义见 README“出发点：因子挖掘面临的问题”，路线定义见 `taxonomy.yaml`。
>
> 问题分两级：“主要针对”是论文动机所在、主要贡献针对的问题（至多 3 个）；“顺带涉及”是论文中有对应机制、但不是主要贡献的问题。

共收录 64 篇（待筛 15，速读 46，精读 3）。

## 1. 总表

按首次公开时间倒序。

“问题”列先列主要针对的问题，括号内为顺带涉及的问题。

| 时间 | 工作 | 一句话 | 问题 | 路线 | 链接 |
| --- | --- | --- | --- | --- | --- |
| 2026-10 | **QBX**（ICAIF 2026） | 面向 alpha 程序的编译器：以版本化模块注册表和整策略端口 DAG 定义可审计的候选空间，编译期检查类型与时间可用性，并以内容寻址支持增量求值、去重与试验计数。 | P1 P6 P10（P2 P3 P5 P7） | `evaluation` `formulaic` | [arXiv](https://arxiv.org/abs/2610.41689) · [速读](notes/cards/2026_QBX.md) |
| 2026-10 | **LineageEvo** | 在 LLM 演化因子挖掘中引入谱系级搜索控制，用谱系经验条件化变异算子，避免搜索集中于结构相似的因子。 | — | `llm-agent` | [arXiv](https://arxiv.org/abs/2610.29663) · 待筛 |
| 2026-10 | **FactorBench** | 组合视角的挖掘基准：在共享数据与评估契约下，从因子、因子池到扣费组合三层，横向比较九种方法在五个股票市场产出的约五千个因子。 | P8 P10（P5 P7） | `evaluation` | [arXiv](https://arxiv.org/abs/2610.06947) · [代码](https://github.com/ZhuoHan1998/FactorBench-Release) · [速读](notes/cards/2026_FactorBench.md) |
| 2026-10 | **EvoQuantLab** | 免训练双循环：内层遗传规划在结构与多样性约束下演化类型化表达式，外层诊断循环审计证据以抑制回测过拟合。 | — | `llm-agent` | [arXiv](https://arxiv.org/abs/2610.17130) · 待筛 |
| 2026-10 | **Det-MASO** | 多智能体序列优化生成神经因子，在联合目标中加入智能体间相关矩阵的可微对数行列式惩罚以保持多样性。 | — | `neural` | [arXiv](https://arxiv.org/abs/2610.34936) · 待筛 |
| 2026-10 | **Auditing LLM Alpha-Factor Mining**（ICAIF 2026 AI4F Workshop（非归档）） | 对一个已留存的 LLM 因子挖掘项目做三层审计：指标统计总体混用、按样本外结果筛选造成的留存偏差，以及对冻结表达式的全量再分析。 | P10（P6） | `evaluation` | [arXiv](https://arxiv.org/abs/2610.29500) · [速读](notes/cards/2026_AuditingLLMAlpha.md) |
| 2026-10 | **AlphaRLM** | 用强化学习训练 LLM 从文献思路和可执行算子直接构造符号因子，奖励包括可执行性与分组收益区分度。 | — | `llm-agent` | [arXiv](https://arxiv.org/abs/2610.14959) · 待筛 |
| 2026-10 | **AlphaPilot** | 用 GRPO 训练多轮调用评价工具的小型 LLM：按逐日市场描述提出 DSL 公式，依据真实评价与边际池贡献维护因子池。 | P4 P8 P9（P1 P3 P7） | `llm-agent` `pool-combination` | [arXiv](https://arxiv.org/abs/2610.15488) · [速读](notes/cards/2026_AlphaPilot.md) |
| 2026-10 | **AlphaPADI** | 以整个因子池为生成单元的层次化离散扩散：在池上下文中按叶、子树、整式三级改写公式，并用池级奖励的偏好学习训练生成器。 | P4 P7 P8（P3） | `formulaic` | [arXiv](https://arxiv.org/abs/2610.04959) · [速读](notes/cards/2026_AlphaPADI.md) |
| 2026-10 | **AlphaLedger** | 用扣除冗余与成本后的组合边际贡献条件化教师，做在线策略蒸馏训练本地因子生成器，并按市场状态调整。 | — | `llm-agent` | [arXiv](https://arxiv.org/abs/2610.23744) · 待筛 |
| 2026-09 | **GoAnt** | 质量-多样性多智能体搜索：在量价与订单簿数据上按无泄漏的执行画像组织因子小生境，并动态分配评估预算。 | — | `llm-agent` `data-space` | [arXiv](https://arxiv.org/abs/2609.08719) · 待筛 |
| 2026-09 | **AlphaRJM** | 用只在终端评价时更新的奖励跳跃记忆和动作条件的 SDE 回报评论家，处理池依赖的延迟反馈。 | — | `formulaic` | [arXiv](https://arxiv.org/abs/2609.08581) · 待筛 |
| 2026-09 | **AlphaPareto**（NeurIPS 2026） | 冻结 LLM 把当前因子池编码进 PPO 状态以缓解池依赖奖励的非平稳，并把 IC、稳定性、稳健性与多样性四维奖励标量化。 | P4 P5 P7 | `formulaic` | [arXiv](https://arxiv.org/abs/2609.34188) · [代码](https://github.com/BiQiBaoWinner/AlphaPareto) · [速读](notes/cards/2026_AlphaPareto.md) |
| 2026-09 | **AlphaDiverse** | 从多样化的 API 研究轨迹构造 SFT 数据，再用兼顾预测增益与多样性的联合 GRPO 训练本地 Planner / Realizer，缓解研究路径坍缩。 | P4 P7（P1 P5 P6 P8） | `llm-agent` | [arXiv](https://arxiv.org/abs/2609.29014) · [速读](notes/cards/2026_AlphaDiverse.md) |
| 2026-08 | **AutoScientist-Quant** | 把量化研究视为受预算约束的搜索，由单一控制器决定改进、组合、转向或停止，并修正沿用评估流程中的前视漏洞。 | — | `llm-agent` | [arXiv](https://arxiv.org/abs/2608.28632) · 待筛 |
| 2026-08 | **AlphaG-OPD** | 在 GFlowNet 公式生成中对中间 AST 状态的兄弟动作做可靠性门控的反事实比较，把终端评价蒸馏为局部动作指导。 | — | `formulaic` | [arXiv](https://arxiv.org/abs/2608.01303) · 待筛 |
| 2026-08 | **AgonAlpha** | 在冻结的研究工件上搜索，由独立上下文的对抗审稿人复核与否决，配合并行预算分配并保留完整证据链。 | — | `llm-agent` | [arXiv](https://arxiv.org/abs/2608.11250) · 待筛 |
| 2026-07 | **X-Alpha** | 把研报抽象为可执行研究路径存入持久研究记忆，用记忆路由引导持续的假设到代码的因子发现。 | — | `llm-agent` | [arXiv](https://arxiv.org/abs/2607.08332) · 待筛 |
| 2026-07 | **MAPLE** | 单个神经模型一次训练输出多个低相关 Alpha：统一预测头、极端秩加权列表损失与成对相关正则，各 Alpha 子组合等权聚合。 | P7（P8） | `neural` | [arXiv](https://arxiv.org/abs/2607.24131) · [速读](notes/cards/2026_MAPLE.md) |
| 2026-07 | **AlphaSchema** | 以五元交易语义计划为搜索对象，代理奖励模型与配额选择器在 LLM 之外分配评价预算，LLM 只把选中的计划实现为因子代码。 | P1 P3（P2 P6 P7） | `llm-agent` | [arXiv](https://arxiv.org/abs/2607.26642) · [代码](https://github.com/JingyangYi/AlphaSchema) · [速读](notes/cards/2026_AlphaSchema.md) |
| 2026-06 | **Agora/SJS** | 多智能体在密封评估下联合搜索交易信号与评价协议的自演化研究环境。 | P5 P6 | `llm-agent` | [arXiv](https://arxiv.org/abs/2606.29194) · [速读](notes/cards/2026_Agora-SJS.md) |
| 2026-05 | **QuantEvolver** | 用 RFT（GRPO + DiCo 奖励）把评价反馈写进轻量 LLM 参数，代替提示词循环。 | P3 P4 P7（P1） | `llm-agent` | [arXiv](https://arxiv.org/abs/2605.15412) · [代码](https://github.com/QuantLLM/QuantEvolver) · [速读](notes/cards/2026_QuantEvolver.md) |
| 2026-03 | **Hubble** | DSL / AST 安全沙箱加正负双通道 RAG 与因子家族感知评分，持久化全部诊断。 | P1 P7 P10（P8 P9） | `llm-agent` | [arXiv](https://arxiv.org/abs/2604.09601) · [速读](notes/cards/2026_Hubble.md) |
| 2026-03 | **FactorEngine**（ICDM 2026） | 图灵完备程序因子：LLM 演化宏观逻辑，贝叶斯优化微观参数，研报知识启动。 | P1 P2（P3 P6） | `llm-agent` | [arXiv](https://arxiv.org/abs/2603.16365) · [速读](notes/cards/2026_FactorEngine.md) |
| 2026-02 | **QuantaAlpha** | 把 LLM 挖掘过程视为可演化轨迹，对高质量轨迹做局部变异与交叉。 | P2 P7 | `llm-agent` | [arXiv](https://arxiv.org/abs/2602.07085) · [代码](https://github.com/QuantaAlpha/QuantaAlpha) · [速读](notes/cards/2026_QuantaAlpha.md) |
| 2026-02 | **FactorMiner** | 技能模块封装算子与评估协议，经验记忆记录应避开的高相关区域。 | P7（P3 P10） | `llm-agent` | [arXiv](https://arxiv.org/abs/2602.14670) · [速读](notes/cards/2026_FactorMiner.md) |
| 2026-02 | **AlphaPROBE** | 在因子谱系有向无环图上检索父节点，沿演化路径有偏地生成新因子。 | P1 P7（P8） | `formulaic` `pool-combination` | [arXiv](https://arxiv.org/abs/2602.11917) · [代码](https://github.com/gta0804/AlphaPROBE) · [速读](notes/cards/2026_AlphaPROBE.md) |
| 2026-01 | **Look-Ahead-Bench** | 在 LLM 交易智能体工作流中，用知识截止前后两个时期的超额收益落差衡量前视偏差，对比标准开源 LLM 与时点化模型。 | P6 | `evaluation` `adjacent` | [arXiv](https://arxiv.org/abs/2601.13770) · [代码](https://github.com/benstaf/lookaheadbench) · [速读](notes/cards/2026_Look-Ahead-Bench.md) |
| 2026-01 | **AlphaCFG** | 用面向 alpha 的上下文无关文法约束语法、语义与长度，在其上做 RL 与 MCTS 搜索。 | P1（P7） | `formulaic` | [arXiv](https://arxiv.org/abs/2601.22119) · [代码](https://github.com/HanYang544/AlphaCFG) · [速读](notes/cards/2026_AlphaCFG.md) |
| 2025-12 | **Alpha-R1** | 用 SFT + GRPO 训练 LLM 按市场状态推理因子启停，做因子筛选。 | P8 P9（P5 P6） | `llm-agent` `pool-combination` | [arXiv](https://arxiv.org/abs/2512.23515) · [代码](https://github.com/FinStep-AI/Alpha-R1) · [速读](notes/cards/2025_Alpha-R1.md) |
| 2025-11 | **CogAlpha** | 七层 LLM 代理生成代码级 Alpha，经质量检查后做思考演化。 | P1 P2（P6） | `llm-agent` | [arXiv](https://arxiv.org/abs/2511.18850) · [速读](notes/cards/2025_CogAlpha.md) |
| 2025-10 | **Factor-Newsflow Fusion** | 比较量化因子与 LLM 新闻表示的多种融合方式，用于收益预测与选股。 | — | `data-space` | [arXiv](https://arxiv.org/abs/2510.15691) · 待筛 |
| 2025-09 | **Tree-GRPO**（ICLR 2026） | 以智能体步骤为节点做树搜索采样，用树内与树间的组相对优势从结果奖励构造过程信号。 | P3 P4 | `adjacent` | [arXiv](https://arxiv.org/abs/2509.21240) · [代码](https://github.com/AMAP-ML/Tree-GRPO) · [速读](notes/cards/2025_Tree-GRPO.md) |
| 2025-09 | **AlphaSAGE**（ICLR 2026（Poster）） | AST + RGCN 编码公式结构，GFlowNet 按多信号奖励成比例采样多样因子。 | P4 P7 | `formulaic` | [arXiv](https://arxiv.org/abs/2509.25055) · [代码](https://github.com/BerkinChen/AlphaSAGE) · [速读](notes/cards/2025_AlphaSAGE.md) · [精读](notes/deep/2025_AlphaSAGE.md) |
| 2025-08 | **TreEvo** | 把 LLM 的扁平思路改为层次化的树状思路并演化，扩大有效搜索空间、缓解位置偏差。 | — | `llm-agent` | [arXiv](https://arxiv.org/abs/2508.16334) · 待筛 |
| 2025-08 | **Sentiment-Aware LLM Alpha**（Digital Finance） | LLM 依据量价、技术指标和关联公司情绪分数生成公式 Alpha，作为 Transformer 股价预测的高层特征。 | — | `llm-agent` `data-space` | [arXiv](https://arxiv.org/abs/2508.04975) · 待筛 |
| 2025-08 | **AlphaEval**（KDD 2026） | 免回测、可并行的公式 Alpha 评估框架：从预测力、时间稳定性、扰动稳健性、金融逻辑与多样性五个维度评价挖掘出的因子集。 | P3 P10（P2 P7 P8） | `evaluation` | [arXiv](https://arxiv.org/abs/2508.13174) · [代码](https://github.com/LeoDingggg/AlphaEval) · [速读](notes/cards/2025_AlphaEval.md) |
| 2025-07 | **TLRS** | 以专家因子子序列匹配做轨迹级奖励塑形，并用奖励中心化稳定训练。 | P4 | `formulaic` | [arXiv](https://arxiv.org/abs/2507.20263) · [速读](notes/cards/2025_TLRS.md) |
| 2025-07 | **EFS** | LLM 演化可执行的资产打分因子，用于只选 Top-m 资产的稀疏组合。 | P8（P7） | `llm-agent` `pool-combination` | [arXiv](https://arxiv.org/abs/2507.17211) · [速读](notes/cards/2025_EFS.md) |
| 2025-06 | **DeepMind AlphaEvolve** | 由 LLM 集成改写代码、自动评价器打分、程序库驱动演化的代码优化智能体；与 2021 年的因子挖掘论文 AlphaEvolve 无关。 | P1（P2 P3 P7） | `adjacent` | [arXiv](https://arxiv.org/abs/2506.13131) · [速读](notes/cards/2025_DeepMind-AlphaEvolve.md) |
| 2025-05 | **RD-Agent(Q)**（NeurIPS 2025） | 多智能体分别迭代因子与模型，用 Thompson 采样调度二者的联合优化。 | P8（P7） | `llm-agent` | [arXiv](https://arxiv.org/abs/2505.15155) · [代码](https://github.com/microsoft/RD-Agent) · [速读](notes/cards/2025_RD-Agent-Quant.md) |
| 2025-05 | **GiGPO**（NeurIPS 2025） | 多轮 LLM 智能体强化学习中，按回合与锚点状态两级分组估计相对优势，无需 critic 与额外 rollout。 | P4 | `adjacent` | [arXiv](https://arxiv.org/abs/2505.10978) · [代码](https://github.com/langfengQ/verl-agent) · [速读](notes/cards/2025_GiGPO.md) |
| 2025-05 | **AlphaQCM**（ICML 2025） | 分布式强化学习估计奖励方差（QCM），作为非平稳稀疏奖励下的探索奖励。 | P4 | `formulaic` | [论文](https://openreview.net/forum?id=3sXMHlhBSs) · [代码](https://github.com/ZhuZhouFan/AlphaQCM) · [速读](notes/cards/2025_AlphaQCM.md) |
| 2025-05 | **Alpha-Jungle**（AAAI 2026） | LLM 驱动的 MCTS 逐步精炼公式，多维评价并规避高频子树。 | P1 P7（P5 P8） | `llm-agent` | [arXiv](https://arxiv.org/abs/2505.11122) · [速读](notes/cards/2025_Alpha-Jungle.md) |
| 2025-02 | **AlphaAgent**（KDD 2025） | 多智能体闭环，以 AST 原创性、假设一致性与复杂度正则对抗因子衰减。 | P7 P9（P2 P5） | `llm-agent` | [arXiv](https://arxiv.org/abs/2502.16789) · [代码](https://github.com/RndmVariableQ/AlphaAgent) · [速读](notes/cards/2025_AlphaAgent.md) |
| 2025 | **AlphaGAT**（IJCAI 2025） | CATimeMixer 生成神经 Alpha，再用 GAT + PPO 动态学习因子权重做组合选择。 | P2 P8（P7） | `neural` `pool-combination` | [论文](https://www.ijcai.org/proceedings/2025/834) · [速读](notes/cards/2025_AlphaGAT.md) · [精读](notes/deep/2025_AlphaGAT.md) |
| 2024-12 | **Warm Start GP** | 以精心选择的初始化和结构约束让遗传规划聚焦有希望的区域，提高搜索效率与因子可解释性。 | — | `formulaic` | [arXiv](https://arxiv.org/abs/2412.00896) · 待筛 |
| 2024-09 | **QFR**（IEEE Transactions on Signal Processing 2025） | 用带贪婪基线、无价值网络的 REINFORCE 替代 PPO，并以信息比率提升稳定性。 | P4 P9 | `formulaic` | [arXiv](https://arxiv.org/abs/2409.05144) · [速读](notes/cards/2024_QFR.md) |
| 2024-09 | **LLM Strategy Finding** | 从多模态财经材料抽取策略要素形成种子 Alpha，经多智能体评估后动态加权。 | P1 P8 | `llm-agent` | [arXiv](https://arxiv.org/abs/2409.06289) · [代码](https://github.com/kouzhizhuo/Automate-Strategy-Finding-with-LLM-in-Quant-investment) · [速读](notes/cards/2024_LLMStrategyFinding.md) |
| 2024-08 | **HRFT/IRFT**（WWW 2025（Industry Track）） | Transformer 以符号-数值混合词表端到端生成含常数的高频风险因子公式。 | P2 | `data-space` | [arXiv](https://arxiv.org/abs/2408.01271) · [代码](https://github.com/wencyxu/IRF-LLM-accepted-at-WWW25-) · [速读](notes/cards/2024_HRFT.md) |
| 2024-06 | **AlphaForge**（AAAI 2025） | 生成器-预测器挖掘因子，使用阶段按近期表现动态筛选并加权组合。 | P4 P8 P9（P3 P7） | `formulaic` `pool-combination` | [arXiv](https://arxiv.org/abs/2406.18394) · [代码](https://github.com/dulyhao/alphaforge) · [速读](notes/cards/2024_AlphaForge.md) · [精读](notes/deep/2024_AlphaForge.md) |
| 2024-06 | **Alpha2** | 把公式生成改为带寄存器的程序构造，搜索中做维度检查，由 RL 引导 MCTS。 | P1（P3） | `formulaic` | [arXiv](https://arxiv.org/abs/2406.16505) · [代码](https://github.com/x35f/alpha2) · [速读](notes/cards/2024_Alpha2.md) |
| 2024-02 | **RiskMiner**（ICAIF 2024） | 风险偏好 MCTS：合法中间表达式即时奖励，并惩罚与已有因子的重复。 | P1 P4（P7 P8） | `formulaic` | [arXiv](https://arxiv.org/abs/2402.07080) · [速读](notes/cards/2024_RiskMiner.md) |
| 2024-02 | **QuantAgent** | 内外双循环的自改进 LLM 智能体，持续积累交易信号知识库。 | P1（P4） | `llm-agent` | [arXiv](https://arxiv.org/abs/2402.03755) · [速读](notes/cards/2024_QuantAgent.md) |
| 2024-02 | **Alpha-GPT 2.0** | 把人在回路的 LLM 交互扩展到研究、建模、分析的完整量化研究流程。 | P1（P8） | `llm-agent` | [arXiv](https://arxiv.org/abs/2402.09746) · [速读](notes/cards/2024_Alpha-GPT2.md) |
| 2024-01 | **Synergistic RL**（ICOIN 2024） | 在 AlphaGen 上扩展算子与长窗口，并用优质种子公式引导探索。 | P1（P7） | `formulaic` | [arXiv](https://arxiv.org/abs/2401.02710) · [速读](notes/cards/2024_SynergisticRL.md) |
| 2023-07 | **Alpha-GPT**（EMNLP 2025（System Demonstrations）） | 人机交互的 LLM 因子挖掘：想法生成、公式实现与结果复盘，配合遗传规划搜索。 | P1（P2） | `llm-agent` | [arXiv](https://arxiv.org/abs/2308.00016) · [速读](notes/cards/2023_Alpha-GPT.md) |
| 2023-05 | **AlphaGen**（KDD 2023（ADS Track）） | 把 RPN 公式生成建模为 MDP，用因子池组合 IC 的边际贡献作为 PPO 奖励。 | P7 P8（P1 P3） | `formulaic` | [arXiv](https://arxiv.org/abs/2306.12964) · [代码](https://github.com/ICT-FinD-Lab/alphagen) · [速读](notes/cards/2023_AlphaGen.md) |
| 2022-01 | **Trajectory Balance**（NeurIPS 2022） | 提出轨迹平衡目标，在完整轨迹上约束 GFlowNet 流量一致，改进长序列的信用分配。 | P4（P7） | `adjacent` | [arXiv](https://arxiv.org/abs/2201.13259) · [代码](https://github.com/GFNOrg/gflownet/tree/trajectory_balance) · [速读](notes/cards/2022_TrajectoryBalance.md) |
| 2021-06 | **GFlowNet**（NeurIPS 2021） | 学习按奖励成比例采样离散对象的生成策略，用于生成多样的高奖励候选。 | P7（P3 P4） | `adjacent` | [arXiv](https://arxiv.org/abs/2106.04399) · [代码](https://github.com/bengioe/gflownet) · [速读](notes/cards/2021_GFlowNet.md) |
| 2021-03 | **AlphaEvolve**（SIGMOD 2021（Data Science and Engineering Track）） | AutoML 进化搜索，引入矩阵 / 向量算子与行业关系，并剪枝冗余表达式。 | P2 P7（P3） | `formulaic` | [arXiv](https://arxiv.org/abs/2103.16196) · [速读](notes/cards/2021_AlphaEvolve.md) |
| 2020-02 | **AutoAlpha** | 从低阶根基因逐层扩展的遗传规划，配合 PCA 近似的质量-多样性搜索。 | P1 P7（P3） | `formulaic` | [arXiv](https://arxiv.org/abs/2002.08245) · [速读](notes/cards/2020_AutoAlpha.md) |
| 2019-12 | **DSR**（ICLR 2021） | 用 RNN 自回归生成表达式，以风险寻求策略梯度只按高分位样本更新，用于符号回归。 | P4（P1） | `adjacent` | [arXiv](https://arxiv.org/abs/1912.04871) · [代码](https://github.com/brendenpetersen/deep-symbolic-regression) · [速读](notes/cards/2019_DSR.md) |
| 2016-01 | **Alpha101**（Wilmott Magazine 2016） | 公开 101 个实盘使用过的公式 Alpha，是后续自动挖掘的基础因子库与基准。 | — | `formulaic` | [arXiv](https://arxiv.org/abs/1601.00991) · [速读](notes/cards/2016_Alpha101.md) |

## 2. 问题 × 工作矩阵

“●”为主要针对，“○”为顺带涉及；末两行是各问题的工作数。尚未判断问题的待筛工作不列入。

| 工作 | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 | P10 |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| QBX | ● | ○ | ○ |   | ○ | ● | ○ |   |   | ● |
| FactorBench |   |   |   |   | ○ |   | ○ | ● |   | ● |
| Auditing LLM Alpha-Factor Mining |   |   |   |   |   | ○ |   |   |   | ● |
| AlphaPilot | ○ |   | ○ | ● |   |   | ○ | ● | ● |   |
| AlphaPADI |   |   | ○ | ● |   |   | ● | ● |   |   |
| AlphaPareto |   |   |   | ● | ● |   | ● |   |   |   |
| AlphaDiverse | ○ |   |   | ● | ○ | ○ | ● | ○ |   |   |
| MAPLE |   |   |   |   |   |   | ● | ○ |   |   |
| AlphaSchema | ● | ○ | ● |   |   | ○ | ○ |   |   |   |
| Agora/SJS |   |   |   |   | ● | ● |   |   |   |   |
| QuantEvolver | ○ |   | ● | ● |   |   | ● |   |   |   |
| Hubble | ● |   |   |   |   |   | ● | ○ | ○ | ● |
| FactorEngine | ● | ● | ○ |   |   | ○ |   |   |   |   |
| QuantaAlpha |   | ● |   |   |   |   | ● |   |   |   |
| FactorMiner |   |   | ○ |   |   |   | ● |   |   | ○ |
| AlphaPROBE | ● |   |   |   |   |   | ● | ○ |   |   |
| Look-Ahead-Bench |   |   |   |   |   | ● |   |   |   |   |
| AlphaCFG | ● |   |   |   |   |   | ○ |   |   |   |
| Alpha-R1 |   |   |   |   | ○ | ○ |   | ● | ● |   |
| CogAlpha | ● | ● |   |   |   | ○ |   |   |   |   |
| Tree-GRPO |   |   | ● | ● |   |   |   |   |   |   |
| AlphaSAGE |   |   |   | ● |   |   | ● |   |   |   |
| AlphaEval |   | ○ | ● |   |   |   | ○ | ○ |   | ● |
| TLRS |   |   |   | ● |   |   |   |   |   |   |
| EFS |   |   |   |   |   |   | ○ | ● |   |   |
| DeepMind AlphaEvolve | ● | ○ | ○ |   |   |   | ○ |   |   |   |
| RD-Agent(Q) |   |   |   |   |   |   | ○ | ● |   |   |
| GiGPO |   |   |   | ● |   |   |   |   |   |   |
| AlphaQCM |   |   |   | ● |   |   |   |   |   |   |
| Alpha-Jungle | ● |   |   |   | ○ |   | ● | ○ |   |   |
| AlphaAgent |   | ○ |   |   | ○ |   | ● |   | ● |   |
| AlphaGAT |   | ● |   |   |   |   | ○ | ● |   |   |
| QFR |   |   |   | ● |   |   |   |   | ● |   |
| LLM Strategy Finding | ● |   |   |   |   |   |   | ● |   |   |
| HRFT/IRFT |   | ● |   |   |   |   |   |   |   |   |
| AlphaForge |   |   | ○ | ● |   |   | ○ | ● | ● |   |
| Alpha2 | ● |   | ○ |   |   |   |   |   |   |   |
| RiskMiner | ● |   |   | ● |   |   | ○ | ○ |   |   |
| QuantAgent | ● |   |   | ○ |   |   |   |   |   |   |
| Alpha-GPT 2.0 | ● |   |   |   |   |   |   | ○ |   |   |
| Synergistic RL | ● |   |   |   |   |   | ○ |   |   |   |
| Alpha-GPT | ● | ○ |   |   |   |   |   |   |   |   |
| AlphaGen | ○ |   | ○ |   |   |   | ● | ● |   |   |
| Trajectory Balance |   |   |   | ● |   |   | ○ |   |   |   |
| GFlowNet |   |   | ○ | ○ |   |   | ● |   |   |   |
| AlphaEvolve |   | ● | ○ |   |   |   | ● |   |   |   |
| AutoAlpha | ● |   | ○ |   |   |   | ● |   |   |   |
| DSR | ○ |   |   | ● |   |   |   |   |   |   |
| Alpha101 |   |   |   |   |   |   |   |   |   |   |
| **主要** | 17 | 6 | 4 | 15 | 2 | 3 | 16 | 10 | 5 | 5 |
| **涉及** | 5 | 6 | 12 | 2 | 6 | 6 | 14 | 8 | 1 | 1 |

## 3. 按问题

每个问题下列出标注它的工作及速读卡中写明的对应机制，按首次公开时间排序。机制的归纳与比较见[各问题的应对机制](topics/problems.md)。

### P1 表达空间巨大，有效因子稀少（主要 17，涉及 5）

主要针对：

- [AutoAlpha](notes/cards/2020_AutoAlpha.md)：从低阶到高阶的层次化搜索。
- [Alpha-GPT](notes/cards/2023_Alpha-GPT.md)：研究员想法与层次化字段检索。
- [Synergistic RL](notes/cards/2024_SynergisticRL.md)：扩展算子集与长窗口以扩大搜索空间，并在经验回放中注入优质种子公式。
- [Alpha-GPT 2.0](notes/cards/2024_Alpha-GPT2.md)：研究员想法贯穿研究、建模、分析全流程，作为搜索先验。
- [QuantAgent](notes/cards/2024_QuantAgent.md)：持续积累并检索的信号知识库。
- [RiskMiner](notes/cards/2024_RiskMiner.md)：MCTS 显式复用已探索结构。
- [Alpha2](notes/cards/2024_Alpha2.md)：寄存器程序表示与维度检查。
- [LLM Strategy Finding](notes/cards/2024_LLMStrategyFinding.md)：从文本、表格、图像材料中抽取种子因子，锚定搜索起点。
- [Alpha-Jungle](notes/cards/2025_Alpha-Jungle.md)：MCTS 显式复用已探索结构。
- [DeepMind AlphaEvolve](notes/cards/2025_DeepMind-AlphaEvolve.md)：用 LLM 依据上下文中的历史程序与得分提出有针对性的 diff，代替需要人工设计、可能抓不住领域性质的手写变异算子（第 2.3、5 节），并用评价级联尽早过滤有错程序（第 2.4 节）→ 对应代码因子空间中随机变异大多无效、LLM 生成代码常不可执行的问题，用带反馈的 LLM 变异和前置执行检查提高有效候选比例；已收录的 FactorEngine（由 LLM 做宏观逻辑变异）与 CogAlpha（思考演化中的精炼、变异与重组）属同类 LLM 代码演化（见两者速读卡）。
- [CogAlpha](notes/cards/2025_CogAlpha.md)：七层代理加自适应生成与多种改写模式，扩大有效搜索范围。
- [AlphaCFG](notes/cards/2026_AlphaCFG.md)：面向 alpha 的上下文无关文法与语义、长度约束。
- [AlphaPROBE](notes/cards/2026_AlphaPROBE.md)：因子谱系图上的有偏演化。
- [FactorEngine](notes/cards/2026_FactorEngine.md)：宏观逻辑演化与微观参数优化分离；从研报和专家因子抽取初始程序池。
- [Hubble](notes/cards/2026_Hubble.md)：白名单 AST 沙箱。
- [AlphaSchema](notes/cards/2026_AlphaSchema.md)：搜索对象从公式或代码换成显式、有限的语义计划空间，代理奖励模型在实现前从大量采样计划中预选；失败计划以零奖励留在缓冲区，代理模型由此学会避开难以实现的语义结构（第 3 节、附录 A）。
- [QBX](notes/cards/2026_QBX.md)：编译器准入与编译器闭合的图编辑动作，把候选限制在类型正确、无环、时间可用、可链接执行的程序空间内；另有只警告、不阻止准入的单位与量纲元数据检查，定位存量与流量混算等无意义运算（E16）。

顺带涉及：

- [DSR](notes/cards/2019_DSR.md)：符号回归中把先验约束放在自回归采样时执行，直接屏蔽违规 token，样本无需事后拒绝即全部合法；论文还报告 GP 加入事后约束反而降低表现（第 3.1、4 节，附录 F）→ 对应公式因子生成中的语法、类型与无意义组合约束，以 mask 前置可把评价预算集中在合法表达式上；已收录的 AlphaSAGE 在语法合法动作中逐步采样，属同类做法（见 AlphaSAGE 速读卡）。
- [AlphaGen](notes/cards/2023_AlphaGen.md)：动作掩码与栈规则。
- [QuantEvolver](notes/cards/2026_QuantEvolver.md)：用因子 DSL 约束可生成的表达式，消融中去掉 DSL 后表现大幅下降。
- [AlphaDiverse](notes/cards/2026_AlphaDiverse.md)：用经济机制目录约束研究方向；为每个计划只检索少量相关特征与算子，减少实现歧义；Realizer 的生成受 JSON 文法约束，无效规格带着校验反馈修复（第 2.1 节、附录 B.2）。
- [AlphaPilot](notes/cards/2026_AlphaPilot.md)：评价工具强制固定 DSL 文法，返回非法表达式与执行错误；搜索以 20 条种子因子库和 regime 描述为起点，近期已试因子记忆用于避免重复失败（第 4.1–4.3 节、附录 A.4、表 14）。

### P2 表达能力与可解释性的权衡（主要 6，涉及 6）

主要针对：

- [AlphaEvolve](notes/cards/2021_AlphaEvolve.md)：矩阵和向量算子与行业关系注入。
- [HRFT/IRFT](notes/cards/2024_HRFT.md)：符号-数值混合词表生成含常数的公式。
- [AlphaGAT](notes/cards/2025_AlphaGAT.md)：神经网络直接输出 alpha。
- [CogAlpha](notes/cards/2025_CogAlpha.md)：以代码而非受限 DSL 表示 Alpha，扩大表达空间。
- [QuantaAlpha](notes/cards/2026_QuantaAlpha.md)：假设、描述、表达式之间的一致性校验。
- [FactorEngine](notes/cards/2026_FactorEngine.md)：把因子表示扩展为可执行程序，超出固定符号文法。

顺带涉及：

- [Alpha-GPT](notes/cards/2023_Alpha-GPT.md)：把生成的公式反编译为自然语言解释，便于审计其声称的逻辑。
- [AlphaAgent](notes/cards/2025_AlphaAgent.md)：假设、描述、表达式之间的一致性校验。
- [DeepMind AlphaEvolve](notes/cards/2025_DeepMind-AlphaEvolve.md)：演化对象从单个函数扩展到整个代码文件与多个组件，并可选择演化解本身、构造函数或定制搜索算法等不同抽象层次（第 2.1 节）；数据中心调度任务选用其代码解而非深度强化学习，理由是可解释、可调试、可预测且易部署（第 3.3.1 节）→ 对应以程序而非受限 DSL 表示因子，在扩大表达能力的同时保留可读、可审计的代码形式；已收录的 FactorEngine 与 CogAlpha 都把因子表示扩展为可执行代码（见两者速读卡）。
- [AlphaEval](notes/cards/2025_AlphaEval.md)：用 LLM 评分的 Logic Score 度量表达式的金融逻辑与可解释性，并以人工专家排序检验其一致性，使不同范式在可解释性上可比。
- [AlphaSchema](notes/cards/2026_AlphaSchema.md)：因子以任意 pandas 代码实现，但实现前先用五元语义计划声明交易逻辑，提示词还要求代码开头的注释逐项对应 Event、Context、Quality、Direction、Output（第 2 节、附录 D）。
- [QBX](notes/cards/2026_QBX.md)：以受限的登记词表换取可审计性，并实测这一限制的代价：只用类型化搜索的因子簿行为广度不足，LLM 提议的广度与 QBX 局部搜索的深度结合后可以弥补。

### P3 评价成本高（主要 4，涉及 12）

主要针对：

- [AlphaEval](notes/cards/2025_AlphaEval.md)：五项指标都是可独立并行计算的信号矩阵函数，不需要按时间顺序推进、带仓位与现金状态的组合回测。
- [Tree-GRPO](notes/cards/2025_Tree-GRPO.md)：共享前缀的树搜索在同一 token 与工具调用预算下得到更多 rollout，在每题约 2 条完整轨迹的低预算下仍能学会多轮交互，并以四分之一预算超过链式方法（第 3.1、4.3 节，表 3）→ 对应 LLM 因子智能体中每轮生成与评价调用都计入成本的情形：从中间轮次分叉、复用已完成的前缀步骤，可在同等生成与评价预算下获得更多训练样本；已收录的 QuantEvolver 与 Alpha-R1 速读卡记录的是 GRPO 组相对优势，未见树结构采样。
- [QuantEvolver](notes/cards/2026_QuantEvolver.md)：用 RFT 把经验写入轻量模型参数，代替不断增长的提示词上下文。
- [AlphaSchema](notes/cards/2026_AlphaSchema.md)：代理模型在 LLM 实现和回测之前给候选打分，配额选择器分配有限的实现与回测预算；论文还比较了同一计划重复实现的预算效率，据此选用单次实现（第 3 节、第 5 节、附录 E）。

顺带涉及：

- [AutoAlpha](notes/cards/2020_AutoAlpha.md)：PCA 近似相似度降低去重成本。
- [AlphaEvolve](notes/cards/2021_AlphaEvolve.md)：冗余剪枝与指纹机制跳过重复计算。
- [GFlowNet](notes/cards/2021_GFlowNet.md)：原领域的真实检测昂贵，论文用廉价代理模型给奖励，生成器拟合代理诱导的分布后每轮只把一批多样样本送真实 oracle，再用新标注数据更新代理（第 4.3 节）；论文还指出这种批量生成的计算成本与批大小呈线性，而两两比较候选的方法至少为平方（第 1 节）→ 对应因子挖掘中用预测器或子样本评价作为代理奖励训练生成器，只把多样化的候选批次送全市场长周期回测；已收录工作中未见在 GFlowNet 中借用这一多轮代理流程，仓库专题“公式因子挖掘的三类训练方法”记录的 AlphaForge Predictor 属同类代理思路，但不是 GFlowNet。
- [AlphaGen](notes/cards/2023_AlphaGen.md)：用预存的 IC 与互相关增量更新组合损失，避免每次重算。
- [Alpha2](notes/cards/2024_Alpha2.md)：搜索阶段的维度预剪枝提前排除不可能合法的程序。
- [AlphaForge](notes/cards/2024_AlphaForge.md)：用可微预测器代替部分真实评价来引导生成。
- [DeepMind AlphaEvolve](notes/cards/2025_DeepMind-AlphaEvolve.md)：评价级联先在小规模、低难度测试上筛掉不理想的候选，评价可异步分发到集群并行执行，整条流水线以总吞吐而非单次计算速度为优化目标，LLM 集成中用低延迟模型提高单位时间的候选数（第 2.3、2.4、2.6 节）→ 对应因子评价中先用短区间、小股票池或子样本做廉价初筛，只把通过者送全市场长周期回测，并按吞吐组织 LLM 生成与回测；已收录工作中未见明确借用评价级联，CogAlpha 先做代码与执行检查再按 IC 等指标过滤的流程与之相近（见 CogAlpha 速读卡）。
- [FactorMiner](notes/cards/2026_FactorMiner.md)：先在小资产集快速筛选，再在相关性剪枝后做全量验证。
- [FactorEngine](notes/cards/2026_FactorEngine.md)：微观参数用贝叶斯优化实例化，运行中不额外调用大模型。
- [AlphaPADI](notes/cards/2026_AlphaPADI.md)：把公式在历史面板上的执行视为主要成本，按去重后的规范式计提交预算（|A| ≤ B，失败提交计入，缓存命中不计），偏好目标复用缓冲区中已评分的池，不必消耗预算采新的同策略样本（第 3 节、附录 B.1.2）。
- [AlphaPilot](notes/cards/2026_AlphaPilot.md)：以短期未来窗口 IC/RankIC 作代理奖励，不在每条训练轨迹中做完整回测；训练 4B 小模型代替大模型推理（第 2.2 节、Limitations、附录 B.1）。
- [QBX](notes/cards/2026_QBX.md)：节点级内容地址只重算编辑影响的依赖锥；准入与去重是微秒级 CPU 开销，每次 LLM 调用可以扩展为大量合法候选。

### P4 学习信号稀疏、延迟且不可微（主要 15，涉及 2）

主要针对：

- [DSR](notes/cards/2019_DSR.md)：奖励只在表达式完成时出现且不可微，论文用策略梯度训练生成器，并以风险寻求目标只用批内高于 (1−ε) 分位数的样本、以该分位数为基线更新（第 3.2 节）→ 对应公式因子只有完整生成后才有 IC、IC 对 token 无梯度，且挖掘最终只保留少数高分因子，可用分位数基线把更新集中到高分尾部；已收录的 RiskMiner 采用同一思路的风险偏好优化，关注回报分布高分位而非均值（见 RiskMiner 速读卡）。
- [Trajectory Balance](notes/cards/2022_TrajectoryBalance.md)：用整条轨迹上的一个残差同时更新所有步的 log P_F，终端奖励一次分配到每个动作，而不是像 FM / DB 那样逐步回传；比特序列任务中 FM 的拟合随轨迹变短而改善，TB 对轨迹长度与动作空间大小都稳健（第 3、5.3.1 节，图 4）→ 对应公式 token 序列只有终端 IC、序列较长且词表大的情形，可用 TB 把终端奖励直接分到每个 token；已收录的 AlphaSAGE 即用 TB 损失训练公式生成的前向策略（见 AlphaSAGE 速读卡与精读第 6 节）。
- [RiskMiner](notes/cards/2024_RiskMiner.md)：合法中间表达式即时奖励。
- [AlphaForge](notes/cards/2024_AlphaForge.md)：可微预测器把 fitness 变成生成器的梯度。
- [QFR](notes/cards/2024_QFR.md)：不带价值网络的 REINFORCE 加贪婪基线。
- [AlphaQCM](notes/cards/2025_AlphaQCM.md)：奖励分布方差作为探索奖励。
- [GiGPO](notes/cards/2025_GiGPO.md)：在不增加 rollout、不训练 critic 的前提下，从已采样轨迹中重复出现的状态回溯构造步骤级组，用同一状态下不同动作之后的折扣回报差异给出逐步信用，并与回合级优势相加（第 4.2–4.3 节）→ 对应公式逐 token 生成或多轮 LLM 因子智能体只在完成后得到 IC 的情形：同一批采样中重复出现的公式前缀或智能体状态可作为锚点，比较其后不同动作的最终奖励，得到比整条轨迹更细的信用；已收录的 QuantEvolver 与 Alpha-R1 使用的是回合级 GRPO 组相对优势（见两者速读卡），未见借用步骤级锚点分组。
- [TLRS](notes/cards/2025_TLRS.md)：专家子序列轨迹级塑形与奖励中心化。
- [AlphaSAGE](notes/cards/2025_AlphaSAGE.md)：预测性能、结构对齐与新颖性的多信号奖励加轨迹平衡。
- [Tree-GRPO](notes/cards/2025_Tree-GRPO.md)：只用结果奖励，在每个分叉点比较兄弟子树回传的奖励，把轨迹级信号转成粒度随子树深度变化的过程信号；树内优势提供隐式步骤级偏好，树间优势提供更稳定的基线（第 3.2–3.3 节、表 4）→ 对应公式生成或多轮因子智能体只有终端 IC 的情形：在共享前缀处分叉，比较不同后续的 IC，得到前缀层面的相对信用；已收录的 QuantEvolver 与 Alpha-R1 只用回合级 GRPO 优势（见两者速读卡），未见借用树结构优势。
- [QuantEvolver](notes/cards/2026_QuantEvolver.md)：组内相对优势更新。
- [AlphaDiverse](notes/cards/2026_AlphaDiverse.md)：联合 GRPO 按角色分配信用，Planner 在计划组合之间比较，Realizer 在同一计划的不同实现之间比较；奖励尺度和最低增益阈值用历史候选与高斯噪声因子组合的得分增益分位数校准（第 2.3 节、附录 B.2）。
- [AlphaPareto](notes/cards/2026_AlphaPareto.md)：把冻结 LLM 编码的当前因子池嵌入并入策略状态，让策略能感知池的组成；论文称这样把依赖因子池的非平稳 MDP 改写为增广状态下的平稳 MDP（第 3、4.1 节）。
- [AlphaPADI](notes/cards/2026_AlphaPADI.md)：池级奖励经符号执行和联合拟合得到，不可微；论文把它转成满足奖励间隔的池对偏好，在相同腐化变量下比较两池的重建分数做偏好学习，不需要逐公式奖励（第 2.2、4.3 节）。
- [AlphaPilot](notes/cards/2026_AlphaPilot.md)：奖励只在轨迹结束时按最终池的未来窗口表现给出，用 GRPO 组内相对优势做轨迹级信用分配，不训练单独的 critic；池完整度乘子惩罚保留因子过少的轨迹（第 4.4–4.5 节、附录 A.5）。

顺带涉及：

- [GFlowNet](notes/cards/2021_GFlowNet.md)：奖励只在终止状态给出，论文把终端奖励作为流网络的边界条件，用流守恒损失为每个中间状态提供训练目标，奖励本身无需可微，且训练可离策略、离线进行（第 2.2 节、命题 3）→ 对应公式只有完整生成后才有 IC、IC 对 token 不可微，已评价过的历史公式也可作为离策略训练轨迹复用；已收录的 AlphaSAGE 采用 GFlowNet 框架，但训练目标用的是后续的 Trajectory Balance（见 AlphaSAGE 速读卡与精读第 6 节）。
- [QuantAgent](notes/cards/2024_QuantAgent.md)：外层循环以真实回测反馈驱动知识库更新，用于下一轮生成。

### P5 低信噪比下的过拟合（主要 2，涉及 6）

主要针对：

- [Agora/SJS](notes/cards/2026_Agora-SJS.md)：最终评估数据对参与搜索的智能体保持密封。
- [AlphaPareto](notes/cards/2026_AlphaPareto.md)：把 RRE（排序的时间稳定性）与 PFS（扰动稳健性）写入奖励，用各目标最低水平约束代替只看样本内 IC，针对“高 IC 但波动大、对扰动脆弱、样本外失效”的因子池（第 3、4.2 节）。

顺带涉及：

- [AlphaAgent](notes/cards/2025_AlphaAgent.md)：AST 节点数、参数数、特征数正则。
- [Alpha-Jungle](notes/cards/2025_Alpha-Jungle.md)：在评价中显式给过拟合风险打分。
- [Alpha-R1](notes/cards/2025_Alpha-R1.md)：用 PSR、DSR、PBO 等多重检验校正评估筛选结果的显著性。
- [AlphaDiverse](notes/cards/2026_AlphaDiverse.md)：研究反馈只来自内层期，最终因子与模型冻结后只在外层期评估一次，以避免 test-set tuning；噪声校准使增益低于噪声水平的计划拿不到正的质量分；多折设置下，保留要求加权得分提升且多数折改进（主比较为单折）（第 1 节、第 2.1 节、附录 B.2、C.1）。
- [FactorBench](notes/cards/2026_FactorBench.md)：用训练期固定因子方向，比较同一批因子在训练、验证、测试期的 IC、RankIC、ICIR，并计算因子内配对的训练–测试退化量，保留样本外符号反转。
- [QBX](notes/cards/2026_QBX.md)：以根身份去重的试验账本记录实际试验次数，为 deflated Sharpe 等多重检验校正提供分母；统计校正本身留作后续工作。

### P6 前视偏差与信息泄漏（主要 3，涉及 6）

主要针对：

- [Look-Ahead-Bench](notes/cards/2026_Look-Ahead-Bench.md)：以模型知识截止时间为界，比较训练窗口内与截止后两个时期的超额收益变化，并以截止时间早于两期的时点化模型和量化基线作对照，区分记忆与真实预测；文中的 alpha decay 指这一前视偏差信号，与因子随时间衰减不是同一概念。
- [Agora/SJS](notes/cards/2026_Agora-SJS.md)：持有期评估数据不进入任何面向模型的输入。
- [QBX](notes/cards/2026_QBX.md)：时间可用性效应系统在编译期、加载数据之前拒绝登记契约可见的前视，同时允许发布时点早于索引的合法时点预测值。

顺带涉及：

- [CogAlpha](notes/cards/2025_CogAlpha.md)：多智能体质量检查器中包含时间泄漏检查。
- [Alpha-R1](notes/cards/2025_Alpha-R1.md)：用 point-in-time 成分、各模块数据截止表与前视内容审计控制泄漏。
- [FactorEngine](notes/cards/2026_FactorEngine.md)：启动资料限定只用测试期之前发布的研报，控制知识泄漏。
- [AlphaSchema](notes/cards/2026_AlphaSchema.md)：代码实现须通过前视泄漏筛查，提示词规定 t 时刻的信号只能使用 t 及之前的信息；因子筛选、相关性过滤和模型选择只用训练与验证窗口（第 3 节、附录 A、附录 D）。
- [AlphaDiverse](notes/cards/2026_AlphaDiverse.md)：执行模块拒绝使用预测时点之后信息的因子规格；特征只用 t 日收盘后可得的信息，标签为 t+1 开盘到 t+2 开盘的超额收益；各时间段边界按标签重叠做 purge；股票池按历史每日指数成分构造（第 2.1 节、附录 B.2、C.1）。
- [Auditing LLM Alpha-Factor Mining](notes/cards/2026_AuditingLLMAlpha.md)：核查“OOS 验证集”的生成过程，发现留存目录写出前已按 OOS Sharpe 剔除非正结果，并提出在接触 OOS 之前冻结并哈希候选清单、只用 IS 数据筛选与去重、保留全部 OOS 结果与报错的干净评估协议。

### P7 因子同质化与冗余（主要 16，涉及 14）

主要针对：

- [AutoAlpha](notes/cards/2020_AutoAlpha.md)：质量-多样性搜索。
- [AlphaEvolve](notes/cards/2021_AlphaEvolve.md)：冗余算子与冗余 Alpha 的剪枝和指纹去重，以及对与既有 Alpha 超出相关性阈值者的剔除。
- [GFlowNet](notes/cards/2021_GFlowNet.md)：以按奖励成比例采样为目标，覆盖奖励函数的多个模式，避免回报最大化收敛到一个或少数几个好样本（第 1–2 节）→ 对应生成器向少数高分模板坍缩、新因子彼此高度相关的问题；已收录的 AlphaSAGE 借用这一目标，使采样分布覆盖多个高奖励公式模式（见 AlphaSAGE 速读卡）。
- [AlphaGen](notes/cards/2023_AlphaGen.md)：用加入因子池后的组合 IC 边际贡献作为奖励。
- [AlphaAgent](notes/cards/2025_AlphaAgent.md)：AST 相似度。
- [Alpha-Jungle](notes/cards/2025_Alpha-Jungle.md)：高频子树规避。
- [AlphaSAGE](notes/cards/2025_AlphaSAGE.md)：结构对齐与新颖性奖励下覆盖多个高奖励模式。
- [AlphaPROBE](notes/cards/2026_AlphaPROBE.md)：谱系图上的多样性检索。
- [FactorMiner](notes/cards/2026_FactorMiner.md)：经验记忆记录应避开的高相关区域。
- [QuantaAlpha](notes/cards/2026_QuantaAlpha.md)：复杂度、结构相似度与输出相关性控制。
- [Hubble](notes/cards/2026_Hubble.md)：因子家族感知评分。
- [QuantEvolver](notes/cards/2026_QuantEvolver.md)：多样性与互补性奖励。
- [MAPLE](notes/cards/2026_MAPLE.md)：多样性正则直接惩罚 Alpha 间成对绝对相关；论文还报告，加正则之前，统一预测头已把 Alpha 间平均相关从仅用股票内路径时的 0.998 降到 0.944（第 3.3 节、第 5.1 节表 3）。
- [AlphaDiverse](notes/cards/2026_AlphaDiverse.md)：Planner 每轮须覆盖不同机制与主题，并满足相邻轮的新颖性要求；同一计划的两个实现须计算结构不同；筛选时与已有因子的平均绝对相关不得高于 0.90；GRPO 奖励中的 D 项对与历史档案相似的预测变化给递减奖励（第 2.1–2.3 节、附录 B.1、D.5）。
- [AlphaPareto](notes/cards/2026_AlphaPareto.md)：以池内因子信号协方差特征值的归一化熵 DH 作为多样性奖励；prompt 也要求 LLM 识别池内表达式同质化和信息盲区（第 4.2.1 节、附录 B）。
- [AlphaPADI](notes/cards/2026_AlphaPADI.md)：池上下文进入反向生成状态，用来决定改写哪些子结构；R_inner 惩罚与池内最近邻相关超过 δ 的成员；规范化后的重复成员替换为随机合法公式（第 4.2–4.3 节）。

顺带涉及：

- [Trajectory Balance](notes/cards/2022_TrajectoryBalance.md)：在保持按奖励比例采样的同时改进分布拟合与样本多样性，分子任务中 TB 生成的 top-1000 分子相似度始终低于 FM，比特序列任务中发现模式更快（第 5.2、5.3.1 节）→ 对应用多模式采样缓解因子模式坍缩；已收录的 AlphaSAGE 借用 TB 使采样覆盖多个高奖励公式模式（见 AlphaSAGE 速读卡）。
- [Synergistic RL](notes/cards/2024_SynergisticRL.md)：扩大算子与窗口后组合中的因子相关性下降。
- [RiskMiner](notes/cards/2024_RiskMiner.md)：中间奖励中加入与已有因子的 MutIC 重复惩罚。
- [AlphaForge](notes/cards/2024_AlphaForge.md)：入库同时检查 IC、ICIR 和相关性阈值；生成器损失中的多样性项。
- [AlphaGAT](notes/cards/2025_AlphaGAT.md)：Stage I 损失惩罚因子间协方差矩阵的非对角项。
- [RD-Agent(Q)](notes/cards/2025_RD-Agent-Quant.md)：相关性去重。
- [DeepMind AlphaEvolve](notes/cards/2025_DeepMind-AlphaEvolve.md)：程序数据库借鉴 MAP-Elites 与岛模型，在改进最优程序与保持多样性之间权衡；多指标优化把不同“好”的定义下的高分程序放入提示，以激发更多样的候选（第 2.4、2.5 节）→ 对应用分岛或按行为特征分格的候选池，防止搜索集中到少数高分模板；已收录的 FactorEngine 采用多岛并行演化促进多样搜索（见 FactorEngine 速读卡）。
- [EFS](notes/cards/2025_EFS.md)：层次聚类去重与基于随机矩阵理论的去噪和软去重。
- [AlphaEval](notes/cards/2025_AlphaEval.md)：以协方差特征值熵 DE 度量因子集的多样性，信号越共线熵越低。
- [AlphaCFG](notes/cards/2026_AlphaCFG.md)：价值目标中加入与因子池的结构相似度惩罚，并处理同构表达式。
- [AlphaSchema](notes/cards/2026_AlphaSchema.md)：探索名额按 Event-Context 覆盖度的新颖性得分分配，优先选少见组合；导出因子池按 |corr|<0.7 贪心去冗余（附录 A）。
- [AlphaPilot](notes/cards/2026_AlphaPilot.md)：池得分中加入多样性项（协方差谱的归一化熵）与稳定性项；池满时，候选须替换最弱或最冗余成员后仍提升池得分才能入池；反馈中返回候选与当前池的相似度（第 4.3 节、附录 A.1）。
- [FactorBench](notes/cards/2026_FactorBench.md)：以截面 Spearman 相关度量方法内冗余、方法间收敛和对 Alpha101 的重复，并用 Pearson 相关做稳健性检验。
- [QBX](notes/cards/2026_QBX.md)：精确字符串、结构/规范化、审计重写饱和、面板外延等价四级身份阶梯识别别名与重复，并以行为生态位占用惩罚降低入选因子间的相关性。

### P8 挖掘目标与实际使用脱节（主要 10，涉及 8）

主要针对：

- [AlphaGen](notes/cards/2023_AlphaGen.md)：组合 IC 边际贡献作为奖励。
- [AlphaForge](notes/cards/2024_AlphaForge.md)：挖掘阶段扩大候选池，使用阶段再按近期表现动态选因子、动态加权。
- [LLM Strategy Finding](notes/cards/2024_LLMStrategyFinding.md)：动态优化因子权重。
- [AlphaGAT](notes/cards/2025_AlphaGAT.md)：GAT-PPO 学习动态权重。
- [RD-Agent(Q)](notes/cards/2025_RD-Agent-Quant.md)：因子与模型联合优化。
- [EFS](notes/cards/2025_EFS.md)：稀疏组合选股。
- [Alpha-R1](notes/cards/2025_Alpha-R1.md)：用 LLM 推理决定因子启停。
- [AlphaPADI](notes/cards/2026_AlphaPADI.md)：以完整池为生成和学习对象，奖励直接取联合拟合的 ridge 组合预测表现，而不是单条公式的边际贡献；第 5.4 节据池容量实验指出，池大小的效果应通过组合预测器检验（第 3、5.4 节）。
- [AlphaPilot](notes/cards/2026_AlphaPilot.md)：入池按候选对组合信号的边际贡献决定，不看单因子质量本身，训练奖励也基于组合后的池信号；案例中几个单因子 RankIC 更高的波动调整变体因边际池增益为负被拒（第 4.3 节、第 5.4 节、表 20）。
- [FactorBench](notes/cards/2026_FactorBench.md)：把交付的因子池经统一选因子、合成与组合构建，报告扣除交易成本（long–short 另计融券成本）后的 long-only 与 long–short 表现，并做成本、调仓频率和合成方式的敏感性分析。

顺带涉及：

- [Alpha-GPT 2.0](notes/cards/2024_Alpha-GPT2.md)：新增组合构建与交易清单的风险过滤。
- [RiskMiner](notes/cards/2024_RiskMiner.md)：终端奖励取加入因子后因子池组合 IC 的变化。
- [Alpha-Jungle](notes/cards/2025_Alpha-Jungle.md)：把换手率纳入候选评分。
- [AlphaEval](notes/cards/2025_AlphaEval.md)：以相对秩熵 RRE 度量相邻期排序稳定性，并验证其与年化换手显著负相关，作为可交易性的免回测代理。
- [AlphaPROBE](notes/cards/2026_AlphaPROBE.md)：组合阶段用动态因子整合器形成每日信号，回测计入交易成本。
- [Hubble](notes/cards/2026_Hubble.md)：把换手率纳入候选评分。
- [MAPLE](notes/cards/2026_MAPLE.md)：极端秩加权损失把学习信号集中在只做多 top-k 组合实际使用的头部排名，相关惩罚取绝对值的理由也来自只做多约束；各 Alpha 先各自成组合再等权聚合（第 3.2–3.3 节、附录 A.4）。
- [AlphaDiverse](notes/cards/2026_AlphaDiverse.md)：保留和奖励都以因子集合加入后 LightGBM 预测得分的增益衡量，多样性也在“对模型预测的改变量”空间中度量，不只看单因子指标（第 2.1 节、第 2.3 节、附录 D.6）。

### P9 非平稳与因子衰减（主要 5，涉及 1）

主要针对：

- [AlphaForge](notes/cards/2024_AlphaForge.md)：滚动窗口动态选因子。
- [QFR](notes/cards/2024_QFR.md)：奖励中加入信息比率，抑制 IC 随时间的剧烈波动。
- [AlphaAgent](notes/cards/2025_AlphaAgent.md)：把原创性约束写入生成目标以对抗衰减。
- [Alpha-R1](notes/cards/2025_Alpha-R1.md)：根据市场状态推理因子启停。
- [AlphaPilot](notes/cards/2026_AlphaPilot.md)：推理时逐日按当日 regime 描述重新搜索、更新保留池，信号集随市场状态变化（第 1 节、第 4 节、第 5.1 节）。

顺带涉及：

- [Hubble](notes/cards/2026_Hubble.md)：负向检索提示应避开的拥挤模板。

### P10 评估口径不统一、难以复现（主要 5，涉及 1）

主要针对：

- [AlphaEval](notes/cards/2025_AlphaEval.md)：在同一平台、同一数据切分下用统一的多维指标评测八个挖掘模型，并开源实现与评估工具。
- [Hubble](notes/cards/2026_Hubble.md)：持久化保存每个候选的多维诊断和提示词元数据。
- [Auditing LLM Alpha-Factor Mining](notes/cards/2026_AuditingLLMAlpha.md)：逐项核对汇总指标所对应的统计总体与计数阶段，按全量队列记账并保留不可评分记录，公开实现的修正以版本化方式全部重算。
- [FactorBench](notes/cards/2026_FactorBench.md)：共享数据、目标、切分与执行契约，用适配器接入各方法的官方实现，逐次记录上游提交、配置、预算、耗时与交付因子。
- [QBX](notes/cards/2026_QBX.md)：携带证据的 IR、内容身份与试验账本统一留痕，并把多种挖掘器的适配器接入同一评估器、去重漏斗和选择协议。

顺带涉及：

- [FactorMiner](notes/cards/2026_FactorMiner.md)：技能模块中封装标准化评估协议。

## 4. 按路线

同一篇工作可以属于多条路线。

### 公式 / 符号因子挖掘（`formulaic`，20 篇）

公式库、遗传规划与 AutoML、RL / MCTS / GFlowNet / 文法搜索等显式公式、DSL、AST 形式的因子生成。

[Alpha101](notes/cards/2016_Alpha101.md)（2016-01） · [AutoAlpha](notes/cards/2020_AutoAlpha.md)（2020-02） · [AlphaEvolve](notes/cards/2021_AlphaEvolve.md)（2021-03） · [AlphaGen](notes/cards/2023_AlphaGen.md)（2023-05） · [Synergistic RL](notes/cards/2024_SynergisticRL.md)（2024-01） · [RiskMiner](notes/cards/2024_RiskMiner.md)（2024-02） · [Alpha2](notes/cards/2024_Alpha2.md)（2024-06） · [AlphaForge](notes/cards/2024_AlphaForge.md)（2024-06） · [QFR](notes/cards/2024_QFR.md)（2024-09） · Warm Start GP（2024-12） · [AlphaQCM](notes/cards/2025_AlphaQCM.md)（2025-05） · [TLRS](notes/cards/2025_TLRS.md)（2025-07） · [AlphaSAGE](notes/cards/2025_AlphaSAGE.md)（2025-09） · [AlphaCFG](notes/cards/2026_AlphaCFG.md)（2026-01） · [AlphaPROBE](notes/cards/2026_AlphaPROBE.md)（2026-02） · AlphaG-OPD（2026-08） · [AlphaPareto](notes/cards/2026_AlphaPareto.md)（2026-09） · AlphaRJM（2026-09） · [AlphaPADI](notes/cards/2026_AlphaPADI.md)（2026-10） · [QBX](notes/cards/2026_QBX.md)（2026-10）

### LLM / Agent 因子挖掘（`llm-agent`，29 篇）

以大语言模型或智能体完成假设生成、公式或代码实现、经验记忆、评价反馈和 RFT 的因子挖掘。

[Alpha-GPT](notes/cards/2023_Alpha-GPT.md)（2023-07） · [Alpha-GPT 2.0](notes/cards/2024_Alpha-GPT2.md)（2024-02） · [QuantAgent](notes/cards/2024_QuantAgent.md)（2024-02） · [LLM Strategy Finding](notes/cards/2024_LLMStrategyFinding.md)（2024-09） · [AlphaAgent](notes/cards/2025_AlphaAgent.md)（2025-02） · [Alpha-Jungle](notes/cards/2025_Alpha-Jungle.md)（2025-05） · [RD-Agent(Q)](notes/cards/2025_RD-Agent-Quant.md)（2025-05） · [EFS](notes/cards/2025_EFS.md)（2025-07） · Sentiment-Aware LLM Alpha（2025-08） · TreEvo（2025-08） · [CogAlpha](notes/cards/2025_CogAlpha.md)（2025-11） · [Alpha-R1](notes/cards/2025_Alpha-R1.md)（2025-12） · [FactorMiner](notes/cards/2026_FactorMiner.md)（2026-02） · [QuantaAlpha](notes/cards/2026_QuantaAlpha.md)（2026-02） · [FactorEngine](notes/cards/2026_FactorEngine.md)（2026-03） · [Hubble](notes/cards/2026_Hubble.md)（2026-03） · [QuantEvolver](notes/cards/2026_QuantEvolver.md)（2026-05） · [Agora/SJS](notes/cards/2026_Agora-SJS.md)（2026-06） · [AlphaSchema](notes/cards/2026_AlphaSchema.md)（2026-07） · X-Alpha（2026-07） · AgonAlpha（2026-08） · AutoScientist-Quant（2026-08） · [AlphaDiverse](notes/cards/2026_AlphaDiverse.md)（2026-09） · GoAnt（2026-09） · AlphaLedger（2026-10） · [AlphaPilot](notes/cards/2026_AlphaPilot.md)（2026-10） · AlphaRLM（2026-10） · EvoQuantLab（2026-10） · LineageEvo（2026-10）

### 神经 / 隐式因子（`neural`，3 篇）

深度网络直接输出 alpha 信号或端到端学习因子表示，输出不是可解释公式。

[AlphaGAT](notes/cards/2025_AlphaGAT.md)（2025） · [MAPLE](notes/cards/2026_MAPLE.md)（2026-07） · Det-MASO（2026-10）

### 因子池与组合（`pool-combination`，6 篇）

候选因子准入、去冗余、筛选启停、动态加权和面向下游投资目标的组合。

[AlphaForge](notes/cards/2024_AlphaForge.md)（2024-06） · [AlphaGAT](notes/cards/2025_AlphaGAT.md)（2025） · [EFS](notes/cards/2025_EFS.md)（2025-07） · [Alpha-R1](notes/cards/2025_Alpha-R1.md)（2025-12） · [AlphaPROBE](notes/cards/2026_AlphaPROBE.md)（2026-02） · [AlphaPilot](notes/cards/2026_AlphaPilot.md)（2026-10）

### 评估与稳健性（`evaluation`，5 篇）

因子评价口径、衰减、拥挤、样本外稳健性、基准数据集与评估框架。

[AlphaEval](notes/cards/2025_AlphaEval.md)（2025-08） · [Look-Ahead-Bench](notes/cards/2026_Look-Ahead-Bench.md)（2026-01） · [Auditing LLM Alpha-Factor Mining](notes/cards/2026_AuditingLLMAlpha.md)（2026-10） · [FactorBench](notes/cards/2026_FactorBench.md)（2026-10） · [QBX](notes/cards/2026_QBX.md)（2026-10）

### 数据与表达空间（`data-space`，4 篇）

算子空间、高频 / 分钟频数据、另类数据（文本、新闻等）和表达空间扩展。

[HRFT/IRFT](notes/cards/2024_HRFT.md)（2024-08） · Sentiment-Aware LLM Alpha（2025-08） · Factor-Newsflow Fusion（2025-10） · GoAnt（2026-09）

### 可借鉴的相邻方法（`adjacent`，7 篇）

不是因子挖掘本身，但机制可迁移的方法，例如 Agentic RL 的信用分配与 advantage 设计。

[DSR](notes/cards/2019_DSR.md)（2019-12） · [GFlowNet](notes/cards/2021_GFlowNet.md)（2021-06） · [Trajectory Balance](notes/cards/2022_TrajectoryBalance.md)（2022-01） · [GiGPO](notes/cards/2025_GiGPO.md)（2025-05） · [DeepMind AlphaEvolve](notes/cards/2025_DeepMind-AlphaEvolve.md)（2025-06） · [Tree-GRPO](notes/cards/2025_Tree-GRPO.md)（2025-09） · [Look-Ahead-Bench](notes/cards/2026_Look-Ahead-Bench.md)（2026-01）
