# 评估口径对照

> 本文比较已收录工作中实验口径的差异，数据来自各篇速读卡“证据”一节和 `papers.yaml` 的 `setup` 字段，逐项核对自论文原文；全部工作与字段见[论文索引](../INDEX.md)第 4 节。本文不比较结果数字，只说明哪些数字放在一起没有可比性，以及比较前需要对齐什么。

## 1. 覆盖情况

- 62 篇中 59 篇有速读卡，均已填写实验口径字段。
- 市场：A 股 43 篇，美股 3 篇，其他市场（欧洲、日本、加密资产、混合市场等）11 篇，方法类论文 5 篇（实验对象不是股票因子挖掘）。
- 交易成本：33 篇没有给出任何成本口径，包括若干以回测收益作主要结论的工作。

## 2. 逐项差异

### 2.1 股票池

- **A 股工作以指数成分股为主**，但指数并不统一：CSI300 最常见，其次是 CSI500、CSI1000；少数使用全市场或 SS50（LLM Strategy Finding 的 SSE50）。同一篇工作也常同时报告多个池，例如 AlphaSAGE 在 v3 中增加 CSI1000，AlphaPilot 报告 CSI300 与 CSI500。
- **成分股权重的处理方式不同**：有的按历史时点取成分（Agora/SJS、AutoScientist-Quant、Alpha-R1），有的未说明是否处理成分变动（多数）。
- **只测单一市场的工作**占多数。同时覆盖中美两地的工作有 QFR、AlphaSAGE、AlphaAgent、AlphaRLM 等，但美国市场的测试区间普遍更短。

### 2.2 数据频率与标签

- 绝大多数为日频。少数例外：HRFT/IRFT 用 1 分钟数据，FactorMiner 用 10 分钟 bar，QuantEvolver 混合 5 分钟、小时频与日频。
- **标签持有期从次日到 30 日不等**：次日收益（AlphaAgent、QuantaAlpha、RD-Agent、AlphaRLM）、5 日（QFR、TLRS、Alpha-R1、AlphaSchema、MAPLE、RiskMiner 之一）、10 日与 30 日（Alpha-Jungle、X-Alpha）、20 日（AlphaGen、Alpha2、AlphaQCM、AlphaSAGE、AlphaPADI、AlphaForge 的 VWAP 口径等）。
- 因此 IC 类指标不能跨持有期直接比较；持有期越长，同一数据长度下的有效样本越少。

### 2.3 训练 / 验证 / 测试切分

- **单一时间切分最常见**，测试期多为 1 至 3 年。
- 有滚动或分段测试的工作少数：AlphaForge（2018-2022 逐年重训）、LLM Strategy Finding（三段半年窗口）、AutoScientist-Quant（四段切分，反馈窗与测试窗分开）、AlphaDiverse（内层研究期与外层评估期分开）。
- 泄漏相关的处理差异较大：少数工作给出 point-in-time 成分、数据截止表（Alpha-R1、FactorEngine）、执行前前视筛查（AlphaSchema、AlphaDiverse），或编译期时间可用性检查（QBX）；多数工作未说明。

### 2.4 交易成本

- 给出明确费率的工作集中在较新的 LLM / Agent 工作：AlphaAgent、QuantaAlpha、AlphaRLM、AlphaPADI、AlphaLedger、X-Alpha、FactorEngine、Agora/SJS、AlphaPROBE、FactorBench 等。
- 33 篇完全没有成本口径，其中 AlphaGen、Alpha2、AlphaCFG 只用 top-k / drop-n 限制换手，没有给费率。
- 成本表达方式不统一：有的给单边或双边 bps，有的给买 / 卖分别的费率加印花税，有的只给换手约束（AlphaForge、LLM Strategy Finding）。比较组合收益前需要换算到同一口径。

## 3. 已知会误导比较的情形

1. **基线复现口径与原文不同**。AlphaDiverse 复现 AlphaSchema 作为基线时，运行规模、时间区间和标签口径都与 AlphaSchema 原文不同，两篇论文中 AlphaSchema 的数字不能直接对照。
2. **基线只用部分模块**。AlphaPADI 在共享评价预算下比较 AlphaForge 时只用了静态组合，没有用 AlphaForge 自己的动态组合，与 AlphaForge“挖掘与组合解耦”的主张相反。
3. **组合池与基线不同**。AlphaLedger 的 55.4% 主结果换用了 EviPool 股票池，其余策略行在时点 CSI500 成分内交易；正文另以 31.6% 作同池结果，池扩展与生成器改进的贡献无法由现有消融拆开。
4. **同一论文内部多套口径**。AutoScientist-Quant 的美股池按绝对收益报告、A 股池按超额收益报告；EvoQuantLab 的 A 股组合是扣费前毛收益，只有 Crypto 计 5 bps。
5. **评测依赖外部平台**。AgonAlpha 的全部性能结论来自商业平台的私有评测，无法独立复核，也不能与学术基线的 IC 类指标同口径比较。
6. **论文内部数字不一致**。Det-MASO 摘要的 Sharpe 提升与表 5 不符；TLRS 第 V-B 节末尾混入了关于 QFR 的旧文。引用这些数字前需回到原表核对。

## 4. 使用建议

- 引用论文的数字时，注明股票池、持有期、测试区间和成本口径；缺一项时标“未说明”。
- 跨论文比较优先在**同一持有期、同一股票池、同一成本口径**下进行；条件不满足时说明差异，不直接比较。
- 新写速读卡时，`setup` 字段按 `papers.yaml` 开头的定义填写；原文没有的信息留空，不推断。
