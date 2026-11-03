# RiskMiner：RiskMiner: Discovering Formulaic Alphas via Risk Seeking Monte Carlo Tree Search

> - 元数据：`papers.yaml` 中 `id: riskminer-2024`；路线：`formulaic`；标签：`mcts`, `rl`。
> - 针对问题：`P1 search-space`、`P4 learning-signal`、`P7 redundancy`。
> - 来源：首轮检索整理，检索截至 2026-07-11。

* **作者单位：** 武汉人工智能研究院、北京大学光华管理学院、湘江实验室、哈尔滨工业大学、北京大学。

* **发表时间：** 2024.02（arXiv；ICAIF 2024 相关工作）。

* **论文链接：** https://arxiv.org/abs/2402.07080

* **开源项目：** 未见官方开源；非官方参考实现：https://github.com/carlosrod723/RiskMiner-Alpha-Discovery-MCTS

* **主要工作/创新点：** RiskMiner 认为 AlphaGen 类神经策略难以充分利用公式空间的树结构，同时平均回报优化不符合“找少量高质量 Alpha”的挖掘目标。论文将挖掘过程建模为奖励更密集的 MDP：当中间状态已经构成合法公式时，就根据 IC 以及与已有因子的 MutIC 重复惩罚给即时奖励；搜索器采用蒙特卡洛树搜索（MCTS）显式记录和复用已探索结构；策略训练采用风险偏好优化，关注回报分布的高分位而非均值，从而鼓励发现高回报尾部样本。MCTS 负责采样和结构化搜索，训练出的风险偏好策略再反过来指导树搜索中的节点选择和随机展开。

* **可参考点：** 1）用 MCTS 记录离散公式搜索空间，避免策略网络重复探索；2）用合法中间表达式奖励缓解稀疏反馈；3）分位数/风险偏好优化适合 Alpha 挖掘“追求极值”的目标；4）MutIC 惩罚适合与因子池准入机制结合，但计算成本需要缓存和近似。
