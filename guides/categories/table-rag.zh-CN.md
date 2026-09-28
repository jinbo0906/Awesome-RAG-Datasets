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
