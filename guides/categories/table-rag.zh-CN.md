# Table RAG：先找表格，再定位单元格与上下文

[English](table-rag.md)

表格问答可以在输入中直接提供相关表格，也可以要求系统从开放语料中检索表格；两者测量的能力明显不同。阅读[表格目录](../../README.zh-CN.md#table-rag)时，要同时核对原生检索范围。

| 设置 | 建议查看 | 应分开报告的内容 |
|---|---|---|
| 开放表格与文本检索 | [OTT-QA](../../dataset-cards/table-rag/ott-qa.zh-CN.md)、[HeteQA](../../dataset-cards/table-rag/heteqa.zh-CN.md) | 表格/段落检索、跨来源连接和最终回答 |
| 已提供表格或混合上下文 | [HybridQA](../../dataset-cards/table-rag/hybridqa.zh-CN.md)、[TAT-QA](../../dataset-cards/table-rag/tat-qa.zh-CN.md)、[WikiTableQuestions](../../dataset-cards/table-rag/wikitablequestions.zh-CN.md)、[SQA](../../dataset-cards/table-rag/sqa.zh-CN.md) | 原生推理任务与任何新建的开放语料检索器 |
| 依托表格的事实核查 | [FEVEROUS](../../dataset-cards/table-rag/feverous.zh-CN.md)、[TabFact](../../dataset-cards/table-rag/tabfact.zh-CN.md) | 判断结果与完整证据，而非只看标签正确率 |
| 给定证据的生成 | [ToTTo](../../dataset-cards/table-rag/totto.zh-CN.md) | 作为输入提供的高亮单元格，与系统自己找回的单元格 |

一个单元格的最小来源锚点至少包含表格及其版本、行、列、表头和单位关系。若从电子表格或 PDF 中抽取，还应保留页面、区域坐标和跨行/跨列信息。分别评测表格召回、单元格召回、表头与单位完整性、跨表格/文本连接、答案正确性和引用。只找回正确数值却丢掉单位，仍是不完整的证据链。

ArcadeQA 和 BirdQA 等大型表格变体对模式或单元格检索很有潜力，但仅有论文描述不足以证明预构建公开版本和评测器可复现。在发布资产被独立核对前，它们仍属于[待核查候选](../coverage-policy.zh-CN.md)。

## 近期论文驱动的补充

[FinQA](../../dataset-cards/table-rag/finqa.zh-CN.md) 和 [ConvFinQA](../../dataset-cards/table-rag/convfinqa.zh-CN.md) 补充数值程序、执行答案和支持事实标注。序列化的表格行标签不是 PDF 单元格坐标；ConvFinQA 还需保留前序轮次的数值依赖。[ChatRAG Bench](../../suite-cards/chatrag-bench.zh-CN.md) 改造的会话答案评测器不同于原生的执行或程序准确率。

[SSRB](../../dataset-cards/table-rag/ssrb.zh-CN.md) 评测带字段条件的异构结构化对象检索，不是生成答案或单元格证据。[TAT-DQA](../../dataset-cards/multimodal-rag/tat-dqa.zh-CN.md) 和 [OHRBench](../../dataset-cards/multimodal-rag/ohrbench.zh-CN.md) 主要属于多模态文档；表格序列化前保留布局与页面证据。[近期论文设置](../recent-paper-index.zh-CN.md)注明采用版本和评测位置。
