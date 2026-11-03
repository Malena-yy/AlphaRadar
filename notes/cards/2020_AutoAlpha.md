# AutoAlpha：AutoAlpha: an Efficient Hierarchical Evolutionary Algorithm for Mining Alpha Factors in Quantitative Investment

> - 元数据：`papers.yaml` 中 `id: autoalpha-2020`；路线：`formulaic`；标签：`genetic-programming`, `quality-diversity`。
> - 针对问题：`P1 search-space`、`P3 eval-cost`、`P7 redundancy`。
> - 来源：首轮检索整理，检索截至 2026-07-11。

* **作者单位：** 清华大学交叉信息研究院。

* **发表时间：** 2020.04（arXiv v2；v1 为 2020.02）。

* **论文链接：** https://arxiv.org/abs/2002.08245

* **开源项目：** 未见官方开源。

* **主要工作/创新点：** AutoAlpha 是自动公式因子挖掘中较早系统解决遗传规划低效率问题的工作。论文把公式 Alpha 表达为算子树，目标是在有限算力下找到尽可能多的高 IC、低相关公式。核心创新有三点：第一，提出层次化搜索，基于“大多数高阶有效 Alpha 至少包含一个有效低阶根基因”的经验假设，从低深度公式逐步扩展到高深度公式，避免在巨大树空间里完全随机搜索；第二，提出 PCA-QD，即基于第一主成分的质量-多样性搜索，用因子值矩阵的主成分近似因子相似性，降低相关性计算成本，并驱动种群远离已充分探索区域；第三，引入热启动和替换策略，先生成更大候选池再筛选初始化种群，并用子代与父代比较替换以抑制早熟收敛。

* **可参考点：** 1）从浅层表达式到深层表达式渐进生成；2）把“有效根基因”沉淀为后续复杂因子构件；3）用 PCA 近似相似度加速大规模因子去重；4）热启动、质量多样性搜索和父子替换适合移植到 RL/LLM 生成后的因子池维护。
