# AlphaForge：AlphaForge: A Framework to Mine and Dynamically Combine Formulaic Alpha Factors

> - 元数据：`papers.yaml` 中 `id: alphaforge-2024`；路线：`formulaic`, `pool-combination`；标签：`generator-predictor`, `dynamic-combination`。
> - 针对问题：`P3 eval-cost`、`P4 learning-signal`、`P7 redundancy`、`P8 objective-gap`、`P9 decay`。
> - 来源：首轮检索整理，检索截至 2026-07-11。
> - 精读：[AlphaForge 核心算法解读](../deep/2024_AlphaForge.md)

* **作者单位：** 中国科学院大学、时代复兴投资管理有限公司、商丘师范学院、中国科学院计算技术研究所、York University、University of Toronto。

* **发表时间：** 2024.06（arXiv v1；AAAI 2025）。

* **论文链接：** https://arxiv.org/abs/2406.18394

* **开源项目：** https://github.com/dulyhao/alphaforge

* **主要工作/创新点：** AlphaForge 针对 AlphaGen 生成固定因子集合和固定权重的问题，提出两阶段框架。第一阶段是因子生成：使用生成器-预测器模型，生成器输出离散表达式矩阵，再通过规则掩码和 Gumbel-Softmax 近似采样转为公式；预测器学习候选因子的适配分数，生成器在最大化预测分数的同时降低两组采样因子的相似度，从而同时追求有效性和多样性。候选因子进入因子库时还要满足 IC、ICIR 以及与已有因子的相关性阈值，使挖掘目标随因子库状态变化。第二阶段是动态组合：给定候选因子池，在每个新市场窗口重新评估因子近期表现，选择排名靠前的若干因子并动态回归权重，生成随时间变化的综合交易信号 Mega-Alpha。

* **可参考点：** 1）因子挖掘与组合使用解耦，挖掘阶段尽量扩大候选池；2）surrogate predictor 可缓解真实回测奖励稀疏和昂贵问题；3）动态选因子和动态权重比固定组合更适应市场风格切换；4）生成器损失中直接加入多样性约束可避免候选池同质化。
