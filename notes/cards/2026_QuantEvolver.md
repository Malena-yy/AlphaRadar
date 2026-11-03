# QuantEvolver：From Feedback Loops to Policy Updates: Reinforcement Fine-Tuning for LLM-Based Alpha Factor Discovery

> - 元数据：`papers.yaml` 中 `id: quantevolver-2026`；路线：`llm-agent`；标签：`llm`, `rft`, `grpo`。
> - 针对问题：`P3 eval-cost`、`P4 learning-signal`、`P7 redundancy`。
> - 来源：首轮检索整理，检索截至 2026-07-11。

* **作者单位：** 官方摘要页未展示单位信息；作者包含 Lingzhe Zhang、Tong Jia、Yunpeng Zhai、Zixuan Xie、Chiming Duan、Minghua He、Philip S. Yu、Ying Li。

* **发表时间：** 2026.05（arXiv v1）。

* **论文链接：** https://arxiv.org/abs/2605.15412

* **开源项目：** 官方仓库：https://github.com/QuantLLM/QuantEvolver（仓库说明仅包含可复用框架代码，不含私有市场数据、训练 checkpoint、实验日志或论文专用复现实验脚本）。

* **主要工作/创新点：** QuantEvolver 指出多数大语言模型因子挖掘依赖“提示词生成-评估-反馈”循环，随着轮次增长会出现上下文膨胀、反馈漂移、推理成本增加和结构重复。论文把可执行量化评价转为模型参数更新，使用强化微调让轻量矿工模型内化历史优化经验。流程包括：由高能力模型构造高质量种子因子；任务库构建器将种子、时间窗口、因子家族、变异提示和场景元数据组合成多样训练任务；矿工模型生成因子 DSL 表达式；因子实现器将其转为可执行代码；市场状态回测给出方向准确率、IC、RankIC、覆盖率等反馈；GRPO 再做组内相对优势更新。奖励函数 DiCo 将预测质量与结构多样性、行为互补性、精确重复惩罚、家族过度使用惩罚结合，最终高质量因子进入挖掘因子数据库。

* **可参考点：** 1）用 RFT/GRPO 替代长 prompt 反馈循环，降低上下文漂移；2）seed + regime-aware task bank 可稳定训练；3）DiCo Reward 适合同时优化预测性、多样性和互补性；4）最终产物应是因子数据库，不只是微调后的生成模型。
