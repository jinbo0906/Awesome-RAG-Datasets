<!-- Generated from catalog/datasets/heteqa.yaml. Edit the YAML source. -->
# HeteQA

Heterogeneous text and table QA introduced alongside the TableRAG method.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `table_rag` |
| Tasks | text_table_reasoning, table_qa |
| Modalities | text, table |
| Evidence levels | table, paragraph, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The release pairs questions with mixed tabular and prose evidence for heterogeneous document reasoning.


## Ground truth and evaluation

Validate evidence IDs in the released files before treating row or cell coordinates as gold.

Official metrics: answer_accuracy.

Protocol: Compare against both table-aware and prose-only retrieval baselines.

## When to use it

- Mixed table and text retrieval
- Testing tabular operations with linked prose

## Limitations and cautions

- The small benchmark requires confidence intervals and external holdout validation

## Access and sources

- [Official resource](https://github.com/yxh-y/TableRAG)
- [Paper](https://aclanthology.org/2025.emnlp-main.710/)
- repository: [source](https://github.com/yxh-y/TableRAG) — supports `summary`, `data.description`, `evaluation.protocol`
- paper: [source](https://aclanthology.org/2025.emnlp-main.710/) — supports `classification.tasks`, `use.best_for`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
