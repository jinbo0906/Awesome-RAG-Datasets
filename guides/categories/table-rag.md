# Table RAG: locate a table, then the right cells and context

Table QA can present the relevant table in the input or require retrieval from an open pool. These are materially different tests. Read [the table catalog section](../../README.md#table-rag) with the native retrieval scope in mind.

| Setting | Inspect | What to keep separate |
|---|---|---|
| Open table plus text retrieval | [OTT-QA](../../dataset-cards/table-rag/ott-qa.md), [HeteQA](../../dataset-cards/table-rag/heteqa.md) | Table/passage retrieval, cross-source join and final answer |
| Supplied table or hybrid context | [HybridQA](../../dataset-cards/table-rag/hybridqa.md), [TAT-QA](../../dataset-cards/table-rag/tat-qa.md), [WikiTableQuestions](../../dataset-cards/table-rag/wikitablequestions.md), [SQA](../../dataset-cards/table-rag/sqa.md) | Native reasoning versus any newly built open-corpus retriever |
| Table-grounded verification | [FEVEROUS](../../dataset-cards/table-rag/feverous.md), [TabFact](../../dataset-cards/table-rag/tabfact.md) | Verdict and complete evidence, not verdict accuracy alone |
| Evidence-conditioned generation | [ToTTo](../../dataset-cards/table-rag/totto.md) | Highlighted cells supplied as input versus cells the system retrieved |

The minimum source anchor for a cell is the table/version, row, column and header/unit relationship. For spreadsheet or PDF extraction, also retain page and region coordinates and any row/column span. Score table recall, cell recall, header-and-unit completeness, cross-table/text joins, answer correctness and citation separately. A correct numeric value retrieved without its unit is an incomplete evidence chain.

Large-table variants such as ArcadeQA and BirdQA are promising for schema/cell retrieval, but a paper description is not enough to claim that a pre-built public release and evaluator can be reproduced. They remain a [coverage candidate](../coverage-policy.md) until the release artifacts are independently checked.
