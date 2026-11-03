# AlphaGen：Generating Synergistic Formulaic Alpha Collections via Reinforcement Learning

> - 元数据：`papers.yaml` 中 `id: alphagen-2023`；路线：`formulaic`；标签：`rl`, `ppo`, `rpn`, `pool-reward`。
> - 针对问题：`P1 search-space`、`P7 redundancy`、`P8 objective-gap`。
> - 来源：首轮检索整理，检索截至 2026-07-11。

* **作者单位：** 中国科学院计算技术研究所、中国科学院大学、华为 EI Innovation Lab。

* **发表时间：** 2023.05（KDD 2023）。

* **论文链接：** https://arxiv.org/abs/2306.12964

* **开源项目：** https://github.com/ICT-FinD-Lab/alphagen

* **主要工作/创新点：** 该工作通常被称为 AlphaGen，是公式化 Alpha 挖掘中较早将深度强化学习用于“组合因子集合生成”的代表性论文。论文把公式写成逆波兰表示（RPN）并建模为马尔可夫决策过程（MDP）：状态是已经生成的符号序列，动作是继续选择一个算子、特征、常量或结束符；生成时用栈规则和动作掩码排除形式非法动作，语义非法公式则给予惩罚，只有完整公式生成后才计算主要奖励。相比传统遗传规划或只优化单个因子的强化学习，AlphaGen 的关键创新是把新因子加入当前因子池后，对线性组合模型 IC 的边际贡献作为回报，并用 PPO 这类策略梯度方法训练生成器，使策略直接优化下游组合效果。训练过程中维护固定容量因子池，通过权重优化和优胜劣汰，保留对组合有增益且相关性较低的因子。

* **可参考点：** 1）组合 IC 奖励能直接对齐多因子使用场景；2）RPN token 生成便于用 PPO 等序列决策算法训练；3）固定容量因子池与线性权重联合优化是后续大量工作的 baseline；4）主要风险是奖励稀疏、非平稳、训练后期策略坍缩和固定权重泛化不足。
