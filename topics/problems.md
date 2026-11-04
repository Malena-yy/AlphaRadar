# 各问题的应对机制

> 问题的定义、边界和跟踪关注点见 README“出发点：因子挖掘面临的问题”。本文按问题汇总已收录工作中的对应机制，只列速读卡中有对应机制描述的论文，不是完整清单。
> `scripts/build_index.py` 会核对每个问题下点名的工作与 `papers.yaml` 的 `problems` 标注是否一致。

## P1 表达空间巨大，有效因子稀少

- 生成时约束：动作掩码与栈规则（AlphaGen），寄存器程序表示与维度检查（Alpha2），面向 alpha 的上下文无关文法与语义、长度约束（AlphaCFG），白名单 AST 沙箱（Hubble），因子 DSL 约束表达空间（QuantEvolver），评价工具强制 DSL 文法校验并记忆已试因子以避免重复失败（AlphaPilot），编译器准入与闭合图编辑，只产出类型正确、可执行的程序（QBX）。
- 利用结构的搜索：MCTS 显式复用已探索结构（RiskMiner、Alpha-Jungle），从低阶到高阶的层次化搜索（AutoAlpha），因子谱系图上的有偏演化（AlphaPROBE），宏观逻辑演化与微观参数优化分离（FactorEngine），以五元交易语义计划为搜索对象、代理模型在实现前预选候选（AlphaSchema）。
- 先验引导：研究员想法与层次化字段检索（Alpha-GPT），研究员想法贯穿研究、建模、分析全流程（Alpha-GPT 2.0），持续积累并检索的信号知识库（QuantAgent），经验回放中注入优质种子公式（Synergistic RL），从研报和专家因子抽取初始程序池（FactorEngine），从文本、表格、图像材料中抽取种子因子（LLM Strategy Finding），多层代理与多种改写模式扩大有效搜索（CogAlpha），经济机制目录约束研究方向并按计划检索少量特征与算子（AlphaDiverse）。
- 相邻方法（可迁移）：采样时按先验约束屏蔽非法 token、免去事后拒绝（DSR），用带历史程序与得分上下文的 LLM diff 代替手写变异算子（DeepMind AlphaEvolve）。

## P2 表达能力与可解释性的权衡

- 扩展表达能力：矩阵和向量算子与行业关系注入（AlphaEvolve），符号-数值混合词表生成含常数的公式（HRFT/IRFT），神经网络直接输出 alpha（AlphaGAT 第一阶段），可执行程序或代码演化（FactorEngine、CogAlpha）。
- 保持可解释：假设、描述、表达式之间的一致性校验（AlphaAgent、QuantaAlpha），把生成公式反编译为自然语言解释（Alpha-GPT），先声明语义计划再生成代码，代码注释逐项对应计划组件（AlphaSchema），用 LLM 评分金融逻辑并与人工专家排序对照（AlphaEval）。
- 量化权衡：实测受限、可审计的程序空间的广度代价，并以 LLM 与类型化搜索的混合弥补（QBX）。
- 相邻方法（可迁移）：演化整份代码与多个组件，以可读程序而非黑箱模型作为解（DeepMind AlphaEvolve）。

## P3 评价成本高

- 减少真实评价：用可微预测器代替部分真实评价来引导生成（AlphaForge），冗余剪枝与指纹机制跳过重复计算（AlphaEvolve），增量更新组合损失避免重算（AlphaGen），PCA 近似相似度降低去重成本（AutoAlpha），搜索阶段的维度预剪枝排除不可能合法的程序（Alpha2），小资产集粗筛后再做全量验证与相关性剪枝（FactorMiner），按去重后的规范式计评价预算，偏好学习复用已评分的因子池（AlphaPADI），代理奖励模型在 LLM 实现与回测之前打分并分配预算（AlphaSchema），以短窗口 IC 代理奖励代替逐轨迹完整回测（AlphaPilot），免回测、可并行的代理指标替代顺序组合回测（AlphaEval），节点内容寻址的增量求值与微秒级编译准入（QBX）。
- 降低 LLM 循环成本：用 RFT 把经验写入轻量模型参数，代替不断增长的提示词上下文（QuantEvolver）；参数实例化不额外调用大模型（FactorEngine）。
- 相邻方法（可迁移）：用代理奖励训练生成器、每轮只把多样候选批次送真实评价（GFlowNet），评价级联先小规模初筛再全量评价并异步并行（DeepMind AlphaEvolve），共享前缀的树搜索在同等预算下获得更多 rollout（Tree-GRPO）。

## P4 学习信号稀疏、延迟且不可微

- 让奖励更密集：合法中间表达式即时奖励（RiskMiner），专家子序列轨迹级塑形与奖励中心化（TLRS）。
- 降低方差、稳定探索：不带价值网络的 REINFORCE 加贪婪基线（QFR），奖励分布方差作为探索奖励（AlphaQCM）。
- 外部反馈驱动：外层循环用真实回测结果更新信号知识库，供下一轮生成检索（QuantAgent）。
- 改变学习目标：可微预测器把 fitness 变成生成器的梯度（AlphaForge），预测性能、结构对齐与新颖性的多信号奖励加轨迹平衡（AlphaSAGE），组内相对优势更新（QuantEvolver），把不可微的池级奖励转成池对偏好，用扩散重建似然做偏好学习（AlphaPADI），以最终因子池的未来窗口表现作轨迹奖励训练多轮工具调用策略（AlphaPilot），Planner 与 Realizer 分角色计算组内优势的联合 GRPO（AlphaDiverse）。
- 补全状态：冻结 LLM 把当前因子池编码进策略状态，缓解池依赖奖励的非平稳（AlphaPareto）。
- 相邻方法（可迁移）：以批内奖励分位数为基线、只用高分尾部样本更新策略（DSR），把终端奖励作为流守恒的边界条件并可离策略复用已评价样本（GFlowNet），整条轨迹一个残差同时更新各步概率（Trajectory Balance），按跨轨迹重复出现的锚点状态分组估计步骤级相对优势（GiGPO），比较分叉点兄弟子树的结果奖励构造过程信号（Tree-GRPO）。

## P5 低信噪比下的过拟合

- 复杂度与风险控制：AST 节点数、参数数、特征数正则（AlphaAgent），在评价中显式给过拟合风险打分（Alpha-Jungle）。
- 评估隔离：最终评估数据对参与搜索的智能体保持密封（Agora/SJS），内层期研究、外层期冻结后一次评估，并用噪声因子校准奖励阈值（AlphaDiverse）。
- 显著性控制：对筛选结果做概率夏普比率、紧缩夏普比率（Deflated Sharpe Ratio）和回测过拟合概率等多重检验校正（Alpha-R1），按根身份去重的试验账本为多重检验校正提供分母（QBX）。
- 稳健性目标：把排序的时间稳定性与扰动稳健性写入多目标奖励，不只追求 IC（AlphaPareto）。
- 过拟合度量：训练期固定因子方向，报告训练到测试的配对退化（FactorBench）。

## P6 前视偏差与信息泄漏

- 代码级检查：多智能体质量检查器中包含时间泄漏检查（CogAlpha），实现代码须通过前视泄漏筛查（AlphaSchema），执行时拒绝用到未来信息的因子规格并在切分边界按标签重叠做 purge（AlphaDiverse），编译期检查时间可用性效应，拒绝契约可见的前视（QBX）。
- 评估数据密封：持有期评估数据不进入任何面向模型的输入（Agora/SJS）。
- 数据边界与审计：point-in-time 成分、各模块数据截止表与前视内容审计（Alpha-R1），启动资料限定使用测试期之前的研报（FactorEngine），审计按样本外结果留存的因子目录，并给出在接触样本外数据前冻结候选清单的协议（Auditing LLM Alpha-Factor Mining）。
- 泄漏度量：比较知识截止前后两期的超额收益落差，并对照时点化 LLM 检测前视（Look-Ahead-Bench）。

## P7 因子同质化与冗余

- 扩大候选多样性：扩展算子集与长窗口降低组合中的因子相关性（Synergistic RL）。
- 以池为目标：用加入因子池后的组合 IC 边际贡献作为奖励（AlphaGen），入库同时检查 IC、ICIR 和相关性阈值（AlphaForge），池上下文进入生成状态，与池内最近邻相关超过阈值即受罚（AlphaPADI）。
- 在生成端施加多样性：生成器损失中的多样性项（AlphaForge），结构对齐与新颖性奖励下覆盖多个高奖励模式（AlphaSAGE），质量-多样性搜索（AutoAlpha），协方差非对角项惩罚（AlphaGAT），池内信号协方差特征值熵作为多样性奖励（AlphaPareto），单模型多输出加成对绝对相关正则（MAPLE），池得分含协方差谱熵多样性项、满池时替换最冗余成员（AlphaPilot），每轮计划须覆盖不同经济机制并以 log-det 多样性项为奖励（AlphaDiverse）。
- 结构和行为去重：中间奖励中加入与已有因子的 MutIC 重复惩罚（RiskMiner），冗余算子、冗余 Alpha 剪枝与集合级相关性阈值剔除（AlphaEvolve），价值目标中的结构相似度惩罚（AlphaCFG），AST 相似度（AlphaAgent），高频子树规避（Alpha-Jungle），因子家族感知评分（Hubble），经验记忆记录应避开的高相关区域（FactorMiner），多样性与互补性奖励（QuantEvolver），复杂度、结构相似度与输出相关性控制（QuantaAlpha），谱系图上的多样性检索（AlphaPROBE），相关性去重（RD-Agent(Q)），层次聚类去重与基于随机矩阵理论的软去重（EFS），按事件与情境覆盖度分配探索名额、导出池做相关性去冗余（AlphaSchema），四级身份阶梯识别别名与值克隆，并以生态位惩罚降低相关（QBX）。
- 多样性度量：以协方差特征值熵度量因子集的多样性与共线性（AlphaEval），度量方法内冗余、方法间收敛及与经典公式库的重复（FactorBench）。
- 相邻方法（可迁移）：按奖励成比例采样以保留多个高奖励模式（GFlowNet），在比例采样下改进分布拟合、样本更分散（Trajectory Balance），MAP-Elites 与岛模型式程序库在改进与多样性之间权衡（DeepMind AlphaEvolve）。

## P8 挖掘目标与实际使用脱节

- 组合目标进入挖掘：组合 IC 边际贡献作为奖励（AlphaGen、RiskMiner），因子与模型联合优化（RD-Agent(Q)），以整个因子池为生成单元，直接优化联合组合的表现（AlphaPADI），极端秩加权损失聚焦只做多组合实际使用的头部排名（MAPLE），按对组合信号的边际贡献决定入池与替换（AlphaPilot），以加入后组合预测得分的增益决定保留与奖励（AlphaDiverse）。
- 挖掘与组合解耦：挖掘阶段扩大候选池，使用阶段再动态选因子、动态加权（AlphaForge），GAT-PPO 学习动态权重（AlphaGAT），稀疏组合选股（EFS），动态优化因子权重（LLM Strategy Finding），用 LLM 推理决定因子启停（Alpha-R1），动态因子整合器加带成本回测（AlphaPROBE），组合构建与交易清单风险过滤（Alpha-GPT 2.0）。
- 可交易性进入评价：把换手率纳入候选评分（Alpha-Jungle、Hubble），以相对秩熵作换手代理并验证其与年化换手负相关（AlphaEval），统一选因子与合成方式后报告扣费的纯多头与多空表现（FactorBench）。

## P9 非平稳与因子衰减

- 稳定性目标：奖励中加入信息比率，抑制 IC 随时间的剧烈波动（QFR）。
- 抗衰减与抗拥挤：把原创性约束写入生成目标以对抗衰减（AlphaAgent）；拥挤度控制见 P7 下 Hubble 的负向检索。
- 随状态调整使用：滚动窗口动态选因子（AlphaForge），根据市场状态推理因子启停（Alpha-R1），逐日按市场状态描述重新搜索并更新保留池（AlphaPilot）。

## P10 评估口径不统一、难以复现

- 标准化与留痕：技能模块中封装标准化评估协议（FactorMiner），持久化保存每个候选的多维诊断和提示词元数据（Hubble），携带证据的中间表示、内容身份与试验账本（QBX），核对指标统计总体与计数口径、全量队列记账并版本化重算（Auditing LLM Alpha-Factor Mining）。
- 统一评测与基准：统一多维指标与数据切分横向评测多个挖掘模型并开源（AlphaEval），共享数据、目标、切分与执行契约接入九种方法的官方实现（FactorBench）。
