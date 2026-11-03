# Alpha-Jungle：Navigating the Alpha Jungle: An LLM-Powered MCTS Framework for Formulaic Factor Mining

> - 元数据：`papers.yaml` 中 `id: alpha-jungle-2025`；路线：`llm-agent`；标签：`llm`, `mcts`。
> - 针对问题：`P1 search-space`、`P5 overfitting`、`P7 redundancy`、`P8 objective-gap`。
> - 来源：首轮检索整理，检索截至 2026-07-11。

* **作者单位：** 官方摘要页未展示单位信息；作者为 Yu Shi、Yitong Duan、Jian Li。

* **发表时间：** 2025.05（arXiv v1；v3 为 2025.11；AAAI 2026）。

* **论文链接：** https://arxiv.org/abs/2505.11122

* **开源项目：** 未见官方开源。

* **主要工作/创新点：** Alpha-Jungle 将大语言模型与蒙特卡洛树搜索（MCTS）结合，专门用于公式化因子挖掘。每个 MCTS 节点是一条候选 Alpha 公式，选择阶段用 UCT 准则平衡探索和利用；扩展阶段不是随机动作，而是让模型根据当前节点的多维评价结果提出改进方向，再生成新的公式；评价阶段直接回测候选公式，并在有效性、稳定性、换手率、多样性和过拟合风险等维度打分；回传阶段更新路径上的节点价值。与传统 MCTS 不同，论文允许对任意内部节点继续扩展，以支持对已有好想法反复精炼。另一个关键机制是高频子树规避：从有效 Alpha 仓库中挖掘高频根基因或子树，并提示模型避免重复这些拥挤结构，从而提升结构多样性。

* **可参考点：** 1）LLM 负责语义化 refinement，MCTS 负责结构化探索；2）多维评价比单 IC 更适合给 LLM 反馈；3）高频子树规避可作为防同质化正则；4）内部节点可重复扩展，适合“从好因子继续微调”的研究工作流。
