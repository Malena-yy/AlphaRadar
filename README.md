# AlphaRadar

AlphaRadar 是一个围绕 **因子挖掘专题** 的研究跟踪仓库：持续收录、阅读和横向比较 alpha 因子挖掘相关的公开工作，覆盖公式 / 符号因子、LLM / Agent 因子挖掘、神经因子、因子池与组合、因子评估以及数据与表达空间。

仓库只保存公开论文的结构化登记、阅读笔记和横向分析。论文 PDF 不入库，只登记 arXiv 或官方页面链接。

## 出发点：因子挖掘面临的问题

因子挖掘的目标可以概括为：在可审计的表达空间里，用有限的计算预算，持续找到一组**样本外有效、彼此互补、能在组合中落地**的信号。公开工作提出的方法五花八门，但它们反复在应对同一批问题。本仓库先把这些问题固定下来，再用它们来读每一篇新工作：**它针对哪个问题、用什么机制、证据是否足够、还留下了什么。**

问题按挖掘流程从前到后排列：

| 编号 | 问题 | 核心矛盾 | 所在环节 |
| --- | --- | --- | --- |
| P1 | 表达空间巨大，有效因子稀少 | 空间随表达式长度组合爆炸，其中大多不合法、无意义或彼此语义等价 | 表达与搜索 |
| P2 | 表达能力与可解释性的权衡 | 公式可解释、可审计但表达受限；神经因子和任意代码表达更强，却难以解释和审计 | 表达 |
| P3 | 评价成本高 | 每个候选都要在全市场长周期面板上求值，评价次数直接决定搜索规模 | 评价 |
| P4 | 学习信号稀疏、延迟且不可微 | 只有完整因子才有奖励，IC 对生成过程没有梯度，奖励还随因子池变化 | 训练 |
| P5 | 低信噪比下的过拟合 | 收益中可预测成分很小，大规模搜索等于大量多重检验 | 评价可信度 |
| P6 | 前视偏差与信息泄漏 | 一处时间对齐错误就能制造虚假的高 IC，且很难从结果上察觉 | 评价可信度 |
| P7 | 因子同质化与冗余 | 搜索集中到少数高分模板，新因子与已有因子高度相关 | 入池 |
| P8 | 挖掘目标与实际使用脱节 | 单因子高 IC 不等于组合增益，也不等于扣除换手和成本后仍可交易 | 组合与交易 |
| P9 | 非平稳与因子衰减 | 市场状态在变，因子被拥挤后失效，挖掘需要持续维护 | 持续使用 |
| P10 | 评估口径不统一、难以复现 | 各工作的股票池、切分、标签、指标和成本假设不同，很多未开源 | 研究方法 |

几处容易混淆的边界：

- **P3 与 P4**：P3 是算力预算问题，任何搜索方法都会遇到；P4 是强化学习、生成模型、RFT 这类学习型生成器特有的信用分配问题。同一机制可以同时针对两者，例如 AlphaForge 的预测器既减少真实评价，又给生成器提供可微信号。
- **P5、P6、P9**：三者都表现为样本外失效，但成因不同。P5 是搜索带来的选择偏差，P6 是评价本身有错，P9 是市场本身在变。
- **先验知识**（研究员想法、研报、专家因子）不单列为问题，它是应对 P1 的一类手段。
- **LLM 路线特有的问题**：代码不可执行归入 P1（生成结果无效），声称的逻辑与实现不一致归入 P2（可解释性）。

下面逐条说明问题本身，并列出**已收录工作**中针对它的机制。代表工作只列速读卡中有对应机制描述的论文，不是完整清单；“跟踪关注点”是本仓库后续阅读时要回答的问题，不是已有结论。问题划分是本仓库的分析框架，不是某篇论文的结论。

### P1 表达空间巨大，有效因子稀少

算子、字段、窗口和常数的组合随表达式长度指数增长。大部分表达式要么不合法，要么合法但没有意义（例如价格与成交量直接相加），要么与已有表达式语义等价；LLM 生成还多一类无效：代码无法执行。搜索预算大量浪费在这些表达式上，策略也可能学到无效动作。

- 生成时约束：动作掩码与栈规则（AlphaGen），寄存器程序表示与维度检查（Alpha2），面向 alpha 的上下文无关文法与语义、长度约束（AlphaCFG），白名单 AST 沙箱（Hubble）。
- 利用结构的搜索：MCTS 显式复用已探索结构（RiskMiner、Alpha-Jungle），从低阶到高阶的层次化搜索（AutoAlpha），因子谱系图上的有偏演化（AlphaPROBE），宏观逻辑演化与微观参数优化分离（FactorEngine）。
- 先验引导：研究员想法与层次化字段检索（Alpha-GPT、Alpha-GPT 2.0），持续积累并检索的信号知识库（QuantAgent），经验回放中注入优质种子公式（Synergistic RL），从研报和专家因子抽取初始程序池（FactorEngine）。
- 跟踪关注点：约束前置能节省多少评价预算？约束和先验会不会把有效区域也排除掉？

### P2 表达能力与可解释性的权衡

公式因子可读、可审计、便于风险归因，但能表达什么受算子集和数据类型限制。神经因子、任意代码和外部信息能表达更多结构，却更难解释和审计，也更难判断它是否只是拟合了噪声。可解释性还有另一面：因子声称的逻辑（例如“流动性”）要真的体现在表达式里。

- 扩展表达能力：矩阵和向量算子与行业关系注入（AlphaEvolve），扩展算子集与长窗口（Synergistic RL），符号-数值混合词表生成含常数的公式（HRFT/IRFT），神经网络直接输出 alpha（AlphaGAT 第一阶段），图灵完备程序或代码演化（FactorEngine、CogAlpha），从文本、表格、图像材料中抽取因子线索（LLM Strategy Finding）。
- 保持可解释：假设、描述、表达式之间的一致性校验（AlphaAgent、QuantaAlpha）。
- 跟踪关注点：表达能力提升带来的增益，在样本外能保留多少？神经因子和代码因子如何审计？

### P3 评价成本高

每个候选因子都要在全市场、长时间的面板上求值，再计算 IC 和与已有因子的相关性；因子池越大，相关性计算越贵。LLM 循环中，每轮还要付出推理成本，并随反馈积累而上下文膨胀。评价预算直接决定能搜索多少候选。

- 减少真实评价：用可微预测器代替部分真实评价来引导生成（AlphaForge），冗余剪枝与指纹机制跳过重复计算（AlphaEvolve），PCA 近似相似度降低去重成本（AutoAlpha）。
- 降低 LLM 循环成本：用 RFT 把经验写入轻量模型参数，代替不断增长的提示词上下文（QuantEvolver）。
- 跟踪关注点：各方法是否在相同评价预算下比较？代理模型的误差在哪里会误导搜索？

### P4 学习信号稀疏、延迟且不可微

对学习型生成器而言，奖励只在因子完整生成后出现，中间步骤没有监督；IC 对生成的 token 没有梯度；奖励依赖当前因子池，池子一变，同一条公式的奖励就变。这些使训练不稳定、信用分配困难。

- 让奖励更密集：合法中间表达式即时奖励（RiskMiner），专家子序列轨迹级塑形与奖励中心化（TLRS）。
- 降低方差、稳定探索：不带价值网络的 REINFORCE 加贪婪基线（QFR），奖励分布方差作为探索奖励（AlphaQCM）。
- 改变学习目标：可微预测器把 fitness 变成生成器的梯度（AlphaForge），预测性能、结构对齐与新颖性的多信号奖励加轨迹平衡（AlphaSAGE），组内相对优势更新（QuantEvolver）。
- 跟踪关注点：塑形奖励会不会把策略引向专家因子附近、降低原创性？池依赖的非平稳奖励下，哪种训练目标更稳？

### P5 低信噪比下的过拟合

股票收益中可预测的成分很小，噪声很大。在巨大空间里搜索，本身就是大量的多重检验，训练期挑出的高 IC 因子很可能只是运气。评价指标越单一（只看 IC 峰值），越容易被搜索利用。

- 稳定性目标：奖励中加入信息比率（QFR）。
- 复杂度与风险控制：AST 节点数、参数数、特征数正则（AlphaAgent），在评价中显式给过拟合风险打分（Alpha-Jungle）。
- 评估隔离：最终评估数据对参与搜索的智能体保持密封（Agora/SJS）。
- 跟踪关注点：有没有工作对搜索规模做多重检验校正？样本外区间是否足够长、覆盖不同市场状态？

### P6 前视偏差与信息泄漏

标签窗口、字段发布时间、复权、停牌、股票池成分变动，任何一处时间对齐错误都会把未来信息带进因子，产生虚假的高 IC，而且很难从结果上察觉。代码形式的因子更容易混入未来函数。LLM 路线还有额外风险：模型的预训练语料可能覆盖了评估区间。

- 代码级检查：多智能体质量检查器中包含时间泄漏检查（CogAlpha）。
- 评估数据密封：持有期评估数据不进入任何面向模型的输入（Agora/SJS）。
- 跟踪关注点：已收录工作中专门处理泄漏的很少，这是重点补检方向。LLM 预训练截止时间与回测区间的关系，有没有工作系统讨论过？

### P7 因子同质化与冗余

奖励最大化会让搜索集中到少数高分模板，生成的因子彼此高度相关，生成器还可能发生模式坍缩。因子库变大后，新因子越来越难与已有因子拉开距离（FactorMiner 称之为“相关性红海”）。冗余因子不增加组合信息，还会放大共同风险。

- 以池为目标：用加入因子池后的组合 IC 边际贡献作为奖励（AlphaGen），入库同时检查 IC、ICIR 和相关性阈值（AlphaForge）。
- 在生成端施加多样性：生成器损失中的多样性项（AlphaForge），结构对齐与新颖性奖励下覆盖多个高奖励模式（AlphaSAGE），质量-多样性搜索（AutoAlpha），协方差非对角项惩罚（AlphaGAT）。
- 结构和行为去重：中间奖励中加入与已有因子的 MutIC 重复惩罚（RiskMiner），演化中剪枝与既有因子高度相关的表达式（AlphaEvolve），AST 相似度（AlphaAgent），高频子树规避（Alpha-Jungle），因子家族感知评分（Hubble），经验记忆记录应避开的高相关区域（FactorMiner），多样性与互补性奖励（QuantEvolver），复杂度、结构相似度与输出相关性控制（QuantaAlpha），谱系图上的多样性检索（AlphaPROBE），相关性去重（RD-Agent(Q)）。
- 跟踪关注点：结构不同但行为相同的因子怎么识别？多样性约束会损失多少单因子质量？

### P8 挖掘目标与实际使用脱节

因子最终要组合起来交易。单因子 IC 高，加进组合未必有增益；组合方式、权重是否随时间变化，会改变一个因子的边际价值；换手、容量和交易成本还会进一步削减可实现收益。只优化单因子指标，挖出来的东西可能用不上。

- 组合目标进入挖掘：组合 IC 边际贡献作为奖励（AlphaGen），因子与模型联合优化（RD-Agent(Q)）。
- 挖掘与组合解耦：挖掘阶段扩大候选池，使用阶段再动态选因子、动态加权（AlphaForge），GAT-PPO 学习动态权重（AlphaGAT），稀疏组合选股（EFS），动态优化因子权重（LLM Strategy Finding），用 LLM 推理决定因子启停（Alpha-R1）。
- 可交易性进入评价：把换手率纳入候选评分（Alpha-Jungle、Hubble）。
- 跟踪关注点：报告的组合收益是否扣除了换手和成本？动态组合的增益来自因子本身，还是来自组合器？

### P9 非平稳与因子衰减

市场状态会切换，因子被广泛使用后会变得拥挤，有效性随时间衰减。今天挖到的因子明天未必有效，挖掘因此不是一次性任务，而是持续的维护。

- 抗衰减与抗拥挤：把原创性约束写入生成目标以对抗衰减（AlphaAgent），负向检索提示应避开的拥挤模板（Hubble）。
- 随状态调整使用：滚动窗口动态选因子（AlphaForge），根据市场状态推理因子启停（Alpha-R1）。
- 跟踪关注点：衰减有没有被直接度量？在线更新或滚动重训的成本和收益如何？

### P10 评估口径不统一、难以复现

各工作使用不同的市场、股票池、时间切分、标签、IC 或 RankIC 口径、组合方式和成本假设，报告的数字通常不能直接横向比较。很多工作没有开源，开源的也常常缺数据处理和实验脚本。

- 标准化与留痕：技能模块中封装标准化评估协议（FactorMiner），持久化保存每个候选的多维诊断和提示词元数据（Hubble）。
- 跟踪关注点：`evaluation` 路线目前还没有收录，需要补检专门的评估框架和基准；本仓库计划单独整理各论文实验口径的对照。

## 导航

| 入口 | 内容 |
| --- | --- |
| [研究全景](topics/landscape.md) | 技术路线总览、RL 与 LLM/Agent 闭环、路线演进和各分组导读 |
| [生成器如何使用真实 IC](topics/generator_training_with_ic.md) | 强化学习、AlphaForge、AlphaSAGE 三类生成器训练机制对照 |
| [算子空间对照](topics/operator_space.md) | 各工作公开的公式算子空间、证据等级与同名异义 |
| [速读卡](notes/cards/) / [精读](notes/deep/) | 单篇论文笔记 |
| [跟踪简报](digests/) | 定期新增工作与状态变化 |
| [`papers.yaml`](papers.yaml) | 论文登记表，下方索引由它生成 |

## 维护方式

- 新论文先登记到 [`papers.yaml`](papers.yaml)，标注它针对的问题（P1-P10），按 `inbox → triaged → card → deep-read` 推进；问题、路线、标签和状态的取值见 [`taxonomy.yaml`](taxonomy.yaml)。
- 速读卡和精读分别按 [`notes/_template_card.md`](notes/_template_card.md)、[`notes/_template_deep.md`](notes/_template_deep.md) 撰写；定期简报按 [`digests/_template.md`](digests/_template.md) 撰写。
- 修改登记表后运行 `python scripts/build_index.py` 重新生成下方索引；CI 会运行 `--check` 校验。
- 收录口径、写作规则和提交前检查见 [`AGENTS.md`](AGENTS.md)，维护记录见 [`CHANGELOG.md`](CHANGELOG.md)。

## 许可

- 文档内容（笔记、专题、简报、登记表等）采用 [CC BY 4.0](LICENSE)。
- 代码（`scripts/`、`.github/`）采用 [MIT](LICENSE-MIT)。
- 收录论文的版权归原作者所有；本仓库只登记链接并撰写独立的阅读笔记，不转载论文原文和图表。

## 论文索引

<!-- PAPER-INDEX:BEGIN (generated by scripts/build_index.py, do not edit) -->

共收录 32 篇（速读 29，精读 3）。同一篇论文可出现在多条路线下；“问题”列对应上文 P1-P10。

### 公式 / 符号因子挖掘（`formulaic`）

公式库、遗传规划与 AutoML、RL / MCTS / GFlowNet / 文法搜索等显式公式、DSL、AST 形式的因子生成。

| 时间 | 工作 | 问题 | 标签 | 状态 | 链接 |
| --- | --- | --- | --- | --- | --- |
| 2016-01 | **Alpha101**<br>101 Formulaic Alphas | — | `formula-library` | 速读 | [arXiv](https://arxiv.org/abs/1601.00991) · [速读](notes/cards/2016_Alpha101.md) |
| 2020-04 | **AutoAlpha**<br>AutoAlpha: an Efficient Hierarchical Evolutionary Algorithm for Mining Alpha Factors in Quantitative Investment | P1 P3 P7 | `genetic-programming` `quality-diversity` | 速读 | [arXiv](https://arxiv.org/abs/2002.08245) · [速读](notes/cards/2020_AutoAlpha.md) |
| 2021-04 | **AlphaEvolve**<br>AlphaEvolve: A Learning Framework to Discover Novel Alphas in Quantitative Investment | P2 P3 P7 | `automl` `evolutionary` | 速读 | [arXiv](https://arxiv.org/abs/2103.16196) · [速读](notes/cards/2021_AlphaEvolve.md) |
| 2023-05 | **AlphaGen**<br>Generating Synergistic Formulaic Alpha Collections via Reinforcement Learning | P1 P7 P8 | `rl` `ppo` `rpn` `pool-reward` | 速读 | [arXiv](https://arxiv.org/abs/2306.12964) · [代码](https://github.com/ICT-FinD-Lab/alphagen) · [速读](notes/cards/2023_AlphaGen.md) |
| 2024-01 | **Synergistic RL**<br>Synergistic Formulaic Alpha Generation for Quantitative Trading based on Reinforcement Learning | P1 P2 | `rl` `rpn` | 速读 | [arXiv](https://arxiv.org/abs/2401.02710) · [速读](notes/cards/2024_SynergisticRL.md) |
| 2024-02 | **RiskMiner**<br>RiskMiner: Discovering Formulaic Alphas via Risk Seeking Monte Carlo Tree Search | P1 P4 P7 | `mcts` `rl` | 速读 | [arXiv](https://arxiv.org/abs/2402.07080) · [速读](notes/cards/2024_RiskMiner.md) |
| 2024-06 | **Alpha2**<br>Alpha2: Discovering Logical Formulaic Alphas using Deep Reinforcement Learning | P1 | `rl` `mcts` `program-search` | 速读 | [arXiv](https://arxiv.org/abs/2406.16505) · [代码](https://github.com/x35f/alpha2) · [速读](notes/cards/2024_Alpha2.md) |
| 2024-06 | **AlphaForge**<br>AlphaForge: A Framework to Mine and Dynamically Combine Formulaic Alpha Factors | P3 P4 P7 P8 P9 | `generator-predictor` `dynamic-combination` | 精读 | [arXiv](https://arxiv.org/abs/2406.18394) · [代码](https://github.com/dulyhao/alphaforge) · [速读](notes/cards/2024_AlphaForge.md) · [精读](notes/deep/2024_AlphaForge.md) |
| 2024-09 | **QFR**<br>QuantFactor REINFORCE: Mining Steady Formulaic Alpha Factors with Variance-bounded REINFORCE | P4 P5 | `rl` `reinforce` | 速读 | [arXiv](https://arxiv.org/abs/2409.05144) · [速读](notes/cards/2024_QFR.md) |
| 2025-05 | **AlphaQCM**<br>AlphaQCM: Alpha Discovery with Distributional Reinforcement Learning | P4 | `rl` `distributional-rl` | 速读 | [论文](https://openreview.net/forum?id=3sXMHlhBSs) · [速读](notes/cards/2025_AlphaQCM.md) |
| 2025-07 | **TLRS**<br>Learning from Expert Factors: Trajectory-level Reward Shaping for Formulaic Alpha Mining | P4 | `rl` `reward-shaping` | 速读 | [arXiv](https://arxiv.org/abs/2507.20263) · [速读](notes/cards/2025_TLRS.md) |
| 2025-09 | **AlphaSAGE**<br>AlphaSAGE: Structure-Aware Alpha Mining via GFlowNets for Robust Exploration | P4 P7 | `gflownet` `gnn` | 精读 | [arXiv](https://arxiv.org/abs/2509.25055) · [代码](https://github.com/BerkinChen/AlphaSAGE) · [速读](notes/cards/2025_AlphaSAGE.md) · [精读](notes/deep/2025_AlphaSAGE.md) |
| 2026-01 | **AlphaCFG**<br>Alpha Discovery via Grammar-Guided Learning and Search | P1 | `grammar` `rl` `mcts` | 速读 | [arXiv](https://arxiv.org/abs/2601.22119) · [代码](https://github.com/HanYang544/AlphaCFG) · [速读](notes/cards/2026_AlphaCFG.md) |
| 2026-02 | **AlphaPROBE**<br>AlphaPROBE: Alpha Mining via Principled Retrieval and On-graph biased evolution | P1 P7 | `evolutionary` `factor-lineage` | 速读 | [arXiv](https://arxiv.org/abs/2602.11917) · [代码](https://github.com/gta0804/AlphaPROBE) · [速读](notes/cards/2026_AlphaPROBE.md) |

### LLM / Agent 因子挖掘（`llm-agent`）

以大语言模型或智能体完成假设生成、公式或代码实现、经验记忆、评价反馈和 RFT 的因子挖掘。

| 时间 | 工作 | 问题 | 标签 | 状态 | 链接 |
| --- | --- | --- | --- | --- | --- |
| 2023-07 | **Alpha-GPT**<br>Alpha-GPT: Human-AI Interactive Alpha Mining for Quantitative Investment | P1 | `llm` `human-in-the-loop` | 速读 | [arXiv](https://arxiv.org/abs/2308.00016) · [速读](notes/cards/2023_Alpha-GPT.md) |
| 2024-02 | **Alpha-GPT 2.0**<br>Alpha-GPT 2.0: Human-in-the-Loop AI for Quantitative Investment | P1 | `llm` `human-in-the-loop` | 速读 | [arXiv](https://arxiv.org/abs/2402.09746) · [速读](notes/cards/2024_Alpha-GPT2.md) |
| 2024-02 | **QuantAgent**<br>QuantAgent: Seeking Holy Grail in Trading by Self-Improving Large Language Model | P1 | `llm` `memory` | 速读 | [arXiv](https://arxiv.org/abs/2402.03755) · [速读](notes/cards/2024_QuantAgent.md) |
| 2024-09 | **LLM Strategy Finding**<br>Automate Strategy Finding with LLM in Quant Investment | P2 P8 | `llm` `multimodal` | 速读 | [arXiv](https://arxiv.org/abs/2409.06289) · [速读](notes/cards/2024_LLMStrategyFinding.md) |
| 2025-02 | **AlphaAgent**<br>AlphaAgent: LLM-Driven Alpha Mining with Regularized Exploration to Counteract Alpha Decay | P2 P5 P7 P9 | `llm` `alpha-decay` | 速读 | [arXiv](https://arxiv.org/abs/2502.16789) · [代码](https://github.com/RndmVariableQ/AlphaAgent) · [速读](notes/cards/2025_AlphaAgent.md) |
| 2025-05 | **Alpha-Jungle**<br>Navigating the Alpha Jungle: An LLM-Powered MCTS Framework for Formulaic Factor Mining | P1 P5 P7 P8 | `llm` `mcts` | 速读 | [arXiv](https://arxiv.org/abs/2505.11122) · [速读](notes/cards/2025_Alpha-Jungle.md) |
| 2025-05 | **RD-Agent(Q)**<br>R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization | P7 P8 | `llm` `multi-agent` `factor-model-joint` | 速读 | [arXiv](https://arxiv.org/abs/2505.15155) · [代码](https://github.com/microsoft/RD-Agent) · [速读](notes/cards/2025_RD-Agent-Quant.md) |
| 2025-07 | **EFS**<br>EFS: Evolutionary Factor Searching for Sparse Portfolio Optimization Using Large Language Models | P8 | `llm` `evolutionary` `portfolio` | 速读 | [arXiv](https://arxiv.org/abs/2507.17211) · [速读](notes/cards/2025_EFS.md) |
| 2025-11 | **CogAlpha**<br>Cognitive Alpha Mining via LLM-Driven Code-Based Evolution | P2 P6 | `llm` `code-evolution` | 速读 | [arXiv](https://arxiv.org/abs/2511.18850) · [速读](notes/cards/2025_CogAlpha.md) |
| 2025-12 | **Alpha-R1**<br>Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning | P8 P9 | `llm` `grpo` `factor-screening` | 速读 | [arXiv](https://arxiv.org/abs/2512.23515) · [代码](https://github.com/FinStep-AI/Alpha-R1) · [速读](notes/cards/2025_Alpha-R1.md) |
| 2026-02 | **FactorMiner**<br>FactorMiner: A Self-Evolving Agent with Skills and Experience Memory for Financial Alpha Discovery | P7 P10 | `llm` `memory` `skills` | 速读 | [arXiv](https://arxiv.org/abs/2602.14670) · [速读](notes/cards/2026_FactorMiner.md) |
| 2026-02 | **QuantaAlpha**<br>QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining | P2 P7 | `llm` `evolutionary` | 速读 | [arXiv](https://arxiv.org/abs/2602.07085) · [代码](https://github.com/QuantaAlpha/QuantaAlpha) · [速读](notes/cards/2026_QuantaAlpha.md) |
| 2026-03 | **FactorEngine**<br>FactorEngine: A Program-level Knowledge-Infused Factor Mining Framework for Quantitative Investment | P1 P2 | `llm` `code-evolution` | 速读 | [arXiv](https://arxiv.org/abs/2603.16365) · [速读](notes/cards/2026_FactorEngine.md) |
| 2026-03 | **Hubble**<br>Hubble: An LLM-Driven Agentic Framework for Safe, Diverse, and Reproducible Alpha Factor Discovery | P1 P7 P8 P9 P10 | `llm` `rag` `safety` | 速读 | [arXiv](https://arxiv.org/abs/2604.09601) · [速读](notes/cards/2026_Hubble.md) |
| 2026-05 | **QuantEvolver**<br>From Feedback Loops to Policy Updates: Reinforcement Fine-Tuning for LLM-Based Alpha Factor Discovery | P3 P4 P7 | `llm` `rft` `grpo` | 速读 | [arXiv](https://arxiv.org/abs/2605.15412) · [代码](https://github.com/QuantLLM/QuantEvolver) · [速读](notes/cards/2026_QuantEvolver.md) |
| 2026-06 | **Agora/SJS**<br>AI Trading's Alpha Singularity: Emergent Market Reasoning through Agent-to-Agent Self-Evolution | P5 P6 | `llm` `multi-agent` `self-play` | 速读 | [arXiv](https://arxiv.org/abs/2606.29194) · [速读](notes/cards/2026_Agora-SJS.md) |

### 神经 / 隐式因子（`neural`）

深度网络直接输出 alpha 信号或端到端学习因子表示，输出不是可解释公式。

| 时间 | 工作 | 问题 | 标签 | 状态 | 链接 |
| --- | --- | --- | --- | --- | --- |
| 2025 | **AlphaGAT**<br>AlphaGAT: A Two-Stage Learning Approach for Adaptive Portfolio Selection | P2 P7 P8 | `neural-alpha` `gnn` `rl` `ppo` `dynamic-combination` | 精读 | [论文](https://www.ijcai.org/proceedings/2025/834) · [速读](notes/cards/2025_AlphaGAT.md) · [精读](notes/deep/2025_AlphaGAT.md) |

### 因子池与组合（`pool-combination`）

候选因子准入、去冗余、筛选启停、动态加权和面向下游投资目标的组合。

| 时间 | 工作 | 问题 | 标签 | 状态 | 链接 |
| --- | --- | --- | --- | --- | --- |
| 2024-06 | **AlphaForge**<br>AlphaForge: A Framework to Mine and Dynamically Combine Formulaic Alpha Factors | P3 P4 P7 P8 P9 | `generator-predictor` `dynamic-combination` | 精读 | [arXiv](https://arxiv.org/abs/2406.18394) · [代码](https://github.com/dulyhao/alphaforge) · [速读](notes/cards/2024_AlphaForge.md) · [精读](notes/deep/2024_AlphaForge.md) |
| 2025 | **AlphaGAT**<br>AlphaGAT: A Two-Stage Learning Approach for Adaptive Portfolio Selection | P2 P7 P8 | `neural-alpha` `gnn` `rl` `ppo` `dynamic-combination` | 精读 | [论文](https://www.ijcai.org/proceedings/2025/834) · [速读](notes/cards/2025_AlphaGAT.md) · [精读](notes/deep/2025_AlphaGAT.md) |
| 2025-07 | **EFS**<br>EFS: Evolutionary Factor Searching for Sparse Portfolio Optimization Using Large Language Models | P8 | `llm` `evolutionary` `portfolio` | 速读 | [arXiv](https://arxiv.org/abs/2507.17211) · [速读](notes/cards/2025_EFS.md) |
| 2025-12 | **Alpha-R1**<br>Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning | P8 P9 | `llm` `grpo` `factor-screening` | 速读 | [arXiv](https://arxiv.org/abs/2512.23515) · [代码](https://github.com/FinStep-AI/Alpha-R1) · [速读](notes/cards/2025_Alpha-R1.md) |
| 2026-02 | **AlphaPROBE**<br>AlphaPROBE: Alpha Mining via Principled Retrieval and On-graph biased evolution | P1 P7 | `evolutionary` `factor-lineage` | 速读 | [arXiv](https://arxiv.org/abs/2602.11917) · [代码](https://github.com/gta0804/AlphaPROBE) · [速读](notes/cards/2026_AlphaPROBE.md) |

### 评估与稳健性（`evaluation`）

因子评价口径、衰减、拥挤、样本外稳健性、基准数据集与评估框架。

_暂无收录，待补检。_

### 数据与表达空间（`data-space`）

算子空间、高频 / 分钟频数据、另类数据（文本、新闻等）和表达空间扩展。

| 时间 | 工作 | 问题 | 标签 | 状态 | 链接 |
| --- | --- | --- | --- | --- | --- |
| 2024-08 | **HRFT/IRFT**<br>HRFT: Mining High-Frequency Risk Factor Collections End-to-End via Transformer | P2 | `high-frequency` `risk-factor` `transformer` | 速读 | [arXiv](https://arxiv.org/abs/2408.01271) · [代码](https://github.com/wencyxu/IRF-LLM-accepted-at-WWW25-) · [速读](notes/cards/2024_HRFT.md) |

### 可借鉴的相邻方法（`adjacent`）

不是因子挖掘本身，但机制可迁移的方法，例如 Agentic RL 的信用分配与 advantage 设计。

_暂无收录，待补检。_

<!-- PAPER-INDEX:END -->
