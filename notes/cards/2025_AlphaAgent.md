# AlphaAgent：AlphaAgent: LLM-Driven Alpha Mining with Regularized Exploration to Counteract Alpha Decay

> - 元数据：`papers.yaml` 中 `id: alphaagent-2025`；路线：`llm-agent`；标签：`llm`, `alpha-decay`。
> - 针对问题：`P2 expressiveness`、`P5 overfitting`、`P7 redundancy`、`P9 decay`。
> - 来源：首轮检索整理，检索截至 2026-07-11。

* **作者单位：** 中山大学、新南威尔士大学、南洋理工大学、鹏城实验室、香港中文大学（深圳）。

* **发表时间：** 2025.02（arXiv v1；KDD 2025）。

* **论文链接：** https://arxiv.org/abs/2502.16789

* **开源项目：** 官方仓库：https://github.com/RndmVariableQ/AlphaAgent

* **主要工作/创新点：** AlphaAgent 聚焦大语言模型生成因子容易同质化、拥挤和衰减的问题，提出带正则约束的多智能体闭环。系统包含想法代理、因子代理和评估代理：想法代理产生市场假设，因子代理用算子库和抽象语法树（AST）表达式实现因子，评估代理做可执行性、稳定性和回测评估。三类约束是核心：第一，用 AST 最大公共子树相似度度量新因子与 Alpha101 或既有因子库的结构相似性，强制保持原创性；第二，用大语言模型评分市场假设、因子描述和表达式之间的语义一致性，避免“说的是流动性，公式里没有成交量”这类错配；第三，用 AST 节点数、参数数和特征数控制复杂度，抑制过拟合。

* **可参考点：** 1）把抗 alpha decay 显式写入生成目标；2）AST 相似度适合做结构去重；3）假设-表达式一致性检查可提高因子可解释性；4）复杂度正则比事后筛选更适合融入 LLM 生成循环。
