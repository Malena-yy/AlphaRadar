# 维护日志

记录仓库结构、收录口径、模板和分类体系的变化。最新记录在前。

## 2026-11-10 统一其余六篇论文精读

- AlphaGAT、AlphaSAGE、AlphaPADI、EvoQuantLab、FactorBench、QBX 按已有困难、核心思路、机制、实验证据与研究结论重组；保留关键公式、比较口径和结论条件，压缩重复映射与参数清单。
- 六篇速读卡同步压缩论证链，仅依据论文正文及附录；移除笔记中的源码分析，保留论文中的算法与程序表示机制。
- 修正关联卡片与专题中的旧章节引用；FactorBench 的历史源码证据在专题与简报中直接引用原固定公开版本，与论文解读分开。

## 2026-11-10 明确论文笔记的技术文体

- 笔记规范与两类模板明确采用客观、严谨的书面表达，标题概括研究对象、机制或实验目的，避免口语化设问、对话和拟人化措辞。
- AlphaForge 试写稿按该文体调整标题与正文，保留论证顺序、公式及实验证据。

## 2026-11-10 AlphaForge 按论文论证链重写

- AlphaForge 精读依据 arXiv v5，按研究困难、核心思路、方法设计、实验证据与结论重组，说明挖掘反馈闭环及动态组合的分工，删除源码分析与复现实现细节；速读卡同步压缩并更新文献依据与章节引用。
- 实验解读区分完整框架、动态组合与单个生成模块的证据范围，区分候选库规模与每日使用因子数上限。
- 两类模板允许按论文实际内容表述关键观察或核心假设，明确组件归因的对照要求；可参考点按需展开，精读可省略。

## 2026-11-10 明确论文笔记的论证主线与文献范围

- 新增 `notes/AGENTS.md`，规定笔记按“已有困难 → 关键观察 → 方法设计 → 实验证据 → 研究结论”展开，只依据论文正文及附录，不涉及源码分析或代码复现。
- 两类模板分别压缩或展开论证链，P1–P10 只作辅助映射，局限围绕核心结论说明；保留现有校验要求的字段与章节关键词。

## 2026-11-10 清理对外文档的维护过程叙述

- 73 张速读卡的开头统一为文献依据，保留论文版本与来源；登记说明、精读、专题、简报和旧维护日志删除阅读、检索操作、访问报错与维护待办等过程叙述。
- 固定源码版本、公开状态、检索口径与证据范围继续保留；未纳入分析的补充材料不改写为论文未披露。
- AGENTS.md 强调维护过程只进入本地工作日志，CHANGELOG 只记录仓库实质变化；卡片、精读和简报模板同步调整。

## 2026-11-10 索引去重与阅读导航

- 删除与总表问题标注、按问题列表重复的问题矩阵，保留总表、按问题、实验口径与按路线四种检索视图。
- README 与索引增加阅读入口，索引增加 P1–P10 跳转；专题与模板使用稳定章节链接，避免章节重新编号后引用失效。
- 机制继续来自单篇卡片，专题只维护横向分析；未增加手写摘要、进展字段或独立明细页面。

## 2026-11-10 按问题的时间排序与单篇维护

- 索引“按问题”将主要针对与顺带涉及的工作合并，按首次公开时间从新到旧排列；逐篇显示时间、相关性与卡片中已有的机制，避免分组遮住较新的相关工作。
- 明确新增工作独立维护登记与笔记，由脚本更新索引；专题归纳单独校对，不要求随每篇新增联动改写。

## 2026-11-10 明确维护目标与任务入口

- README 明确读者、围绕 P1–P10 的研究产出与公开边界，区分论文登记、分类定义和手写分析的事实来源。
- 明确每轮维护顺序及当前待办与历史简报的分工：当前进度和任务集中在本地工作日志，历史检索结论保留时点；正文阅读完成与外部资料缺口分别记录。

## 2026-11-05 CAVB 写卡与 EvoQuantLab 精读

- CAVB 从待写推进为速读：补齐共同隐因子、分位条件载荷、训练与预测信息边界及月频滚动口径；正文公式歧义与分析证据范围分别说明，不按常见实现补全。
- 新增 EvoQuantLab 精读，核查协议冻结、GP / LLM 分工、等预算置换与外循环选择的边界。全文未披露 B₀、区块配置、实际 p 值和完整重放产物，相关专题不再保留“待精读”的旧任务表述。
- 修正 EvoQuantLab 旧卡的数字和口径：CSI500 单因子 OOS IR 为 1.041，1.002 属于 RD-Agent；两张原表一致，旧卡为文本抽取误读。Crypto IC 高于 FactorMiner，权益毛收益与 Crypto 扣费且不含资金费的口径分开记录。
- 按主要贡献与主文分工将 EvoQuantLab 路线改为 `formulaic` + `llm-agent`，研究全景导读同步；附录对候选提议来源的含糊处保留为待核点。
- 当前 73 篇全部有卡，状态为速读 66、精读 7，待写清零；评估口径与本期简报更新，成本字段仍有 40 个空值。

## 2026-11-05 维护基线、源码核查与搜索多重性专题

- 评估口径专题按 72 篇已写卡工作更新，另列新增待写 CAVB；成本字段空值与明确不计成本、非金融方法不适用分别说明，删除已过期的互斥市场计数。
- AlphaGAT 补充正式发表信息与作者单位；FactorBench 精读增加固定版本的官方源码口径，明确测试期可评分性进入选池的边界，论文与源码结论分别记录。
- 新增 `topics/search_multiplicity.md`，比较试验计数、等预算伪搜索、发表偏差估计与候选族错误率控制；修正 README 和相关专题对 EvoQuantLab 的遗漏，以及把无需估计相关矩阵误写成无分布假设等表述。
- 本轮增量与覆盖补检写入 `digests/2026-11-05.md`：arXiv 增量无新增，会议录补录 CAVB 为待写；原简报补充历史口径说明，保留当期路线、计数和状态。
- 修正校验脚本与待筛最小字段规则的冲突：未写卡条目可以省略 `problems` / `also`；已写卡仍必须显式提供列表，待筛条目若主动填写也继续校验类型与取值。

## 2026-11-03 README 问题小节改名

- README 的“出发点：因子挖掘面临的问题”改为“因子挖掘面临的问题”，去掉冗余的前缀。
- 同步更新引用该标题的 `taxonomy.yaml`、`AGENTS.md`、`topics/problems.md` 与 `scripts/build_index.py` 的生成提示；历史 CHANGELOG 条目中的旧标题保持原样，不改写记录。

## 2026-11-03 方向分类调整：拆分 LLM 与评估路线

- 问题：72 篇读完后，`llm-agent` 混了三类东西（公式输出、代码输出、流程编排）；`evaluation` 混了两类（给方法排名 vs 审视证据链）；`pool-combination` 没有一篇单独成篇，实为下游模块。
- 路线由 7 条改为 9 条：
  - `llm-agent` 拆为 `llm-formula`（LLM 提出或改写表达式，20 篇）与 `llm-agent`（以流程编排为主要贡献，12 篇）。
  - `evaluation` 拆为 `benchmark`（统一数据与执行契约，给方法排名，4 篇）与 `auditing`（留存方式、口径、前视检查与试验计数，3 篇）。
  - `formulaic` 定义扩展为公式 / 符号 / 代码；`pool-combination` 名称与说明改为“下游模块”，并把 AlphaEval、FactorBench 这类以池为评价单位的基准纳入（13 篇）。
- 判定规则写进 AGENTS.md：看“谁提候选”区分 `formulaic` 与 `llm-formula`；`llm-agent` 只收以流程编排为主要贡献的工作。
- `topics/landscape.md` 分组导读按新路线重组，由 9 组变为 11 组；README 简介与收录概况同步更新。

## 2026-11-03 CogAlpha 会议信息补登

- CogAlpha 补充为 ACL 2026 主会（Proceedings of the 64th Annual Meeting of the ACL，Volume 1: Long Papers），依据为 Crossref 记录。

## 2026-11-03 研究全景的演进叙述与第二期增量

- `topics/landscape.md` 新增「三条演进主线」一节，把现有 9 个分组按时间横切成三条线：优化单位从单条公式变成因子池、学习信号从外部反馈转向模型内部、评价从报一个 IC 变成可审计的证据链；每条线给出现有工作的先后与转折点，并指出三条线交会处的问题（池状态让奖励不平稳、训练化让证据链更难追溯、所有校正都需要搜索规模）。
- 第 1 节的阅读路径随之调整，建议先读演进主线再进入分组导读。
- 第二期增量检索（统计口径自 2026-11-03 起）在 arXiv 上只命中 1 篇、且已收录，本期增量为 0；这一结果与检索口径记入简报，避免下一期误以为漏检。

## 2026-11-03 `data-space` 补检

- 新增 3 篇：AlphaSeek（轨迹级自迭代，`llm-agent` `formulaic`）、AlphaLogics（逻辑编译器 + 双循环，`llm-agent`）、TextToAlpha（季度披露文本因子，`data-space`）。
- 路线判断：AlphaSeek 与 AlphaLogics 的“多源”只出现在选题与先验层，因子输入仍为量价字段，未归入 `data-space`；只有 TextToAlpha 扩展了因子输入的数据类型。这条判据已写进简报，避免以后按“摘要里的数据多样性”误归类。
- TextToAlpha 属边界收录：机制成立（给出可复用的文本打分函数），但论文称的 Fama-MacBeth 显著性与其表 4 的 t 值不符，且全样本既用于估计又用于评价；按“看机制不看证据强度”的口径收录，证据缺口写在卡片局限。
- 现状：72 篇（速读 66、精读 6）；`data-space` 3 篇。

## 2026-11-03 精读完成与路线补检

- 3 篇精读完成并接入：FactorBench、AlphaPADI、QBX；读原文后修正了 AlphaPADI 速读卡的两处机制描述与 QBX 的自我指涉说明。
- 标签治理：50 个标签补定义，合并 4 个重叠标签，现为 47 个。
- 补检 `neural`、`data-space` 两条较薄路线，新收录 3 篇：CosmosAlpha（关系图 + Pareto 选父）、PRISM-VQ（离散隐因子，`neural`）、MarketSenseAI（相邻方法：实时生成规避前视 + 零分布检验）。PRISM-VQ 的会议信息据 arXiv comment 记为 IJCAI 2026，PDF 本身未印会议名。
- 现状：69 篇（速读 63、精读 6）；路线公式 23、LLM / Agent 30、因子池与组合 11、相邻方法 10、评估 7、神经 4、数据与表达 2。

## 2026-11-03 精读、标签定义与覆盖补检

- 新增 3 篇精读：FactorBench（组合视角基准的评估契约）、AlphaPADI（池级扩散生成）、QBX（编译期准入、身份去重与试验账本）。精读均把“论文明确 / 公式推出 / 未披露”分开记录；QBX 与 AlphaPADI 不公开代码或注册表，相关结论标注为无法外部复核。
- 读原文后修正速读卡：
  - AlphaPADI：`R_inner` 惩罚的是最坏邻居的平方 hinge，不是平均邻居相关；共享评价预算只约束六个非 LLM 方法，AlphaAgent 未作说明；所有基线都用同一静态组合器评价，表 1 数字不能与各基线原文表格直接比较。
  - QBX：补注其未公开代码与注册表、却把可复现性列为主要针对问题之一的自我指涉风险。
- 标签治理：50 个标签全部补一行定义；合并 4 个重叠标签（`generator-predictor` → `surrogate-model`、`automl` → `evolutionary`、`self-play` → `multi-agent`、`skills` → `memory`），现为 47 个，仅 `alternative-data` 暂无使用。

## 2026-11-03 研究全景补全

- `topics/landscape.md` 的分组导读补齐本轮新增的全部工作：2.1 加 Warm Start GP，2.2 加池级生成与训练信号的近期做法，2.3 加 AlphaLedger、GoAnt，2.5 加 Det-MASO、GoAnt，2.6 链接评估口径专题，2.7 加本轮收录的 LLM 训练化与语义空间工作，2.8 加两篇多重检验相邻方法。
- 新增 2.9「过拟合控制与显著性检验」：把 EvoQuantLab、AlphaMemo、AgenticFactorInvesting 与 Publication Bias、Sequential Cauchy 归为一组，说明这一组回答的是“挖出来的因子有多少是真的”。
- 收录概况的“未进入研究全景”提示随之清零。

## 2026-11-03 补 P5：过拟合与多重检验

- P5「低信噪比下的过拟合」补充以下 4 篇，覆盖多重检验、发表偏差与经验复用中的选择偏差：
  - `llm-agent` 路线 2 篇：AlphaMemo（按父因子质量分桶校正残差信用，控制经验复用带来的选择偏差）、AgenticFactorInvesting（经济理由约束、显著性门槛与样本外冻结三层准入闸门）。
  - `adjacent` 路线 2 篇：Publication Bias（经验贝叶斯收缩与 FDR，附“短窗口衰减是选择偏差上界”的归因规则）、Sequential Cauchy（强 FWER 控制并能指认个体显著项的多重检验程序）。
- P5 主要针对由 3 篇增至 5 篇，另有 2 篇相邻方法；`topics/problems.md` 的 P5 归纳与 `topics/adjacent/transferable_methods.md` 同步更新（新增 2.5 节）。
- taxonomy 标签新增 `multiple-testing`。
- AgenticFactorInvesting 的显著性门槛只写 `|t|>3.0`，未披露搜索规模，是本仓库 P5 谱系里最弱的一档，已在卡片局限与专题中标注；其第 7.2 节收益数字与 Exhibit 13 口径冲突，卡片保留“需核对”标注。

## 2026-11-03 实验口径结构化与对照专题

- `papers.yaml` 每条记录新增 `setup` 字段：`markets`、`freq`、`test`、`label`、`cost`，62 篇全部按原文填写，原文没有的字段留空，不推断。字段定义见文件开头注释。
- `INDEX.md` 新增第 4 节“实验口径”，分两张表列出市场与频率、样本外区间与标签与成本；按路线分组顺延为第 5 节。
- 新增专题 `topics/evaluation_protocol.md`：按股票池、频率与标签、切分、成本四项比较口径差异，并列出 6 类已知会误导比较的情形（基线复现口径不同、基线只用部分模块、组合池与基线不同、论文内部多套口径、依赖外部平台评测、论文内部数字不一致）。
- 读原文核对时修正的卡片错误：
  - QFR：卡片原写“回测假设 TWAP/VWAP 执行、报告换手与最大回撤”，原文第 V-E 节只有累计收益曲线，表 V 只是 IC/RankIC，相关表述已删除；阅读版本由 v3 改为 v2。
  - AlphaSAGE：实验口径以 v3 为准，包含 CSI1000；v2 仅包含 CSI300、CSI500、S&P500。

## 2026-11-03 待筛工作逐篇判断

- 15 篇待筛全部读了原文：13 篇收录并写速读卡（AlphaLedger、EvoQuantLab、LineageEvo、AutoScientist-Quant、Warm Start GP、X-Alpha、AlphaRLM、AgonAlpha、TreEvo、GoAnt、Det-MASO、AlphaG-OPD、AlphaRJM），2 篇按收录口径第 2 条不收录并从登记表移除（Sentiment-Aware LLM Alpha、Factor-Newsflow Fusion，理由记入简报）。
- 路线修正：GoAnt 的候选由共享符号算子文法生成、LLM 只做预算调度，路线由 `llm-agent` `data-space` 改为 `data-space` `pool-combination`，去掉 `multi-agent` 标签。
- AgonAlpha 收录，但性能结论基于商业平台私有评测、无法独立复核，已写入 `code_note` 与卡片局限。
- 登记表现在 62 篇，全部有速读卡或精读，待筛清零；`evaluation` 路线增至 7 篇。
- 构建脚本：收录概况新增“未进入研究全景”提示，列出未被 `topics/landscape.md` 提及的卡片；据此补充了评估与基准、LLM 训练化与语义空间、相邻方法三组导读。

## 2026-11-03 问题标注分为“主要针对”和“顺带涉及”

- 背景：49 张卡里有 17 篇标了 4 个以上问题，P7 覆盖 30/64 篇，矩阵越来越分不出重点工作。此前每条机制在卡片和 `topics/problems.md` 各写一遍，维护量随论文数线性增长。
- `papers.yaml`：`problems` 只放论文动机所在、主要贡献针对的问题（至多 3 个）；新增 `also` 放有对应机制但不是主要贡献的问题；两者不能重叠，`also` 不能脱离 `problems` 单独存在。
- 速读卡：问题行改为 `- P<k> <名称>（主要|涉及）：<机制>`，先主要后涉及；脚本核对级别与问题名。
- `INDEX.md` 新增第 3 节：每个问题按“主要针对 / 顺带涉及”列出全部工作，机制直接取自速读卡；矩阵用 ● 表示主要、○ 表示涉及，并分两行统计。
- `topics/problems.md` 改为归纳性专题：每类机制一句说明加代表工作，不再罗列全部机制，代表工作不超过 5 篇；脚本改为单向核对这些工作确实标注了该问题。
- README 问题总表增加“主要针对 / 顺带涉及”两列；登记表注释、AGENTS.md、`taxonomy.yaml` 注释与速读卡模板同步更新。
- 待筛条目改为只填最少字段：`summary`、`affiliation`、`versions`、`tags`、`checked` 等写卡时再补。

## 2026-11-03 新增速读卡与相邻方法专题

- 新写 17 张速读卡，均据原文撰写：
  - 评估与泄漏 5 篇：AlphaEval、FactorBench、Auditing LLM Alpha-Factor Mining、QBX、Look-Ahead-Bench。
  - 新方法 6 篇：AlphaPareto、AlphaPADI、MAPLE、AlphaPilot、AlphaSchema、AlphaDiverse。
  - 相邻方法 6 篇：DSR、GFlowNet、Trajectory Balance、DeepMind AlphaEvolve、GiGPO、Tree-GRPO。
  - 登记时按摘要初判的问题，读原文后多有增补，以原文机制为准。
- 新增专题 `topics/adjacent/transferable_methods.md`：相邻方法向因子挖掘的迁移点与迁移时要注意的差异。AGENTS.md 写明相邻方法的标注口径：标注其机制可迁移去应对的问题。
- 新增 15 篇待筛候选，包括 `data-space` 方向的 GoAnt 和两篇新闻、情绪类工作；其中 4 篇早于首轮检索截止日（2026-07-11），属首轮漏检。
- 不收录：Chain-of-Alpha（arXiv 两个版本均被移除，无原文）、GPU 常数优化（读原文后判断迁移关系太弱）；已从登记表移除，理由记入简报。
- 标签新增 `symbolic-regression`、`distillation`、`alternative-data`、`multi-objective`、`preference-optimization`、`surrogate-model`。
- README 中 P5、P6、P10 的“跟踪关注点”按当前收录改写；第一期简报按本轮结果更新。
- 修正：FactorBench 的 id 由 `factorb-bench-2026` 改为 `factorbench-2026`；AlphaQCM 据 PMLR 论文集补充页码与官方仓库。
- AlphaQCM：据 ICML 2025 论文集版原文补写证据与局限，改正标题（补上 “in Finance”）并补作者单位；至此全部速读卡已无待补项。

## 2026-11-03 内容补写、候选登记与第一期简报

- 31 张速读卡补充“证据”与“局限”，注明章节或表格来源；推断与论文结论分别标明。AlphaQCM 的证据与局限保留原状态。
- 问题标注修正（读原文核对后发现）：
  - QFR：P5 改为 P9。信息比率针对的是因子随时间是否稳定，原文没有讨论搜索规模带来的选择偏差。
  - Synergistic RL：P2 改为 P7。扩展算子与窗口是为了扩大搜索空间和因子多样性，原文未讨论可解释性代价。
  - LLM Strategy Finding：P2 改为 P1。论文抽取的是显式公式因子，没有在表达能力与可解释性之间取舍；同时补上官方仓库 kouzhizhuo/Automate-Strategy-Finding-with-LLM-in-Quant-investment（v4 原文给出）。
  - 补标：AlphaGen、Alpha2 加 P3；RiskMiner 加 P8；AlphaCFG、EFS 加 P7；AlphaPROBE 加 P8；Alpha-GPT 加 P2；QuantAgent 加 P4；Alpha-GPT 2.0 加 P8。
  - 相应修改 `papers.yaml`、速读卡和 `topics/problems.md`，脚本核对通过。
- 文字修正：Alpha101 的“101 个真实交易中使用过的 Alpha”按原文改为“生产中使用、写作时其中 80 个处于生产状态”；AlphaEvolve 的冗余剪枝与集合级相关性阈值剔除分开表述；AlphaGen 的因子池淘汰规则改为按权重绝对值最小。
- 新增候选 11 篇：`evaluation` 路线 5 篇（AlphaEval、FactorBench、Auditing LLM Alpha-Factor Mining、QBX、Look-Ahead-Bench，状态 `triaged`），新方法 6 篇（AlphaPareto、AlphaPADI、AlphaPilot、AlphaSchema、MAPLE、AlphaDiverse，状态 `inbox`）。新增标签 `benchmark`、`auditing`、`dsl`、`diffusion`。
- 第一期跟踪简报 `digests/2026-11.md`：统计区间 2026-07-11 至 2026-11-03，记录检索口径、新增收录、问题视角、状态变化、建议精读和未收录候选。
- 脚本：收录概况增加“待处理”一行；问题编号识别限定为一到两位数字，避免把“2022-2024”这类年份误判为 P2024。

## 2026-11-03 结构优化与首次状态核查

- 原则：只有 `papers.yaml`、`taxonomy.yaml` 和手写分析是事实源；清单、计数和卡片元数据由脚本生成，手写分析中能核对的引用由脚本校验。
- README：保留问题框架（目标、问题总表、易混淆边界、各问题说明与跟踪关注点）；问题总表和收录概况改为生成区块。论文索引移到生成的 `INDEX.md`（总表、问题 × 工作矩阵、按路线分组）；各问题下“已收录工作的应对”移到 `topics/problems.md`。
- `papers.yaml`：新增 `summary`、`versions`（取代 `published`）、`venue`、`checked`；字段说明移到文件开头注释；`first_public` 统一为最早公开版本；有官方仓库时 `code_note` 不再重复链接。
- `taxonomy.yaml`：问题新增 `tension`（核心矛盾）和 `stage`（所在环节）；开头注释改为“路线表示工作所属的研究板块”。
- 速读卡：开头的元数据改由脚本生成；32 张卡按原 README 各问题下的机制描述补“针对问题与证据”；“局限”和多数卡片的“证据”标为待补，不凭空补写。
- 精读：3 篇补“针对的问题”；精读模板改为必备章节加自由结构，证据统一为四级。
- `topics/landscape.md`：逐篇清单压缩为分组导读，完整列表以 `INDEX.md` 为准。
- `scripts/build_index.py`：生成 README 区块、`INDEX.md` 和卡片开头；新增问题专题、速读卡、精读和 `first_public` 校验。
- AGENTS.md：字段说明移出，新增“事实源与生成物”“任务入口”，人工一致性规则改由脚本校验。Issue 模板改为引用 `taxonomy.yaml`，并增加“针对的问题”。
- 状态核查（2026-11-03；arXiv API，AlphaSAGE 经 OpenReview，RiskMiner 经 Crossref）：
  - 修正 `first_public`：AutoAlpha 2020-04 → 2020-02，AlphaEvolve 2021-04 → 2021-03，原值是 v2 日期。
  - 新增或确认发表信息：Alpha101（Wilmott Magazine 2016）、Synergistic RL（ICOIN 2024）、RiskMiner（ICAIF 2024）、QFR（IEEE Transactions on Signal Processing 2025）、Alpha-GPT（EMNLP 2025 System Demonstrations）、AlphaSAGE（ICLR 2026 Poster）、FactorEngine（ICDM 2026）、HRFT/IRFT（WWW 2025 Industry Track）。
  - 首轮检索（2026-07-11）之后出现的新版本：EFS v2、Alpha-R1 v2、FactorMiner v2、FactorEngine v3、CogAlpha v4。
  - AlphaQCM 与 AlphaGAT 的外部状态记录保留截至 2026-07-11 的口径。

## 2026-11-03 以问题为出发点组织仓库

- 目标：先固定因子挖掘面临的普遍问题，再用它们阅读和对照每篇工作，作为仓库的出发点。
- README 新增“出发点：因子挖掘面临的问题”，共 10 个问题，按挖掘流程排列：P1 表达空间巨大、有效因子稀少，P2 表达能力与可解释性的权衡，P3 评价成本高，P4 学习信号稀疏、延迟且不可微，P5 低信噪比下的过拟合，P6 前视偏差与信息泄漏，P7 因子同质化与冗余，P8 挖掘目标与实际使用脱节，P9 非平稳与因子衰减，P10 评估口径不统一、难以复现。每个问题列出已收录工作中的对应机制和跟踪关注点，并说明易混淆问题之间的边界。
- 划分依据：评价的算力成本（P3）与学习型生成器的信用分配（P4）应对手段不同，分开列；先验知识是应对 P1 的手段，不单列；过拟合、泄漏、衰减按成因而非“样本外失效”这一共同表现区分；换手、容量、成本并入 P8。
- `taxonomy.yaml` 新增 `problems`（字段 `code` 为 P 编号）；`papers.yaml` 新增必填列表字段 `problems`，32 篇按速读卡中的机制描述回填，Alpha101 作为基线工作为 `[]`；速读卡元数据新增“针对问题”行；README 索引新增“问题”列。
- 模板：速读卡新增“针对问题与证据”字段，精读新增“针对的问题”一节，简报新增“问题视角”一节和“针对问题”列。

## 2026-11-03 初始化

- 目标：建立因子挖掘专题的研究跟踪仓库，持续收录、阅读和横向比较公开工作。
- 结构：`papers.yaml` 作为唯一事实源，`taxonomy.yaml` 定义 7 条路线（`formulaic`、`llm-agent`、`neural`、`pool-combination`、`evaluation`、`data-space`、`adjacent`）、标签和状态；README 论文索引由 `scripts/build_index.py` 生成，`scripts/check_links.py` 检查相对链接。
- 首批内容：
  - 32 篇论文的登记与速读卡，检索截至 2026-07-11。
  - AlphaForge、AlphaGAT、AlphaSAGE 三篇精读。
  - 专题：研究全景（`topics/landscape.md`）、算子空间对照（`topics/operator_space.md`，检索日期 2026-08-12，补充检索 2026-08-27）、生成器如何使用真实 IC（`topics/generator_training_with_ic.md`）。
- 资料规则：论文 PDF 不入库，只登记链接；仓库不保存图片，论文笔记和专题不附图，流程示意用表格、文本或 Mermaid，`check_links.py` 会拒绝图片引用。
- 许可：文档内容采用 CC BY 4.0（`LICENSE`），代码（`scripts/`、`.github/`）采用 MIT（`LICENSE-MIT`）。
