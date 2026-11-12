# 各问题的应对机制

> 本文按问题归纳已收录工作的应对思路：每类机制给出说明和代表工作，不是完整清单。全部工作与单篇笔记入口见[论文索引的按问题列表](../INDEX.md#by-problem)；问题的定义、边界和跟踪关注点见 [README](../README.md#因子挖掘面临的问题)。
>
> 代表工作优先选主要针对该问题的工作；“观察”是本仓库的归纳，不是论文结论。列出应对机制不代表其效果已普遍验证，相邻方法的迁移条件另行说明。

## P1 表达空间巨大，有效因子稀少

- 生成时约束：把语法、类型、维度或时间可用性约束前置到生成或准入阶段，不合法的候选不进入评价。代表：AlphaCFG（面向 alpha 的上下文无关文法与语义、长度约束）、Alpha2（寄存器程序与维度检查）、Hubble（白名单 AST 沙箱）、QBX（编译器准入）。
- 利用结构的搜索：显式复用已探索的结构，或在结构化空间里搜索。代表：RiskMiner、Alpha-Jungle（MCTS）、AutoAlpha（从低阶到高阶的层次化搜索）、AlphaPROBE（因子谱系图上的有偏演化）、AlphaSchema（以交易语义计划为搜索对象）。
- 先验引导：用研究员想法、研报、专家因子或经济机制确定搜索起点和方向。代表：Alpha-GPT（研究员想法与层次化字段检索）、FactorEngine（研报与专家因子启动程序池）、LLM Strategy Finding（从多模态材料抽取种子因子）、QuantAgent（持续积累的信号知识库）。
- 相邻方法：DSR 在采样时屏蔽非法 token；DeepMind AlphaEvolve 用带历史程序与得分上下文的 LLM diff 代替手写变异算子。见[可迁移的相邻方法](adjacent/transferable_methods.md)。
- 观察：AlphaSchema 的交易语义计划、AlphaDiverse 的经济机制目录把约束对象扩展到语义与机制层，仍需要实现后的语法、数值和时间可用性检查。

## P2 表达能力与可解释性的权衡

- 扩展表达能力：更丰富的算子与数据类型、含连续常数的公式、神经网络输出或可执行程序。代表：AlphaEvolve（矩阵、向量算子与行业关系注入）、HRFT/IRFT（符号-数值混合词表）、AlphaGAT（神经 Alpha）、FactorEngine 与 CogAlpha（可执行程序与代码演化）。
- 逻辑与实现对照：校验或约束因子声称的逻辑与计算过程一致。代表：AlphaAgent、QuantaAlpha（假设、描述、表达式之间的一致性校验）、AlphaSchema（先声明语义计划再生成代码）、Alpha-GPT（把公式反编译为自然语言解释）。
- 度量权衡：QBX 实测了受限、可审计的程序空间在行为广度上的代价；AlphaEval 用 LLM 给金融逻辑打分并与人工专家排序对照。
- 观察：代码可读、自然语言解释与经济机制验证是不同证据；一致性评分不能单独证明因子具有所述经济含义。

## P3 评价成本高

- 代理评价：用学到的模型或廉价指标替代部分真实评价。代表：AlphaForge（可微预测器）、AlphaSchema（代理奖励模型在实现前预选）、AlphaEval（免回测、可并行的代理指标）、AlphaPilot（短窗口 IC 代理奖励）。
- 减少重复计算：剪枝、指纹、增量求值与近似相似度。代表：AlphaEvolve（冗余剪枝与指纹）、AlphaGen（增量更新组合损失）、QBX（节点内容寻址的增量求值）、AutoAlpha（PCA 近似相似度）。
- 分级评价：先在小样本上粗筛，再做全量验证。代表：FactorMiner。
- 控制 LLM 上下文成本：QuantEvolver 用强化微调把经验写进轻量模型参数；评价整体效率时仍须计入种子生成与训练成本。
- 相邻方法：GFlowNet 的代理奖励加少量真实评价、DeepMind AlphaEvolve 的评价级联、Tree-GRPO 的共享前缀采样。

## P4 学习信号稀疏、延迟且不可微

- 让奖励更密集：RiskMiner（合法中间表达式即时奖励）、TLRS（专家子序列轨迹级塑形）。
- 基线与探索信号：QFR（不带价值网络的 REINFORCE 加贪婪基线）、AlphaQCM（累积回报分布方差作为探索奖励）。
- 改变学习目标：AlphaForge（可微预测器把 fitness 变成梯度）、AlphaSAGE（按奖励成比例采样的轨迹平衡）、AlphaPADI（把池级奖励转成池对偏好）。
- 增广状态：AlphaPareto 把当前因子池编码进策略状态，让策略感知奖励所依赖的池；表示能否充分保留相关信息仍需检验。
- LLM 的强化微调：QuantEvolver（组内相对优势）、AlphaPilot（多轮工具调用与池级轨迹奖励）、AlphaDiverse（Planner 与 Realizer 分角色的联合 GRPO）。
- 相邻方法：DSR、GFlowNet、Trajectory Balance，以及多轮智能体步骤级信用分配的 GiGPO、Tree-GRPO。
- 观察：公式动作、多轮工具调用与编辑记忆有不同的信用分配对象，训练目标需与决策粒度对应。三类公式生成器的梯度路径见[训练机制对照](generator_training_with_ic.md)。

## P5 低信噪比下的过拟合

- 评估隔离：Agora/SJS（最终评估数据对参与搜索的智能体密封）、AlphaDiverse（内层期研究、外层期冻结后一次评估）。
- 稳健性目标：AlphaPareto 把排序的时间稳定性与扰动稳健性写入奖励，不只追求 IC。
- 经验复用的信用校正：AlphaMemo 以父子 AST 差异为编辑单元、按父因子质量分桶计算残差信用，减少对继承高分的重复计功；论文限定其不构成过拟合保证。
- 准入闸门与样本外冻结：AgenticFactorInvesting 用经济理由约束、显著性门槛与样本外冻结三层闸门筛因子；其显著性门槛未与搜索规模挂钩，见[单篇证据与局限](../notes/cards/2026_AgenticFactorInvesting.md)。
- 复杂度与风险控制：AlphaAgent（AST 节点数、参数数、特征数正则）、Alpha-Jungle（在评价中给过拟合风险打分）。
- 结果诊断与试验记录：Alpha-R1 报告概率夏普比率、紧缩夏普比率与回测过拟合概率，结论仍依赖试验数和比较集等假设；QBX 记录候选身份与试验数，账本不直接产生有效 p 值或校正结果。
- 搜索过程诊断：EvoQuantLab 在预登记的区块置换零假设下重跑等预算伪搜索，比较真实与零假设下的最高开发分数；这不是对每个交付因子的错误率控制。
- 过拟合度量：FactorBench 报告训练到测试的配对退化。
- 相邻方法：Publication Bias 在显式发表选择模型下估计经验贝叶斯收缩幅度与文中定义的 FDR，并澄清样本外衰减的归因；Sequential Cauchy 从一族有效 p 值指认具体拒绝项，无需估计相关矩阵，但强 FWER 控制依赖分布假设与渐近条件。见[可迁移的相邻方法](adjacent/transferable_methods.md)。
- 观察：QBX 的计数、EvoQuantLab 的搜索过程诊断与相邻方法的错误率控制不能直接互换；即使记录全部候选，同一数据上的自适应选择仍需进入推断。分工与迁移条件见[搜索规模与过拟合校正](search_multiplicity.md)。

## P6 前视偏差与信息泄漏

- 表示层检查：QBX 在编译期、加载数据之前检查时间可用性。
- 执行层检查：CogAlpha（质量检查器中的时间泄漏检查）、AlphaSchema（实现代码须通过前视筛查）、AlphaDiverse（拒绝用到未来信息的规格，并在切分边界 purge）。
- 数据密封与协议：Agora/SJS（持有期数据不进入任何面向模型的输入）、Alpha-R1（point-in-time 成分、数据截止表与前视审计）、FactorEngine（只用测试期之前的研报）、Auditing LLM Alpha-Factor Mining（在接触样本外数据前冻结候选清单）。
- 知识截止对照：Look-Ahead-Bench 用知识截止前后两期的表现落差诊断潜在前视；市场变化与模型记忆效应仍有混杂，不能仅由表现落差确认泄漏。

## P7 因子同质化与冗余

- 以池为目标：AlphaGen（加入池后的组合 IC 边际贡献作为奖励）、AlphaPADI（池上下文进入生成状态）、AlphaForge（入库检查相关性阈值）。
- 在生成端施加多样性：AlphaSAGE（以奖励比例分布为采样目标，配合新颖性奖励）、AutoAlpha（质量-多样性搜索）、AlphaPareto（协方差特征值熵奖励）、MAPLE（成对相关正则）、AlphaDiverse（每轮覆盖不同经济机制）。
- 结构和行为去重：AlphaAgent（AST 相似度）、Alpha-Jungle（高频子树规避）、Hubble（因子家族感知评分）、QBX（四级身份阶梯识别别名与值克隆）。
- 记忆与检索：FactorMiner（经验记忆记录应避开的高相关区域）、AlphaPROBE（谱系图上的多样性检索）。
- 多样性度量：AlphaEval（协方差特征值熵）、FactorBench（方法内冗余与方法间收敛）。
- 相邻方法：GFlowNet 以奖励比例分布为目标，Trajectory Balance 提供对应训练约束；多模式覆盖仍依赖奖励与优化条件，不保证行为低相关。
- 观察：结构去重、采样分散和组合增量是不同层次；生成目标中的多样性需要用信号行为与下游组合对照检验。

## P8 挖掘目标与实际使用脱节

- 组合目标进入挖掘：AlphaGen（组合 IC 边际贡献作为奖励）、AlphaPADI（以整个因子池为生成单元）、AlphaPilot（按对组合信号的边际贡献入池）、RD-Agent(Q)（因子与模型联合优化）。
- 挖掘与组合解耦：AlphaForge（使用阶段动态选因子、动态加权）、AlphaGAT（GAT-PPO 学习动态权重）、Alpha-R1（LLM 推理决定因子启停）、EFS（稀疏组合选股）。
- 可交易性进入评价：Alpha-Jungle 与 Hubble（换手率进入候选评分）、FactorBench（统一合成方式后报告扣费组合表现）。

## P9 非平稳与因子衰减

- 稳定性目标：QFR 在奖励中加入信息比率，抑制 IC 随时间的剧烈波动。
- 面向衰减与拥挤的设计：AlphaAgent 把原创性约束写入生成目标；Hubble 的负向检索提示应避开的拥挤模板。原创性或低相关性本身不足以证明信号更耐衰减。
- 随状态调整使用：AlphaForge（滚动窗口动态选因子）、Alpha-R1（按市场状态推理因子启停）、AlphaPilot（逐日按市场状态重新搜索并更新因子池）。

## P10 评估口径不统一、难以复现

- 统一评测与基准：AlphaEval（统一多维指标与数据切分）、FactorBench（共享数据、目标、切分与执行契约，接入多种方法的官方实现）。
- 标准化与留痕：QBX（携带证据的中间表示、内容身份与试验账本）、Hubble（持久化每个候选的多维诊断）、FactorMiner（技能模块中的标准化评估协议）。
- 证据审计：Auditing LLM Alpha-Factor Mining 核对指标统计总体、计数口径与结果留存方式。
- 观察：基线原生组合器与共同组合器回答不同问题，不能把受控预测比较扩大为完整框架排名；具体差异见[评估口径对照](evaluation_protocol.md)。
