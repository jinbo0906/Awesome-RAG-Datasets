<!-- Generated from catalog/datasets/hybridqa.yaml. Edit the YAML source. -->
# HybridQA

[简体中文](hybridqa.zh-CN.md)

Multi-hop QA combining Wikipedia table rows with linked passage evidence.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `table_rag` |
| Tasks | table_qa, text_table_reasoning |
| Modalities | table, text |
| Gold annotation levels | table, paragraph, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Questions require table lookup and linked textual passage reasoning in a fixed released collection.


## Ground truth and evaluation

Table and linked passage associations support a cross-structure reasoning protocol.

Official metrics: answer_em, answer_f1.

Protocol: Compare retrieval and answer stages separately; preserve table-to-passage links.

## When to use it

- Table-text evidence linking
- Cross-structure multi-hop reasoning

## Limitations and cautions

- A table flattened to plain text can lose row and header associations

## Access and sources

- [Official resource](https://github.com/wenhuchen/HybridQA)
- [Paper](https://aclanthology.org/2020.findings-emnlp.91/)
- repository: [source](https://github.com/wenhuchen/HybridQA) — supports `summary`, `data.description`, `ground_truth.description`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
