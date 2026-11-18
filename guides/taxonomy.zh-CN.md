# 分类体系、实体与审查状态

[English](taxonomy.md)

本目录区分 **dataset**（记录与样本）、**suite**（一组选择及共享评测协议）、**corpus**（版本化来源集合）、**task**（要测的能力）与 **paper**（出版物）。Benchmark 是数据加评测契约，不一定要创建另一个数据对象；详见 [dataset 与 benchmark](benchmark-vs-dataset.zh-CN.md)。一篇论文使用了数据集，并不会产生一个新数据集。套件变体可能改变语料、相关性标注或评分方法，不能悄悄替换原始数据集。

## RAG 角色

| 角色 | 可操作的判断标准 | 常见误判 |
|---|---|---|
| `rag_native` | 已发布查询、答案目标或量规，且有官方来源或工具环境，足以评测检索增强回答 | 把已提供上下文误当作开放检索 |
| `rag_convertible` | 存在 QA 或 VQA，但仍需构建来源池、相关性标注、证据映射或检索划分 | 把自行改造版称为官方 benchmark |
| `auxiliary` | 可测检索或事实性等有用组件，但不能完整评测回答 | 把信息检索 NDCG 当作端到端 RAG 质量 |
| `out_of_scope` | 用现有数据无法隔离检索的贡献 | 把通识考试题直接加入 RAG 真值目录 |

这些角色是**本目录的判断**，并非数据集作者的原话。每张卡片会说明缺失的条件。特别是 BEIR 和 M-BEIR 属于检索套件；检索得分高不代表回答有依据。Natural Questions 原生的候选页面设置，也不等同于开放域 Natural Questions。

## 证据粒度

`ground_truth.levels` 描述**已经发布的标注**，不是 LLM 能推测出的内容。`answer` 不是证据。`response_span` 是生成回答中的错误或支持性片段标注；`span` 是来源材料中的坐标，不能互换。版面 `bbox` 可能标出图表的所有元素，却不标明哪一个元素回答当前问题。图的逻辑形式可能表示计算过程，却不能自动给出最小自然语言引用路径。多个可接受证据集合应保留为候选方案，不能合并成一个并集。

文本、多模态、图、表格和跨类别 RAG 是导航分类；任务与模态仍为独立标签。PDF 中的表格可以同时涉及表格、图像和版面模态，但只设一个主分类。这里的 `GraphRAG` 表示图表示或图证据检索是核心；原始数据集仅包含多跳文本问题，不等于原生图 benchmark。

`rubric` 表示已发布的输出评分要求，例如 [DeepResearch Bench II](../dataset-cards/text-rag/deepresearch-bench-ii.zh-CN.md)；`response_preference` 表示优选与拒选回答的顺序，例如 [RAG-RewardBench](../dataset-cards/text-rag/rag-rewardbench.zh-CN.md)。二者都不是来源标注，不能当作来源片段、检索相关性或完整证据链。评判模型从生成报告中抽取的证据文字，也不是原始来源真值。

## 2026 年十一月分类评估

保留五个主分类及已有路径。新的搜索代理、时效性和可信性评测会横跨来源表示；将其与文本、图像、图、表格并列，会混合能力与表示维度并造成重复。视频沿用 `multimodal_rag` 主分类及已有 `video` 模态；[SGR-Bench](../dataset-cards/text-rag/sgr-bench.zh-CN.md) 输出表格，也不因此变成 Table RAG。

| 维度 | 记录位置 | 维护规则 |
|---|---|---|
| 主要来源表示 | `primary_category`，可选 `secondary_categories` | 只设一个主位置，次分类关联不重复建条目 |
| 评测能力 | `tasks` | 优先复用标签，仅针对已证实缺口增加 `agentic_search`、`citation_prediction`、`response_preference` |
| 来源媒介 | `modalities` | 视频和音频是媒介，不等于代理搜索 |
| 领域及语言 | `domains`、`languages` | 企业、医学和多语言覆盖属于独立维度 |
| 评测环境及版本 | `evaluation.protocol`、`data.splits`、`sources` | 区分实时网页、固定语料、给定上下文、快照、工具预算与评分器版本 |
| 已发布标注类型 | `ground_truth` | 区分来源坐标、答案、量规与偏好，不推断缺失的时间区间或图路径 |

[能力选型入口](selecting-a-benchmark.zh-CN.md#capability-routes)提供跨维度人工索引，不另建一套分类或重复目录。方法在 HotpotQA 上建图，不意味着原生数据应迁入图分类。[GRBench](../dataset-cards/graph-rag/grbench.zh-CN.md) 与 [GraphRAG-Bench](../dataset-cards/graph-rag/graphrag-bench.zh-CN.md) 是不同发布；ViDoRAG/ViDoSeek 则是方法名与数据名之别，不是两份数据。

### 11 月 18 日标注与任务扩展

本轮增加三个来源标注层级。`chunk` 表示发布时指定的分块 ID。`graph_triplet` 表示知识图谱的三元组。`time_interval` 表示媒体内可定位的起止时间。卡片需注明提供该标注的评测轨、划分及映射条件。文档有效期是时间元数据，`time_interval` 专用于媒体位置。

继续按来源组织五个主类别。声学证据使用多模态主分类和 `audio` 模态。带图像知识图谱以图为主分类，辅以多模态次分类。新增 `audio_qa` 和 `retrieval_routing` 任务标签，并在选型指南中提供时序回放、版本检索和过程诊断入口。

## 审查阶梯

`discovered` 仅确认身份；`screened` 从上游来源确认实体类型和可能用途；`source_checked` 表示关键字段有一手来源和核对日期，**不意味着**数据已下载或评测器已复现。`reproduced` 需要记录过的数据加载与评测器运行；`verified` 还需要第二位独立审查者。`deprecated` 表示上游明确替换或撤回，而不是仓库暂时没有活动。未知许可保持为 `unknown`，不能把模型仓库的代码许可推定为数据许可。

本目录采取保守立场：经过来源核对的描述仍可能含作者自报信息，访问状况会变化，也可能存在未列出的变体。贡献应凭证据升级具体字段，不能只凭卡片看起来完整就提升整条记录的状态。

## 字段解释

- `data.corpus/queries/answers` 可取 `provided`、`external`、`not_provided` 或 `unknown`；`external` 表示需要从另一来源检索或重建。
- `ground_truth.provenance` 表示标注来源；`mixed` 包含人工与合成或弱监督混合流程。
- `ground_truth.alternatives` 表示多组可接受的证据或答案是明确给出、仅隐含，还是未说明。
- `access.license` 是原始数据集条款，不是本仓库的许可。代码、数据、图像与来源文档可能各有许可。
- `sources[].fields` 精确列出官方页面、论文、仓库或数据卡支持的字段。

比较数量时必须说明单位、版本、划分和来源。“问题”“问答对”“页面”“PDF”“表格”“检索候选”和“标注”是不同分母。例如项目页面与论文摘要可能公布不同的问答数量；卡片应保留差异，并指出描述的是哪个发布版本。
