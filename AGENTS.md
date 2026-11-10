# AGENTS.md

## 定位

AlphaRadar 是围绕“因子挖掘专题”的研究跟踪仓库：持续收录、阅读和横向比较 alpha 因子挖掘相关的公开工作。它不是代码实现仓库，也不记录任何项目的实验结果或开发流水。仓库计划公开：所有内容必须可以对外公开，独立成立，不依赖、不引用任何私有项目。

## 事实源与生成物

- 事实源：`papers.yaml`（论文登记，字段含义见文件开头注释）、`taxonomy.yaml`（问题、路线、标签和状态的取值），以及手写的笔记、专题和简报。
- 生成物：README 中 `PROBLEMS`、`STATUS` 两个标记区块，`INDEX.md`，速读卡从文件开头到 `META:END` 的部分。改了事实源就运行 `python scripts/build_index.py`，不要手改生成内容。
- 脚本同时校验：登记表取值、日期和路径；README 问题标题与 `taxonomy.yaml` 一致；`topics/problems.md` 点名的工作确实标注了对应问题；速读卡四个字段齐全，问题行的“（主要）/（涉及）”与 `problems` / `also` 一致、问题名与 `taxonomy.yaml` 一致；精读含必备章节。

## 目录

| 路径 | 内容 |
| --- | --- |
| `notes/cards/`、`notes/deep/` | 单篇速读卡与精读 |
| `topics/` | 横向专题；`topics/problems.md` 归纳各问题的应对思路，全部工作与机制见[索引的按问题列表](INDEX.md#by-problem) |
| `topics/adjacent/` | 不属于因子挖掘、但机制可迁移的相邻方法分析 |
| `digests/` | 定期跟踪简报 |
| `scripts/` | 生成与校验脚本 |
| `WORKLOG.md` | 本地工作日志，不入库；过程记录见该文件，仓库级变化写 `CHANGELOG.md` |

## 收录口径

1. 收录主题是因子挖掘，分 9 条路线（定义见 `taxonomy.yaml`）：`formulaic`（公式 / 符号 / 代码）、`llm-formula`（LLM 生成因子）、`llm-agent`（研究流程编排）、`neural`（神经 / 隐式因子）、`pool-combination`（池与组合，下游模块）、`benchmark`（基准与统一评测）、`auditing`（审计、复现与泄漏检查）、`data-space`（数据与表达空间）、`adjacent`（可迁移的相邻方法）。路线可多选；一篇工作通常会同时属于一条方法路线与 `pool-combination` 或 `benchmark`。
2. 纯收益预测模型只在提出因子表示、因子生成或因子组合机制时收录；只做通用时序预测的不收录。
3. 不属于因子挖掘但机制可迁移的方法，收录到 `adjacent` 路线，并在正文说明迁移点。判断 `formulaic` 与 `llm-formula` 看“谁提候选”：传统搜索器提议、LLM 只做评价或复盘时归 `formulaic`；LLM 负责提出或改写表达式时归 `llm-formula`。`llm-agent` 只收以流程编排为主要贡献的工作。
4. 每篇论文必须能给出公开链接；只有转述、没有原文的工作不收录。

## 问题标注

1. README“因子挖掘面临的问题”定义的 P1-P10 是分析主线。`problems` 只放论文动机所在、主要贡献针对的问题，至多 3 个；其余有对应机制的问题放 `also`。只标注论文中有对应机制的问题，不按标题或宣传语标注；作为基线或背景收录的工作两者都写 `[]`。
2. `adjacent` 路线的工作标注其机制可迁移去应对的问题；速读卡的每条机制要写清“原领域解决什么 → 迁移到因子挖掘对应什么”，并说明已收录工作中谁借用了它。
3. 新工作引出现有框架覆盖不了的问题时，先在 `taxonomy.yaml`、README 和 `topics/problems.md` 中新增问题并记入 `CHANGELOG.md`，再标注论文；已发布的编号不改。

## 任务入口

- 新增工作以单篇为独立维护单元：更新该篇登记与笔记后生成索引，不要求联动改写旧卡或专题；专题归纳作为独立校对任务维护。发现已有内容存在事实错误时仍须修正。
- 新增论文：在 `papers.yaml` 追加记录，`id` 为 `<小写简称>-<首次公开年份>`，状态从 `inbox` 或 `triaged` 开始。待筛条目只填 `id`、`short`、`title`、`first_public`、`url`、`routes`、`status`、`added` 和标签；`summary`、`affiliation`、`versions`、`checked` 与问题标注等写卡时再补。
- 写速读卡：按 `notes/_template_card.md` 新建卡片，在登记表填 `card`、`summary`、`affiliation`、`versions`、问题标注，并把状态改为 `card`，运行脚本生成卡片开头。`topics/problems.md` 只在校对整节时更新归纳和代表工作。
- 写精读：按 `notes/_template_deep.md` 撰写，填 `deep` 并把状态改为 `deep-read`。
- 定期跟踪：按 `digests/_template.md` 写简报，沿用上一期的检索口径，口径变化写入本期。
- 状态核查：核查论文页、会议页或官方仓库，更新 `versions`、`venue`、`code`、`code_note`、`checked`，并把变化记入简报或 `CHANGELOG.md`。
- 路线脉络变化：更新 `topics/landscape.md` 等专题；专题是综合分析，不维护完整清单。

## 写作规则

1. 使用严谨、客观、中文优先的技术语言；术语、算子名和公式符号保持原文写法。
2. 证据分四级：论文明确、公式推出、官方源码口径、未披露。源码与论文不一致时单独标注，不改写论文结论。
3. 机制、创新点、局限和可参考点分开写；不把推断写成论文结论，不作收益承诺。没有依据的内容写“待补”，不凭空补写。
4. 不写凭证、私有数据、内部系统信息或本地绝对路径；不引用、不对照任何私有项目或内部实现。“可参考点”只写面向公开读者的方法启示。

## 资料规则

1. 论文 PDF 不入库，只登记 arXiv 或官方页面链接。
2. 仓库不保存图片，笔记和专题不附图；需要示意流程时，用 Markdown 表格、文本框图或 Mermaid。
3. 移动或重命名文件前先搜索引用，移动后再检查路径。

## 提交前检查

1. `python scripts/build_index.py --check` 通过。
2. `python scripts/check_links.py` 通过：相对链接都能打开，且没有图片引用。
3. `git diff --check` 无输出。
4. 结构、口径或模板变化记入 `CHANGELOG.md`，最新记录在前。
