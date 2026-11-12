# 评估口径对照

> 本文依据单篇笔记与登记中的实验设置比较评估口径；文献版本与详细证据见各篇卡片，完整明细见[论文索引](../INDEX.md#setups)。重点是比较所需条件与已知混杂，不据跨论文数字给方法排名。涉及官方源码的结论单独注明版本与依据。

## 1. 比较对象

- 单因子评价、因子池预测与交易组合回答不同问题。IC 类指标不包含执行成本，扣费收益还受到组合器、成交时点和风险暴露影响。
- 覆盖市场包括 A 股、美股、港股、欧洲、日本与加密资产；非金融的相邻方法不属于股票因子挖掘实验比较。
- 登记的 `setup` 空值表示未披露或不适用；不能据此推断某种默认设置，也不能将空成本字段一律解释为未扣费回测。

## 2. 逐项差异

### 2.1 股票池

- **市场与股票池不同**：CSI300、CSI500、CSI1000、全市场与 SSE50 等不能等同。同一论文也可报告多个池，如 [AlphaSAGE v3](../notes/deep/2025_AlphaSAGE.md) 与 [AlphaPilot](../notes/cards/2026_AlphaPilot.md)。
- **成分身份与权重需区分**：按历史时点取成分与固定一组成分股不同，指数权重又是另一个设置。Agora/SJS、AutoScientist-Quant、Alpha-R1 说明了历史时点成分处理；未说明的工作不能默认使用 point-in-time 股票池。
- **跨市场测试不一定共用时间区间**：AlphaSAGE v3 的中国测试期为 2022–2024，美国测试期为 2018–2020。市场差异与时期差异相互混杂，不能仅由该对照推出跨市场泛化。

### 2.2 数据频率与标签

- 数据频率包括日频、分钟、小时与月度：[HRFT/IRFT](../notes/cards/2024_HRFT.md) 用 1 分钟数据，[FactorMiner](../notes/cards/2026_FactorMiner.md) 用 10 分钟 bar，[QuantEvolver](../notes/cards/2026_QuantEvolver.md) 比较 5 分钟、小时与日频任务，[CAVB](../notes/cards/2025_CAVB.md) 用月度公司特征和收益。
- **标签包括次日、多日与次月收益**：次日收益（AlphaAgent、QuantaAlpha、RD-Agent、AlphaRLM）、5 日（QFR、TLRS、Alpha-R1、AlphaSchema、MAPLE、RiskMiner 之一）、10 日与 30 日（Alpha-Jungle、X-Alpha）、20 日（AlphaGen、Alpha2、AlphaQCM、AlphaSAGE、AlphaPADI、AlphaForge 的 VWAP 口径等），以及 CAVB 的次月收益。
- **标签期限不等于实际持有期**：20 日预测标签仍可用于逐日调仓。还需核对收益起止点、价格口径与信号生效时点；例如 AlphaForge 使用 `VWAP[t+21]/VWAP[t+1]-1`，不能与当日收盘起算的 20 日标签视为完全相同。
- 若逐日计算多日收益标签，相邻标签会重叠，可能增强序列依赖；推断时不能将日数直接当作独立样本数。不同标签期限的 IC 也不宜直接排名。

### 2.3 训练 / 验证 / 测试切分

- 固定切分与滚动测试有不同的适应范围。例如 AlphaSAGE 使用固定切分；AlphaForge 在 2018–2022 逐年重训；CAVB 使用 20 年训练、10 年验证、1 年测试的年度滚动。
- **模型切分与搜索切分需分别说明**：[AutoScientist-Quant](../notes/cards/2026_AutoScientist-Quant.md) 将研究反馈窗与最终测试窗分开；[AlphaDiverse](../notes/cards/2026_AlphaDiverse.md) 区分内层研究与外层冻结评价。反复按测试结果修改候选，即使模型仅在训练期拟合，也会破坏最终评价的独立性。
- 时间可用性检查有不同对象：Alpha-R1 的成分与文本截止、FactorEngine 的研报日期、AlphaSchema 的实现筛查、QBX 的编译期检查，不能相互替代。跨边界标签的剔除与 LLM 预训练知识截止也需另行说明。

### 2.4 交易成本

- 买卖分侧计费与统一费率不同：AlphaPADI 给买入 5 bp、卖出 15 bp；Alpha-R1 给双边 10 bps；FactorBench 的多空组合另计融券费。`1 bp = 0.01%`，但单位换算不能消除计费基数的差异。
- top-k / drop-n、换手上限是交易约束，不能代替明确费率。AlphaGen、Alpha2、AlphaCFG 未给费率；AlphaForge 的每日最多换 5 只也不足以推出收益已经扣费。
- 比较时需同时明确单边或往返费率、换手定义、最低收费、滑点、融券与冲击假设。半 L1 换手与买卖绝对权重变化总和的计费口径不同，不能只比较 bps 数字。

### 2.5 指标与组合器

- IC 需区分截面或时间序列、Pearson 或 Spearman、是否取绝对值、因子方向在哪个数据段确定，以及跨日如何汇总。ICIR、信息比率与 Sharpe 的定义、年化和基准也按论文核对。
- 固定原生组合器评估整个系统；共同组合器更适合控制下游差异，评价上游产出的预测信息。两者结果不能直接互换，还需保持因子池选择、拟合窗口与训练预算可比。

## 3. 已知会误导比较的情形

1. **基线复现口径与原文不同**。[AlphaDiverse](../notes/cards/2026_AlphaDiverse.md) 复现 AlphaSchema 时，运行规模、时间区间和标签口径均不同于原文，两篇论文中 AlphaSchema 的数字不能直接对照。
2. **共同组合器不覆盖原生完整框架**。[AlphaPADI](../notes/deep/2026_AlphaPADI.md) 在共享公式评价预算下采用静态 ridge，包括 AlphaForge 基线。这便于控制下游差异，但不能据此评价 AlphaForge 原生动态组合的完整效果；共享公式预算也不等于共享总计算成本。
3. **股票池与基线不同**。[AlphaLedger](../notes/cards/2026_AlphaLedger.md) 的 55.4% 主结果换用了 EviPool 股票池，其余策略行在时点 CSI500 成分内交易；正文另以 31.6% 作同池结果，池扩展与生成器改进的贡献无法由现有消融拆开。
4. **同一论文内部多套口径**。[AutoScientist-Quant](../notes/cards/2026_AutoScientist-Quant.md) 的美股池按绝对收益报告、A 股池按超额收益报告；[EvoQuantLab](../notes/deep/2026_EvoQuantLab.md) 的 A 股组合是扣费前毛收益，只有 Crypto 计单边 5 bps。
5. **评测依赖外部平台**。[AgonAlpha](../notes/cards/2026_AgonAlpha.md) 的性能结论来自商业平台的私有评测，公开材料不足以独立复核，也不能与学术基线的 IC 类指标同口径比较。
6. **论文内部文本或数字不一致**。[Det-MASO](../notes/cards/2026_Det-MASO.md) 摘要的 Sharpe 提升与表 5 不符；[TLRS](../notes/cards/2025_TLRS.md) 第 V-B 节末尾出现关于 QFR 的文本。数值比较应以对应版本的实验设置与原表为依据。
7. **论文口径与所引源码要分别核对**。FactorBench 的源码补出了排名归一化、岭回归网格、半 L1 换手计费与年化 50 bp 融券费；选池还读取包含测试期可评分日数的 `admitted` 标志。这属于按测试期可评分性筛样本，不等同于按测试 IC 高低选因子，也不能称为完全不读取测试期信息。依据为[官方仓库固定版本](https://github.com/ZhuoHan1998/FactorBench-Release/tree/8dbc5b42e005a4038dd52e4790b30b467a5c1575)。
8. **样本外解释力不是样本外预测力**。CAVB 的 total R² 使用实现后的收益编码隐因子，predictive R² 改用截至当期的过去 60 个月因子均值。前者不能当作当时可交易的预测结果，两者也不能与日频 IC 数字混比。详见[CAVB 速读](../notes/cards/2025_CAVB.md)。

## 4. 使用建议

- 引用 IC 类指标时注明股票池、频率、标签、切分与指标定义；引用收益时另注明组合器、持有与调仓规则、成交时点和成本。
- 共同市场、标签和成本是比较的部分条件；数据可用性、搜索预算、因子筛选与模型拟合窗口仍需对齐。条件不同的结果可以描述，不能据此直接给算法排名。
- 登记中的 `setup` 空值表示未披露或不适用，不能据此推断实验采用了某种默认设置。
