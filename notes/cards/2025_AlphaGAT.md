# AlphaGAT：AlphaGAT: A Two-Stage Learning Approach for Adaptive Portfolio Selection

> - 元数据：`papers.yaml` 中 `id: alphagat-2025`；路线：`neural`, `pool-combination`；标签：`neural-alpha`, `gnn`, `rl`, `ppo`, `dynamic-combination`。
> - 针对问题：`P2 expressiveness`、`P7 redundancy`、`P8 objective-gap`。
> - 来源：首轮检索整理，检索截至 2026-07-11。
> - 精读：[AlphaGAT 核心算法解读](../deep/2025_AlphaGAT.md)

* **作者单位：** IJCAI 官方页面未展示单位信息；作者为 Shicheng Li、Jinshan Zhang、Feng Wang。

* **发表时间：** 2025（IJCAI 2025，Proceedings pages 7500-7508）。

* **论文链接：** https://www.ijcai.org/proceedings/2025/834

* **开源项目：** 未见官方开源。

* **主要工作/创新点：** AlphaGAT 面向组合选择，而不是公式型因子挖掘。论文提出两阶段学习框架：第一阶段用 CATimeMixer 从原始市场序列中生成多个神经 Alpha 因子，通过多尺度下采样、趋势/季节项分解、自上而下和自下而上的一维卷积，以及跨资产注意力机制提升信号质量；训练目标同时最大化平均 IC，并用协方差矩阵非对角项惩罚因子间相关性，以约束预测性和多样性。第二阶段把这些 Alpha 因子转成因子图状态，使用图注意力网络（GAT）作为策略网络建模因子间依赖，再用 PPO 动态学习因子权重，最终形成交易信号和排名前 G 的资产配置。

* **可参考点：** 1）适合作为后续组合器或因子图 reranker 的参考，而不是公式挖掘主线替代；2）Stage I 的 covariance penalty 可借鉴为因子多样性约束；3）Stage II 的 GAT/PPO 动态权重思路可与 rolling OLS/lstsq 等简单组合器对照；4）必须在正文中明确其输出是神经 alpha factors，不是可解释 DSL 公式。
