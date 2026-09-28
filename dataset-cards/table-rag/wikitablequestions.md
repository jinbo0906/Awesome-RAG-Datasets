<!-- Generated from catalog/datasets/wikitablequestions.yaml. Edit the YAML source. -->
# WikiTableQuestions

[简体中文](wikitablequestions.zh-CN.md)

Complex questions on supplied semi-structured Wikipedia HTML tables.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_convertible` |
| Primary category | `table_rag` |
| Tasks | table_qa |
| Modalities | text, table |
| Gold annotation levels | table, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Each question is paired with a Wikipedia table and answer; the official evaluator checks answer denotations.


## Ground truth and evaluation

The table and answer are given, but a minimal supporting cell set or open-table qrel is not guaranteed.

Official metrics: denotation_accuracy.

Protocol: For table retrieval, construct a fixed table corpus and qrels without leaking the paired table into input.

## When to use it

- Table reasoning after retrieval
- Denotation evaluation

## Limitations and cautions

- Native task supplies the table; it is not an open-table retrieval benchmark

## Access and sources

- [Official resource](https://github.com/ppasupat/WikiTableQuestions)
- repository: [source](https://github.com/ppasupat/WikiTableQuestions) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
