<!-- Generated from catalog/datasets/sqa.yaml. Edit the YAML source. -->
# Sequential Question Answering (SQA)

[简体中文](sqa.zh-CN.md)

Conversational sequences of questions answered over supplied Wikipedia HTML tables.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_convertible` |
| Primary category | `table_rag` |
| Tasks | conversational_qa, table_qa |
| Modalities | text, table |
| Gold annotation levels | table_cell, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Microsoft Research decomposed 2,022 WikiTableQuestions into 6,066 sequences with 17,553 inter-related questions. The table is supplied to the native task; an open table index and retrieval negatives must be defined for TableRAG evaluation.

Published scale: 6,066 sequences and 17,553 questions in release 1.0.

## Ground truth and evaluation

Answers are associated with cell locations. These support within-table evidence checks, but do not provide a table-retrieval qrel from a multi-table corpus.

Official metrics: answer_accuracy.

Protocol: Keep question order and conversation context. Report the supplied-table task separately from any constructed table retrieval stage.

## When to use it

- Multi-turn table reasoning
- Cell-level answer localization

## Limitations and cautions

- The original task supplies the table
- Split by table and sequence before building retrieval chunks

## Access and sources

- [Official resource](https://www.microsoft.com/en-us/download/details.aspx?id=54253)
- official: [source](https://www.microsoft.com/en-us/download/details.aspx?id=54253) — supports `summary`, `data.description`, `data.size`, `ground_truth.description`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
