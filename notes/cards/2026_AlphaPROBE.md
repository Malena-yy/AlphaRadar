# AlphaPROBE：AlphaPROBE: Alpha Mining via Principled Retrieval and On-graph biased evolution

> - 元数据：`papers.yaml` 中 `id: alphaprobe-2026`；路线：`formulaic`, `pool-combination`；标签：`evolutionary`, `factor-lineage`。
> - 针对问题：`P1 search-space`、`P7 redundancy`。
> - 来源：首轮检索整理，检索截至 2026-07-11。

* **作者单位：** 官方摘要页未展示单位信息；作者包含 Taian Guo、Haiyang Shen、Junyu Luo、Binqi Chen、Hongjun Ding、Jinsheng Huang、Luchen Liu、Yun Ma、Ming Zhang。

* **发表时间：** 2026.02（arXiv v1）。

* **论文链接：** https://arxiv.org/abs/2602.11917

* **开源项目：** 官方仓库：https://github.com/gta0804/AlphaPROBE

* **主要工作/创新点：** AlphaPROBE 将公式化因子研究组织为有向无环图上的有偏演化搜索。每个节点表示一个因子候选，边表示从父因子到子因子的改写、组合或变异关系；检索器综合因子自身质量、谱系深度、被检索次数、与已有因子的数值/语义/语法多样性，选择最有潜力的父节点。生成器再利用该父节点从根到当前节点的完整演化路径，生成更有上下文的新候选，避免重复做已经无效的局部修改。与传统遗传规划或强化学习只维护种群、序列轨迹不同，AlphaPROBE 显式保存因子谱系和图拓扑，有助于分析哪些结构改写带来边际收益。

* **可参考点：** 1）把因子演化轨迹持久化为图，便于去重、溯源和人工复盘；2）on-graph biased exploration 可作为因子池扩展策略；3）需要结合严格样本外评估，避免图上高分分支被训练期过拟合持续放大。
