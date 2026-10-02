# Graph RAG：图结构不等于图证据真值

[English](graph-rag.md)

[Graph RAG 目录](../../README.zh-CN.md#graph-rag)有意区分两种设置：GraphRAG 系统可能从文本**构建**图，再检索与图相连的上下文；知识库问答系统则查询已有结构化图。两者都有价值，但真值标注和失败方式不同。

| 设置 | 建议查看 | 主要注意点 |
|---|---|---|
| 建图后进行 RAG 生成 | [GraphRAG-Bench](../../dataset-cards/graph-rag/graphrag-bench.zh-CN.md) | 系统生成的边，不等于独立标注的金标准证据路径 |
| 已有知识库推理 | [GrailQA](../../dataset-cards/graph-rag/grailqa.zh-CN.md)、[WebQuestionsSP](../../dataset-cards/graph-rag/webqsp.zh-CN.md)、[MetaQA](../../dataset-cards/graph-rag/metaqa.zh-CN.md) | 逻辑形式、跳数和答案不会自动变成可引用的证据子图 |
| 长来源的全局摘要 | [Microsoft GraphRAG 播客语料](../../catalog/corpora/ms-graphrag-podcasts.yaml) | 语料与开放式问题需要明确的回答或证据评测器 |

构建 GraphRAG benchmark 时，应固定原始文档、建图方法和版本、实体消歧、边的来源、检索预算以及回答评测器。分别报告建图成本、来源节点召回、**存在金标准时**的路径或边正确率、回答质量和引用有效性。不能仅因为模型生成的图与模型自身输出一致就给分。多跳文本 QA 可作迁移测试，但把原始 HotpotQA 或 MuSiQue 称为“原生 GraphRAG”会改变其任务身份。

本分类故意比使用图的论文数量少：方法、来源语料和 benchmark 数据集是不同实体。收录依据见 [dataset 与 benchmark 的区别](../benchmark-vs-dataset.zh-CN.md)。

## 近期论文驱动的补充

[ComplexWebQuestions](../../dataset-cards/graph-rag/complexwebquestions.zh-CN.md) 和 [KQA Pro](../../dataset-cards/graph-rag/kqa-pro.zh-CN.md) 扩展已有知识库的语义解析与组合推理。[OpenDialKG](../../dataset-cards/graph-rag/opendialkg.zh-CN.md) 提供参与者选择的会话图路径；这是对话转换的监督，不是每个回复唯一的证明图。[MINTQA](../../dataset-cards/graph-rag/mintqa.zh-CN.md) 补充新知识、长尾知识、子问题和关联图谱，生成的事实链与答案包含评分必须分开评测。

[论文索引](../recent-paper-index.zh-CN.md)链接 ACL 2025 KG-Agent 的具体数据与 ICML 2025 HippoRAG 2 的文本问答改造。[mmRAG](../../dataset-cards/text-rag/mmrag.zh-CN.md) 在序列化的图谱、表格和文本记录上评测路由与检索，固定分块相关性不能变成原生图路径真值。
