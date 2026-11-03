# RD-Agent(Q)：R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization

> - 元数据：`papers.yaml` 中 `id: rd-agent-quant-2025`；路线：`llm-agent`；标签：`llm`, `multi-agent`, `factor-model-joint`。
> - 针对问题：`P7 redundancy`、`P8 objective-gap`。
> - 来源：首轮检索整理，检索截至 2026-07-11。

* **作者单位：** Microsoft Research / Microsoft 相关团队（论文作者包含 Yuante Li、Xu Yang、Xiao Yang、Minrui Xu、Xisen Wang、Weiqing Liu、Jiang Bian）。

* **发表时间：** 2025.05（arXiv v1；NeurIPS 2025）。

* **论文链接：** https://arxiv.org/abs/2505.15155

* **开源项目：** 官方仓库：https://github.com/microsoft/RD-Agent

* **主要工作/创新点：** RD-Agent(Q) 不是只挖公式因子，而是把量化研究拆成“因子挖掘”和“模型创新”两条闭环，并做联合优化。研究阶段由规格定义和假设生成单元根据目标、历史结果和领域先验形成因子或模型假设；开发阶段由 Co-STEER 代码生成代理实现任务代码，并运行真实市场回测；分析阶段统一评估指标并反馈下一轮，同时用带上下文的 Thompson 采样在“继续优化因子”与“优化模型”之间自适应调度。对于因子任务，系统会先做相关性去重，再将候选因子与当前最优模型结合评估。

* **可参考点：** 1）把因子挖掘从单算法扩展为完整 R&D 闭环；2）用知识森林和执行反馈沉淀研究经验；3）因子与模型联合优化能避免只优化单因子指标；4）多臂 bandit 调度可用于决定下一轮资源投向。
