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
