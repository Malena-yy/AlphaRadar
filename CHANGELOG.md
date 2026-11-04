# 维护日志

记录仓库结构、收录口径、模板和分类体系的变化。最新记录在前。

## 2026-11-03 补 P5：过拟合与多重检验

- `problems.md` 此前只剩 P5「低信噪比下的过拟合」一个覆盖缺口（主要针对 3 篇）。本轮两轮 arXiv 检索（多重检验、数据窥探、回测过拟合、发表偏差等关键词）选出 4 篇候选，读原文后全部收录：
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
  - AlphaSAGE：本地 PDF 曾为 v2（只含 CSI300、CSI500、S&P500），已换成 v3（28 页，含 CSI1000），并在卡片注明版本；本地 Alpha-Jungle PDF 同步换成 v3。
- 待核查：Alpha-Jungle 的复现审计记录提到 v3 含 S&P500 实验，本次 v3 全文检索只命中 4 处 S&P，未确认是否有 S&P500 实验，暂不写入兜底结论。

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

- 速读卡：除 AlphaQCM（OpenReview 返回 403，需换来源）外，31 张卡的“证据”与“局限”按论文原文补写，每句注明章节或表格来源；无依据处写明“据实验设置”或“推断”。三篇有精读的卡片据本仓库精读补写。
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
  - AlphaQCM（OpenReview 需要人机验证）和 AlphaGAT（没有 arXiv）未重新核查，`checked` 保持 2026-07-11；开源情况沿用 2026-07-11 的检索结论。

## 2026-11-03 以问题为出发点组织仓库

- 目标：先固定因子挖掘面临的普遍问题，再用它们阅读和对照每篇工作，作为仓库的出发点。
- README 新增“出发点：因子挖掘面临的问题”，共 10 个问题，按挖掘流程排列：P1 表达空间巨大、有效因子稀少，P2 表达能力与可解释性的权衡，P3 评价成本高，P4 学习信号稀疏、延迟且不可微，P5 低信噪比下的过拟合，P6 前视偏差与信息泄漏，P7 因子同质化与冗余，P8 挖掘目标与实际使用脱节，P9 非平稳与因子衰减，P10 评估口径不统一、难以复现。每个问题列出已收录工作中的对应机制和跟踪关注点，并说明易混淆问题之间的边界。
- 划分依据：评价的算力成本（P3）与学习型生成器的信用分配（P4）应对手段不同，分开列；先验知识是应对 P1 的手段，不单列；过拟合、泄漏、衰减按成因而非“样本外失效”这一共同表现区分；换手、容量、成本并入 P8。
- `taxonomy.yaml` 新增 `problems`（字段 `code` 为 P 编号）；`papers.yaml` 新增必填列表字段 `problems`，32 篇按速读卡中的机制描述回填，Alpha101 作为基线工作为 `[]`；速读卡元数据新增“针对问题”行；README 索引新增“问题”列。
- 模板：速读卡新增“针对问题与证据”字段，精读新增“针对的问题”一节，简报新增“问题视角”一节和“针对问题”列。
- 待办：P6 泄漏和 P10 评估复现的已收录工作很少，列为补检重点。

## 2026-11-03 初始化

- 目标：建立因子挖掘专题的研究跟踪仓库，持续收录、阅读和横向比较公开工作。
- 结构：`papers.yaml` 作为唯一事实源，`taxonomy.yaml` 定义 7 条路线（`formulaic`、`llm-agent`、`neural`、`pool-combination`、`evaluation`、`data-space`、`adjacent`）、标签和状态；README 论文索引由 `scripts/build_index.py` 生成，`scripts/check_links.py` 检查相对链接。
- 首批内容：
  - 32 篇论文的登记与速读卡，检索截至 2026-07-11。
  - AlphaForge、AlphaGAT、AlphaSAGE 三篇精读。
  - 专题：研究全景（`topics/landscape.md`）、算子空间对照（`topics/operator_space.md`，检索日期 2026-08-12，补充检索 2026-08-27）、生成器如何使用真实 IC（`topics/generator_training_with_ic.md`）。
- 资料规则：论文 PDF 不入库，只登记链接；仓库不保存图片，论文笔记和专题不附图，流程示意用表格、文本或 Mermaid，`check_links.py` 会拒绝图片引用。
- 许可：文档内容采用 CC BY 4.0（`LICENSE`），代码（`scripts/`、`.github/`）采用 MIT（`LICENSE-MIT`）。
- 待办：
  - `neural`、`evaluation`、`adjacent` 路线目前只有少量或没有收录，需要补检代表工作。
  - 补检 2026-07-11 之后的新工作，形成第一期跟踪简报。
  - 首批速读卡没有单独的“局限”字段；后续更新时按新模板补齐。
