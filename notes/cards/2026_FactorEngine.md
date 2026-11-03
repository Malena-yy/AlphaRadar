# FactorEngine：FactorEngine: A Program-level Knowledge-Infused Factor Mining Framework for Quantitative Investment

> - 元数据：`papers.yaml` 中 `id: factorengine-2026`；路线：`llm-agent`；标签：`llm`, `code-evolution`。
> - 针对问题：`P1 search-space`、`P2 expressiveness`。
> - 来源：首轮检索整理，检索截至 2026-07-11。

* **作者单位：** 官方摘要页未展示单位信息；作者包含 Qinhong Lin、Ruitao Feng、Yinglun Feng、Zhenxin Huang、Yukun Chen、Zhongliang Yang、Linna Zhou、Binjie Fei、Jiaqi Liu、Yu Li。

* **发表时间：** 2026.03（arXiv v1；v2 为 2026.04）。

* **论文链接：** https://arxiv.org/abs/2603.16365

* **开源项目：** 未见官方开源；方法借鉴 OpenEvolve：https://github.com/algorithmicsuperintelligence/openevolve

* **主要工作/创新点：** FactorEngine 把因子表示从有限 DSL 公式扩展到图灵完备程序，并通过“宏观逻辑演化”和“微观参数优化”分离来提高表达力和效率。系统先用知识注入式启动模块，从金融研报和专家因子中抽取核心想法、伪代码和可执行 Python，形成初始程序池；演化阶段采用树结构程序池，每个节点都是一个可独立执行和评估的程序，用 UCT 准则选择高潜力节点。大语言模型负责宏观变异，即改写因子逻辑和结构；局部参数如窗口、衰减系数则交给贝叶斯优化做微观搜索。最后系统用回测反馈、经验链和多岛并行演化促进多样搜索。

* **可参考点：** 1）将逻辑演化和参数寻优解耦，减少 LLM 反复调参数的低效；2）研报到可执行因子的闭环抽取可扩展专家知识来源；3）树结构 program pool + UCT 可复用 MCTS 思想；4）代码级表达力更强，但必须有接口约束、执行沙箱和时间泄漏测试。
