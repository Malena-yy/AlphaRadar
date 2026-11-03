# 各问题的应对机制

> 问题的定义、边界和跟踪关注点见 README“出发点：因子挖掘面临的问题”。本文按问题汇总已收录工作中的对应机制，只列速读卡中有对应机制描述的论文，不是完整清单。
> `scripts/build_index.py` 会核对每个问题下点名的工作与 `papers.yaml` 的 `problems` 标注是否一致。

## P1 表达空间巨大，有效因子稀少

- 生成时约束：动作掩码与栈规则（AlphaGen），寄存器程序表示与维度检查（Alpha2），面向 alpha 的上下文无关文法与语义、长度约束（AlphaCFG），白名单 AST 沙箱（Hubble）。
- 利用结构的搜索：MCTS 显式复用已探索结构（RiskMiner、Alpha-Jungle），从低阶到高阶的层次化搜索（AutoAlpha），因子谱系图上的有偏演化（AlphaPROBE），宏观逻辑演化与微观参数优化分离（FactorEngine）。
- 先验引导：研究员想法与层次化字段检索（Alpha-GPT），研究员想法贯穿研究、建模、分析全流程（Alpha-GPT 2.0），持续积累并检索的信号知识库（QuantAgent），经验回放中注入优质种子公式（Synergistic RL），从研报和专家因子抽取初始程序池（FactorEngine）。

## P2 表达能力与可解释性的权衡

- 扩展表达能力：矩阵和向量算子与行业关系注入（AlphaEvolve），扩展算子集与长窗口（Synergistic RL），符号-数值混合词表生成含常数的公式（HRFT/IRFT），神经网络直接输出 alpha（AlphaGAT 第一阶段），图灵完备程序或代码演化（FactorEngine、CogAlpha），从文本、表格、图像材料中抽取因子线索（LLM Strategy Finding）。
- 保持可解释：假设、描述、表达式之间的一致性校验（AlphaAgent、QuantaAlpha）。

## P3 评价成本高

- 减少真实评价：用可微预测器代替部分真实评价来引导生成（AlphaForge），冗余剪枝与指纹机制跳过重复计算（AlphaEvolve），PCA 近似相似度降低去重成本（AutoAlpha）。
- 降低 LLM 循环成本：用 RFT 把经验写入轻量模型参数，代替不断增长的提示词上下文（QuantEvolver）。

## P4 学习信号稀疏、延迟且不可微

- 让奖励更密集：合法中间表达式即时奖励（RiskMiner），专家子序列轨迹级塑形与奖励中心化（TLRS）。
- 降低方差、稳定探索：不带价值网络的 REINFORCE 加贪婪基线（QFR），奖励分布方差作为探索奖励（AlphaQCM）。
- 改变学习目标：可微预测器把 fitness 变成生成器的梯度（AlphaForge），预测性能、结构对齐与新颖性的多信号奖励加轨迹平衡（AlphaSAGE），组内相对优势更新（QuantEvolver）。

## P5 低信噪比下的过拟合

- 稳定性目标：奖励中加入信息比率（QFR）。
- 复杂度与风险控制：AST 节点数、参数数、特征数正则（AlphaAgent），在评价中显式给过拟合风险打分（Alpha-Jungle）。
- 评估隔离：最终评估数据对参与搜索的智能体保持密封（Agora/SJS）。

## P6 前视偏差与信息泄漏

- 代码级检查：多智能体质量检查器中包含时间泄漏检查（CogAlpha）。
- 评估数据密封：持有期评估数据不进入任何面向模型的输入（Agora/SJS）。

## P7 因子同质化与冗余

- 以池为目标：用加入因子池后的组合 IC 边际贡献作为奖励（AlphaGen），入库同时检查 IC、ICIR 和相关性阈值（AlphaForge）。
- 在生成端施加多样性：生成器损失中的多样性项（AlphaForge），结构对齐与新颖性奖励下覆盖多个高奖励模式（AlphaSAGE），质量-多样性搜索（AutoAlpha），协方差非对角项惩罚（AlphaGAT）。
- 结构和行为去重：中间奖励中加入与已有因子的 MutIC 重复惩罚（RiskMiner），演化中剪枝与既有因子高度相关的表达式（AlphaEvolve），AST 相似度（AlphaAgent），高频子树规避（Alpha-Jungle），因子家族感知评分（Hubble），经验记忆记录应避开的高相关区域（FactorMiner），多样性与互补性奖励（QuantEvolver），复杂度、结构相似度与输出相关性控制（QuantaAlpha），谱系图上的多样性检索（AlphaPROBE），相关性去重（RD-Agent(Q)）。

## P8 挖掘目标与实际使用脱节

- 组合目标进入挖掘：组合 IC 边际贡献作为奖励（AlphaGen），因子与模型联合优化（RD-Agent(Q)）。
- 挖掘与组合解耦：挖掘阶段扩大候选池，使用阶段再动态选因子、动态加权（AlphaForge），GAT-PPO 学习动态权重（AlphaGAT），稀疏组合选股（EFS），动态优化因子权重（LLM Strategy Finding），用 LLM 推理决定因子启停（Alpha-R1）。
- 可交易性进入评价：把换手率纳入候选评分（Alpha-Jungle、Hubble）。

## P9 非平稳与因子衰减

- 抗衰减与抗拥挤：把原创性约束写入生成目标以对抗衰减（AlphaAgent），负向检索提示应避开的拥挤模板（Hubble）。
- 随状态调整使用：滚动窗口动态选因子（AlphaForge），根据市场状态推理因子启停（Alpha-R1）。

## P10 评估口径不统一、难以复现

- 标准化与留痕：技能模块中封装标准化评估协议（FactorMiner），持久化保存每个候选的多维诊断和提示词元数据（Hubble）。
