# AlphaSAGE：AlphaSAGE: Structure-Aware Alpha Mining via GFlowNets for Robust Exploration

> - 元数据：`papers.yaml` 中 `id: alphasage-2025`；路线：`formulaic`；标签：`gflownet`, `gnn`。
> - 针对问题：`P4 learning-signal`、`P7 redundancy`。
> - 来源：首轮检索整理，检索截至 2026-07-11。
> - 精读：[AlphaSAGE 核心算法解读](../deep/2025_AlphaSAGE.md)

* **作者单位：** 官方摘要页未展示单位信息；作者为 Binqi Chen、Hongjun Ding、Ning Shen、Jinsheng Huang、Taian Guo、Luchen Liu、Ming Zhang。

* **发表时间：** 2025.09（arXiv v1；v3 为 2026.05）。

* **论文链接：** https://arxiv.org/abs/2509.25055

* **开源项目：** 官方仓库：https://github.com/BerkinChen/AlphaSAGE

* **主要工作/创新点：** AlphaSAGE 针对公式因子挖掘中完整公式生成后才有奖励、线性序列难以表达公式树结构、以及最大化期望奖励容易集中到少数相似公式的问题，提出结构感知的生成流网络（GFlowNet）框架。方法将候选公式表示为抽象语法树（AST）及其前缀状态，用关系图卷积网络（RGCN）编码算子、特征、常量以及滞后/时序关系，再由生成流网络的前向策略在语法合法动作中逐步采样下一个词元、算子或特征。公式完成后，奖励同时包含 IC/RankIC 等预测性能、结构感知对齐奖励和新颖性奖励，并通过轨迹平衡损失、熵正则和动态权重训练，使采样分布覆盖多个高奖励模式，而不是坍缩到少数相似公式。最终候选因子经过真实评估、准入过滤和相关性去重，进入高质量、多样化因子池。

* **可参考点：** 1）AST/RGCN 结构编码比纯 RPN/LSTM 更适合表达公式语义；2）GFlowNet 的多 mode 采样目标天然契合“因子池多样性”；3）性能、结构对齐和新颖性多信号奖励可缓解单 IC 奖励的模式坍缩；4）落地时仍需与样本外评估、准入规则和组合贡献约束结合。
