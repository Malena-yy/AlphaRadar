# Synergistic RL：Synergistic Formulaic Alpha Generation for Quantitative Trading based on Reinforcement Learning

> - 元数据：`papers.yaml` 中 `id: synergisticrl-2024`；路线：`formulaic`；标签：`rl`, `rpn`。
> - 针对问题：`P1 search-space`、`P2 expressiveness`。
> - 来源：首轮检索整理，检索截至 2026-07-11。

* **作者单位：** 韩国光云大学机器人学部。

* **发表时间：** 2024.01（arXiv v1；v2 为 2024.07）。

* **论文链接：** https://arxiv.org/abs/2401.02710

* **开源项目：** 未见官方开源。

* **主要工作/创新点：** 论文在 AlphaGen 基础上做工程增量，重点解决原始动作空间偏小和冷启动探索效率不足。方法扩展算子集合，加入符号、截面排序、乘积、缩放、幂函数、偏度、峰度、排名、极值位置和条件判断等操作，并把时间窗口扩展到 60、120、252 等中长期尺度；同时把预先生成或已有的优质公式因子写入经验回放池，作为初始种子引导 PPO 策略向高质量区域探索。实验表明，在相同因子池容量下，扩展搜索空间和种子初始化能提高 CSI300 上的 IC/RankIC，但过大因子池也会出现边际收益下降。

* **可参考点：** 1）通过扩展算子和窗口提升搜索空间表达能力；2）用 Alpha101 或历史挖掘结果做 replay buffer 热启动；3）分阶段训练，先形成基础池再挖互补因子；4）需要监控搜索空间扩大后的训练稳定性和计算成本。
