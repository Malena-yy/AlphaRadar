# AlphaEvolve：AlphaEvolve: A Learning Framework to Discover Novel Alphas in Quantitative Investment

> - 元数据：`papers.yaml` 中 `id: alphaevolve-2021`；路线：`formulaic`；标签：`automl`, `evolutionary`。
> - 针对问题：`P2 expressiveness`、`P3 eval-cost`、`P7 redundancy`。
> - 来源：首轮检索整理，检索截至 2026-07-11。

* **作者单位：** 新加坡国立大学、北京理工大学、浙江大学。

* **发表时间：** 2021.04（SIGMOD 2021 / arXiv v2）。

* **论文链接：** https://arxiv.org/abs/2103.16196

* **开源项目：** 未见官方开源。

* **主要工作/创新点：** AlphaEvolve 用自动机器学习和进化搜索扩展传统公式 Alpha 的表示能力，目标是在保持可挖掘、可组合、弱相关的前提下，吸收机器学习 Alpha 对高维信息的表达优势。它把 Alpha 表示为一串操作指令，并引入能处理标量、向量、矩阵特征的算子，允许表达式访问更长周期和更高维的市场状态；同时选择性注入行业/板块关系信息，使因子可以建模股票间关系而不完全退化为黑盒模型。论文还提出冗余 Alpha 剪枝和指纹机制，在候选演化过程中淘汰不参与最终计算、与既有因子高度相关或重复计算的表达式，减少大规模任务评估成本。

* **可参考点：** 1）扩展公式因子的数据结构，不局限于标量量价字段；2）把行业关系、板块关系作为可选算子或上下文注入；3）搜索阶段即进行冗余剪枝；4）保持“弱相关集合”作为挖掘目标，而不是单因子最大化。
