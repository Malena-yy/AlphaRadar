# Alpha-R1：Alpha-R1: Alpha Screening with LLM Reasoning via Reinforcement Learning

> - 元数据：`papers.yaml` 中 `id: alpha-r1-2025`；路线：`llm-agent`, `pool-combination`；标签：`llm`, `grpo`, `factor-screening`。
> - 针对问题：`P8 objective-gap`、`P9 decay`。
> - 来源：首轮检索整理，检索截至 2026-07-11。

* **作者单位：** 官方摘要页未展示单位信息；作者包含 Zuoyou Jiang、Li Zhao、Rui Sun、Ruohan Sun、Zhongjian Li、Jing Li、Daxin Jiang、Zuo Bai、Cheng Hua。

* **发表时间：** 2025.12（arXiv v1）。

* **论文链接：** https://arxiv.org/abs/2512.23515

* **开源项目：** 官方仓库：https://github.com/FinStep-AI/Alpha-R1

* **主要工作/创新点：** Alpha-R1 不直接生成公式因子，而是面向因子筛选：给定大量候选因子，训练大语言模型根据市场语境推理哪些因子未来值得启用。论文先把价格指标、新闻和宏观叙事汇总成长期市场记忆与当前市场状态，再为每个候选因子生成机制画像，描述其适用市场环境、风险和衰减特征；推理核心根据因子画像和当前市场状态输出是否启用该因子的判断及解释。训练上采用两阶段路线，先通过监督微调学习解释与筛选格式，再用 GRPO 根据未来市场表现、推理质量、动作合法性和稀疏性约束优化筛选策略，其中市场奖励来自实际组合结果而不是人工偏好。实验还强调跨资产池回测和从 CSI300 到 CSI1000 的零样本泛化能力。它把强化学习从“公式生成器”移动到“因子激活/选择器”层面。

* **可参考点：** 1）可借鉴其 regime-aware 因子筛选思想；2）适合在已有因子池上做启停、打分和解释，不替代公式挖掘；3）训练数据必须严格按时间切分，避免用未来表现污染筛选理由。
