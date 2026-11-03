# LLM Strategy Finding：Automate Strategy Finding with LLM in Quant Investment

> - 元数据：`papers.yaml` 中 `id: llmstrategyfinding-2024`；路线：`llm-agent`；标签：`llm`, `multimodal`。
> - 针对问题：`P2 expressiveness`、`P8 objective-gap`。
> - 来源：首轮检索整理，检索截至 2026-07-11。

* **作者单位：** 官方摘要页未展示单位信息；作者为 Zhizhuo Kou、Holam Yu、Jingshu Peng、Lei Chen。

* **发表时间：** 2024.09。

* **论文链接：** https://arxiv.org/abs/2409.06289

* **开源项目：** 未见官方开源。

* **主要工作/创新点：** 该工作不是严格的强化学习公式 Alpha 生成算法，但补足了“大语言模型如何从金融文本、表格和图像研究材料中自动形成策略/因子假设”的路线。论文把多模态财经信息作为输入，用模型抽取策略关键要素，按动量、基本面、流动性等类别组织种子 Alpha，再通过多智能体市场评估和收益回测进行筛选，最后动态优化因子权重。与 Alpha-GPT 一类系统相比，它更强调从外部信息源抽取策略线索，而不是在固定 DSL 表达式空间内搜索。

* **可参考点：** 1）可作为研报、公告、图表到因子假设的上游模块；2）需要再接 DSL parser、时点一致性检查和样本外回测，才能进入公式因子池；3）它属于“想法发现/策略发现”相关工作，不应直接作为 RL 公式生成 baseline。
