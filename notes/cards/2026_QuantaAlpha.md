# QuantaAlpha：QuantaAlpha: An Evolutionary Framework for LLM-Driven Alpha Mining

> - 元数据：`papers.yaml` 中 `id: quantaalpha-2026`；路线：`llm-agent`；标签：`llm`, `evolutionary`。
> - 针对问题：`P2 expressiveness`、`P7 redundancy`。
> - 来源：首轮检索整理，检索截至 2026-07-11。

* **作者单位：** 官方摘要页未展示单位信息；作者包含 Jun Han、Shuo Zhang、Wei Li、Yifan Dong、Tu Hu、Yumo Zhu、Xiaomin Yu、Xin Guo、Zhaowei Liu、Kunyi Wang、Jingping Liu、Tianyi Jiang、Ruichuan An、Sen Hu、Zhi Yang、Ronghao Che、Huacan Wang。

* **发表时间：** 2026.02（arXiv v1；v3 为 2026.05）。

* **论文链接：** https://arxiv.org/abs/2602.07085

* **开源项目：** 官方仓库：https://github.com/QuantaAlpha/QuantaAlpha

* **主要工作/创新点：** QuantaAlpha 将大语言模型因子挖掘过程视为可演化轨迹，而不是单轮生成表达式。每条轨迹覆盖假设生成、符号因子构造、代码实现和回测评估；系统先通过多样化规划初始化生成互补研究方向，再对高质量轨迹进行变异和交叉。变异阶段通过自反思定位导致低回报的步骤，只改写局部片段以保持轨迹连贯；交叉阶段复用不同高分轨迹中的假设模板、构造模式和修复行为。系统还对假设、语义描述、符号表达式和代码做一致性验证，并用复杂度、结构相似度和输出相关性控制冗余。

* **可参考点：** 1）把完整研究过程作为演化对象，而不只是公式本身；2）局部 mutation 可避免每轮从头生成导致的语义漂移；3）crossover 适合复用已验证经验片段；4）一致性 gate 和相关性过滤是 LLM 因子挖掘必备工程约束。
