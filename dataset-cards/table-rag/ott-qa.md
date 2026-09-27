<!-- Generated from catalog/datasets/ott-qa.yaml. Edit the YAML source. -->
# OTT-QA

Open-domain table-and-text QA requiring retrieval from large table and passage pools.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `table_rag` |
| Tasks | table_qa, text_table_reasoning, evidence_retrieval |
| Modalities | text, table |
| Evidence levels | table, paragraph, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | MIT |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Decontextualized questions are paired with candidate pools exceeding 400K tables and 5M passages; the gold table and passage are hidden from the model in the open setting.


## Ground truth and evaluation

Question records and linked source data support table and passage retrieval evaluation; no universal table-cell citation gold is asserted.

Official metrics: table_hits_at_k, answer_em, answer_f1.

Protocol: Use the open retrieval setting, not HybridQA with a supplied table; test scoring uses the official challenge.

## When to use it

- Joint table and text retrieval
- Open-domain evidence assembly

## Limitations and cautions

- The original linked passages and table snapshots must be versioned
- Gold table or passage is coarser than a minimal cell-span chain

## Access and sources

- [Official resource](https://github.com/wenhuchen/OTT-QA)
- repository: [source](https://github.com/wenhuchen/OTT-QA) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.protocol`, `access.license`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
