# 维护日志

记录仓库结构、收录口径、模板和分类体系的变化。最新记录在前。

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
