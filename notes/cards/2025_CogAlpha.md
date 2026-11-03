# CogAlpha：Cognitive Alpha Mining via LLM-Driven Code-Based Evolution

> - 元数据：`papers.yaml` 中 `id: cogalpha-2025`；路线：`llm-agent`；标签：`llm`, `code-evolution`。
> - 针对问题：`P2 expressiveness`、`P6 leakage`。
> - 来源：首轮检索整理，检索截至 2026-07-11。

* **作者单位：** 中国移动九天研究院、香港大学计算与数据科学学院、Grace Investment Machine。

* **发表时间：** 2025.11（arXiv v1；v3 为 2026.04）。

* **论文链接：** https://arxiv.org/abs/2511.18850

* **开源项目：** 论文称代码将发布；截至本次检索未见官方仓库。

* **主要工作/创新点：** CogAlpha 提出“认知式 Alpha 挖掘”，目标是让大语言模型不只是重复已有公式模板，而是通过多层次推理和进化搜索进行更宽、更深的结构探索。其核心包含七层代理体系，分别关注市场结构与周期、极端风险、价量动态、波动行为、多尺度复杂性、稳定性与市场状态门控、几何与融合等方向；随后用多智能体质量检查器检查代码语法、执行稳定性、逻辑合理性、数值异常和时间泄漏；通过 IC、RankIC、信息比率和互信息等指标过滤候选因子；最后通过“思考演化”对合格因子进行精炼、变异和重组。与领域特定语言（DSL）公式相比，CogAlpha 更强调代码级 Alpha 表示，扩大表达空间，但也需要更强的安全和可审计约束。

* **可参考点：** 1）用多层专家视角引导 LLM 产生多样假设；2）质量检查器必须覆盖代码执行、数值稳定和时间泄漏；3）code-based 表达更灵活，但要配套 DSL/AST 或 sandbox；4）thinking evolution 可与 QuantaAlpha/FactorEngine 的轨迹演化结合。
