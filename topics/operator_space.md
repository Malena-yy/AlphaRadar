# 公式因子的算子空间对照

> 首次检索日期：2026-08-12；补充检索日期：2026-08-27。本文只记录公开论文、官方仓库和官方文档能够核实的算子空间，并按计算语义比较各工作之间的异同；不评价哪一套算子更好，也不给出实现建议。补充检索还复核了 Qlib、KunQuant 和通用符号回归函数集中的常见定义，见第 3.3 节。

## 1. 主要结论

1. 已收录的 RL 与结构化搜索工作大多沿用或扩展 AlphaGen 的算子空间：一元 `Abs`、`Log`，四则运算，`Greater/Less`，以及 `Ref`、滚动均值 / 和 / 标准差 / 方差 / 极值 / 中位数 / MAD、`Delta`、`WMA/EMA`、`Cov/Corr` 等时序算子。QFR、TLRS 直接沿用；Synergistic RL、RiskMiner、AlphaQCM、AlphaCFG、AlphaSAGE、AlphaPROBE 在此基础上增减。
2. 在这一基础空间之外，扩展集中在五类：
   - 条件与逻辑：Alpha101 的三元条件，Synergistic RL 的 `Cond`，QuantaAlpha 的 `Where` 与逻辑算子，FactorMiner 的 `IfElse` 与 `And/Or/Eq/Ne`，Hubble 的 `IF`；
   - 横截面标准化：Alpha101 的 `Scale`，Synergistic RL 的 `CSScale`，QuantaAlpha 与 Hubble 的横截面 Z-score；
   - 数学变换：Alpha-Jungle 与 HRFT/IRFT 的三角函数，FactorMiner、QuantaAlpha、HRFT/IRFT 的 `Exp/Sqrt`；
   - 滚动回归与技术指标：QuantaAlpha、FactorMiner；
   - 依赖分组字段的算子：Alpha101 的 `IndNeutralize`，AlphaEvolve 的关系排序和关系去均值。
3. LLM / Agent 路线多数没有有限的算子空间：CogAlpha、FactorEngine、EFS、QuantAgent 直接生成或演化代码；AlphaAgent、Hubble、QuantEvolver 有 DSL 约束，但未公开完整算子表。对这些工作只能确认表达形式，不能据示例推断算子全集。
4. 同一个算子名在不同工作中可能是不同的计算（见第 4 节）。对照或复现时必须按定义映射，不能按名称映射。

## 2. 比较口径

本文按计算语义而不是名称判断两个算子是否相同。证据等级如下：

| 等级 | 判定依据 |
| --- | --- |
| A | 论文附录或正文给出明确算子表，或官方仓库给出实际注册表 |
| B | 论文明确继承另一工作、只列代表算子，或公开实现只覆盖论文空间的一部分 |
| C | 只披露表达式示例、允许生成任意代码，或没有公开完整算子表 |

算子表中的省略号只表示论文原文未穷举，不能把 Python、NumPy、Pandas、TA-Lib 或 Qlib 的全部 API 自动视为该方法的搜索空间。

## 3. 各工作的算子空间

### 3.1 具有明确或可还原算子空间的工作

| 相关工作 | 公开算子空间 | 说明 | 证据 |
| --- | --- | --- | --- |
| 101 Formulaic Alphas | 算术与逻辑：`Abs`、`Log`、`Sign`、`Add/Sub/Mul/Div`、`Greater/Less`、`Equal`、`Or`、三元条件；横截面：`Rank`、`Scale`、`IndNeutralize`；时序：`Delay`、`Correlation`、`Covariance`、`Delta`、`SignedPower`、`DecayLinear`、`TsMin/TsMax`、`TsArgMax/TsArgMin`、`TsRank`、`TsSum`、`TsProduct`、`TsStd` | `IndNeutralize` 依赖行业分组字段；`DecayLinear` 是线性衰减加权，与其他工作的 `WMA` 对照时需核对权重和窗口边界 | A |
| AutoAlpha | 论文说明算子集合取自 101 Formulaic Alphas，并展示加减乘除、最值、均值、标准差和时序排序等例子 | 按 Alpha101 派生空间处理；论文没有给出独立完整列表 | B |
| AlphaEvolve | 标量、向量、矩阵类型操作；重点增加 `RankOp`、同板块 / 行业内 `RelationRankOp`、分组去均值 `RelationDemeanOp`，以及从输入矩阵取标量 / 向量的 `GetScalarOp/GetVectorOp` | 关系排序和关系去均值依赖行业 / 板块分组；矩阵类型操作超出常见的二维面板公式表达式 | A |
| AlphaGen | `Abs`、`Log`、`Add/Sub/Mul/Div`、`Greater/Less`；`Ref`、`Mean/Med/Sum/Std/Var/Max/Min/Mad`、`Delta`、`WMA/EMA`、`Cov/Corr` | 后续多数 RL 工作的基础空间 | A |
| Synergistic Formulaic Alpha Generation | 在 AlphaGen 空间上增加 `Sign`、`CSRank`、`Pow`、`Skew/Kurt`、`TsRank`、`TsProduct`、`CSScale`、`IdxMax/IdxMin` 和条件算子 `Cond` | 相对 AlphaGen 增加横截面排序与缩放、高阶矩、时序乘积、位置索引和条件算子 | A |
| RiskMiner | `Sign`、`Abs`、`Log`、`CSRank`、`Add/Sub/Mul/Div`、`Greater/Less`；`Ref`、`TsRank`、`Skew/Kurt`、`Mean/Med/Sum/Std/Var/Max/Min`、`WMA/EMA`、`Cov/Corr` | 表中 `Sign` 定义为“正数为 1，否则为 0”的二值函数，不同于常见的三值 `Sign` | A |
| QuantFactor REINFORCE（QFR） | 实验沿用 AlphaGen 的一元、二元和时序算子集合 | 没有独立的新算子空间 | A/B |
| AlphaQCM | `Sign`、`Abs`、`Log`、横截面 `Rank`、`Add/Sub/Mul/Div`、`Greater/Less`；`Ref`、`TsRank`、`Mean/Med/Sum/Std/Var/Max/Min`、`WMA/EMA`、`Cov/Corr` | 与 RiskMiner 相同，`Sign` 为二值定义 | A |
| TLRS | 明确沿用 AlphaGen 环境，正文仅以 `Abs`、`Log`、`Ref` 等说明轨迹和奖励 | 按 AlphaGen 空间理解；没有独立完整算子表 | B |
| AlphaSAGE | `Abs/SLog1p/Inv/Sign/Log/CSRank`；`Add/Sub/Mul/Div/Pow` 与比较；`Ref`、均值、和、标准差、方差、高阶矩、极值、中位数、`TsMad`、排序、差分、比率、收益率、WMA/EMA、协方差和相关系数，以及若干价量复合统计 | 比较算子与逐元素最值是两类算子；`TsMad` 定义为滚动中位数绝对偏差（median absolute deviation） | A |
| AlphaCFG | `Abs/Sign/Log/CSRank`、算术、`Pow`、最值；`TsRank/WMA/EMA/Ref/Mean/Sum/Std/Var/Skew/Kurt/Max/Min/Med/Mad/Delta/Cov/Corr` | 在 AlphaGen 空间上增加 `Sign`、`CSRank`、`Pow`、`TsRank` 和高阶矩 | A |
| AlphaForge | 官方 action space 实际启用 `Inv`、`S_log1p`、算术、`Pow`、`Ref`、均值 / 和 / 标准差 / 方差 / 极值 / 中位数 / Mad、当前值除以滚动均值、收益率、差分、WMA/EMA、Cov/Corr | 依据官方源码；源码中的 `ts_div` 是当前值除以滚动均值；源码中还有未启用的其他算子 | A（官方源码） |
| AlphaPROBE | AlphaSAGE 主体空间，并明确区分比较 `Greater/Less` 与逐元素最值 `GetGreater/GetLess` | `TsMad` 同样定义为中位数绝对偏差 | A |
| Alpha-Jungle | 一元变换：负号、绝对值、平方、倒数、`Sign/Sin/Cos/Tanh/Log`；时序：`Delay/Diff/Pct/Ma/Med/Sum/Std/Max/Min/Rank/Skew/Kurt/Vari/Autocorr/Zscore`；二元算术、比较、Cov/Corr | `Vari` 为滚动变异系数；时序 Z-score 和自相关以独立算子出现 | A |
| QuantaAlpha | 时序统计、ArgMax/ArgMin、Z-score、Quantile；横截面 Rank、Z-score、Scale 和聚合统计；`Abs/Sign/Log/Exp/Sqrt/Pow/Inv`；SMA/EMA/WMA、MACD、RSI、布林带、线性衰减、回归 beta / 残差；比较、逻辑、`Where`；`Count/SumIf/Filter/Prod/HighDay/LowDay` | 包含技术指标模板和滚动回归；`ArgMax/ArgMin` 与 `HighDay/LowDay` 返回位置的方向需按定义核对 | A |
| FactorMiner | 代表性 60+ typed operator registry：算术含 `SignedPower/Sqrt/Exp/Tanh`；滚动统计含 `Product`；时序、横截面排序、平滑、线性回归；逻辑含 `IfElse`、四类大小比较、`And/Or/Eq/Ne` | 论文只公开代表算子，不是完整的 60+ 注册表；其 `Slope` 是线性回归斜率 | A/B |
| Hubble | 公开示例和 DSL 说明包含 `TS_SMA/TS_STD/TS_VAR/TS_LOGRET`、`CS_RANK/CS_ZSCORE`、`IF`，但未公开完整 registry | 不对未列出的算子作推断 | B/C |
| HRFT/IRFT | 横截面表达式使用 `Add/Sub/Mul/Div`、`Inv/Abs/Square/Sqrt/Sin/Cos/Tan/Atan/Log/Exp` | 面向高频风险因子；只有横截面表达式，没有时序算子 | A |

### 3.2 没有有限或完整公开算子空间的工作

| 相关工作 | 公开边界 | 本文处理 |
| --- | --- | --- |
| Alpha2 | 论文只举 `Abs/Ln/Sign`、算术、时序均值、相关和协方差等类型例子；官方仓库说明为伪代码和算法结构 | 不把示例或占位实现当作完整算子表；其 typed / register 表达方式可作为结构设计参考 |
| AlphaGAT | 神经 Alpha 生成和图强化学习组合，不生成公式表达式 | 不适用公式算子比较 |
| EFS | LLM 生成 NumPy 因子函数，使用种子因子和可执行代码，而非受限 DSL | 不把 NumPy 全部 API 当作算子空间 |
| Alpha-R1 | 对已有因子做推理筛选，不负责生成公式 | 不适用生成算子空间比较 |
| Alpha-GPT、Alpha-GPT 2.0 | 人机交互式遗传规划和因子优化，公开论文未列出可核实的完整算子表 | 只保留方法层参考，不据示例补全算子 |
| QuantAgent | 通过 LLM 生成和改进交易信号代码 | 没有有限的公式算子表 |
| Automate Strategy Finding | 以种子策略和代码生成扩展策略 | 没有完整公式算子表 |
| AlphaAgent | 论文和官方仓库展示滚动极值、移动平均、条件判断、MACD、RSI 等例子，但未披露完整 registry | 例子说明需要条件分支和技术指标模板，不足以确定完整算子空间 |
| R&D-Agent-Quant | 以代码和 Qlib workflow 联合优化因子及模型 | 不把整个 Qlib / Python 空间算作该方法的固定算子空间 |
| CogAlpha | 直接演化 Pandas / SciPy / TA-Lib 代码 | 不把通用库 API 视为该方法的算子空间 |
| FactorEngine | 演化完整 Python 程序并注入程序级知识 | 图灵完备的程序空间，不同于有限公式 DSL |
| QuantEvolver | 生成可执行 Factor DSL，但论文和官方仓库未公开完整算子 registry | 只确认存在 DSL 约束，不推断算子全集 |
| Agora/SJS | 关注多智能体自演化和搜索行为，公开论文未给出新的完整算子表 | 不单列算子空间 |

### 3.3 常见表达式引擎的参照定义

以下来源不是因子挖掘论文，只用于核对常见算子的定义。

| 来源 | 相关算子 |
| --- | --- |
| Qlib 表达式算子 | 六类比较、`And/Or/Not`、三元 `If`（条件、真值、假值相互独立），以及 `Count` 和滚动回归类算子 |
| KunQuant 算子文档 | 比较、`And/Or/Not`、三元 `Select`、`Exp/Sqrt`、窗口乘积、窗口最大回撤、`SetInfOrNanToValue`；`Clip` 作为可分解的复合算子 |
| gplearn 函数集 | 通用符号回归原语 `Sqrt/Log/Abs/Neg/Inv/Max/Min/Sin/Cos/Tan` |

## 4. 同名异义与定义差异

| 名称 | 不同来源中的含义 | 对照时的处理 |
| --- | --- | --- |
| `Greater/Less` | 有些工作表示 0/1 比较，有些表示逐元素最大 / 最小；AlphaPROBE 显式区分比较 `Greater/Less` 与逐元素最值 `GetGreater/GetLess` | 按定义映射，不能只看名称 |
| `Sign` | RiskMiner、AlphaQCM 的表格写为二值（正数为 1，否则为 0）；常见定义为三值（负数 -1、零 0、正数 1） | 二值版本等价于“大于 0”的比较，不应与三值 `Sign` 混用 |
| `Mad` / `TsMad` | AlphaSAGE、AlphaPROBE 定义为滚动中位数绝对偏差；MAD 也常指均值绝对偏差 | 核对是 median 还是 mean absolute deviation |
| `Slope` | FactorMiner、QuantaAlpha、Qlib 指对窗口时间索引的滚动 OLS 回归斜率 | 同名算子需确认是否为回归斜率 |
| 回归类算子 | QuantaAlpha 提供回归 beta 与残差，FactorMiner 提供线性回归统计；OLS 可以输出 beta、截距、残差、预测值或 R² | 按输出量区分，不把“回归”当作单一算子 |
| `SMA` | 可能是简单滚动均值，也可能是递推平滑 | 每个来源单独核对 |
| `Scale` | 可指横截面 L1 缩放（Alpha101）、Z-score、min-max 或时间序列标准化 | 按定义区分 |
| `ArgMax/ArgMin`、`HighDay/LowDay` | 返回位置的方向和起点在不同来源中不统一 | 核对返回值的计数方向和起点 |
| `DecayLinear` 与 `WMA` | 都是线性加权，但权重归一化、缺失值处理和窗口方向可能不同 | 核对权重定义后再视为等价 |
| MACD、RSI、ATR、布林带 | 不同来源的平滑方式、初始化和参数定义不唯一 | 按来源记录定义，不按名称合并 |

## 5. 主要来源

本文以[因子挖掘研究全景](landscape.md)收录的工作为范围，优先核对论文原文和官方仓库：

- 101 Formulaic Alphas 论文（[arXiv:1601.00991](https://arxiv.org/abs/1601.00991)）
- AutoAlpha 论文（[arXiv:2002.08245](https://arxiv.org/abs/2002.08245)）
- AlphaEvolve 论文（[arXiv:2103.16196](https://arxiv.org/abs/2103.16196)）
- AlphaGen 论文（[arXiv:2306.12964](https://arxiv.org/abs/2306.12964)）与[官方仓库](https://github.com/ICT-FinD-Lab/alphagen)
- Synergistic Formulaic Alpha Generation 论文（[arXiv:2401.02710](https://arxiv.org/abs/2401.02710)）
- RiskMiner 论文（[arXiv:2402.07080](https://arxiv.org/abs/2402.07080)）
- QFR 论文（[arXiv:2409.05144](https://arxiv.org/abs/2409.05144)）
- AlphaQCM 论文（[OpenReview](https://openreview.net/forum?id=3sXMHlhBSs)）
- AlphaSAGE 论文（[arXiv:2509.25055](https://arxiv.org/abs/2509.25055)）与[官方仓库](https://github.com/BerkinChen/AlphaSAGE)
- AlphaCFG 论文（[arXiv:2601.22119](https://arxiv.org/abs/2601.22119)）与[官方仓库](https://github.com/HanYang544/AlphaCFG)
- AlphaForge 论文（[arXiv:2406.18394](https://arxiv.org/abs/2406.18394)）与[官方仓库](https://github.com/dulyhao/alphaforge)
- AlphaPROBE 论文（[arXiv:2602.11917](https://arxiv.org/abs/2602.11917)）与[官方仓库](https://github.com/gta0804/AlphaPROBE)
- Alpha-Jungle 论文（[arXiv:2505.11122](https://arxiv.org/abs/2505.11122)）
- QuantaAlpha 论文（[arXiv:2602.07085](https://arxiv.org/abs/2602.07085)）与[官方仓库](https://github.com/QuantaAlpha/QuantaAlpha)
- FactorMiner 论文（[arXiv:2602.14670](https://arxiv.org/abs/2602.14670)）
- Hubble 论文（[arXiv:2604.09601](https://arxiv.org/abs/2604.09601)）
- HRFT/IRFT 论文（[arXiv:2408.01271](https://arxiv.org/abs/2408.01271)）与[官方仓库](https://github.com/wencyxu/IRF-LLM-accepted-at-WWW25-)
- [Qlib 表达式算子官方 API](https://qlib.readthedocs.io/en/latest/reference/api.html)与[算子源码](https://github.com/microsoft/qlib/blob/main/qlib/data/ops.py)
- [KunQuant 算子文档](https://github.com/Menooker/KunQuant/blob/main/doc/Operators.md)
- [gplearn 函数集文档](https://gplearn.readthedocs.io/en/stable/reference.html)
