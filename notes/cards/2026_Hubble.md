# Hubble：Hubble: An LLM-Driven Agentic Framework for Safe, Diverse, and Reproducible Alpha Factor Discovery

> - 元数据：`papers.yaml` 中 `id: hubble-2026`；路线：`llm-agent`；标签：`llm`, `rag`, `safety`。
> - 针对问题：`P1 search-space`、`P7 redundancy`、`P8 objective-gap`、`P9 decay`、`P10 reproducibility`。
> - 来源：首轮检索整理，检索截至 2026-07-11。

* **作者单位：** 官方摘要页未展示单位信息；作者为 Runze Shi、Shengyu Yan、Yuecheng Cai、Chengxi Lv。

* **发表时间：** 2026.03（arXiv v1；v2 为 2026.04）。

* **论文链接：** https://arxiv.org/abs/2604.09601

* **开源项目：** 未见官方开源。

* **主要工作/创新点：** Hubble 强调大语言模型公式因子挖掘的工程安全、可复现和诊断完整性。系统不让模型直接生成任意 Python，而是限制在精选 DSL 和抽象语法树沙箱中：只允许白名单 AST 节点、限制表达式深度和节点数、校验变量和算子签名，避免任意代码执行。生成侧引入双通道检索增强生成：正向检索提供值得学习的机制，负向检索提供应避免的拥挤模板；选择侧使用因子家族感知评分，把预测力、稳定性、换手率、覆盖率、复杂度、拥挤度、相似度和因子家族集中度统一评分。所有候选因子都持久化保存 RankIC、Pearson IC、分组收益、多空收益差、换手率、覆盖率、复杂度和提示词元数据。

* **可参考点：** 1）LLM 因子生成应优先做 DSL 和 AST 安全沙箱；2）positive/negative RAG 可同时促进探索和规避拥挤；3）family-aware selection 能防止最终 top-k 又集中到单一模板；4）持久化诊断结果有助于复现实验和人工复盘。
