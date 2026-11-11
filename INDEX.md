# 论文索引

> 本文件由 `scripts/build_index.py` 根据 `papers.yaml` 和速读卡生成，请勿手改。问题编号的含义见 README“因子挖掘面临的问题”，路线定义见 `taxonomy.yaml`。
>
> 问题分两级：“主要针对”是论文动机所在、主要贡献针对的问题（至多 3 个）；“顺带涉及”是论文中有对应机制、但不是主要贡献的问题。

共收录 73 篇（速读 66，精读 7）。

查找论文：[总表](#all-papers) · [按问题](#by-problem) · [实验口径](#setups) · [按路线](#by-route)。

理解方法：[研究全景](topics/landscape.md) · [各问题的应对机制](topics/problems.md) · [评估口径对照](topics/evaluation_protocol.md)；查看新增与状态变化：[跟踪简报](digests/)。

<a id="all-papers"></a>

## 1. 总表

按首次公开时间倒序。

“问题”列先列主要针对的问题，括号内为顺带涉及的问题。

| 时间 | 工作 | 一句话 | 问题 | 路线 | 链接 |
| --- | --- | --- | --- | --- | --- |
| 2026-11 | **CosmosAlpha** | 把已评价因子组织成生成、结构、相关三类边的图，按 Pareto 前沿选父并引导 LLM 改写公式。 | P1 P7（P3 P8） | `formulaic` `llm-formula` | [arXiv](https://arxiv.org/abs/2611.04555) · [代码](https://github.com/wzhmtldswz/CosmosAlpha) · [速读](notes/cards/2026_CosmosAlpha.md) |
| 2026-10 | **QBX**（ICAIF 2026） | 面向 alpha 程序的编译器：以版本化模块注册表和整策略端口 DAG 定义可审计的候选空间，编译期检查类型与时间可用性，并以内容寻址支持增量求值、去重与试验计数。 | P1 P6 P10（P2 P3 P5 P7） | `formulaic` `auditing` | [arXiv](https://arxiv.org/abs/2610.41689) · [速读](notes/cards/2026_QBX.md) · [精读](notes/deep/2026_QBX.md) |
| 2026-10 | **LineageEvo** | 以因子谱系为搜索单位：谱系内经验改写 LLM 变异先验，并按质量与稀少度分层分配评价预算。 | P1 P7（P3） | `llm-formula` | [arXiv](https://arxiv.org/abs/2610.29663) · [速读](notes/cards/2026_LineageEvo.md) |
| 2026-10 | **FactorBench** | 组合视角的挖掘基准：在共享数据与评估契约下，从因子、因子池到扣费组合三层，横向比较九种方法在五个股票市场产出的约五千个因子。 | P8 P10（P5 P7） | `pool-combination` `benchmark` | [arXiv](https://arxiv.org/abs/2610.06947) · [代码](https://github.com/ZhuoHan1998/FactorBench-Release) · [速读](notes/cards/2026_FactorBench.md) · [精读](notes/deep/2026_FactorBench.md) |
| 2026-10 | **EvoQuantLab** | 免训练遗传规划内循环加诊断外循环：以等预算置换检验审计搜索多重性，并在样本外前冻结协议与准入因子。 | P3 P5 P6（P1 P2 P7 P10） | `formulaic` `llm-agent` | [arXiv](https://arxiv.org/abs/2610.17130) · [速读](notes/cards/2026_EvoQuantLab.md) · [精读](notes/deep/2026_EvoQuantLab.md) |
| 2026-10 | **Det-MASO** | 多智能体神经因子生成：对智能体间相关矩阵加可微行列式惩罚抑制同质化，并按市场状态聚类分配专精。 | P7 P9（P2 P8） | `neural` | [arXiv](https://arxiv.org/abs/2610.34936) · [速读](notes/cards/2026_Det-MASO.md) |
| 2026-10 | **Auditing LLM Alpha-Factor Mining**（ICAIF 2026 AI4F Workshop（非归档）） | 对一个已留存的 LLM 因子挖掘项目做三层审计：指标统计总体混用、按样本外结果筛选造成的留存偏差，以及对冻结表达式的全量再分析。 | P10（P6） | `auditing` | [arXiv](https://arxiv.org/abs/2610.29500) · [速读](notes/cards/2026_AuditingLLMAlpha.md) |
| 2026-10 | **AlphaRLM** | 用 DAPO 训练 LLM 从文献思路直接构造可执行符号因子，奖励为可执行有效性与池化分组收益极差。 | P1 P4（P3 P6 P8） | `formulaic` `llm-formula` | [arXiv](https://arxiv.org/abs/2610.14959) · [速读](notes/cards/2026_AlphaRLM.md) |
| 2026-10 | **AlphaPilot** | 用 GRPO 训练多轮调用评价工具的小型 LLM：按逐日市场描述提出 DSL 公式，依据真实评价与边际池贡献维护因子池。 | P4 P8 P9（P1 P3 P7） | `llm-agent` `pool-combination` | [arXiv](https://arxiv.org/abs/2610.15488) · [速读](notes/cards/2026_AlphaPilot.md) |
| 2026-10 | **AlphaPADI** | 以整个因子池为生成单元的层次化离散扩散：在池上下文中按叶、子树、整式三级改写公式，并用池级奖励的偏好学习训练生成器。 | P4 P7 P8（P3） | `formulaic` | [arXiv](https://arxiv.org/abs/2610.04959) · [速读](notes/cards/2026_AlphaPADI.md) · [精读](notes/deep/2026_AlphaPADI.md) |
| 2026-10 | **AlphaLedger** | 以扣费组合边际贡献为教师特权上下文做在线策略蒸馏，训练本地生成器并按市场状态动态定池与配权。 | P4 P8 P9（P1 P6） | `llm-agent` `pool-combination` | [arXiv](https://arxiv.org/abs/2610.23744) · [速读](notes/cards/2026_AlphaLedger.md) |
| 2026-09 | **GoAnt** | 质量-多样性存档按无泄漏的执行画像组织小生境，在量价与订单簿数据上分配评价预算。 | P3 P7 P8（P5 P6 P10） | `pool-combination` `data-space` | [arXiv](https://arxiv.org/abs/2609.08719) · [速读](notes/cards/2026_GoAnt.md) |
| 2026-09 | **AlphaRJM** | 把终端评价的奖励与结果写入事件驱动的持久记忆，并用动作条件 SDE 粒子回报评论家引导池依赖的公式搜索。 | P4（P5） | `formulaic` | [arXiv](https://arxiv.org/abs/2609.08581) · [速读](notes/cards/2026_AlphaRJM.md) |
| 2026-09 | **AlphaPareto**（NeurIPS 2026） | 冻结 LLM 把当前因子池编码进 PPO 状态以缓解池依赖奖励的非平稳，并把 IC、稳定性、稳健性与多样性四维奖励标量化。 | P4 P5 P7 | `formulaic` | [arXiv](https://arxiv.org/abs/2609.34188) · [代码](https://github.com/BiQiBaoWinner/AlphaPareto) · [速读](notes/cards/2026_AlphaPareto.md) |
| 2026-09 | **AlphaDiverse** | 从多样化的 API 研究轨迹构造 SFT 数据，再用兼顾预测增益与多样性的联合 GRPO 训练本地 Planner / Realizer，缓解研究路径坍缩。 | P4 P7（P1 P5 P6 P8） | `llm-formula` | [arXiv](https://arxiv.org/abs/2609.29014) · [速读](notes/cards/2026_AlphaDiverse.md) |
| 2026-08 | **AutoScientist-Quant** | 把因子发现、库筛选与模型搜索交给同一预算控制器，并隔离反馈窗与测试窗以修正前视。 | P3 P6 P8（P5 P7 P10） | `llm-agent` `pool-combination` | [arXiv](https://arxiv.org/abs/2608.28632) · [速读](notes/cards/2026_AutoScientist-Quant.md) |
| 2026-08 | **AlphaSeek** | LLM 以研究轨迹为单位演化公式因子：方向自动生成、AST 去冗余，并在组合层自迭代。 | P1 P7 P8（P2 P5 P9） | `formulaic` `llm-formula` | [arXiv](https://arxiv.org/abs/2608.13913) · [速读](notes/cards/2026_AlphaSeek.md) |
| 2026-08 | **AlphaG-OPD** | 在 GFlowNet 公式搜索中用同前缀兄弟动作的配对终端评价做可靠性门控的局部蒸馏，固定评价预算下改进信用分配。 | P3 P4（P7） | `formulaic` | [arXiv](https://arxiv.org/abs/2608.01303) · [速读](notes/cards/2026_AlphaG-OPD.md) |
| 2026-08 | **AgonAlpha** | 在冻结的研究工件上做搜索，由独立上下文的审稿者重跑与否决，并以感知未决状态的 MCTS 分配平台评价预算。 | P3 P10（P2 P5 P7） | `llm-agent` `auditing` | [arXiv](https://arxiv.org/abs/2608.11250) · [速读](notes/cards/2026_AgonAlpha.md) |
| 2026-07 | **X-Alpha** | 把研报抽象为可执行研究路径存入持久研究记忆，以跨周期记忆路由改写探索方向与搜索空间。 | P1 P7 P9（P2 P5 P6） | `llm-agent` `pool-combination` | [arXiv](https://arxiv.org/abs/2607.08332) · [速读](notes/cards/2026_X-Alpha.md) |
| 2026-07 | **MAPLE** | 单个神经模型一次训练输出多个低相关 Alpha：统一预测头、极端秩加权列表损失与成对相关正则，各 Alpha 子组合等权聚合。 | P7（P8） | `neural` | [arXiv](https://arxiv.org/abs/2607.24131) · [速读](notes/cards/2026_MAPLE.md) |
| 2026-07 | **AlphaSchema** | 以五元交易语义计划为搜索对象，代理奖励模型与配额选择器在 LLM 之外分配评价预算，LLM 只把选中的计划实现为因子代码。 | P1 P3（P2 P6 P7） | `llm-formula` | [arXiv](https://arxiv.org/abs/2607.26642) · [代码](https://github.com/JingyangYi/AlphaSchema) · [速读](notes/cards/2026_AlphaSchema.md) |
| 2026-06 | **AlphaMemo** | 以父子 AST 差异为编辑单元、按父因子质量分桶校正残差信用，并加置信门与否决记忆的 LLM 因子挖掘智能体。 | P4 P5（P1 P7） | `llm-formula` | [arXiv](https://arxiv.org/abs/2606.20625) · [代码](https://github.com/jarrettyu/sspm) · [速读](notes/cards/2026_AlphaMemo.md) |
| 2026-06 | **Agora/SJS** | 多智能体在密封评估下联合搜索交易信号与评价协议的自演化研究环境。 | P5 P6 | `llm-agent` | [arXiv](https://arxiv.org/abs/2606.29194) · [速读](notes/cards/2026_Agora-SJS.md) |
| 2026-05 | **QuantEvolver** | 用 RFT（GRPO + DiCo 奖励）把评价反馈写进轻量 LLM 参数，代替提示词循环。 | P3 P4 P7（P1） | `llm-agent` | [arXiv](https://arxiv.org/abs/2605.15412) · [代码](https://github.com/QuantLLM/QuantEvolver) · [速读](notes/cards/2026_QuantEvolver.md) |
| 2026-05 | **PRISM-VQ**（IJCAI 2026） | 用向量量化码本学离散隐因子、以码字路由生成动态载荷，并把先验因子直接纳入因子定价方程的选股模型。 | P2 P9（P5 P6 P8） | `neural` | [arXiv](https://arxiv.org/abs/2605.13407) · [代码](https://github.com/finxlab/PRISM-VQ) · [速读](notes/cards/2026_PRISM-VQ.md) |
| 2026-04 | **MarketSenseAI** | 对一个已部署的多智能体 LLM 选股系统做组合层验证：实时生成信号规避前视，用随机零分布检验组合是否胜过运气。 | P5 P6（P8） | `benchmark` `adjacent` | [arXiv](https://arxiv.org/abs/2604.17327) · [速读](notes/cards/2026_MarketSenseAI.md) |
| 2026-03 | **Hubble** | DSL / AST 安全沙箱加正负双通道 RAG 与因子家族感知评分，持久化全部诊断。 | P1 P7 P10（P8 P9） | `llm-formula` | [arXiv](https://arxiv.org/abs/2604.09601) · [速读](notes/cards/2026_Hubble.md) |
| 2026-03 | **FactorEngine**（ICDM 2026） | 图灵完备程序因子：LLM 演化宏观逻辑，贝叶斯优化微观参数，研报知识启动。 | P1 P2（P3 P6） | `llm-agent` | [arXiv](https://arxiv.org/abs/2603.16365) · [速读](notes/cards/2026_FactorEngine.md) |
| 2026-03 | **AlphaLogics** | 多智能体把市场逻辑做成可编译的先验，内外双循环交替优化逻辑与 DSL 因子。 | P1 P2（P3 P6 P9 P10） | `llm-formula` | [arXiv](https://arxiv.org/abs/2603.20247) · [速读](notes/cards/2026_AlphaLogics.md) |
| 2026-03 | **AgenticFactorInvesting** | 智能体闭环提出经济假设、生成公式并按固定闸门准入，再以线性与 LightGBM 聚合构建多空组合。 | P5 P8（P2 P6） | `llm-agent` `pool-combination` | [arXiv](https://arxiv.org/abs/2603.14288) · [速读](notes/cards/2026_AgenticFactorInvesting.md) |
| 2026-02 | **QuantaAlpha** | 把 LLM 挖掘过程视为可演化轨迹，对高质量轨迹做局部变异与交叉。 | P2 P7 | `llm-formula` | [arXiv](https://arxiv.org/abs/2602.07085) · [代码](https://github.com/QuantaAlpha/QuantaAlpha) · [速读](notes/cards/2026_QuantaAlpha.md) |
| 2026-02 | **FactorMiner** | 技能模块封装算子与评估协议，经验记忆记录应避开的高相关区域。 | P7（P3 P10） | `llm-formula` | [arXiv](https://arxiv.org/abs/2602.14670) · [速读](notes/cards/2026_FactorMiner.md) |
| 2026-02 | **AlphaPROBE** | 在因子谱系有向无环图上检索父节点，沿演化路径有偏地生成新因子。 | P1 P7（P8） | `formulaic` `pool-combination` | [arXiv](https://arxiv.org/abs/2602.11917) · [代码](https://github.com/gta0804/AlphaPROBE) · [速读](notes/cards/2026_AlphaPROBE.md) |
| 2026-01 | **Look-Ahead-Bench** | 在 LLM 交易智能体工作流中，用知识截止前后两个时期的超额收益落差衡量前视偏差，对比标准开源 LLM 与时点化模型。 | P6 | `benchmark` `adjacent` | [arXiv](https://arxiv.org/abs/2601.13770) · [代码](https://github.com/benstaf/lookaheadbench) · [速读](notes/cards/2026_Look-Ahead-Bench.md) |
| 2026-01 | **AlphaCFG** | 用面向 alpha 的上下文无关文法约束语法、语义与长度，在其上做 RL 与 MCTS 搜索。 | P1（P7） | `formulaic` | [arXiv](https://arxiv.org/abs/2601.22119) · [代码](https://github.com/HanYang544/AlphaCFG) · [速读](notes/cards/2026_AlphaCFG.md) |
| 2025-12 | **Alpha-R1** | 用 SFT + GRPO 训练 LLM 按市场状态推理因子启停，做因子筛选。 | P8 P9（P5 P6） | `llm-agent` `pool-combination` | [arXiv](https://arxiv.org/abs/2512.23515) · [代码](https://github.com/FinStep-AI/Alpha-R1) · [速读](notes/cards/2025_Alpha-R1.md) |
| 2025-11 | **CogAlpha**（ACL 2026（Volume 1: Long Papers）） | 七层 LLM 代理生成代码级 Alpha，经质量检查后做思考演化。 | P1 P2（P6） | `llm-formula` | [arXiv](https://arxiv.org/abs/2511.18850) · [速读](notes/cards/2025_CogAlpha.md) |
| 2025-10 | **TextToAlpha** | LLM 抽取电话会指标、嵌入比对跨期变化，构成可解释的文本因子打分函数。 | P2 | `data-space` | [arXiv](https://arxiv.org/abs/2510.03195) · [速读](notes/cards/2025_TextToAlpha.md) |
| 2025-09 | **Tree-GRPO**（ICLR 2026） | 以智能体步骤为节点做树搜索采样，用树内与树间的组相对优势从结果奖励构造过程信号。 | P3 P4 | `adjacent` | [arXiv](https://arxiv.org/abs/2509.21240) · [代码](https://github.com/AMAP-ML/Tree-GRPO) · [速读](notes/cards/2025_Tree-GRPO.md) |
| 2025-09 | **AlphaSAGE**（ICLR 2026（Poster）） | AST + RGCN 编码公式结构，GFlowNet 按多信号奖励成比例采样多样因子。 | P4 P7 | `formulaic` | [arXiv](https://arxiv.org/abs/2509.25055) · [代码](https://github.com/BerkinChen/AlphaSAGE) · [速读](notes/cards/2025_AlphaSAGE.md) · [精读](notes/deep/2025_AlphaSAGE.md) |
| 2025-08 | **TreEvo** | 把 LLM 的扁平思路改写为层次化思路树并在树上演化，扩大有效搜索空间、缓解位置偏差。 | P1 P3（P2 P7） | `llm-formula` | [arXiv](https://arxiv.org/abs/2508.16334) · [速读](notes/cards/2025_TreEvo.md) |
| 2025-08 | **AlphaEval**（KDD 2026） | 免回测、可并行的公式 Alpha 评估框架：从预测力、时间稳定性、扰动稳健性、金融逻辑与多样性五个维度评价挖掘出的因子集。 | P3 P10（P2 P7 P8） | `pool-combination` `benchmark` | [arXiv](https://arxiv.org/abs/2508.13174) · [代码](https://github.com/LeoDingggg/AlphaEval) · [速读](notes/cards/2025_AlphaEval.md) |
| 2025-07 | **TLRS** | 以专家因子子序列匹配做轨迹级奖励塑形，并用奖励中心化稳定训练。 | P4 | `formulaic` | [arXiv](https://arxiv.org/abs/2507.20263) · [速读](notes/cards/2025_TLRS.md) |
| 2025-07 | **EFS** | LLM 演化可执行的资产打分因子，用于只选 Top-m 资产的稀疏组合。 | P8（P7） | `llm-agent` `pool-combination` | [arXiv](https://arxiv.org/abs/2507.17211) · [速读](notes/cards/2025_EFS.md) |
| 2025-06 | **DeepMind AlphaEvolve** | 由 LLM 集成改写代码、自动评价器打分、程序库驱动演化的代码优化智能体；与 2021 年的因子挖掘论文 AlphaEvolve 无关。 | P1（P2 P3 P7） | `adjacent` | [arXiv](https://arxiv.org/abs/2506.13131) · [速读](notes/cards/2025_DeepMind-AlphaEvolve.md) |
| 2025-05 | **RD-Agent(Q)**（NeurIPS 2025） | 多智能体分别迭代因子与模型，用 Thompson 采样调度二者的联合优化。 | P8（P7） | `llm-agent` | [arXiv](https://arxiv.org/abs/2505.15155) · [代码](https://github.com/microsoft/RD-Agent) · [速读](notes/cards/2025_RD-Agent-Quant.md) |
| 2025-05 | **GiGPO**（NeurIPS 2025） | 多轮 LLM 智能体强化学习中，按回合与锚点状态两级分组估计相对优势，无需 critic 与额外 rollout。 | P4 | `adjacent` | [arXiv](https://arxiv.org/abs/2505.10978) · [代码](https://github.com/langfengQ/verl-agent) · [速读](notes/cards/2025_GiGPO.md) |
| 2025-05 | **AlphaQCM**（ICML 2025） | 分布式强化学习估计奖励方差（QCM），作为非平稳稀疏奖励下的探索奖励。 | P4 | `formulaic` | [论文](https://openreview.net/forum?id=3sXMHlhBSs) · [代码](https://github.com/ZhuZhouFan/AlphaQCM) · [速读](notes/cards/2025_AlphaQCM.md) |
| 2025-05 | **Alpha-Jungle**（AAAI 2026） | LLM 驱动的 MCTS 逐步精炼公式，多维评价并规避高频子树。 | P1 P7（P5 P8） | `llm-formula` | [arXiv](https://arxiv.org/abs/2505.11122) · [速读](notes/cards/2025_Alpha-Jungle.md) |
| 2025-02 | **AlphaAgent**（KDD 2025） | 多智能体闭环，以 AST 原创性、假设一致性与复杂度正则对抗因子衰减。 | P7 P9（P2 P5） | `llm-formula` | [arXiv](https://arxiv.org/abs/2502.16789) · [代码](https://github.com/RndmVariableQ/AlphaAgent) · [速读](notes/cards/2025_AlphaAgent.md) |
| 2025 | **CAVB**（IJCAI 2025（Main Track）） | 对抗变分贝叶斯学习共同隐因子，对比学习区分分位条件载荷，以历史因子均值预测收益。 | P2（P7） | `neural` | [论文](https://www.ijcai.org/proceedings/2025/842) · [速读](notes/cards/2025_CAVB.md) |
| 2025 | **AlphaGAT**（IJCAI 2025） | CATimeMixer 生成神经 Alpha，再用 GAT + PPO 动态学习因子权重做组合选择。 | P2 P8（P7） | `neural` `pool-combination` | [论文](https://www.ijcai.org/proceedings/2025/834) · [速读](notes/cards/2025_AlphaGAT.md) · [精读](notes/deep/2025_AlphaGAT.md) |
| 2024-12 | **Warm Start GP** | 用一条有效 alpha 的结构热启动遗传规划，只允许同结构受限交叉，在有限子空间内挖矿并增强原因子。 | P1 P7（P2 P3 P5） | `formulaic` | [arXiv](https://arxiv.org/abs/2412.00896) · [速读](notes/cards/2024_WarmStartGP.md) |
| 2024-09 | **QFR**（IEEE Transactions on Signal Processing 2025） | 用带贪婪基线、无价值网络的 REINFORCE 替代 PPO，并以信息比率提升稳定性。 | P4 P9 | `formulaic` | [arXiv](https://arxiv.org/abs/2409.05144) · [速读](notes/cards/2024_QFR.md) |
| 2024-09 | **LLM Strategy Finding** | 从多模态财经材料抽取策略要素形成种子 Alpha，经多智能体评估后动态加权。 | P1 P8 | `llm-formula` | [arXiv](https://arxiv.org/abs/2409.06289) · [代码](https://github.com/kouzhizhuo/Automate-Strategy-Finding-with-LLM-in-Quant-investment) · [速读](notes/cards/2024_LLMStrategyFinding.md) |
| 2024-08 | **HRFT/IRFT**（WWW 2025（Industry Track）） | Transformer 以符号-数值混合词表端到端生成含常数的高频风险因子公式。 | P2 | `data-space` | [arXiv](https://arxiv.org/abs/2408.01271) · [代码](https://github.com/wencyxu/IRF-LLM-accepted-at-WWW25-) · [速读](notes/cards/2024_HRFT.md) |
| 2024-06 | **AlphaForge**（AAAI 2025） | 生成器-预测器挖掘因子，使用阶段按近期表现动态筛选并加权组合。 | P4 P8 P9（P3 P7） | `formulaic` `pool-combination` | [arXiv](https://arxiv.org/abs/2406.18394) · [代码](https://github.com/dulyhao/alphaforge) · [速读](notes/cards/2024_AlphaForge.md) · [精读](notes/deep/2024_AlphaForge.md) |
| 2024-06 | **Alpha2** | 把公式生成改为带寄存器的程序构造，搜索中做维度检查，由 RL 引导 MCTS。 | P1（P3） | `formulaic` | [arXiv](https://arxiv.org/abs/2406.16505) · [代码](https://github.com/x35f/alpha2) · [速读](notes/cards/2024_Alpha2.md) |
| 2024-02 | **RiskMiner**（ICAIF 2024） | 风险偏好 MCTS：合法中间表达式即时奖励，并惩罚与已有因子的重复。 | P1 P4（P7 P8） | `formulaic` | [arXiv](https://arxiv.org/abs/2402.07080) · [速读](notes/cards/2024_RiskMiner.md) |
| 2024-02 | **QuantAgent** | 内外双循环的自改进 LLM 智能体，持续积累交易信号知识库。 | P1（P4） | `llm-formula` | [arXiv](https://arxiv.org/abs/2402.03755) · [速读](notes/cards/2024_QuantAgent.md) |
| 2024-02 | **Alpha-GPT 2.0** | 把人在回路的 LLM 交互扩展到研究、建模、分析的完整量化研究流程。 | P1（P8） | `llm-formula` | [arXiv](https://arxiv.org/abs/2402.09746) · [速读](notes/cards/2024_Alpha-GPT2.md) |
| 2024-01 | **Synergistic RL**（ICOIN 2024） | 在 AlphaGen 上扩展算子与长窗口，并用优质种子公式引导探索。 | P1（P7） | `formulaic` | [arXiv](https://arxiv.org/abs/2401.02710) · [速读](notes/cards/2024_SynergisticRL.md) |
| 2023-07 | **Alpha-GPT**（EMNLP 2025（System Demonstrations）） | 人机交互的 LLM 因子挖掘：想法生成、公式实现与结果复盘，配合遗传规划搜索。 | P1（P2） | `llm-formula` | [arXiv](https://arxiv.org/abs/2308.00016) · [速读](notes/cards/2023_Alpha-GPT.md) |
| 2023-05 | **AlphaGen**（KDD 2023（ADS Track）） | 把 RPN 公式生成建模为 MDP，用因子池组合 IC 的边际贡献作为 PPO 奖励。 | P7 P8（P1 P3） | `formulaic` | [arXiv](https://arxiv.org/abs/2306.12964) · [代码](https://github.com/ICT-FinD-Lab/alphagen) · [速读](notes/cards/2023_AlphaGen.md) |
| 2023-03 | **Sequential Cauchy** | 把全局 Cauchy 组合检验递归施于升序 p 值的后缀，实现强 FWER 控制并能指认个体显著项的多重检验程序。 | P5（P7 P10） | `adjacent` | [arXiv](https://arxiv.org/abs/2303.13406) · [速读](notes/cards/2023_SequentialCauchy.md) |
| 2022-09 | **Publication Bias** | 综述资产定价研究的发表偏差：四条元研究事实、经验贝叶斯收缩与 FDR 校正，并澄清样本外衰减等常见误读。 | P5（P9 P10） | `adjacent` | [arXiv](https://arxiv.org/abs/2209.13623) · [代码](https://github.com/chenandrewy/PBR) · [速读](notes/cards/2022_PublicationBias.md) |
| 2022-01 | **Trajectory Balance**（NeurIPS 2022） | 提出轨迹平衡目标，在完整轨迹上约束 GFlowNet 流量一致，改进长序列的信用分配。 | P4（P7） | `adjacent` | [arXiv](https://arxiv.org/abs/2201.13259) · [代码](https://github.com/GFNOrg/gflownet/tree/trajectory_balance) · [速读](notes/cards/2022_TrajectoryBalance.md) |
| 2021-06 | **GFlowNet**（NeurIPS 2021） | 学习按奖励成比例采样离散对象的生成策略，用于生成多样的高奖励候选。 | P7（P3 P4） | `adjacent` | [arXiv](https://arxiv.org/abs/2106.04399) · [代码](https://github.com/bengioe/gflownet) · [速读](notes/cards/2021_GFlowNet.md) |
| 2021-03 | **AlphaEvolve**（SIGMOD 2021（Data Science and Engineering Track）） | AutoML 进化搜索，引入矩阵 / 向量算子与行业关系，并剪枝冗余表达式。 | P2 P7（P3） | `formulaic` | [arXiv](https://arxiv.org/abs/2103.16196) · [速读](notes/cards/2021_AlphaEvolve.md) |
| 2020-02 | **AutoAlpha** | 从低阶根基因逐层扩展的遗传规划，配合 PCA 近似的质量-多样性搜索。 | P1 P7（P3） | `formulaic` | [arXiv](https://arxiv.org/abs/2002.08245) · [速读](notes/cards/2020_AutoAlpha.md) |
| 2019-12 | **DSR**（ICLR 2021） | 用 RNN 自回归生成表达式，以风险寻求策略梯度只按高分位样本更新，用于符号回归。 | P4（P1） | `adjacent` | [arXiv](https://arxiv.org/abs/1912.04871) · [代码](https://github.com/brendenpetersen/deep-symbolic-regression) · [速读](notes/cards/2019_DSR.md) |
| 2016-01 | **Alpha101**（Wilmott Magazine 2016） | 公开 101 个实盘使用过的公式 Alpha，是后续自动挖掘的基础因子库与基准。 | — | `formulaic` | [arXiv](https://arxiv.org/abs/1601.00991) · [速读](notes/cards/2016_Alpha101.md) |

<a id="by-problem"></a>

## 2. 按问题

每个问题下的相关工作按首次公开时间从新到旧统一排列，逐篇标明时间与“主要针对 / 顺带涉及”，机制取自各自速读卡。机制的归纳与比较见[各问题的应对机制](topics/problems.md)。

[P1 表达空间巨大，有效因子稀少](#p1) · [P2 表达能力与可解释性的权衡](#p2) · [P3 评价成本高](#p3) · [P4 学习信号稀疏、延迟且不可微](#p4) · [P5 低信噪比下的过拟合](#p5) · [P6 前视偏差与信息泄漏](#p6) · [P7 因子同质化与冗余](#p7) · [P8 挖掘目标与实际使用脱节](#p8) · [P9 非平稳与因子衰减](#p9) · [P10 评估口径不统一、难以复现](#p10)

<a id="p1"></a>

### P1 表达空间巨大，有效因子稀少（主要 25，涉及 8）

- 2026-11 [CosmosAlpha](notes/cards/2026_CosmosAlpha.md)（主要针对）：把已评价因子当作可复用的搜索状态而在日志之外：跨分支但结构或行为相近的因子通过图上的边共享证据；繁殖力把“这个父节点历史上是否产出了推进质量前沿的子代”作为选父依据，而不只看它当前的分数；Graph Flow 把局部测量与邻域证据叠加后再决定往哪里扩展（第 3.3–3.4 节、式 10）。
- 2026-10 [QBX](notes/cards/2026_QBX.md)（主要针对）：编译器准入与编译器闭合的图编辑动作，把候选限制在类型正确、无环、时间可用、可链接执行的程序空间内；另有只警告、不阻止准入的单位与量纲元数据检查，定位存量与流量混算等无意义运算（E16）。
- 2026-10 [LineageEvo](notes/cards/2026_LineageEvo.md)（主要针对）：把同一谱系内已验证的“有效/失败改写模式”写成结构化先验并持续注入变异与交叉提示，使 LLM 不必每代从零探索；按有效评价次数计，方法在约 75 次有效评价处即进入较高平台，而 RD-Agent 早期上升后停在中低水平、AlphaPROBE 需更多评价才追平（第 3 节、第 5.3 节、图 3）。
- 2026-10 [EvoQuantLab](notes/cards/2026_EvoQuantLab.md)（顺带涉及）：类型化终端与算子限制合法树空间，知识提案验证后才可跨周期启用（原文第 3.1、3.3 节）。
- 2026-10 [AlphaRLM](notes/cards/2026_AlphaRLM.md)（主要针对）：LEGO 把文献的经济思想作为语义先验、把算子库定义作为可执行空间的边界，要求每个假设落到可得的价格与成交量代理上，而不是凭空搜索；可执行有效性奖励直接惩罚无法解析、无法计算或含负滞后（Ref 的 lag 为负）的表达式，把无效区域从搜索中挤出去（第 3.2–3.3 节、附录 B）。消融中把金融文献换成 2,000 篇非金融文献后，CSI300 的 AR 从 12.14% 降到 2.13%，S&P 500 从 6.94% 降到 2.90%（表 2）。
- 2026-10 [AlphaPilot](notes/cards/2026_AlphaPilot.md)（顺带涉及）：评价工具强制固定 DSL 文法，返回非法表达式与执行错误；搜索以 20 条种子因子库和 regime 描述为起点，近期已试因子记忆用于避免重复失败（第 4.1–4.3 节、附录 A.4、表 14）。
- 2026-10 [AlphaLedger](notes/cards/2026_AlphaLedger.md)（顺带涉及）：因子是类型化文法程序，教师与学生的分布都被限制在当前前缀的合法动作集 A(s_j) 上；生成时按意图规定必须使用的数据族与允许的持有期，减少无意义组合（第 3.1、3.3 节、附录 D）。
- 2026-09 [AlphaDiverse](notes/cards/2026_AlphaDiverse.md)（顺带涉及）：用经济机制目录约束研究方向；为每个计划只检索少量相关特征与算子，减少实现歧义；Realizer 的生成受 JSON 文法约束，无效规格带着校验反馈修复（第 2.1 节、附录 B.2）。
- 2026-08 [AlphaSeek](notes/cards/2026_AlphaSeek.md)（主要针对）：以轨迹而非单个表达式为优化单位，把有效的假设、代码与反馈沿轨迹继承；并行方向扩展、Mutation、Crossover 三个演化算子替代随机搜索；表达式须经 AST 校验并编译成可执行代码，复杂度项约束符号长度、自由参数数与原始特征使用数（第 3.2 节，式 5、10–11）。
- 2026-07 [X-Alpha](notes/cards/2026_X-Alpha.md)（主要针对）：RMA 的 A 层以“能否用日频 OHLCV 表达”为硬条件剔除不可实现的研究方向，B/C 层把噪声文本压成可执行研究路径，路由再按主题限定本周期的机制家族与档案，使搜索从受数据契约约束的先验出发而不是从原始报告文本出发；候选还需通过静态检查、三对齐与执行检查才能进入评价（第 3.1–3.3 节）。对照“直接喂报告”的同一流程，RMA 使 mean held-out RankIC 提高 6.40%、RankICIR 提高 29.76%（表 2）。
- 2026-07 [AlphaSchema](notes/cards/2026_AlphaSchema.md)（主要针对）：搜索对象从公式或代码换成显式、有限的语义计划空间，代理奖励模型在实现前从大量采样计划中预选；失败计划以零奖励留在缓冲区，代理模型由此学会避开难以实现的语义结构（第 3 节、附录 A）。
- 2026-06 [AlphaMemo](notes/cards/2026_AlphaMemo.md)（顺带涉及）：生成被限制在十类 motif 与提示中的可用算子内，无效或语法重复的子表达式不进入记忆统计、也不计为失败（第 4.1、4.5 节）；motif 由实际 AST 差异而非请求的编辑标签决定，使同一编辑行为在不同表面写法间共享信用（第 4.3 节）。
- 2026-05 [QuantEvolver](notes/cards/2026_QuantEvolver.md)（顺带涉及）：用因子 DSL 约束可生成的表达式，消融中去掉 DSL 后表现大幅下降。
- 2026-03 [Hubble](notes/cards/2026_Hubble.md)（主要针对）：白名单 AST 沙箱。
- 2026-03 [FactorEngine](notes/cards/2026_FactorEngine.md)（主要针对）：宏观逻辑演化与微观参数优化分离；从研报和专家因子抽取初始程序池。
- 2026-03 [AlphaLogics](notes/cards/2026_AlphaLogics.md)（主要针对）：逻辑先于表达式，H_struct 经确定性编译得到 Γ，限定变量、算子族、参数范围与方向一致性，违反 Γ 的程序被拒绝并重生成；逻辑库本身随轮次增长，为后续生成提供可复用的先验而不是自由组合（第 3.2–3.3 节，附录 A.4，图 3）。消融：同一 DSL 算子集与参数范围下去掉 Γ 自由组合，在 GPT-3.5-Turbo、DeepSeek V3、Gemini-2.5-Flash 三个模型和两个市场上 IC 与 IR 一致下降（第 4.4 节，图 3）。
- 2026-02 [AlphaPROBE](notes/cards/2026_AlphaPROBE.md)（主要针对）：因子谱系图上的有偏演化。
- 2026-01 [AlphaCFG](notes/cards/2026_AlphaCFG.md)（主要针对）：面向 alpha 的上下文无关文法与语义、长度约束。
- 2025-11 [CogAlpha](notes/cards/2025_CogAlpha.md)（主要针对）：七层代理加自适应生成与多种改写模式，扩大有效搜索范围。
- 2025-08 [TreEvo](notes/cards/2025_TreEvo.md)（主要针对）：论文的核心论点是扁平思路导致位置偏差与冗余精修，把搜索限制在少数位置上反复改动，因而有效搜索空间远小于名义空间；层次化思路树把变异定位到明确的子树与叶子，配合剪枝抑制冗余分支，从而扩大实际可达的有效区域。证据包括：10 组配对样本中思路变化点的分布，树状表示明显比扁平表示更均匀（对均匀分布的 MSE 为 0.00869 对 0.01829，约降 52.49%）；配对变体的文本余弦相似度与因子 IC 相关性的联合分布上，扁平文本的相似度挤在 0.8–0.9 而 IC 相关散落 −1 到 1，树状表示的相似度分布更宽、正相关占多数（第 4.2.1 节、图 3）。
- 2025-06 [DeepMind AlphaEvolve](notes/cards/2025_DeepMind-AlphaEvolve.md)（主要针对）：用 LLM 依据上下文中的历史程序与得分提出有针对性的 diff，代替需要人工设计、可能抓不住领域性质的手写变异算子（第 2.3、5 节），并用评价级联尽早过滤有错程序（第 2.4 节）→ 对应代码因子空间中随机变异大多无效、LLM 生成代码常不可执行的问题，用带反馈的 LLM 变异和前置执行检查提高有效候选比例；已收录的 FactorEngine（由 LLM 做宏观逻辑变异）与 CogAlpha（思考演化中的精炼、变异与重组）属同类 LLM 代码演化（见两者速读卡）。
- 2025-05 [Alpha-Jungle](notes/cards/2025_Alpha-Jungle.md)（主要针对）：MCTS 显式复用已探索结构。
- 2024-12 [Warm Start GP](notes/cards/2024_WarmStartGP.md)（主要针对）：用一条已知有效 alpha 的结构把搜索空间从无限收缩为该结构下的有限子空间，并用图 2 与图 4 的 10,000 条随机采样对比给出有效密度从不足 3% 升到 13% 以上的直接测量；同时避免了树深与树长无约束增长带来的 code bloat（第 2–3.2 节、图 2、图 4）。
- 2024-09 [LLM Strategy Finding](notes/cards/2024_LLMStrategyFinding.md)（主要针对）：从文本、表格、图像材料中抽取种子因子，锚定搜索起点。
- 2024-06 [Alpha2](notes/cards/2024_Alpha2.md)（主要针对）：寄存器程序表示与维度检查。
- 2024-02 [RiskMiner](notes/cards/2024_RiskMiner.md)（主要针对）：MCTS 显式复用已探索结构。
- 2024-02 [QuantAgent](notes/cards/2024_QuantAgent.md)（主要针对）：持续积累并检索的信号知识库。
- 2024-02 [Alpha-GPT 2.0](notes/cards/2024_Alpha-GPT2.md)（主要针对）：研究员想法贯穿研究、建模、分析全流程，作为搜索先验。
- 2024-01 [Synergistic RL](notes/cards/2024_SynergisticRL.md)（主要针对）：扩展算子集与长窗口以扩大搜索空间，并在经验回放中注入优质种子公式。
- 2023-07 [Alpha-GPT](notes/cards/2023_Alpha-GPT.md)（主要针对）：研究员想法与层次化字段检索。
- 2023-05 [AlphaGen](notes/cards/2023_AlphaGen.md)（顺带涉及）：动作掩码与栈规则。
- 2020-02 [AutoAlpha](notes/cards/2020_AutoAlpha.md)（主要针对）：从低阶到高阶的层次化搜索。
- 2019-12 [DSR](notes/cards/2019_DSR.md)（顺带涉及）：符号回归中把先验约束放在自回归采样时执行，直接屏蔽违规 token，样本无需事后拒绝即全部合法；论文还报告 GP 加入事后约束反而降低表现（第 3.1、4 节，附录 F）→ 对应公式因子生成中的语法、类型与无意义组合约束，以 mask 前置可把评价预算集中在合法表达式上；已收录的 AlphaSAGE 在语法合法动作中逐步采样，属同类做法（见 AlphaSAGE 速读卡）。

<a id="p2"></a>

### P2 表达能力与可解释性的权衡（主要 10，涉及 14）

- 2026-10 [QBX](notes/cards/2026_QBX.md)（顺带涉及）：以受限的登记词表换取可审计性，并实测这一限制的代价：只用类型化搜索的因子簿行为广度不足，LLM 提议的广度与 QBX 局部搜索的深度结合后可以弥补。
- 2026-10 [EvoQuantLab](notes/cards/2026_EvoQuantLab.md)（顺带涉及）：以分支消融、符号翻转、参与者互换和残差检验约束经济解释与增量（原文第 3.2 节、附录 D.2）。
- 2026-10 [Det-MASO](notes/cards/2026_Det-MASO.md)（顺带涉及）：放弃公式级表达以换取可微性，用训练后的 Shapley interaction index 提供 agent 级互补/替代解释（第 3.2.7 节）。
- 2026-08 [AlphaSeek](notes/cards/2026_AlphaSeek.md)（顺带涉及）：一致性项 C(h,d,f) 同时约束“假设文本—因子描述”与“描述—表达式”，把声称的经济逻辑是否落到实现作为准入条件，不通过则重生成（第 3.2 节，式 9）。
- 2026-08 [AgonAlpha](notes/cards/2026_AgonAlpha.md)（顺带涉及）：审稿者按五个维度审计冻结报告，其中“符号逻辑”要求表达式每一项的方向与所述市场机制一致（不一致即记符号警告），“常数依据”要求每个不寻常的系数或窗口都有经济、日历或搜索风险上的解释；第 5.3 节记录一次因“声称机制与所执行算子语义不符”而触发置零的干预。
- 2026-07 [X-Alpha](notes/cards/2026_X-Alpha.md)（顺带涉及）：三对齐显式检查“假设—解释—可执行代码”三者一致，并对不一致做定点修复；167 条因子记录的成对人工复核中，同时通过解释—代码一致、代码金融合理、解释金融合理三项的比例由修复前 12.57% 升至 89.82%（第 4.5 节、附录 L）。
- 2026-07 [AlphaSchema](notes/cards/2026_AlphaSchema.md)（顺带涉及）：因子以任意 pandas 代码实现，但实现前先用五元语义计划声明交易逻辑，提示词还要求代码开头的注释逐项对应 Event、Context、Quality、Direction、Output（第 2 节、附录 D）。
- 2026-05 [PRISM-VQ](notes/cards/2026_PRISM-VQ.md)（主要针对）：在保留可解释因子结构的前提下引入神经表达：预测仍是“载荷 × 因子”的线性组合，隐因子来自离散码本，码字可通过与 13 个先验因子收益的 Spearman 相关解释（表 4 中最大的 |ρ| 约 0.12，如 S&P 500 的 Code 72 对应盈利、低风险、动量，呈质量成长型），并用 t-SNE 显示码字聚类跨越 GICS 行业、也不由市值或未来收益单独决定（第 5.5 节、图 5）；消融中同时报告去掉码本、先验与 MoE 三种结构后的退化（表 2）。
- 2026-03 [FactorEngine](notes/cards/2026_FactorEngine.md)（主要针对）：把因子表示扩展为可执行程序，超出固定符号文法。
- 2026-03 [AlphaLogics](notes/cards/2026_AlphaLogics.md)（主要针对）：市场逻辑作为可读的中间表示 H = ⟨C, B⟩，一端连向自然语言的机制解释，另一端经 Γ 连向可执行的公式约束，使“因子为什么该有效”成为可审计的对象而非事后叙事；外循环在这个表示上迭代，把解释改进与因子改进解耦（第 3.1–3.3 节）。可重建性检验：用 LLM 给出的数学解释与金融解释反向重建公式，与原式比较截面排名与时序走势，在 90% 以上一致即视为等价，重复 100 次（第 4.3 节）；Alpha101、Alpha158、Alpha360、Alpha191 的数学解释一致率为 97.5%、98.1%、100.0%、94.9%，金融解释为 92.7%、95.5%、98.8%、93.8%（表 2）。
- 2026-03 [AgenticFactorInvesting](notes/cards/2026_AgenticFactorInvesting.md)（顺带涉及）：论文把“黑箱机器学习”列为要解决的两个问题之一，主张以透明符号公式替代神经因子，并给出每条因子的经济含义清单（第 2.2 节、第 6.5.2 节、Exhibit 15）。
- 2026-02 [QuantaAlpha](notes/cards/2026_QuantaAlpha.md)（主要针对）：假设、描述、表达式之间的一致性校验。
- 2025-11 [CogAlpha](notes/cards/2025_CogAlpha.md)（主要针对）：以代码而非受限 DSL 表示 Alpha，扩大表达空间。
- 2025-10 [TextToAlpha](notes/cards/2025_TextToAlpha.md)（主要针对）：把“文本 → 因子”的瓶颈放在抽取环节而不是下游模型，LLM 保留上下文限定词与语义等价（“sales growth” 与 “revenue increase” 视为同一指标的延续），使同一可解释的比值型分数能表达更多语义；代价是需要为每次抽取支付 LLM 调用成本，且分数依赖抽取与嵌入两个模型的质量（第 3–4 节，式 2–4；Limitations）。
- 2025-08 [TreEvo](notes/cards/2025_TreEvo.md)（顺带涉及）：因子同时以“可读的思路树”和“可执行代码”两种形式存在，树结构本身限制节点类型与层次语义（金融语义节点—统计算子节点—数据叶节点），使每个因子可自上而下审计；论文把可解释性作为选择符号范式而非神经网络范式的主要理由（第 1 节、第 3.2 节、附录 G.2）。
- 2025-08 [AlphaEval](notes/cards/2025_AlphaEval.md)（顺带涉及）：用 LLM 评分的 Logic Score 度量表达式的金融逻辑与可解释性，并以人工专家排序检验其一致性，使不同范式在可解释性上可比。
- 2025-06 [DeepMind AlphaEvolve](notes/cards/2025_DeepMind-AlphaEvolve.md)（顺带涉及）：演化对象从单个函数扩展到整个代码文件与多个组件，并可选择演化解本身、构造函数或定制搜索算法等不同抽象层次（第 2.1 节）；数据中心调度任务选用其代码解而非深度强化学习，理由是可解释、可调试、可预测且易部署（第 3.3.1 节）→ 对应以程序而非受限 DSL 表示因子，在扩大表达能力的同时保留可读、可审计的代码形式；已收录的 FactorEngine 与 CogAlpha 都把因子表示扩展为可执行代码（见两者速读卡）。
- 2025-02 [AlphaAgent](notes/cards/2025_AlphaAgent.md)（顺带涉及）：假设、描述、表达式之间的一致性校验。
- 2025 [CAVB](notes/cards/2025_CAVB.md)（主要针对）：用隐式后验增强共同隐因子的分布表达能力，同时保留“公司特征 → 条件载荷 × 共同因子”的资产定价结构；结构可解释不等于每个神经隐因子都能被命名或审计（第 1–2 节、式 2–8）。
- 2025 [AlphaGAT](notes/cards/2025_AlphaGAT.md)（主要针对）：神经网络直接输出 alpha。
- 2024-12 [Warm Start GP](notes/cards/2024_WarmStartGP.md)（顺带涉及）：结构固定的搜索保证产出的因子保持可辨认的结构，论文以此作为可解释性优于随机搜索的理由，并用“同结构、不同数据与函数”的四个券商实际使用 alpha 作为动机（第 3.1–3.4 节）。
- 2024-08 [HRFT/IRFT](notes/cards/2024_HRFT.md)（主要针对）：符号-数值混合词表生成含常数的公式。
- 2023-07 [Alpha-GPT](notes/cards/2023_Alpha-GPT.md)（顺带涉及）：把生成的公式反编译为自然语言解释，便于审计其声称的逻辑。
- 2021-03 [AlphaEvolve](notes/cards/2021_AlphaEvolve.md)（主要针对）：矩阵和向量算子与行业关系注入。

<a id="p3"></a>

### P3 评价成本高（主要 10，涉及 17）

- 2026-11 [CosmosAlpha](notes/cards/2026_CosmosAlpha.md)（顺带涉及）：以“父节点扩展尝试”而非 token 或轮次计预算，失败与重复也计入；繁殖力复用已评分子代相对冻结档案的增量来分配后续扩展预算；论文同时公开了每次运行的 LLM 调用时长与 token 量（第 4.1 节、附录 A.5、C.4）。
- 2026-10 [QBX](notes/cards/2026_QBX.md)（顺带涉及）：节点级内容地址只重算编辑影响的依赖锥；准入与去重是微秒级 CPU 开销，每次 LLM 调用可以扩展为大量合法候选。
- 2026-10 [LineageEvo](notes/cards/2026_LineageEvo.md)（顺带涉及）：全部方法共用 B=200 个有效评价预算，无效、重复与执行失败的候选不计入预算；论文以“前 5 个绝对验证 IC 的均值随有效评价数的变化”比较搜索效率，而不是只看终点分数（附录 D、第 5.3 节、图 3）。
- 2026-10 [EvoQuantLab](notes/cards/2026_EvoQuantLab.md)（主要针对）：用 GP 承担候选级搜索，LLM 集中用于知识与周期诊断，减少部分调用和 token 开销（原文第 3.3–3.4、5.3 节）。
- 2026-10 [AlphaRLM](notes/cards/2026_AlphaRLM.md)（顺带涉及）：为降低 rollout 评价成本，奖励只在各市场 2018–2019 的数据子集上计算，而不是全程回测；动态采样也只保留有奖励方差的组（第 3.3 节、附录 C、附录 A 的数据说明）。
- 2026-10 [AlphaPilot](notes/cards/2026_AlphaPilot.md)（顺带涉及）：以短期未来窗口 IC/RankIC 作代理奖励，不在每条训练轨迹中做完整回测；训练 4B 小模型代替大模型推理（第 2.2 节、Limitations、附录 B.1）。
- 2026-10 [AlphaPADI](notes/cards/2026_AlphaPADI.md)（顺带涉及）：把公式在历史面板上的执行视为主要成本，按去重后的规范式计提交预算（|A| ≤ B，失败提交计入，缓存命中不计），偏好目标复用缓冲区中已评分的池，不必消耗预算采新的同策略样本（第 3 节、附录 B.1.2）。
- 2026-09 [GoAnt](notes/cards/2026_GoAnt.md)（主要针对）：把“每一次模拟都是稀缺资源”做成显式的两级分配：上层 pending 感知的渐进扩展 MCTS 决定下一条血统拿预算，其 pending 计数保证在途工作影响后续分配、非根节点最多一个在途子节点、走到死路时回根兜底、冷启动由兜底处理；下层提议者内部用 16→8→4→2→1 的折半锦标赛，31 次模拟完成 80 次才能完成的五轮修订，形成 61% 的模拟节省。诊断日志给出解析失败、低置信弃权、回退率与“与 UCB 最优臂的一致/偏离率”（0.62/0.59 一致，0.38/0.41 偏离），用来证明调度器不是披着语言模型外壳的赌博机（第 4.4 节、算法 1、附录 D、表 S2）。
- 2026-08 [AutoScientist-Quant](notes/cards/2026_AutoScientist-Quant.md)（主要针对）：把预算、每轮生成数与是否继续都做成运行时的显式决策，而不是预先固定的方向数、轮数与因子数；STOP 的触发条件是边际证据不再明显，避免在饱和方向继续消耗评价（第 1.3 节、第 2.2 节、Eq. 3）。
- 2026-08 [AlphaG-OPD](notes/cards/2026_AlphaG-OPD.md)（主要针对）：所有实验臂固定在 10,000 次物理终端评分的同一账本下比较，探针成本按 3×4 显式计入、门控弃权也计费，重放不耗预算（附录 E）。
- 2026-08 [AgonAlpha](notes/cards/2026_AgonAlpha.md)（主要针对）：把每次平台模拟当作按次计费、耗时数分钟的稀缺资源，把“下一次调用给哪条血统”做成显式的序贯决策问题：上层 pending 感知 MCTS 在并行流水线之间分配，下层折半锦标赛把 16 个候选压到 1 个，31 次模拟即可完成 80 次才能完成的五轮修订（少 61%）；九种基线（单智能体、辩论投票、R&D-Agent-Quant、TradingAgents、AlphaAgent、AlphaGen、AutoAlpha、CVT-MAP-Elites、CMA-ME）在同一预算下重实现并对照（第 4.4 节、5.4 节、图 3、表 1）。
- 2026-07 [AlphaSchema](notes/cards/2026_AlphaSchema.md)（主要针对）：代理模型在 LLM 实现和回测之前给候选打分，配额选择器分配有限的实现与回测预算；论文还比较了同一计划重复实现的预算效率，据此选用单次实现（第 3 节、第 5 节、附录 E）。
- 2026-05 [QuantEvolver](notes/cards/2026_QuantEvolver.md)（主要针对）：用 RFT 把经验写入轻量模型参数，代替不断增长的提示词上下文。
- 2026-03 [FactorEngine](notes/cards/2026_FactorEngine.md)（顺带涉及）：微观参数用贝叶斯优化实例化，运行中不额外调用大模型。
- 2026-03 [AlphaLogics](notes/cards/2026_AlphaLogics.md)（顺带涉及）：内循环在固定 Γ 下以 T_early = 3 早停，候选缓冲只在同一逻辑内比较，改进停滞即返回逻辑级证据摘要，把预算从“继续搜表达式”转向“换逻辑”或直接结束（算法 1–2，第 4.1 节）；论文对 agent 类基线统一试验数（20 次试验、5 轮演化）与每轮候选上限，使比较在相同 LLM 调用预算下进行（第 4.1 节）。
- 2026-02 [FactorMiner](notes/cards/2026_FactorMiner.md)（顺带涉及）：先在小资产集快速筛选，再在相关性剪枝后做全量验证。
- 2025-09 [Tree-GRPO](notes/cards/2025_Tree-GRPO.md)（主要针对）：共享前缀的树搜索在同一 token 与工具调用预算下得到更多 rollout，在每题约 2 条完整轨迹的低预算下仍能学会多轮交互，并以四分之一预算超过链式方法（第 3.1、4.3 节，表 3）→ 对应 LLM 因子智能体中每轮生成与评价调用都计入成本的情形：从中间轮次分叉、复用已完成的前缀步骤，可在同等生成与评价预算下获得更多训练样本；已收录的 QuantEvolver 与 Alpha-R1 速读卡记录的是 GRPO 组相对优势，未见树结构采样。
- 2025-08 [TreEvo](notes/cards/2025_TreEvo.md)（主要针对）：把 LLM 的先验直接用作搜索的组织方式，使达到同等 IC 所需的评价次数大幅减少。论文报告在 CSI300 上，TreEvo 用比 XGBoost 与 LightGBM 少 5 倍、比其他传统方法少最多 200 倍的评价值取得更高 IC；LLM 驱动方法统一只用 200 次评价的预算，而 GP 为 40,000 次、AlphaGen/AlphaForge/QFR 至少 50,000 次、XGBoost/LightGBM 为 1,000 次（第 4.1.2、4.2.2 节、图 4）。TreeEvo 单次运行的实际开销为 20 分钟、65.4 万 token，EoH 为 40 分钟、63.2 万 token，ReEvo 为 18 分钟、41.4 万 token（附录 F.2、表 4）。
- 2025-08 [AlphaEval](notes/cards/2025_AlphaEval.md)（主要针对）：五项指标都是可独立并行计算的信号矩阵函数，不需要按时间顺序推进、带仓位与现金状态的组合回测。
- 2025-06 [DeepMind AlphaEvolve](notes/cards/2025_DeepMind-AlphaEvolve.md)（顺带涉及）：评价级联先在小规模、低难度测试上筛掉不理想的候选，评价可异步分发到集群并行执行，整条流水线以总吞吐而非单次计算速度为优化目标，LLM 集成中用低延迟模型提高单位时间的候选数（第 2.3、2.4、2.6 节）→ 对应因子评价中先用短区间、小股票池或子样本做廉价初筛，只把通过者送全市场长周期回测，并按吞吐组织 LLM 生成与回测；已收录工作中未见明确借用评价级联，CogAlpha 先做代码与执行检查再按 IC 等指标过滤的流程与之相近（见 CogAlpha 速读卡）。
- 2024-12 [Warm Start GP](notes/cards/2024_WarmStartGP.md)（顺带涉及）：搜索被限制在有限子空间且结构不增长，论文据此论证计算负担下降；但未给出收敛所需的评价次数或运行时间统计（第 3.4 节）。
- 2024-06 [AlphaForge](notes/cards/2024_AlphaForge.md)（顺带涉及）：用可微预测器代替部分真实评价来引导生成。
- 2024-06 [Alpha2](notes/cards/2024_Alpha2.md)（顺带涉及）：搜索阶段的维度预剪枝提前排除不可能合法的程序。
- 2023-05 [AlphaGen](notes/cards/2023_AlphaGen.md)（顺带涉及）：用预存的 IC 与互相关增量更新组合损失，避免每次重算。
- 2021-06 [GFlowNet](notes/cards/2021_GFlowNet.md)（顺带涉及）：原领域的真实检测昂贵，论文用廉价代理模型给奖励，生成器拟合代理诱导的分布后每轮只把一批多样样本送真实 oracle，再用新标注数据更新代理（第 4.3 节）；论文还指出这种批量生成的计算成本与批大小呈线性，而两两比较候选的方法至少为平方（第 1 节）→ 对应因子挖掘中用预测器或子样本评价作为代理奖励训练生成器，只把多样化的候选批次送全市场长周期回测；已收录工作中未见在 GFlowNet 中借用这一多轮代理流程，仓库专题“公式因子挖掘的三类训练方法”记录的 AlphaForge Predictor 属同类代理思路，但不是 GFlowNet。
- 2021-03 [AlphaEvolve](notes/cards/2021_AlphaEvolve.md)（顺带涉及）：冗余剪枝与指纹机制跳过重复计算。
- 2020-02 [AutoAlpha](notes/cards/2020_AutoAlpha.md)（顺带涉及）：PCA 近似相似度降低去重成本。

<a id="p4"></a>

### P4 学习信号稀疏、延迟且不可微（主要 20，涉及 2）

- 2026-10 [AlphaRLM](notes/cards/2026_AlphaRLM.md)（主要针对）：用 DAPO 的组内相对优势替代 critic，同一文献提示下的 8 个补全互相比较，为“同一经济思想的不同落地方式”提供相对学习信号；奖励分解为可行性（有效）与经验质量（TMB）两项规则化信号，训练全程不依赖完整回测的对话式反馈（第 3.3–3.4 节、附录 C）。消融上去掉 DAPO 后 CSI300 AR 由 12.14% 降至 9.66%，S&P 500 由 6.94% 降至 3.14% 且 MDD 由 −14.84% 恶化到 −30.72%（表 2）。
- 2026-10 [AlphaPilot](notes/cards/2026_AlphaPilot.md)（主要针对）：奖励只在轨迹结束时按最终池的未来窗口表现给出，用 GRPO 组内相对优势做轨迹级信用分配，不训练单独的 critic；池完整度乘子惩罚保留因子过少的轨迹（第 4.4–4.5 节、附录 A.5）。
- 2026-10 [AlphaPADI](notes/cards/2026_AlphaPADI.md)（主要针对）：池级奖励经符号执行和联合拟合得到，不可微；论文把它转成满足奖励间隔的池对偏好，在相同腐化变量下比较两池的重建分数做偏好学习，不需要逐公式奖励（第 2.2、4.3 节）。
- 2026-10 [AlphaLedger](notes/cards/2026_AlphaLedger.md)（主要针对）：因子的经济价值只有写完整程序后才能评价，而生成是逐动作进行的；论文用“完整程序 + 组合边际贡献账本”作为教师的特权上下文，在学生的每个合法动作前缀上给出偏好，把终点标量变成动作级监督，学生在蒸馏时仍不接收结果输入（第 3.3 节、Eq. 5–7、Table 1）。
- 2026-09 [AlphaRJM](notes/cards/2026_AlphaRJM.md)（主要针对）：持久记忆把跨公式的“奖励 + 结果类别”序列保留下来，弥补“只按当前池条件化”丢失的历史；SDE 评论家把不确定的未来折扣发现回报表示成可采样分布，用均值与离散度共同引导动作，形成比点估计更密的信用信号（第 1、3.2–3.4 节），并以分布式 Bellman 目标训练（式 20–23）。
- 2026-09 [AlphaPareto](notes/cards/2026_AlphaPareto.md)（主要针对）：把冻结 LLM 编码的当前因子池嵌入并入策略状态，让策略能感知池的组成；论文称这样把依赖因子池的非平稳 MDP 改写为增广状态下的平稳 MDP（第 3、4.1 节）。
- 2026-09 [AlphaDiverse](notes/cards/2026_AlphaDiverse.md)（主要针对）：联合 GRPO 按角色分配信用，Planner 在计划组合之间比较，Realizer 在同一计划的不同实现之间比较；奖励尺度和最低增益阈值用历史候选与高斯噪声因子组合的得分增益分位数校准（第 2.3 节、附录 B.2）。
- 2026-08 [AlphaG-OPD](notes/cards/2026_AlphaG-OPD.md)（主要针对）：用同前缀下多个兄弟动作的配对终端评分构造局部教师，替代只有轨迹级标量的 TB 信用分配；可靠性门控与梯度配比控制辅助信号的强度与寿命（第 3 节、组件 I–III）。
- 2026-06 [AlphaMemo](notes/cards/2026_AlphaMemo.md)（主要针对）：论文把问题定义为 search-level credit assignment——子因子的分数包含父因子继承的信号，直接把它当成“这次编辑的奖励”会强化只是保住了好起点的改动（第 1 节）。AlphaMemo 因此不训练策略、不算梯度，而是对每次“可执行父—子转移”记录实际发生的结构编辑与其相对信用，在线累积到 (g,m) 单元，并在下一轮用于 motif 选择（第 4.2、4.5 节、Algorithm 1）；记忆只用搜索期反馈更新，样本外不参与（第 6.1 节）。论文把这一步与 policy fine-tuning、RL、全轨迹回放区分开，理由是不需要另起训练循环、记忆表可读可改（第 5.4 节、附录 E 的 Q6）。
- 2026-05 [QuantEvolver](notes/cards/2026_QuantEvolver.md)（主要针对）：组内相对优势更新。
- 2025-09 [Tree-GRPO](notes/cards/2025_Tree-GRPO.md)（主要针对）：只用结果奖励，在每个分叉点比较兄弟子树回传的奖励，把轨迹级信号转成粒度随子树深度变化的过程信号；树内优势提供隐式步骤级偏好，树间优势提供更稳定的基线（第 3.2–3.3 节、表 4）→ 对应公式生成或多轮因子智能体只有终端 IC 的情形：在共享前缀处分叉，比较不同后续的 IC，得到前缀层面的相对信用；已收录的 QuantEvolver 与 Alpha-R1 只用回合级 GRPO 优势（见两者速读卡），未见借用树结构优势。
- 2025-09 [AlphaSAGE](notes/cards/2025_AlphaSAGE.md)（主要针对）：预测性能、结构对齐与新颖性的多信号奖励加轨迹平衡。
- 2025-07 [TLRS](notes/cards/2025_TLRS.md)（主要针对）：专家子序列轨迹级塑形与奖励中心化。
- 2025-05 [GiGPO](notes/cards/2025_GiGPO.md)（主要针对）：在不增加 rollout、不训练 critic 的前提下，从已采样轨迹中重复出现的状态回溯构造步骤级组，用同一状态下不同动作之后的折扣回报差异给出逐步信用，并与回合级优势相加（第 4.2–4.3 节）→ 对应公式逐 token 生成或多轮 LLM 因子智能体只在完成后得到 IC 的情形：同一批采样中重复出现的公式前缀或智能体状态可作为锚点，比较其后不同动作的最终奖励，得到比整条轨迹更细的信用；已收录的 QuantEvolver 与 Alpha-R1 使用的是回合级 GRPO 组相对优势（见两者速读卡），未见借用步骤级锚点分组。
- 2025-05 [AlphaQCM](notes/cards/2025_AlphaQCM.md)（主要针对）：奖励分布方差作为探索奖励。
- 2024-09 [QFR](notes/cards/2024_QFR.md)（主要针对）：不带价值网络的 REINFORCE 加贪婪基线。
- 2024-06 [AlphaForge](notes/cards/2024_AlphaForge.md)（主要针对）：以可微预测器近似真实 fitness，通过预测评分为生成器提供梯度信号。
- 2024-02 [RiskMiner](notes/cards/2024_RiskMiner.md)（主要针对）：合法中间表达式即时奖励。
- 2024-02 [QuantAgent](notes/cards/2024_QuantAgent.md)（顺带涉及）：外层循环以真实回测反馈驱动知识库更新，用于下一轮生成。
- 2022-01 [Trajectory Balance](notes/cards/2022_TrajectoryBalance.md)（主要针对）：用整条轨迹上的一个残差同时更新所有步的 log P_F，终端奖励一次分配到每个动作，而不是像 FM / DB 那样逐步回传；比特序列任务中 FM 的拟合随轨迹变短而改善，TB 对轨迹长度与动作空间大小都稳健（第 3、5.3.1 节，图 4）→ 对应公式 token 序列只有终端 IC、序列较长且词表大的情形，可用 TB 把终端奖励直接分到每个 token；已收录的 AlphaSAGE 即用 TB 损失训练公式生成的前向策略（见 AlphaSAGE 精读的“轨迹平衡与探索目标”）。
- 2021-06 [GFlowNet](notes/cards/2021_GFlowNet.md)（顺带涉及）：奖励只在终止状态给出，论文把终端奖励作为流网络的边界条件，用流守恒损失为每个中间状态提供训练目标，奖励本身无需可微，且训练可离策略、离线进行（第 2.2 节、命题 3）→ 对应公式只有完整生成后才有 IC、IC 对 token 不可微，已评价过的历史公式也可作为离策略训练轨迹复用；已收录的 AlphaSAGE 采用 GFlowNet 框架，但训练目标用的是后续的 Trajectory Balance（见 AlphaSAGE 精读的“轨迹平衡与探索目标”）。
- 2019-12 [DSR](notes/cards/2019_DSR.md)（主要针对）：奖励只在表达式完成时出现且不可微，论文用策略梯度训练生成器，并以风险寻求目标只用批内高于 (1−ε) 分位数的样本、以该分位数为基线更新（第 3.2 节）→ 对应公式因子只有完整生成后才有 IC、IC 对 token 无梯度，且挖掘最终只保留少数高分因子，可用分位数基线把更新集中到高分尾部；已收录的 RiskMiner 采用同一思路的风险偏好优化，关注回报分布高分位而非均值（见 RiskMiner 速读卡）。

<a id="p5"></a>

### P5 低信噪比下的过拟合（主要 8，涉及 14）

- 2026-10 [QBX](notes/cards/2026_QBX.md)（顺带涉及）：以根身份去重的试验账本记录实际试验次数，为 deflated Sharpe 等多重检验校正提供分母；统计校正本身留作后续工作。
- 2026-10 [FactorBench](notes/cards/2026_FactorBench.md)（顺带涉及）：用训练期固定因子方向，比较同一批因子在训练、验证、测试期的 IC、RankIC、ICIR，并计算因子内配对的训练–测试退化量，保留样本外符号反转。
- 2026-10 [EvoQuantLab](notes/cards/2026_EvoQuantLab.md)（主要针对）：最差开发折适应度、复杂度约束与等预算零假设搜索诊断候选及搜索选择的过拟合（原文第 3.1、3.4 节）。
- 2026-09 [GoAnt](notes/cards/2026_GoAnt.md)（顺带涉及）：适应度用 deflated t 统计量而非原始 RankIC，对日 IC 随机变号的噪声因子给出接近零的分数；只保留正 IC 期比例与正日 IC 占比达标的候选；所有臂共享同一常数的有效样本量做通胀校正，多重比较负担在报告时按共同评价预算施加一次；选择风险作为审稿/闸门维度之一（第 3 节、附录 A、表 S4）。
- 2026-09 [AlphaRJM](notes/cards/2026_AlphaRJM.md)（顺带涉及）：沿用 AlphaQCM 一类的分布式视角，把回报分布的离散度当作不确定性探索信号，避免过早集中在单次高 IC 结果上；图 2 显示过度扩散反而退化，表 4 显示去掉分布式损失会同时压低 IC 与 ICIR（第 4.4 节、附录 E.1）。
- 2026-09 [AlphaPareto](notes/cards/2026_AlphaPareto.md)（主要针对）：把 RRE（排序的时间稳定性）与 PFS（扰动稳健性）写入奖励，用各目标最低水平约束代替只看样本内 IC，针对“高 IC 但波动大、对扰动脆弱、样本外失效”的因子池（第 3、4.2 节）。
- 2026-09 [AlphaDiverse](notes/cards/2026_AlphaDiverse.md)（顺带涉及）：研究反馈只来自内层期，最终因子与模型冻结后只在外层期评估一次，以避免 test-set tuning；噪声校准使增益低于噪声水平的计划拿不到正的质量分；多折设置下，保留要求加权得分提升且多数折改进（主比较为单折）（第 1 节、第 2.1 节、附录 B.2、C.1）。
- 2026-08 [AutoScientist-Quant](notes/cards/2026_AutoScientist-Quant.md)（顺带涉及）：论文引用回测过拟合文献说明“每次接受都在测试期上选择”会带来选择效应，并以反馈窗与评估窗分离来消解；消融中“去掉动态决策（dynamics）”使扣费超额收益下降最多 3.8 个百分点，是研究中单项降幅最大者（第 1.2 节、第 4.2 节、表 2）。
- 2026-08 [AlphaSeek](notes/cards/2026_AlphaSeek.md)（顺带涉及）：复杂度正则（符号长度 SL、自由参数数 PC、原始特征数 log(1+|F_f|)）进入目标函数，与演化算子共同约束生成过程；消融中去掉复杂度控制后性能下降，但三项控制中影响最小（第 4.3 节，图 4）。
- 2026-08 [AgonAlpha](notes/cards/2026_AgonAlpha.md)（顺带涉及）：“选择风险”审计维度专门检查反复搜索是否产出已提交 alpha 的近似副本、或调参是否集中在狭窄的因子家族；评分用总体中位秩百分位而非原始分，使奖励对分数分布非平稳不敏感；论文引 DSR、Reality Check 等数据窥探文献作为解释框架，但未做多重检验校正（表 2、第 4.4 节、第 6 节）。
- 2026-07 [X-Alpha](notes/cards/2026_X-Alpha.md)（顺带涉及）：选择阶段加入硬性滚动样本外过滤，在 normal 池 top-200 上使 mean held-out RankIC 与 RankICIR 分别提高 14.56% 与 17.85%；复杂度折扣的四种函数使 RankIC 提高 5.07–7.98%、平均复杂度下降 7.31–12.69%（第 4.5 节、附录表 18–19）。
- 2026-06 [AlphaMemo](notes/cards/2026_AlphaMemo.md)（主要针对）：摘要列出的四项挑战之一即“naively reusing past successes 带来的过拟合风险”。机制上有三层：残差信用把编辑收益相对同质量父因子桶做基准化，避免把父因子的高分重复计功（第 4.2 节、式 6）；置信门按样本数、准入率熵与残差方差折扣稀疏或不稳定的信用，n<2 时直接为 0（式 9）；不对称否决在重复失败后抑制该 (g,m)，正向证据只作软偏好（第 4.4 节、式 11）。消融给出同种子对照：CSI500 上“绝对信用”（直接用子因子 |ICIR| 作信用）的 ICIR 为 0.2468，低于残差信用的 0.2698（表 3）。论文自己限定这类机制是“经验复用的校准控制，不构成过拟合保证”（附录 E 的 Q5）。
- 2026-06 [Agora/SJS](notes/cards/2026_Agora-SJS.md)（主要针对）：最终评估数据对参与搜索的智能体保持密封。
- 2026-05 [PRISM-VQ](notes/cards/2026_PRISM-VQ.md)（顺带涉及）：以有限码本作为信息瓶颈、限制有效模型容量，使嵌入吸附到重复出现的截面原型上，配合对比损失与重构/辅助预测正则，抑制个股特异性噪声；论文把这一点列为主要设计理由之一（第 4.2 节）。需要区分的是，这里的机制是表示层面的容量约束与正则化，不是对搜索规模做多重检验校正。
- 2026-04 [MarketSenseAI](notes/cards/2026_MarketSenseAI.md)（主要针对）：用同股票池、同日期、同持仓数的 10,000 个随机等权组合构造零分布，使市场层面与行业层面的收益在比较中相互抵消，唯一变量是选股；报告的 p 值是对“选择技能是否超过运气”的直接检验，而不是只看单条收益曲线（第 3.1 节、表 3）。S&P 500 队列的强买组合月度均值 +2.18% 对基准 +1.15%，处于零分布第 99.7 百分位（p=0.003）；S&P 100 队列 +2.02% 对 +1.47%，第 83.4 百分位（p=0.166），论文据每日期均仅约 10 只持仓导致的检验功效不足来解释不显著，并明确称该队列“方向一致但未独立确认”（表 3、第 5.1 节）。需要区分的是，这是组合选择层面的零分布检验，不是对挖掘搜索规模的多重检验校正。迁移点：原领域解决的是“选股建议的收益是否只是运气”的问题 → 迁移到因子挖掘，对应单因子或因子池的显著性检验，即在同股票池、同日期、同持仓数下构造随机零分布，而不是只与指数或等权基准比较；已收录工作中 FactorBench 与 AlphaEval 提供跨方法基准，但未使用这一同构零分布设计。
- 2026-03 [AgenticFactorInvesting](notes/cards/2026_AgenticFactorInvesting.md)（主要针对）：论文把“大规模搜索即多重检验”作为核心动机，并用三层机制应对——生成阶段的经济理由约束收缩假设空间（作者称其相当于一个降低多重检验负担的贝叶斯先验，第 6.1 节）；显著性门槛由 2.0 提高到 3.0，并引入 Harvey & Liu (2021) 的 Scaled Intercept 式“增量解释力”要求（第 6.2 节）；样本外协议上，所有发现与智能体学习在 2020-12 前冻结，2021–2024 期间因子库与内部状态不再更新，声称是可防止“迭代造成隐式测试集反馈”的盲测（第 3.3 节、第 6.4 节）。第 6.3 节还以 López de Prado 的 False Strategy Theorem 与 Deflated Sharpe Ratio 作为设计依据，但只落实为多目标闸门这一“功能性启发式”，正文未给出 DSR 的计算（据原文脚注 10）。
- 2025-12 [Alpha-R1](notes/cards/2025_Alpha-R1.md)（顺带涉及）：用 PSR、DSR、PBO 等多重检验校正评估筛选结果的显著性。
- 2025-05 [Alpha-Jungle](notes/cards/2025_Alpha-Jungle.md)（顺带涉及）：在评价中显式给过拟合风险打分。
- 2025-02 [AlphaAgent](notes/cards/2025_AlphaAgent.md)（顺带涉及）：AST 节点数、参数数、特征数正则。
- 2024-12 [Warm Start GP](notes/cards/2024_WarmStartGP.md)（顺带涉及）：论文引用受限结构可降低过拟合风险的既有结果，并观察到增强后的 alpha 样本外 IC（均值 0.047）高于样本内（0.034），而原始 Alpha101 alpha 样本内外几乎相同（第 3.4 节、第 4.3 节、表 1）。
- 2023-03 [Sequential Cauchy](notes/cards/2023_SequentialCauchy.md)（主要针对）：原领域解决的是“大量相关检验下，显著性检验本身会因重复尝试而膨胀”。方法给出的是检验侧的控制工具：给定一族候选因子的 p 值（每个因子对“真实 IC 或 alpha 为零”的单检验），SCC 给出在 α 水平上强控制 FWER 的拒绝集 R，且不要求因子彼此独立——这一点对因子挖掘直接相关，因为同一算子空间生成的因子必然高度相关，Bonferroni/Holm/BH 在强相关下会过度保守、把真因子也一并丢掉。模拟中这一点被量化：相关矩阵指数衰减 θ=0.95 时 Bonferroni/Holm 的实测 FWER 只有 1.76%，而 SCC 为 5.38%，接近名义 5%；对应地全局功效 SCC 高出约 10 个百分点（表 1、表 2）。迁移到因子挖掘对应的是：把挖掘全过程（含被淘汰与被去重的候选）的统计量收成一个检验族，用 SCC 一次性给出“哪些因子在考虑整个搜索族之后仍然显著”，取代逐个因子看 t 值或对全部候选统一乘 Bonferroni 惩罚。论文的两个应用之一（检验 Fama-French 五因子模型下哪些组合有非零 alpha）与“检验一批候选因子是否真的带来超额收益”在结构上同构。
- 2022-09 [Publication Bias](notes/cards/2022_PublicationBias.md)（主要针对）：原领域解决的是“一群已发表的显著结果里，有多少是选择偏差造成的、平均被高估多少”。给出的是两件可直接落到因子挖掘结果上的量：对一组候选因子的 t 统计量，用经验贝叶斯把 t 收缩为校正后的 θ（式 14），得到“平均有多少幅度是运气”；用 FDR=Pr(θ≤0|发现) 给出“这批因子里预期有多大比例其实没有正期望收益”（式 10）。迁移到因子挖掘对应的是：把挖掘流程产出的 N 个因子（含被淘汰的）的统计量当作检验族，估计 σ_θ 后报告收缩后的 IC/t 与 FDR，而不是只报最好因子的原始 t 值；四条风格化事实同时给出了“什么时候可以说挖掘找到了真实结构”的判据清单——可复现、样本外持续、t 值远超门槛、彼此弱相关。论文还提示了最容易被误用的方向：样本外衰减不能直接当作选择偏差的证据，必须先把偏差与期望收益变化分开（第 4.2 节）。

<a id="p6"></a>

### P6 前视偏差与信息泄漏（主要 6，涉及 13）

- 2026-10 [QBX](notes/cards/2026_QBX.md)（主要针对）：时间可用性效应系统在编译期、加载数据之前拒绝登记契约可见的前视，同时允许发布时点早于索引的合法时点预测值。
- 2026-10 [EvoQuantLab](notes/cards/2026_EvoQuantLab.md)（主要针对）：前缀重放不变性、purged 开发折、OOS 隔离与 L5 冻结限制信息回流（原文第 3.1–3.2 节）。
- 2026-10 [Auditing LLM Alpha-Factor Mining](notes/cards/2026_AuditingLLMAlpha.md)（顺带涉及）：核查“OOS 验证集”的生成过程，发现留存目录写出前已按 OOS Sharpe 剔除非正结果，并提出在接触 OOS 之前冻结并哈希候选清单、只用 IS 数据筛选与去重、保留全部 OOS 结果与报错的干净评估协议。
- 2026-10 [AlphaRLM](notes/cards/2026_AlphaRLM.md)（顺带涉及）：有效性奖励把计算窗口分别向前延长 1 天、1 周、1 月、1 年后重算因子值，若原窗口的因子值改变即判为使用了未来数据并给 0 分；文献语料限定为 2015–2019 年发表，测试区间在 2019 年文献截止之后（附录 B 的有效性奖励、附录 A 的文献数据）。消融中把金融文献换成同期非金融文献，等于同时去掉这一先验，因此无法分离“语料时点控制”的单独贡献（表 2）。
- 2026-10 [AlphaLedger](notes/cards/2026_AlphaLedger.md)（顺带涉及）：Table 1 逐阶段列出信息边界——学生 rollout 不看结果、教师只看 t0=2024-12-31 前到期的标签、部署只用 t−1 前信息、RRG 记录须满足 u+h_g+1 ≤ t−1；论文也承认无法排除 2025 年后发布模型的预训练区间覆盖测试期（Table 1、第 3.5 节、Limitations）。
- 2026-09 [GoAnt](notes/cards/2026_GoAnt.md)（顺带涉及）：描述子轴的准入规则是构造性的——一个量只有在不读取未来收益标签的前提下可算才能进入描述子，并且这一点通过检查调用图验证而不是估计相关性；描述子的稳健标准化统计量只在开发集上拟合一次并冻结，任何臂都不得在搜索中重新估计；开发窗口与锁定窗口严格不相交，锁定窗口只用于样本外重放；早期版本曾把 RankIC 与日 IC 统计量放进描述子，论文专门报告了这一污染诊断（附录 E、F.1）。
- 2026-09 [AlphaDiverse](notes/cards/2026_AlphaDiverse.md)（顺带涉及）：执行模块拒绝使用预测时点之后信息的因子规格；特征只用 t 日收盘后可得的信息，标签为 t+1 开盘到 t+2 开盘的超额收益；各时间段边界按标签重叠做 purge；股票池按历史每日指数成分构造（第 2.1 节、附录 B.2、C.1）。
- 2026-08 [AutoScientist-Quant](notes/cards/2026_AutoScientist-Quant.md)（主要针对）：论文把“循环反馈窗口与最终评估窗口重叠”列为核心动机之一，指出模型层面的训练/验证/测试切分并不等于搜索层面的切分，因为每个被接受的 alpha 都是按测试期表现选出的；解决方案是把数据切成训练、验证、反馈（2021-06 至 2023-06）、测试（2023-06 至 2026-05）四段，反馈窗与测试窗不相交，测试窗只在最后一次读取；同时修正了沿用代码中的两处前视问题并全量重跑基线（第 1.2 节、第 3.1 节、第 1.3 节）。
- 2026-07 [X-Alpha](notes/cards/2026_X-Alpha.md)（顺带涉及）：候选执行后筛查未来信息泄漏，可修复的进入修复—复验、持续失败的在实证评价前丢弃（第 3.3 节、图 2 的 Numerical & Leakage Tests）；训练/验证/测试按 2011–2020、2021、2022–2025 划分，测试期只用于报告（第 4.1 节、附录 J）。
- 2026-07 [AlphaSchema](notes/cards/2026_AlphaSchema.md)（顺带涉及）：代码实现须通过前视泄漏筛查，提示词规定 t 时刻的信号只能使用 t 及之前的信息；因子筛选、相关性过滤和模型选择只用训练与验证窗口（第 3 节、附录 A、附录 D）。
- 2026-06 [Agora/SJS](notes/cards/2026_Agora-SJS.md)（主要针对）：持有期评估数据不进入任何面向模型的输入。
- 2026-05 [PRISM-VQ](notes/cards/2026_PRISM-VQ.md)（顺带涉及）：股票池使用当期指数成分以规避幸存者偏差，先验因子只用截至 t−1 的信息、取前 20 日累计收益（附录 B、式 B.1），预处理用 RobustZScoreNorm 与按日截面排名归一化（第 5.1 节）。
- 2026-04 [MarketSenseAI](notes/cards/2026_MarketSenseAI.md)（主要针对）：以“实时生成”取代回溯回测——每个观察日的信号都由系统当场运行产生，而不是在已知结果后再生成；观察区间整体落在底层 LLM 训练截止之后，使评估期不进入模型预训练语料；同时用固定队列（只在扩容后始终在册的成分）避免幸存者偏差与成分变动带来的后见之明（第 2 节）。论文称这是避免前视偏差的主要防线，也是经验分析必须锚定这两个固定队列与观察日的原因。迁移点：原领域解决的是“已部署选股系统的信号无法追溯、只能在事后补生成”的问题 → 迁移到因子挖掘，对应 LLM 生成阶段的泄漏控制，即把信号产生时间固定在决策时点、让评估期落在模型知识截止之后；已收录工作中 Look-Ahead-Bench 用知识截止前后两期比较来度量同类泄漏，Auditing LLM Alpha-Factor Mining 用“接触 OOS 前冻结并哈希候选清单”约束同一风险，本文提供的是部署状态下的实时生成口径。
- 2026-03 [FactorEngine](notes/cards/2026_FactorEngine.md)（顺带涉及）：启动资料限定只用测试期之前发布的研报，控制知识泄漏。
- 2026-03 [AlphaLogics](notes/cards/2026_AlphaLogics.md)（顺带涉及）：显式声明“无泄漏与统一评价协议”，早停、因子/逻辑选择与反馈全部只用 D_val，D_train 仅用于拟合与因子值计算，结果只在 D_test 报告（第 4.1 节）。该机制只覆盖系统内部的信息流，未处理 LLM 预训练语料与 2021–2024 测试区间重叠的风险（据原文，未见讨论）。
- 2026-03 [AgenticFactorInvesting](notes/cards/2026_AgenticFactorInvesting.md)（顺带涉及）：以 filtration 形式约定 f_{i,t}∈F_t=σ({X_{j,s}}_{j∈N,s≤t})（式 3.4）；截面预处理逐日进行而非用全样本矩，时序算子只用截至该日的历史；晋升阈值只在样本内计算，样本外不参与再排序或策略更新（第 3.3 节）。附录 A.1 用 ReAct 与思维链把“先写理由再写公式”形式化（式 A.1–A.2），并明确其为概念框架而非可估计的计量模型（附录 A.3）。
- 2026-01 [Look-Ahead-Bench](notes/cards/2026_Look-Ahead-Bench.md)（主要针对）：以模型知识截止时间为界，比较训练窗口内与截止后两个时期的超额收益变化，并以截止时间早于两期的时点化模型和量化基线作对照，区分记忆与真实预测；文中的 alpha decay 指这一前视偏差信号，与因子随时间衰减不是同一概念。
- 2025-12 [Alpha-R1](notes/cards/2025_Alpha-R1.md)（顺带涉及）：用 point-in-time 成分、各模块数据截止表与前视内容审计控制泄漏。
- 2025-11 [CogAlpha](notes/cards/2025_CogAlpha.md)（顺带涉及）：多智能体质量检查器中包含时间泄漏检查。

<a id="p7"></a>

### P7 因子同质化与冗余（主要 23，涉及 22）

- 2026-11 [CosmosAlpha](notes/cards/2026_CosmosAlpha.md)（主要针对）：三类关系显式编码冗余来源，其中结构边与相关边直接度量结构相似与截面暴露相似（取绝对值，负相关也算冗余）；多样性效用按到固定参考集的近邻距离计算，并在选父时以非支配排序保留质量、繁殖力、多样性之间的权衡，而不压成标量（第 3.2–3.4 节、附录 A.4）。
- 2026-10 [QBX](notes/cards/2026_QBX.md)（顺带涉及）：精确字符串、结构/规范化、审计重写饱和、面板外延等价四级身份阶梯识别别名与重复，并以行为生态位占用惩罚降低入选因子间的相关性。
- 2026-10 [LineageEvo](notes/cards/2026_LineageEvo.md)（主要针对）：论文把“随机变异 + 适应度选择”导致的搜索集中、谱系接管作为核心问题；LSPS 在谱系层按质量与稀少度混合分配预算，并限制单谱系在活跃种群中的占比不超过 0.40；消融去掉 LSPS 后，谱系熵从 2.154 降到 0.405、平均成对 AST 距离从 0.747 降到 0.509、有效结构数从 41.90 降到 37.89（第 1 节、第 3 节、表 3）。
- 2026-10 [FactorBench](notes/cards/2026_FactorBench.md)（顺带涉及）：以截面 Spearman 相关度量方法内冗余、方法间收敛和对 Alpha101 的重复，并用 Pearson 相关做稳健性检验。
- 2026-10 [EvoQuantLab](notes/cards/2026_EvoQuantLab.md)（顺带涉及）：家族分层、定向移民和搜索期克隆替换维持结构多样性，最终另按持仓相关去冗余（原文第 3.3 节、附录 C.2）。
- 2026-10 [Det-MASO](notes/cards/2026_Det-MASO.md)（主要针对）：联合目标内加入 agent 间秩相关矩阵的可微 −log det 惩罚，在训练过程中压制同质化而非事后过滤；步成本 O(Nn²+n³)，对资产数 N 线性（式 10 后、表 3）。
- 2026-10 [AlphaPilot](notes/cards/2026_AlphaPilot.md)（顺带涉及）：池得分中加入多样性项（协方差谱的归一化熵）与稳定性项；池满时，候选须替换最弱或最冗余成员后仍提升池得分才能入池；反馈中返回候选与当前池的相似度（第 4.3 节、附录 A.1）。
- 2026-10 [AlphaPADI](notes/cards/2026_AlphaPADI.md)（主要针对）：池上下文参与被遮盖子结构的重建；R_inner 惩罚各成员与池内相关最高邻居（最坏邻居，不是平均）超过 δ 的部分，形式是平方 hinge；规范化后的重复成员替换为随机合法公式（第 4.2–4.3 节、式 8）。
- 2026-09 [GoAnt](notes/cards/2026_GoAnt.md)（主要针对）：论文把“反复探索冗余的因子家族”列为现有系统的两个核心失效之一，用 QD 存档直接对抗模式坍缩：每个小生境只留精英、覆盖只在一个新细胞的精英越过预注册质量下限 q* 后才计入，从而把探索变成需要兑现的赌注而不是白给的补贴；Connector 通过互近邻图（k=4）跨小生境重组。表 1 中 GoAnt 在价格—成交量（PV）与订单簿（L2）两个数据类别上的质量加权有效产出为 41.8 与 47.6，分别比最强基线 AutoAlpha 高 57% 与 97%，同时 distinct 因子数 34/37（AutoAlpha 为 24/22），保留下来的因子两两 |Spearman| 均值 0.31/0.28（AutoAlpha 0.36/0.37）；去掉地图的 No-Map 对照质量加权仅 8.7/7.6、distinct 9/8。角色消融（附录表 S3）显示单个角色都不足以复现完整群体：Exploiter 单独 11.6/10.4、Explorer 单独 24.3/26.1、含 Connector 的两两组合占 116/128 个细胞、缺 Connector 的两两组合只有 92/101，去掉 Connector 的损失（−8.7/−10.9）大于去掉 Exploiter（−6.0/−7.4）。
- 2026-09 [AlphaPareto](notes/cards/2026_AlphaPareto.md)（主要针对）：以池内因子信号协方差特征值的归一化熵 DH 作为多样性奖励；prompt 也要求 LLM 识别池内表达式同质化和信息盲区（第 4.2.1 节、附录 B）。
- 2026-09 [AlphaDiverse](notes/cards/2026_AlphaDiverse.md)（主要针对）：Planner 每轮须覆盖不同机制与主题，并满足相邻轮的新颖性要求；同一计划的两个实现须计算结构不同；筛选时与已有因子的平均绝对相关不得高于 0.90；GRPO 奖励中的 D 项对与历史档案相似的预测变化给递减奖励（第 2.1–2.3 节、附录 B.1、D.5）。
- 2026-08 [AutoScientist-Quant](notes/cards/2026_AutoScientist-Quant.md)（顺带涉及）：单独的 alpha 筛选阶段专治“成员各自有效但彼此冗余”；案例中保留 91 条中的 89 条，但单次 swap 就让测试期 ARR 移动超过 1 个百分点，加入两条同族 volume z-score 因子使子集降到阶段最低，替换两条相对成交量成员为两条成交量增长成员后升到阶段最佳（第 2.3 节、第 4.5 节、图 2）。
- 2026-08 [AlphaSeek](notes/cards/2026_AlphaSeek.md)（主要针对）：冗余惩罚 S(f) 以 AST 最大公共同构子树大小度量新因子与已有因子库的最大结构相似度；Mutation 只做局部正交改写以保留已验证逻辑、避免语义漂移，Crossover 跨并行方向重组以扩大多样性（第 3.2 节，式 7–8、10–11）。消融中去掉冗余控制退化最明显：IC 降幅最大，ARR 下降 6.91%，MDD 上升 12.10%（第 4.3 节，图 4）。
- 2026-08 [AlphaG-OPD](notes/cards/2026_AlphaG-OPD.md)（顺带涉及）：沿用 AlphaSAGE 的 GFlowNet 奖励成比例分布与多模态采样，OPD 只在已访问状态的合法兄弟集合内重分配概率，不改变全局奖励比例（第 3 节）。
- 2026-08 [AgonAlpha](notes/cards/2026_AgonAlpha.md)（顺带涉及）：自相关阈值 0.85 从审稿警告升级为提议者侧的硬性排序前闸门，近重复在排名之前被删除；与已提交祖先的冗余作为建议性记录；五个代表 alpha 的自相关分别为 0.1827、0.4498、0.4173、0.4968、0.6321，均低于 0.70 的上限（表 2、表 3、第 5.2 节）。
- 2026-07 [X-Alpha](notes/cards/2026_X-Alpha.md)（主要针对）：论文把“搜索空间近视”列为核心瓶颈之一——候选级反馈无法告诉系统何时该离开已探索的研究方向，仅调整动量窗口等会产出机制相同的“表面不同”候选；记忆驱动路由据此按周期切换主题与机制家族。跨周期信号多样性上，记忆路由相对固定路由使平均绝对相关下降 35.6%（0.2106→0.1357）、P90 相关从 0.5374 降至 0.3489、有效秩从 27.01 升至 45.22（表 3）；新颖性注入的 10 次事件中父代池平均相关全部下降，平均降 5.90%、有效秩升 12.87%（第 4.5 节、附录表 17）；生成级还有去重与相关性控制，以及入库时 0.60 的相关上限（第 3.3、4.1 节）。
- 2026-07 [MAPLE](notes/cards/2026_MAPLE.md)（主要针对）：多样性正则直接惩罚 Alpha 间成对绝对相关；论文还报告，加正则之前，统一预测头已把 Alpha 间平均相关从仅用股票内路径时的 0.998 降到 0.944（第 3.3 节、第 5.1 节表 3）。
- 2026-07 [AlphaSchema](notes/cards/2026_AlphaSchema.md)（顺带涉及）：探索名额按 Event-Context 覆盖度的新颖性得分分配，优先选少见组合；导出因子池按 |corr|<0.7 贪心去冗余（附录 A）。
- 2026-06 [AlphaMemo](notes/cards/2026_AlphaMemo.md)（顺带涉及）：准入失败记忆专门惩罚“反复因质量或相关性被拒”的 (g,m)，与 |ρ|≤0.70 的准入规则配合（式 3、第 4.4 节）；去掉失败惩罚后 CSI500 的 ICIR 由 0.2698 降到 0.2047、Sharpe 由 0.3994 降到 0.2429（表 3）。
- 2026-05 [QuantEvolver](notes/cards/2026_QuantEvolver.md)（主要针对）：多样性与互补性奖励。
- 2026-03 [Hubble](notes/cards/2026_Hubble.md)（主要针对）：因子家族感知评分。
- 2026-02 [QuantaAlpha](notes/cards/2026_QuantaAlpha.md)（主要针对）：复杂度、结构相似度与输出相关性控制。
- 2026-02 [FactorMiner](notes/cards/2026_FactorMiner.md)（主要针对）：经验记忆记录应避开的高相关区域。
- 2026-02 [AlphaPROBE](notes/cards/2026_AlphaPROBE.md)（主要针对）：谱系图上的多样性检索。
- 2026-01 [AlphaCFG](notes/cards/2026_AlphaCFG.md)（顺带涉及）：价值目标中加入与因子池的结构相似度惩罚，并处理同构表达式。
- 2025-09 [AlphaSAGE](notes/cards/2025_AlphaSAGE.md)（主要针对）：结构对齐与新颖性奖励下覆盖多个高奖励模式。
- 2025-08 [TreEvo](notes/cards/2025_TreEvo.md)（顺带涉及）：剪枝算子显式删除结构冗余或语义中性的子树；论文用五个独立运行所发现最优因子之间的 IC 相关性热图做对照，指出 ReEvo 存在显著冗余（一致的高正相关）、EoH 出现两个方向上的极端绝对相关，而 TreEvo 的非对角系数明显更低、更稀疏，说明其探索了更广的功能空间（第 4.2.3 节、图 8）。
- 2025-08 [AlphaEval](notes/cards/2025_AlphaEval.md)（顺带涉及）：以协方差特征值熵 DE 度量因子集的多样性，信号越共线熵越低。
- 2025-07 [EFS](notes/cards/2025_EFS.md)（顺带涉及）：层次聚类去重与基于随机矩阵理论的去噪和软去重。
- 2025-06 [DeepMind AlphaEvolve](notes/cards/2025_DeepMind-AlphaEvolve.md)（顺带涉及）：程序数据库借鉴 MAP-Elites 与岛模型，在改进最优程序与保持多样性之间权衡；多指标优化把不同“好”的定义下的高分程序放入提示，以激发更多样的候选（第 2.4、2.5 节）→ 对应用分岛或按行为特征分格的候选池，防止搜索集中到少数高分模板；已收录的 FactorEngine 采用多岛并行演化促进多样搜索（见 FactorEngine 速读卡）。
- 2025-05 [RD-Agent(Q)](notes/cards/2025_RD-Agent-Quant.md)（顺带涉及）：相关性去重。
- 2025-05 [Alpha-Jungle](notes/cards/2025_Alpha-Jungle.md)（主要针对）：高频子树规避。
- 2025-02 [AlphaAgent](notes/cards/2025_AlphaAgent.md)（主要针对）：AST 相似度。
- 2025 [CAVB](notes/cards/2025_CAVB.md)（顺带涉及）：通过分位多头间的对比学习避免不同载荷函数学成难以区分的表示；作用对象是载荷网络的分位表示，不是直接惩罚 K 个隐因子的相关性，也没有维护去冗余的公式因子池（第 2.2 节）。
- 2025 [AlphaGAT](notes/cards/2025_AlphaGAT.md)（顺带涉及）：Stage I 损失惩罚因子间协方差矩阵的非对角项。
- 2024-12 [Warm Start GP](notes/cards/2024_WarmStartGP.md)（主要针对）：传统 GP 的 10 次运行各取前 10 条 alpha，平均 Spearman 相关达 0.87，其中 7 次运行产出完全相同的因子；本框架从 10 个不同起点并行搜索，平均相关降到约 0.60 且不产出相同因子，机制上靠拒绝重复个体与“不同起点—不同结构”并行（第 4.1–4.2 节、图 6）。
- 2024-06 [AlphaForge](notes/cards/2024_AlphaForge.md)（顺带涉及）：入库同时检查 IC、ICIR 和相关性阈值；生成器损失中的多样性项。
- 2024-02 [RiskMiner](notes/cards/2024_RiskMiner.md)（顺带涉及）：中间奖励中加入与已有因子的 MutIC 重复惩罚。
- 2024-01 [Synergistic RL](notes/cards/2024_SynergisticRL.md)（顺带涉及）：扩大算子与窗口后组合中的因子相关性下降。
- 2023-05 [AlphaGen](notes/cards/2023_AlphaGen.md)（主要针对）：用加入因子池后的组合 IC 边际贡献作为奖励。
- 2023-03 [Sequential Cauchy](notes/cards/2023_SequentialCauchy.md)（顺带涉及）：原领域要处理的是“检验统计量之间相关”造成的控制失效。SCC 的结论是：对依赖结构只要求两两二元正态与相关矩阵特征值有界，极端相关（σ_max 接近 1、块对角等强截面相关）会破坏 Assumption 2.2 的前提，论文将这种情况列为未解决（第 2.3 节脚注 4）。迁移到因子挖掘对应的是：SCC 在中等至强相关下仍然稳健且更省功效，但若候选因子的收益序列几乎是彼此的复制（接近完全相关），SCC 的拒绝集与小样本 Bonferroni 的差距会缩小、功效也会损失；这正好说明去冗余不仅是组合层的需要，也是多重检验校正有效性的前提（推断）。
- 2022-01 [Trajectory Balance](notes/cards/2022_TrajectoryBalance.md)（顺带涉及）：在保持按奖励比例采样的同时改进分布拟合与样本多样性，分子任务中 TB 生成的 top-1000 分子相似度始终低于 FM，比特序列任务中发现模式更快（第 5.2、5.3.1 节）→ 对应用多模式采样缓解因子模式坍缩；已收录的 AlphaSAGE 借用 TB 使采样覆盖多个高奖励公式模式（见 AlphaSAGE 速读卡）。
- 2021-06 [GFlowNet](notes/cards/2021_GFlowNet.md)（主要针对）：以按奖励成比例采样为目标，覆盖奖励函数的多个模式，避免回报最大化收敛到一个或少数几个好样本（第 1–2 节）→ 对应生成器向少数高分模板坍缩、新因子彼此高度相关的问题；已收录的 AlphaSAGE 借用这一目标，使采样分布覆盖多个高奖励公式模式（见 AlphaSAGE 速读卡）。
- 2021-03 [AlphaEvolve](notes/cards/2021_AlphaEvolve.md)（主要针对）：冗余算子与冗余 Alpha 的剪枝和指纹去重，以及对与既有 Alpha 超出相关性阈值者的剔除。
- 2020-02 [AutoAlpha](notes/cards/2020_AutoAlpha.md)（主要针对）：质量-多样性搜索。

<a id="p8"></a>

### P8 挖掘目标与实际使用脱节（主要 15，涉及 13）

- 2026-11 [CosmosAlpha](notes/cards/2026_CosmosAlpha.md)（顺带涉及）：单因子质量里包含方向对齐的 Top-20% 收益（头部暴露组合的远期收益均值），最终池以 LightGBM 组合信号在 TopK-Drop 组合上评价，而不是只看单因子 IC（式 6、附录 B.2、C.5）。
- 2026-10 [FactorBench](notes/cards/2026_FactorBench.md)（主要针对）：把交付的因子池经统一选因子、合成与组合构建，报告扣除交易成本（long–short 另计融券成本）后的 long-only 与 long–short 表现，并做成本、调仓频率和合成方式的敏感性分析。
- 2026-10 [Det-MASO](notes/cards/2026_Det-MASO.md)（顺带涉及）：目标函数含滚动窗口组合 Sharpe 项，把组合层目标纳入训练（式 12）；评估也用 top-decile 多头组合的 AR/SR/MDD。
- 2026-10 [AlphaRLM](notes/cards/2026_AlphaRLM.md)（顺带涉及）：TMB 不比较 IC，而比较池化后的分组收益跨组极差，以容纳非单调的因子—收益关系；论文据此说明 S&P 500 上 AR 为正而 IC、RankIC 接近零的现象——边际预测相关不能完全解释组合表现（第 1 节、第 4.2 节）。线性端点价差（只比第 1 与第 K 组）的对照在 CSI300 上 IC 更高（0.031 对 0.026）但 MDD 明显更大（−15.60% 对 −6.15%）、S&P 500 AR 更低（0.77% 对 6.94%）（表 2、第 4.3 节）。
- 2026-10 [AlphaPilot](notes/cards/2026_AlphaPilot.md)（主要针对）：入池按候选对组合信号的边际贡献决定，不看单因子质量本身，训练奖励也基于组合后的池信号；案例中几个单因子 RankIC 更高的波动调整变体因边际池增益为负被拒（第 4.3 节、第 5.4 节、表 20）。
- 2026-10 [AlphaPADI](notes/cards/2026_AlphaPADI.md)（主要针对）：以完整池为生成和学习对象，奖励直接取联合拟合的 ridge 组合预测表现，而不是单条公式的边际贡献；第 5.4 节据池容量实验指出，池大小的效果应通过组合预测器检验（第 3、5.4 节）。
- 2026-10 [AlphaLedger](notes/cards/2026_AlphaLedger.md)（主要针对）：信用函数直接度量“换入后 Top-K 组合收益的变化再扣替代成本”，库筛选也用这一组合口径而非 IC 峰值；消融中把 EC-OPD 换成 SFT/OPD/PPO/GRPO 后，IC 类指标未必同步下降但 ARR 与 Sharpe 明显更低（Eq. 4、第 3.4 节、Table 4）。
- 2026-09 [GoAnt](notes/cards/2026_GoAnt.md)（主要针对）：论文把 Execution Trap 作为首要诊断：在保守的全价差成本墙下，RankIC 强的因子净收益为负，而只按预测代理选择的系统在搜索期间从不会撞上这堵墙。对应机制是三层分离——搜索适应度只含 deflated 信号质量，换手进入描述子轴，净收益只做事后验证与样本外闸门，外加一组冻结的准入闸门（|RankIC|≥0.01、|t_dsr|≥2.0、正 IC 期占比≥0.52、正日 IC 占比≥0.60、样本内与后段 IC 差≤0.02、平均有效价差≤25 bps、净累计收益>0、毛净保留率>0、净收益最大回撤>−0.50）。arm 7 把入档适应度换成原始净收益后，质量加权产出从 41.8/47.6 跌到 9.9/6.8，distinct 降到 11/8，是全部消融中最差的一档（表 1）。论文同时指出这一分歧在日频量价面板上只是二阶修正、在订单簿数据上才占主导，因此两类数据都跑（第 3 节的 Execution Trap 与 Formulation）。
- 2026-09 [AlphaDiverse](notes/cards/2026_AlphaDiverse.md)（顺带涉及）：保留和奖励都以因子集合加入后 LightGBM 预测得分的增益衡量，多样性也在“对模型预测的改变量”空间中度量，不只看单因子指标（第 2.1 节、第 2.3 节、附录 D.6）。
- 2026-08 [AutoScientist-Quant](notes/cards/2026_AutoScientist-Quant.md)（主要针对）：论文指出自动化通常止于因子生成，因子库被直接交给一个固定预测器、没有组合层面的选择与模型搜索；本文用同一控制器依次做 alpha 筛选与模型搜索，目标函数是带成本的组合指标而非 IC；主表中所有 agentic 基线 IC 在 0.023–0.034 但扣费超额收益多为负，本文是唯一在四种 alpha 设置下均为正的方法（第 1.2 节、第 2.3–2.4 节、表 1）。
- 2026-08 [AlphaSeek](notes/cards/2026_AlphaSeek.md)（主要针对）：把“方向—挖掘—组合回测”接成闭环，新因子在冗余约束下与已有 SOTA 因子库交互，组合层直接在 ARR/IR/MDD/CR 的加权目标上迭代，并按历史收益的条件期望在权重与模型配置两个方向间分配搜索（第 3.2 节，式 12–15）。
- 2026-07 [MAPLE](notes/cards/2026_MAPLE.md)（顺带涉及）：极端秩加权损失把学习信号集中在只做多 top-k 组合实际使用的头部排名，相关惩罚取绝对值的理由也来自只做多约束；各 Alpha 先各自成组合再等权聚合（第 3.2–3.3 节、附录 A.4）。
- 2026-05 [PRISM-VQ](notes/cards/2026_PRISM-VQ.md)（顺带涉及）：以 TopK–DropN（K=30、N=5）组合而非仅 IC 评价，组合收益按买入 5 bp、卖出 15 bp 计交易成本，并额外扫描 2/3 bp 至 20/40 bp 六档成本与不同 N_drop，报告换手（N 从 1 增至 15 时日均换手放大约 14 倍，N≥10 后边际收益被 20–50 bp 往返成本抵消）（第 5.1 节、附录 D–F）。
- 2026-04 [MarketSenseAI](notes/cards/2026_MarketSenseAI.md)（顺带涉及）：评价直接落在组合层面而非单因子 IC：等权强买组合对等权基准与 ETF（RSP、EQWL）比较复合收益，并对月度组合收益做 Jensen 回归与上下行分解，用以排除“只是买了高 beta”的解释——β̂=0.865、α̂=+1.18%/月（t=1.45，p=0.17），下行月超额（+1.31%）反而高于上行月（+0.82%）（第 6 节、图 10）。论文据此把强买信号定位为上游的“股票池过滤器”，可接在任意的组合构建方法之前，而不是一个逐日 alpha 预测（第 6 节）。迁移点：原领域论证的是“选股信号应以组合层增益而非单票评级高低来评价” → 迁移到因子挖掘，对应单因子 IC 与组合增益脱节的检验方式，即把信号当准入过滤再交给既有组合器；已收录工作中 FactorBench 与 Det-MASO 也从组合层评价因子池。
- 2026-03 [Hubble](notes/cards/2026_Hubble.md)（顺带涉及）：把换手率纳入候选评分。
- 2026-03 [AgenticFactorInvesting](notes/cards/2026_AgenticFactorInvesting.md)（主要针对）：选股目标是“在严格控制换手与交易成本下最大化风险调整收益”（第 1 节）；闸门与记忆对高换手、快速衰减的候选施加惩罚（第 6.3 节），因子库最终以线性和 LightGBM 两种方式聚合为可交易组合，并在 3 bps 单边成本下报告净表现（第 5.2、7.2–7.3 节）。
- 2026-02 [AlphaPROBE](notes/cards/2026_AlphaPROBE.md)（顺带涉及）：组合阶段用动态因子整合器形成每日信号，回测计入交易成本。
- 2025-12 [Alpha-R1](notes/cards/2025_Alpha-R1.md)（主要针对）：用 LLM 推理决定因子启停。
- 2025-08 [AlphaEval](notes/cards/2025_AlphaEval.md)（顺带涉及）：以相对秩熵 RRE 度量相邻期排序稳定性，并验证其与年化换手显著负相关，作为可交易性的免回测代理。
- 2025-07 [EFS](notes/cards/2025_EFS.md)（主要针对）：稀疏组合选股。
- 2025-05 [RD-Agent(Q)](notes/cards/2025_RD-Agent-Quant.md)（主要针对）：因子与模型联合优化。
- 2025-05 [Alpha-Jungle](notes/cards/2025_Alpha-Jungle.md)（顺带涉及）：把换手率纳入候选评分。
- 2025 [AlphaGAT](notes/cards/2025_AlphaGAT.md)（主要针对）：GAT-PPO 学习动态权重。
- 2024-09 [LLM Strategy Finding](notes/cards/2024_LLMStrategyFinding.md)（主要针对）：动态优化因子权重。
- 2024-06 [AlphaForge](notes/cards/2024_AlphaForge.md)（主要针对）：挖掘阶段扩大候选池，使用阶段再按近期表现动态选因子、动态加权。
- 2024-02 [RiskMiner](notes/cards/2024_RiskMiner.md)（顺带涉及）：终端奖励取加入因子后因子池组合 IC 的变化。
- 2024-02 [Alpha-GPT 2.0](notes/cards/2024_Alpha-GPT2.md)（顺带涉及）：新增组合构建与交易清单的风险过滤。
- 2023-05 [AlphaGen](notes/cards/2023_AlphaGen.md)（主要针对）：组合 IC 边际贡献作为奖励。

<a id="p9"></a>

### P9 非平稳与因子衰减（主要 9，涉及 4）

- 2026-10 [Det-MASO](notes/cards/2026_Det-MASO.md)（主要针对）：由市场状态聚类确定 agent 数并把 agent 与 regime 一一绑定（式 4、14），context-conditioned 调度器按当前市场状态重分配生成能力，无需推理期 regime 标签（第 3.2.4 节）。
- 2026-10 [AlphaPilot](notes/cards/2026_AlphaPilot.md)（主要针对）：推理时逐日按当日 regime 描述重新搜索、更新保留池，信号集随市场状态变化（第 1 节、第 4 节、第 5.1 节）。
- 2026-10 [AlphaLedger](notes/cards/2026_AlphaLedger.md)（主要针对）：RRG 只读取“信号日后 h_g 日收益已到期”的记录，按当日市场状态匹配后向全样本均值收缩，并保证每个因子至少保留等权份额的 (1−α) 部分；EviPool 每 10 个池日按滞后证据重新进出，使资格集随市场证据变化（第 3.2、3.5 节、Eq. 8–9、图 4）。
- 2026-08 [AlphaSeek](notes/cards/2026_AlphaSeek.md)（顺带涉及）：第 1 节以 McLean–Pontiff 的“因子公开后收益衰减”为动机，方向生成阶段持续抓取最新论文与新闻，使研究选题随文献更新；训练/验证/测试按时间切分，测试区间延伸到 2025-12（第 1 节、第 4.1 节）。论文未直接度量衰减，属机制层面的对应。
- 2026-07 [X-Alpha](notes/cards/2026_X-Alpha.md)（主要针对）：系统被设计为持续研究而非一次性挖掘，每周期依据上一周期的真实结果改写研究主题与搜索空间，记忆随时间累积并使探索行为随之改变（论文明确“self-evolution 指记忆与研究行为的反馈驱动更新，不改变底层 LLM 参数”，第 1 节）；评价端用扩张历史、每 128 个交易日重拟合、h+1 日 embargo 的滚动协议（第 4.1 节、附录 J）。
- 2026-05 [PRISM-VQ](notes/cards/2026_PRISM-VQ.md)（主要针对）：阶段二以离散码作为路由条件，让不同专家在时间维度上专精不同市场状态，从而生成随截面结构变化的动态载荷；图 6 显示 S&P 500 上专家激活显著异质（8 个专家两两共 28 组 Wilcoxon 符号秩检验全部 p<0.001，专家 2 均值约 7.09%、专家 6 约 16.46%），激活尖峰的 Jaccard 重叠仅 6.8%，低于 8.11% 的基准，说明专家并非同步响应（第 5.6 节）。论文还报告最优点专家数随市场不同（CSI 300 为 M_e=2，S&P 500 为 M_e=8），并认为更有效的市场更需要专家分工（第 5.4 节）。
- 2026-03 [Hubble](notes/cards/2026_Hubble.md)（顺带涉及）：负向检索提示应避开的拥挤模板。
- 2026-03 [AlphaLogics](notes/cards/2026_AlphaLogics.md)（顺带涉及）：论文以“跨周期稳健”为动机，把市场逻辑当作可复用资产而非一次性产物：同一逻辑跨多轮复用并持续吸收反馈，持久设置下 IC 从第 1 轮的 0.0199 升至第 5 轮的 0.0232、ICIR 从 0.1792 升至 0.2137，而每轮即弃的瞬时逻辑 IC 从 0.0182 降至 0.0165、ICIR 从 0.1776 降至 0.1320（第 4.6 节，表 3）。该机制针对的是“逻辑被充分探索前就换方向”造成的浪费，未直接度量因子随时间或拥挤而衰减（据原文）。
- 2025-12 [Alpha-R1](notes/cards/2025_Alpha-R1.md)（主要针对）：根据市场状态推理因子启停。
- 2025-02 [AlphaAgent](notes/cards/2025_AlphaAgent.md)（主要针对）：把原创性约束写入生成目标以对抗衰减。
- 2024-09 [QFR](notes/cards/2024_QFR.md)（主要针对）：奖励中加入信息比率，抑制 IC 随时间的剧烈波动。
- 2024-06 [AlphaForge](notes/cards/2024_AlphaForge.md)（主要针对）：滚动窗口动态选因子。
- 2022-09 [Publication Bias](notes/cards/2022_PublicationBias.md)（顺带涉及）：原领域要回答“样本外变弱是发表偏差还是市场变了”。论文用收益自相关的时限作识别：由于月度因子收益 3 个月后自相关归零，发表偏差应在样本结束后的数月内显现，因此 3 年处的 25% 衰减是偏差的上界（Fact #2），而 10 年处的 50% 衰减中只有约 12 个百分点可由偏差解释，剩下约 38 个百分点是期望收益的真实变化，且与原文多以“错误定价”解释其发现相一致（第 4.2 节、图 9）。迁移到因子挖掘对应的是：给“因子上线后衰减”做归因时，用短窗口（与标签期同量级）衡量选择偏差、用长窗口衡量拥挤与定价修正，而不是把全部衰减都记在过拟合账上，也不是反过来把拥挤当成挖掘失败。

<a id="p10"></a>

### P10 评估口径不统一、难以复现（主要 6，涉及 7）

- 2026-10 [QBX](notes/cards/2026_QBX.md)（主要针对）：携带证据的 IR、内容身份与试验账本统一留痕，并把多种挖掘器的适配器接入同一评估器、去重漏斗和选择协议。
- 2026-10 [FactorBench](notes/cards/2026_FactorBench.md)（主要针对）：共享数据、目标、切分与执行契约，用适配器接入各方法的官方实现，逐次记录上游提交、配置、预算、耗时与交付因子。
- 2026-10 [EvoQuantLab](notes/cards/2026_EvoQuantLab.md)（顺带涉及）：协议版本、内容哈希与追加式记录固定研究条件和补丁生效边界（原文附录 A、F）。
- 2026-10 [Auditing LLM Alpha-Factor Mining](notes/cards/2026_AuditingLLMAlpha.md)（主要针对）：逐项核对汇总指标所对应的统计总体与计数阶段，按全量队列记账并保留不可评分记录，公开实现的修正以版本化方式全部重算。
- 2026-09 [GoAnt](notes/cards/2026_GoAnt.md)（顺带涉及）：定义了一个与地图无关的 effective-yield 协议——所有臂只从各自的评价记录中读取结果，候选须越过同一个预注册下限 q*=随机基因组合分布的 95 分位（在任何臂运行前校准并冻结），多样性固定在一个方法无关的四因子家族 × 五换手分箱网格上统计（ρ=0.7，附录另给 0.3/0.5/0.9 全扫），使有存档与无存档的系统用同一把尺子；静态对照用“运行结束时的不变量断言”定义（中心、细胞数、边界、合并/分裂/重拟合、缩放器重估全部为 0，违反即中止），并公开断言表；批注也承认自己一度把“关闭重绘 tick”误当成让地图更静态，结果那个臂看起来最好，这一自我报告增强了协议的可信度（附录 A、B、表 S1）。
- 2026-08 [AutoScientist-Quant](notes/cards/2026_AutoScientist-Quant.md)（顺带涉及）：指出前作评估代码的两处前视缺陷并给出修正，使所有方法在同一修正管线、同一切分、同一成本假设下重跑；并明确排除 R&D-Agent-Quant 作为基线，理由是它的循环在它所报告的那一段上选因子（第 1.2–1.3 节、第 3.3 节）。
- 2026-08 [AgonAlpha](notes/cards/2026_AgonAlpha.md)（主要针对）：论文的出发点之一是 30 篇 LLM 交易论文的审计结论——时点数据控制、训练测试切分、样本外评价、交易成本、换手与工件可得性普遍报告不足；对应做法是把评测交给一个作者无法修改的外部平台（数据、模拟器、闸门、评级与提交约束都由平台控制），并公开提示词、每次搜索决策、平台记录、审稿文本与逐条可执行 FASTEXPR（第 1、5.1、5.5 节）。作者声称 60 次提交的提示词到因子的完整轨迹全部释放（第 5.5 节、补充材料）。
- 2026-03 [Hubble](notes/cards/2026_Hubble.md)（主要针对）：持久化保存每个候选的多维诊断和提示词元数据。
- 2026-03 [AlphaLogics](notes/cards/2026_AlphaLogics.md)（顺带涉及）：所有基线共享股票池、时间切分、OHLCV 输入、top-outside 规则与成本模型，并输出逐日截面分数（因子方法为基准因子加生成因子上的 LightGBM，深度基线为模型预测），使差异只来自信号构造；agent 与 LLM 基线的试验数、演化轮次、每轮候选上限对齐（第 4.1 节）。
- 2026-02 [FactorMiner](notes/cards/2026_FactorMiner.md)（顺带涉及）：技能模块中封装标准化评估协议。
- 2025-08 [AlphaEval](notes/cards/2025_AlphaEval.md)（主要针对）：在同一平台、同一数据切分下用统一的多维指标评测八个挖掘模型，并开源实现与评估工具。
- 2023-03 [Sequential Cauchy](notes/cards/2023_SequentialCauchy.md)（顺带涉及）：方法只需要原始 p 值、不需要重采样与参数假设，实现只有排序、tan 变换、后缀累加三步，且不随样本变化重估阈值；论文把这条性质作为相对重采样方案（Christensen et al. 2022 的 AR(1) 模拟临界值）的实际优势提出——后者要为每条序列单独生成临界值、计算量大、且依赖可能被设定错误的依赖结构（第 4.1 节）。迁移到因子挖掘对应的是：多重检验校正若要成为论文的固定披露项，需要一个几乎零成本、不引入额外建模假设的算法，SCC 满足这一条。
- 2022-09 [Publication Bias](notes/cards/2022_PublicationBias.md)（顺带涉及）：原领域用统一的复现语料把“原文报告值”与“独立复现值”对齐（207 个因子来自 140 篇论文，手抄原始 t 值与复现 t 值逐点比较，数据与代码公开并在每年更新时修错），并把“复现失败”严格定义为可复现的实现下不显著，从而把口径差异从结论差异里剥离出来（第 2.1 节、第 4.4.2 节）。迁移到因子挖掘对应的是：同一方法在不同论文中作为基线出现时，需要先固定标签、切分、股票池与组合构造，再比较 IC 或收益，否则“复现不出来”很可能只是口径不同；本仓库《评估口径对照》专题处理的正是这件事。

<a id="setups"></a>

## 3. 实验口径

各篇速读卡“证据”一节的摘要，逐项核对自论文原文；口径差异的比较见[评估口径](topics/evaluation_protocol.md)。

“未说明”表示论文没有给出该项。`markets` 为“不适用”的是方法类论文，实验对象不是股票因子挖掘。

### 4.1 市场、股票池与频率

| 工作 | 市场 / 股票池 | 频率 |
| --- | --- | --- |
| [Auditing LLM Alpha-Factor Mining](notes/cards/2026_AuditingLLMAlpha.md) | A 股 40 只股票（BaoStock 便利样本） | 日频 |
| [AlphaEval](notes/cards/2025_AlphaEval.md) | A 股（Qlib）、S&P 500 | 日频 |
| [GoAnt](notes/cards/2026_GoAnt.md) | A 股（价格—成交量面板与订单簿 L2 快照，标的数与股票池未披露） | 日频（PV）与订单簿 L2 快照（快照频率未披露） |
| [Look-Ahead-Bench](notes/cards/2026_Look-Ahead-Bench.md) | AAPL、MSFT、GOOGL、NVDA、TSLA（五只美股大盘科技股） | 日频（月度调仓） |
| [Agora/SJS](notes/cards/2026_Agora-SJS.md) | CSI1000 | 日频 |
| [Synergistic RL](notes/cards/2024_SynergisticRL.md) | CSI300 | 日频 |
| [Alpha-Jungle](notes/cards/2025_Alpha-Jungle.md) | CSI300、CSI1000 | 日频 |
| [AlphaRLM](notes/cards/2026_AlphaRLM.md) | CSI300、CSI1000、S&P 500 | 日频 |
| [AlphaGen](notes/cards/2023_AlphaGen.md) | CSI300、CSI500 | 日频 |
| [RiskMiner](notes/cards/2024_RiskMiner.md) | CSI300、CSI500 | 日频 |
| [Alpha2](notes/cards/2024_Alpha2.md) | CSI300、CSI500 | 日频 |
| [AlphaForge](notes/cards/2024_AlphaForge.md) | CSI300、CSI500 | 日频 |
| [FactorEngine](notes/cards/2026_FactorEngine.md) | CSI300、CSI500 | 日频 |
| [AlphaPilot](notes/cards/2026_AlphaPilot.md) | CSI300、CSI500 | 日频 |
| [AlphaPROBE](notes/cards/2026_AlphaPROBE.md) | CSI300、CSI500、CSI1000 | 日频 |
| [AlphaG-OPD](notes/cards/2026_AlphaG-OPD.md) | CSI300、CSI500、CSI1000、S&P 500 | 日频 |
| [AlphaSAGE](notes/cards/2025_AlphaSAGE.md) | CSI300、CSI500、CSI1000、S&P500 | 日频 |
| [X-Alpha](notes/cards/2026_X-Alpha.md) | CSI300、CSI500、CSI1000、S&P500、HSI90 | 日频 |
| [QFR](notes/cards/2024_QFR.md) | CSI300、CSI500、CSI1000、SPX、DJI、NDX | 日频 |
| [TLRS](notes/cards/2025_TLRS.md) | CSI300、CSI500、CSI1000、SPX、DJI、NDX | 日频 |
| [AlphaDiverse](notes/cards/2026_AlphaDiverse.md) | CSI300、CSI500、CSI1000、沪深 A 股全市场 | 日频、分钟级 |
| [AutoScientist-Quant](notes/cards/2026_AutoScientist-Quant.md) | CSI300、CSI500、CSI800、CSI1000、S&P500、NASDAQ100 | 日频 |
| [AlphaRJM](notes/cards/2026_AlphaRJM.md) | CSI300、CSI500、CSI800（CSI1000 为附录补充） | 日频 |
| [RD-Agent(Q)](notes/cards/2025_RD-Agent-Quant.md) | CSI300、CSI500、NASDAQ100 | 日频 |
| [MAPLE](notes/cards/2026_MAPLE.md) | CSI300、CSI500、NI225、SP500 | 日频 |
| [AlphaPADI](notes/cards/2026_AlphaPADI.md) | CSI300、CSI500、S&P500 | 日频 |
| [TreEvo](notes/cards/2025_TreEvo.md) | CSI300、CSI500、SPX、NDX | 日频 |
| [AlphaQCM](notes/cards/2025_AlphaQCM.md) | CSI300、CSI500、沪深全市场（Market）；附录另测 S&P 500 | 未说明 |
| [CosmosAlpha](notes/cards/2026_CosmosAlpha.md) | CSI300、CSI500（时点成分） | 日频 |
| [AlphaPareto](notes/cards/2026_AlphaPareto.md) | CSI300、CSI800、全市场（附录另测 S&P 500） | 日频 |
| [AlphaCFG](notes/cards/2026_AlphaCFG.md) | CSI300、S&P500 | 日频 |
| [Det-MASO](notes/cards/2026_Det-MASO.md) | CSI300、S&P500 | 日频 |
| [PRISM-VQ](notes/cards/2026_PRISM-VQ.md) | CSI300、S&P500（当期成分） | 日频 |
| [CogAlpha](notes/cards/2025_CogAlpha.md) | CSI300（主）、CSI500、S&P500、HSI、HSCI | 日频 |
| [AlphaSchema](notes/cards/2026_AlphaSchema.md) | CSI300（主）、CSI500（附录） | 日频 |
| [QuantaAlpha](notes/cards/2026_QuantaAlpha.md) | CSI300（另在 CSI500、S&P 500 做零样本迁移） | 日频 |
| [AutoAlpha](notes/cards/2020_AutoAlpha.md) | CSI300（挖掘）、CSI800（回测） | 日频 |
| [AlphaSeek](notes/cards/2026_AlphaSeek.md) | CSI300（零样本迁移 CSI500） | 日频 |
| [FactorMiner](notes/cards/2026_FactorMiner.md) | CSI500、CSI1000、CSI300、Binance 64 个加密资产 | 10 分钟 |
| [AlphaAgent](notes/cards/2025_AlphaAgent.md) | CSI500、S&P 500 | 日频 |
| [EvoQuantLab](notes/cards/2026_EvoQuantLab.md) | CSI500、S&P 500、Crypto（数字资产） | 日频（权益）；小时频（Crypto） |
| [AlphaLogics](notes/cards/2026_AlphaLogics.md) | CSI500、S&P500 | 日频 |
| [LineageEvo](notes/cards/2026_LineageEvo.md) | CSI500、S&P500 | 日频 |
| [AlphaMemo](notes/cards/2026_AlphaMemo.md) | CSI500、S&P500（Qlib） | 日频 |
| [QBX](notes/cards/2026_QBX.md) | CSI500（主）、CSI300；机制实验用 AAPL | 日频（面板）；1 小时（AAPL 机制实验） |
| [AlphaLedger](notes/cards/2026_AlphaLedger.md) | CSI500（统一账户比较）；EviPool 动态池（A 股全市场）；另列 CSI300、CSI1000 指数池 | 日频 |
| [AlphaGAT](notes/cards/2025_AlphaGAT.md) | DJIA、HSI、CSI100、CRYPTO | 未说明 |
| [EFS](notes/cards/2025_EFS.md) | FF25、FF32、FF49、FF100（Fama-French 组合）；US50、HSI45、CSI300 | 月度（FF）；日频（US50、HSI45、CSI300） |
| [HRFT/IRFT](notes/cards/2024_HRFT.md) | HS300、S&P500 | 1 分钟 |
| [AlphaEvolve](notes/cards/2021_AlphaEvolve.md) | NASDAQ（筛选后 1026 只） | 日频 |
| [Hubble](notes/cards/2026_Hubble.md) | S&P 500（501 只） | 日频 |
| [TextToAlpha](notes/cards/2025_TextToAlpha.md) | S&P100 | 季度披露 × 月度收益 |
| [FactorBench](notes/cards/2026_FactorBench.md) | S&P100、恒生指数、CSI300、FTSE100、Nikkei225 | 日频 |
| [Alpha-R1](notes/cards/2025_Alpha-R1.md) | S&P500、CSI300（另有 Russell2000、CSI1000 泛化检验） | 日频 |
| [MarketSenseAI](notes/cards/2026_MarketSenseAI.md) | S&P500（467 只固定队列）、S&P100（94 只固定队列） | 日频数据、月度观察与调仓 |
| [LLM Strategy Finding](notes/cards/2024_LLMStrategyFinding.md) | SSE50、CSI300、S&P500 | 日频 |
| [AgonAlpha](notes/cards/2026_AgonAlpha.md) | U.S. TOP3000（WorldQuant BRAIN，delay one） | 日频 |
| [Alpha101](notes/cards/2016_Alpha101.md) | WorldQuant 自有数据，股票池未公开（论文未披露具体市场与股票范围） | 日频 |
| [Trajectory Balance](notes/cards/2022_TrajectoryBalance.md) | 未说明 | 未说明 |
| [Alpha-GPT 2.0](notes/cards/2024_Alpha-GPT2.md) | 未说明 | 未说明 |
| [Tree-GRPO](notes/cards/2025_Tree-GRPO.md) | 不适用（11 个单跳/多跳问答与网页智能体数据集） | 不适用 |
| [DeepMind AlphaEvolve](notes/cards/2025_DeepMind-AlphaEvolve.md) | 不适用（数学构造问题、矩阵乘法算法、Google 计算栈工程任务） | 不适用 |
| [QuantAgent](notes/cards/2024_QuantAgent.md) | 中国 A 股 500 只股票 | 日频 |
| [Warm Start GP](notes/cards/2024_WarmStartGP.md) | 中国 A 股全市场 | 日频 |
| [Alpha-GPT](notes/cards/2023_Alpha-GPT.md) | 中国与美国股票的日内量价数据（未给出具体股票池） | 日内 |
| [QuantEvolver](notes/cards/2026_QuantEvolver.md) | 单资产 5 分钟方向预测（Benchmark A）、数字资产小时频截面（Benchmark B）、CSI300 ETF 成分股（Benchmark Γ） | 5 分钟、小时频、日频 |
| [AgenticFactorInvesting](notes/cards/2026_AgenticFactorInvesting.md) | 美股 CRSP（NYSE/AMEX/NASDAQ 普通股） | 日频 |
| [CAVB](notes/cards/2025_CAVB.md) | 美股 NYSE、AMEX、NASDAQ；流动性筛选后的逐期股票数未披露 | 月频 |
| [Publication Bias](notes/cards/2022_PublicationBias.md) | 美股（207 个截面预测因子） | 月频 |
| [Sequential Cauchy](notes/cards/2023_SequentialCauchy.md) | 美股（Kenneth French 100 个组合）；另 Nasdaq 与 S&P500 ETF 高频 | 月频；另 1 分钟 |
| [GiGPO](notes/cards/2025_GiGPO.md) | 非金融：ALFWorld、WebShop、搜索增强问答（NQ、TriviaQA、PopQA、HotpotQA 等） | 未说明 |
| [DSR](notes/cards/2019_DSR.md) | 非金融：Nguyen 符号回归基准（12 个表达式） | 未说明 |
| [GFlowNet](notes/cards/2021_GFlowNet.md) | 非金融：超网格合成任务、分子生成 | 未说明 |

### 4.2 样本外区间、标签与交易成本

| 工作 | 样本外区间 | 标签与持有期 | 交易成本 |
| --- | --- | --- | --- |
| [Auditing LLM Alpha-Factor Mining](notes/cards/2026_AuditingLLMAlpha.md) | 2024 至 2025 | 5 日收益（复权收盘价 5 日变化） | 未说明 |
| [AlphaEval](notes/cards/2025_AlphaEval.md) | A 股 2021-01-01 至 2024-12-31；S&P 500 2017-01-01 至 2020-12-31 | ΔT 日远期收益（未指定时 ΔT=1，即次日收益） | 未说明 |
| [GoAnt](notes/cards/2026_GoAnt.md) | 开发窗口与更晚的锁定窗口，仅给数据区间 2023 至 2026，起止日期未披露 | 未来收益作为 RankIC 的标签（收益期限未披露）；另有执行感知净收益 | 有分类别的成本模型但未披露费率公式，仅给准入门限平均有效价差 ≤25 bps |
| [Look-Ahead-Bench](notes/cards/2026_Look-Ahead-Bench.md) | 第一期 2021-04-01 至 2021-09-30；第二期 2024-07-01 至 2024-12-31 | 五只股票的目标权重（组合收益），持有 1 个月 | 未说明 |
| [Agora/SJS](notes/cards/2026_Agora-SJS.md) | 2020-01 至 2025-12（测试段）；2026-01 至 2026-05（密封 holdout） | 5 日开盘到开盘收益 | 单边 9 bps（双边 0.04% 佣金 + 0.05% 印花税） |
| [Synergistic RL](notes/cards/2024_SynergisticRL.md) | 2020-01-01 至 2021-12-31 | 20 日收益 | 未说明 |
| [Alpha-Jungle](notes/cards/2025_Alpha-Jungle.md) | 2021-01-01 至 2024-11-30 | 10 日与 30 日收益 | 每笔 0.15% |
| [AlphaRLM](notes/cards/2026_AlphaRLM.md) | 2021-01-01 至 2024-12-30 | 次日收益 | 开仓 0.05%、平仓 0.15%，最低 5 元 |
| [AlphaGen](notes/cards/2023_AlphaGen.md) | 2020-01-01 至 2021-12-31 | 20 日收益（Ref(close,-20)/close-1，按收盘价买卖） | 未说明 |
| [RiskMiner](notes/cards/2024_RiskMiner.md) | 2021-01-01 至 2022-12-31 | 5 日与 10 日收益 | 未说明 |
| [Alpha2](notes/cards/2024_Alpha2.md) | 2021-01-01 至 2023-12-31 | 20 日收益 | 未说明 |
| [AlphaForge](notes/cards/2024_AlphaForge.md) | 2018 至 2022，逐年测试并年度重训 | Ref(VWAP,-21)/Ref(VWAP,-1)-1（约 20 日 VWAP 收益） | 每日最多换 5 只（论文未给费率） |
| [FactorEngine](notes/cards/2026_FactorEngine.md) | 2017-01-01 至 2024-12-31 | 1、3、5、10 日远期收益（多滞后评价） | 佣金双边 1.5×10⁻⁴、卖出印花税 5×10⁻⁴、滑点 8×10⁻⁴ |
| [AlphaPilot](notes/cards/2026_AlphaPilot.md) | 2025-07-11 至 2026-03-02（逐日推理） | 次日收益（IC/RankIC 用次日收益；训练奖励用 21 日与 63 日未来窗口） | 10 bps |
| [AlphaPROBE](notes/cards/2026_AlphaPROBE.md) | 2022-07-01 至 2025-06-30 | 20 日远期收益 | 往返 0.1% |
| [AlphaG-OPD](notes/cards/2026_AlphaG-OPD.md) | 中国 2022 至 2024；S&P 500 2018 至 2020 | 20 个交易日远期收益 Ref(close,-20)/close-1 | 未说明 |
| [AlphaSAGE](notes/cards/2025_AlphaSAGE.md) | 中国市场 2022-01-01 至 2024-12-31；美国市场 2018-01-01 至 2020-12-31 | 未说明 | 未说明 |
| [X-Alpha](notes/cards/2026_X-Alpha.md) | 2022-01-01 至 2025-12-31 | 10 日与 30 日开盘到开盘收益 | 买入 0.026%、卖出 0.076%（含 0.05% 印花税）、每单最低 5 元 |
| [QFR](notes/cards/2024_QFR.md) | 2021-01-01 至 2024-01-01 | 5 日收益 | 未说明 |
| [TLRS](notes/cards/2025_TLRS.md) | 2021-01-01 至 2024-01-01 | 未来 5 日收益 | 未说明 |
| [AlphaDiverse](notes/cards/2026_AlphaDiverse.md) | 2026-01 至 2026-08（外层，只评估一次；内层 2022-05 至 2025-12） | t+1 开盘至 t+2 开盘的超额收益 | 回测收益不扣交易成本（毛收益） |
| [AutoScientist-Quant](notes/cards/2026_AutoScientist-Quant.md) | 2023-06 至 2026-05 | 未说明 | 未说明 |
| [AlphaRJM](notes/cards/2026_AlphaRJM.md) | 2022-01-01 至 2024-12-31 | 20 日收益（h=20；另有 h=42 长周期） | 未说明 |
| [RD-Agent(Q)](notes/cards/2025_RD-Agent-Quant.md) | CSI300 2017-01-01 至 2020-08-01；CSI500 与 NASDAQ100 2024-01-01 至 2025-06-30 | 次日收益 | 买入 0.05%、卖出 0.15%、每笔最低 5 元 |
| [MAPLE](notes/cards/2026_MAPLE.md) | 2021 至 2024 | 5 日收益 | CSI300、CSI500 买入约 0.006%、卖出约 0.056%；NI225 双边 0.002%；SP500 约 0（附录 C.1 情景） |
| [AlphaPADI](notes/cards/2026_AlphaPADI.md) | 2023-01-01 至 2025-12-31 | 20 日收益 | 买入 0.05%（c_buy=0.0005）、卖出 0.15%（c_sell=0.0015） |
| [TreEvo](notes/cards/2025_TreEvo.md) | 2021-01-01 至 2024-01-01 | 5 日收益 | 未说明 |
| [AlphaQCM](notes/cards/2025_AlphaQCM.md) | 2021-01-01 至 2022-12-31 | 20 日未来收益 | 未说明 |
| [CosmosAlpha](notes/cards/2026_CosmosAlpha.md) | 2021-01-01 至 2025-12-31 | 次一交易日收盘对收盘收益 | 未说明 |
| [AlphaPareto](notes/cards/2026_AlphaPareto.md) | 2024-07-01 至 2025-06-30 | 20 日收益 | 单边 15 bp、最低 5 元（全市场月度调仓回测） |
| [AlphaCFG](notes/cards/2026_AlphaCFG.md) | 2021-01-01 至 2024-12-31（2020 年数据按设计剔除） | 20 日远期收益（Ref(close,-20)/close-1） | 未说明 |
| [Det-MASO](notes/cards/2026_Det-MASO.md) | 2024-03-01 至 2026-03-01 | 20 个交易日远期收益 | 未说明 |
| [PRISM-VQ](notes/cards/2026_PRISM-VQ.md) | 2022 至 2024（训练 2009–2019，验证 2020–2021） | 5 日远期收益（t+1 开盘至 t+5 收盘） | 买入 5 bp、卖出 15 bp（附录另扫六档） |
| [CogAlpha](notes/cards/2025_CogAlpha.md) | CSI300、CSI500 2021-01-01 至 2024-12-01；S&P500 2016-01-01 至 2020-12-01；HSI、HSCI 2021-01-01 至 2025-12-01 | 10 日收益（另用 30 日收益） | 开仓 0.05%、平仓 0.15%，最低 5 元 |
| [AlphaSchema](notes/cards/2026_AlphaSchema.md) | 2023-01-01 至 2025-12-31 | 5 日前向 close-to-close 收益 | 买入 0.05%、卖出 0.15%，单笔最低 5，次日开盘成交，开启涨跌停过滤 |
| [QuantaAlpha](notes/cards/2026_QuantaAlpha.md) | 2022-01-01 至 2025-12-26 | 次日收益 y_t = P_{t+2}/P_{t+1} - 1 | 买入 0.05%、卖出 0.15% |
| [AutoAlpha](notes/cards/2020_AutoAlpha.md) | 2017-09-01 至 2019-07-31 | 1 日与 5 日收益 | 0.3%（未区分买卖） |
| [AlphaSeek](notes/cards/2026_AlphaSeek.md) | 2022-01-01 至 2025-12-26 | 次一交易日收益 | 未说明 |
| [FactorMiner](notes/cards/2026_FactorMiner.md) | 2025 年（训练 2024-Q1 至 2024-Q4） | 同频非重叠的下一步收益比（10 分钟） | 未说明 |
| [AlphaAgent](notes/cards/2025_AlphaAgent.md) | 2021-01 至 2024-12 | 次日收益 | CSI500 买入万 5、卖出万 15；S&P 500 仅卖出万 5 |
| [EvoQuantLab](notes/cards/2026_EvoQuantLab.md) | CSI500 2026-05-06 至 2026-08-17；S&P500 2026-05-01 至 2026-08-14；Crypto 2026-04-01 至 2026-06-09 | 次日截面收益（Crypto 为下一小时截面收益） | 权益回测为扣费前毛收益；Crypto 单边 5 bps，不含永续资金费 |
| [AlphaLogics](notes/cards/2026_AlphaLogics.md) | 2021-01 至 2024-12 | 次一交易日收益 | CSI500 买 0.0005、卖 0.0015；S&P500 仅卖 0.0005 |
| [LineageEvo](notes/cards/2026_LineageEvo.md) | 2022-05-01 至 2026-04-30 | Ref($close,-2)/Ref($close,-1)-1（次一交易日收益） | 买入 0.15%、卖出 0.25%，单笔最低 5（Qlib 默认） |
| [AlphaMemo](notes/cards/2026_AlphaMemo.md) | 2022-01 至 2025-12-26（验证 2021） | 20 日远期收益 | 未说明 |
| [QBX](notes/cards/2026_QBX.md) | 2022-07 起（扩展数据至 2026-05） | 20 日远期收益 | 未说明 |
| [AlphaLedger](notes/cards/2026_AlphaLedger.md) | 2025-01-02 至 2026-07-31 | 20 日远期收益 | 买入 5 bps、卖出 15 bps |
| [AlphaGAT](notes/cards/2025_AlphaGAT.md) | 股票市场 2022-01 至 2023-06；CRYPTO 2023-09 至 2024-04 | 资产价格变动真值 y_t（论文未给收益公式与预测期限） | 交易费率 0.25% |
| [EFS](notes/cards/2025_EFS.md) | FF 1971-07 至 2023-05；US50 2019-01 至 2025-12；HSI45 2022-01 至 2025-03；CSI300 2022-01 至 2025-05 | 下一期收益（FF 为下月、日频市场池为次日），按 RankIC 评价 | 10 bp 单次交易（附录另做 0/5/10/20 bp 敏感性） |
| [HRFT/IRFT](notes/cards/2024_HRFT.md) | S&P500 2023-10-31 至 2023-12-29；HS300 2023-08-31 至 2023-10-31 | 一日远期已实现波动率 RV | 未说明 |
| [AlphaEvolve](notes/cards/2021_AlphaEvolve.md) | 2013 至 2017 年按 988/116/116 天切分，测试为最后 116 个交易日（未给具体日期） | 次日收益（(今日收盘价−昨日收盘价)/昨日收盘价） | 未说明 |
| [Hubble](notes/cards/2026_Hubble.md) | 2025-06-01 至 2026-03-13（发现期 2022-01-01 至 2025-05-31） | 前向 h 期收益（论文未给出 h 的具体取值） | 未说明 |
| [TextToAlpha](notes/cards/2025_TextToAlpha.md) | 2010-01 至 2024-12（全样本，无样本外切分） | 次月股票收益 | 未说明 |
| [FactorBench](notes/cards/2026_FactorBench.md) | 2024-01 至 2025-10 | 20 日收益 | 每交易 1 美元 10 个基点 |
| [Alpha-R1](notes/cards/2025_Alpha-R1.md) | 2025-01-01 至 2025-12-31 | 5 日持有期收益 | 双边 10 bps |
| [MarketSenseAI](notes/cards/2026_MarketSenseAI.md) | S&P500：2024-09 至 2026-03；S&P100：2023-05 至 2026-03 | 一个月买入持有收益 | 未说明 |
| [LLM Strategy Finding](notes/cards/2024_LLMStrategyFinding.md) | SSE50 2023-01 至 2024-01；CSI300、S&P500 为 2021-01 至 2023-06 的三段滚动测试（2021H1、2022H1、2023H1） | 未来收益（IC 为 alpha 值与未来收益的相关；论文未说明持有期） | 未给费率；以每日最多换 5 只、日换手上限约 38% 控制成本 |
| [AgonAlpha](notes/cards/2026_AgonAlpha.md) | 2019-01-01 至 2023-12-31（平台评测窗口，全部提交进入样本外跟踪） | 平台综合评价分对应的截面 alpha 收益（论文未给收益公式与持有期） | 未说明 |
| [Alpha101](notes/cards/2016_Alpha101.md) | 无样本外切分；统计区间 2010-01-04 至 2013-12-31，1006 个交易日 | 无显式预测标签；alpha 直接给出内部持仓，按日频 P&L 统计，平均持有期 0.6–6.4 日 | 不计交易成本与价格冲击（表 1 注明） |
| [Trajectory Balance](notes/cards/2022_TrajectoryBalance.md) | 未说明 | 未说明 | 未说明 |
| [Alpha-GPT 2.0](notes/cards/2024_Alpha-GPT2.md) | 未说明 | 未说明 | 未说明 |
| [Tree-GRPO](notes/cards/2025_Tree-GRPO.md) | 不适用 | 不适用（答案精确匹配 EM；网页智能体用 F1） | 未说明 |
| [DeepMind AlphaEvolve](notes/cards/2025_DeepMind-AlphaEvolve.md) | 不适用 | 不适用（目标为算法正确性与指标改进，如矩阵乘法的秩、内核加速比） | 未说明 |
| [QuantAgent](notes/cards/2024_QuantAgent.md) | 未说明 | 未来收益（论文未说明持有期） | 未说明 |
| [Warm Start GP](notes/cards/2024_WarmStartGP.md) | 2022-01 至 2024-10（因子层）；组合层 2023-01 至 2024-10 | 5 日 VWAP 累计收益 | 0.6‰ |
| [Alpha-GPT](notes/cards/2023_Alpha-GPT.md) | 未说明 | 未来收益（论文未说明持有期） | 未说明 |
| [QuantEvolver](notes/cards/2026_QuantEvolver.md) | 未说明 | 未来 5 分钟涨跌方向（A）；未来一小时的截面收益排名（B）；未来收益（Γ） | 未说明 |
| [AgenticFactorInvesting](notes/cards/2026_AgenticFactorInvesting.md) | 2021-01 至 2024-12（晋升仅用 2020-12 前） | 次日收益 | 单边 3 bps |
| [CAVB](notes/cards/2025_CAVB.md) | 2010 至 2022 年（由 1980 年起、20 年训练 + 10 年验证 + 1 年测试、13 次年度滚动推出） | 次月收益；模型以超额收益定义因子结构，正文未细化无风险收益处理 | 月度调仓 30 bps；未明确单边 / 双边与换手计费基数 |
| [Publication Bias](notes/cards/2022_PublicationBias.md) | 无统一样本外；另报告样本结束后 1–3 年与 10 年 | 未说明 | 未说明 |
| [Sequential Cauchy](notes/cards/2023_SequentialCauchy.md) | 1963-07 至 2022-11 滚动窗口 | 未说明 | 未说明 |
| [GiGPO](notes/cards/2025_GiGPO.md) | 未说明 | 任务完成与否（ALFWorld、WebShop 成功率）与问答正确率 | 未说明 |
| [DSR](notes/cards/2019_DSR.md) | 未说明 | 拟合输入 X 到标量 y 的映射（符号回归，无金融标签） | 未说明 |
| [GFlowNet](notes/cards/2021_GFlowNet.md) | 未说明 | 超网格任务为给定奖励函数的成比例采样；分子任务为预训练代理模型预测的结合能 | 未说明 |

<a id="by-route"></a>

## 4. 按路线

同一篇工作可以属于多条路线。

### 公式 / 符号 / 代码因子挖掘（`formulaic`，24 篇）

以公式、符号表达式、DSL、AST、文法或可执行程序表示的因子生成与搜索，包括遗传规划、AutoML、RL / MCTS / GFlowNet 与代码演化。

[Alpha101](notes/cards/2016_Alpha101.md)（2016-01） · [AutoAlpha](notes/cards/2020_AutoAlpha.md)（2020-02） · [AlphaEvolve](notes/cards/2021_AlphaEvolve.md)（2021-03） · [AlphaGen](notes/cards/2023_AlphaGen.md)（2023-05） · [Synergistic RL](notes/cards/2024_SynergisticRL.md)（2024-01） · [RiskMiner](notes/cards/2024_RiskMiner.md)（2024-02） · [Alpha2](notes/cards/2024_Alpha2.md)（2024-06） · [AlphaForge](notes/cards/2024_AlphaForge.md)（2024-06） · [QFR](notes/cards/2024_QFR.md)（2024-09） · [Warm Start GP](notes/cards/2024_WarmStartGP.md)（2024-12） · [AlphaQCM](notes/cards/2025_AlphaQCM.md)（2025-05） · [TLRS](notes/cards/2025_TLRS.md)（2025-07） · [AlphaSAGE](notes/cards/2025_AlphaSAGE.md)（2025-09） · [AlphaCFG](notes/cards/2026_AlphaCFG.md)（2026-01） · [AlphaPROBE](notes/cards/2026_AlphaPROBE.md)（2026-02） · [AlphaG-OPD](notes/cards/2026_AlphaG-OPD.md)（2026-08） · [AlphaSeek](notes/cards/2026_AlphaSeek.md)（2026-08） · [AlphaPareto](notes/cards/2026_AlphaPareto.md)（2026-09） · [AlphaRJM](notes/cards/2026_AlphaRJM.md)（2026-09） · [AlphaPADI](notes/cards/2026_AlphaPADI.md)（2026-10） · [AlphaRLM](notes/cards/2026_AlphaRLM.md)（2026-10） · [EvoQuantLab](notes/cards/2026_EvoQuantLab.md)（2026-10） · [QBX](notes/cards/2026_QBX.md)（2026-10） · [CosmosAlpha](notes/cards/2026_CosmosAlpha.md)（2026-11）

### LLM 驱动的因子生成（`llm-formula`，19 篇）

由大语言模型提出、实现或改写因子表达式；搜索与评价循环可以是传统搜索器，LLM 负责生成与变异。

[Alpha-GPT](notes/cards/2023_Alpha-GPT.md)（2023-07） · [Alpha-GPT 2.0](notes/cards/2024_Alpha-GPT2.md)（2024-02） · [QuantAgent](notes/cards/2024_QuantAgent.md)（2024-02） · [LLM Strategy Finding](notes/cards/2024_LLMStrategyFinding.md)（2024-09） · [AlphaAgent](notes/cards/2025_AlphaAgent.md)（2025-02） · [Alpha-Jungle](notes/cards/2025_Alpha-Jungle.md)（2025-05） · [TreEvo](notes/cards/2025_TreEvo.md)（2025-08） · [CogAlpha](notes/cards/2025_CogAlpha.md)（2025-11） · [FactorMiner](notes/cards/2026_FactorMiner.md)（2026-02） · [QuantaAlpha](notes/cards/2026_QuantaAlpha.md)（2026-02） · [AlphaLogics](notes/cards/2026_AlphaLogics.md)（2026-03） · [Hubble](notes/cards/2026_Hubble.md)（2026-03） · [AlphaMemo](notes/cards/2026_AlphaMemo.md)（2026-06） · [AlphaSchema](notes/cards/2026_AlphaSchema.md)（2026-07） · [AlphaSeek](notes/cards/2026_AlphaSeek.md)（2026-08） · [AlphaDiverse](notes/cards/2026_AlphaDiverse.md)（2026-09） · [AlphaRLM](notes/cards/2026_AlphaRLM.md)（2026-10） · [LineageEvo](notes/cards/2026_LineageEvo.md)（2026-10） · [CosmosAlpha](notes/cards/2026_CosmosAlpha.md)（2026-11）

### LLM / Agent 研究流程（`llm-agent`，13 篇）

重点在流程编排：研究轨迹、经验记忆、预算调度、多智能体分工与自改进闭环，而不是某种特定的表达式表示。

[RD-Agent(Q)](notes/cards/2025_RD-Agent-Quant.md)（2025-05） · [EFS](notes/cards/2025_EFS.md)（2025-07） · [Alpha-R1](notes/cards/2025_Alpha-R1.md)（2025-12） · [AgenticFactorInvesting](notes/cards/2026_AgenticFactorInvesting.md)（2026-03） · [FactorEngine](notes/cards/2026_FactorEngine.md)（2026-03） · [QuantEvolver](notes/cards/2026_QuantEvolver.md)（2026-05） · [Agora/SJS](notes/cards/2026_Agora-SJS.md)（2026-06） · [X-Alpha](notes/cards/2026_X-Alpha.md)（2026-07） · [AgonAlpha](notes/cards/2026_AgonAlpha.md)（2026-08） · [AutoScientist-Quant](notes/cards/2026_AutoScientist-Quant.md)（2026-08） · [AlphaLedger](notes/cards/2026_AlphaLedger.md)（2026-10） · [AlphaPilot](notes/cards/2026_AlphaPilot.md)（2026-10） · [EvoQuantLab](notes/cards/2026_EvoQuantLab.md)（2026-10）

### 神经 / 隐式因子（`neural`，5 篇）

深度网络直接输出 alpha 信号或学习因子表示，包括离散隐因子、动态载荷等保留部分可解释结构的做法。

[AlphaGAT](notes/cards/2025_AlphaGAT.md)（2025） · [CAVB](notes/cards/2025_CAVB.md)（2025） · [PRISM-VQ](notes/cards/2026_PRISM-VQ.md)（2026-05） · [MAPLE](notes/cards/2026_MAPLE.md)（2026-07） · [Det-MASO](notes/cards/2026_Det-MASO.md)（2026-10）

### 因子池与组合（下游模块）（`pool-combination`，13 篇）

候选因子的准入、去冗余、筛选启停、动态加权与组合构建。它通常与方法路线并用，也用于以池为评价单位的基准。

[AlphaForge](notes/cards/2024_AlphaForge.md)（2024-06） · [AlphaGAT](notes/cards/2025_AlphaGAT.md)（2025） · [EFS](notes/cards/2025_EFS.md)（2025-07） · [AlphaEval](notes/cards/2025_AlphaEval.md)（2025-08） · [Alpha-R1](notes/cards/2025_Alpha-R1.md)（2025-12） · [AlphaPROBE](notes/cards/2026_AlphaPROBE.md)（2026-02） · [AgenticFactorInvesting](notes/cards/2026_AgenticFactorInvesting.md)（2026-03） · [X-Alpha](notes/cards/2026_X-Alpha.md)（2026-07） · [AutoScientist-Quant](notes/cards/2026_AutoScientist-Quant.md)（2026-08） · [GoAnt](notes/cards/2026_GoAnt.md)（2026-09） · [AlphaLedger](notes/cards/2026_AlphaLedger.md)（2026-10） · [AlphaPilot](notes/cards/2026_AlphaPilot.md)（2026-10） · [FactorBench](notes/cards/2026_FactorBench.md)（2026-10）

### 基准与统一评测（`benchmark`，4 篇）

给出统一数据、切分、指标或执行契约，用来横向比较多个挖掘方法。

[AlphaEval](notes/cards/2025_AlphaEval.md)（2025-08） · [Look-Ahead-Bench](notes/cards/2026_Look-Ahead-Bench.md)（2026-01） · [MarketSenseAI](notes/cards/2026_MarketSenseAI.md)（2026-04） · [FactorBench](notes/cards/2026_FactorBench.md)（2026-10）

### 审计、复现与泄漏检查（`auditing`，3 篇）

审视证据链本身：结果留存方式、指标口径、前视检查、试验计数与显著性校正，而不是给方法排名。

[AgonAlpha](notes/cards/2026_AgonAlpha.md)（2026-08） · [Auditing LLM Alpha-Factor Mining](notes/cards/2026_AuditingLLMAlpha.md)（2026-10） · [QBX](notes/cards/2026_QBX.md)（2026-10）

### 数据与表达空间（`data-space`，3 篇）

扩展因子的输入数据（高频、订单簿、文本、另类数据）或表达空间本身。

[HRFT/IRFT](notes/cards/2024_HRFT.md)（2024-08） · [TextToAlpha](notes/cards/2025_TextToAlpha.md)（2025-10） · [GoAnt](notes/cards/2026_GoAnt.md)（2026-09）

### 可迁移的相邻方法（`adjacent`，10 篇）

不是因子挖掘本身，但机制可以迁移的方法，例如符号回归、生成流网络、智能体信用分配与多重检验。

[DSR](notes/cards/2019_DSR.md)（2019-12） · [GFlowNet](notes/cards/2021_GFlowNet.md)（2021-06） · [Trajectory Balance](notes/cards/2022_TrajectoryBalance.md)（2022-01） · [Publication Bias](notes/cards/2022_PublicationBias.md)（2022-09） · [Sequential Cauchy](notes/cards/2023_SequentialCauchy.md)（2023-03） · [GiGPO](notes/cards/2025_GiGPO.md)（2025-05） · [DeepMind AlphaEvolve](notes/cards/2025_DeepMind-AlphaEvolve.md)（2025-06） · [Tree-GRPO](notes/cards/2025_Tree-GRPO.md)（2025-09） · [Look-Ahead-Bench](notes/cards/2026_Look-Ahead-Bench.md)（2026-01） · [MarketSenseAI](notes/cards/2026_MarketSenseAI.md)（2026-04）
