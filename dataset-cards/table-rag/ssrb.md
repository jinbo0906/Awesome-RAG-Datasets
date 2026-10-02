<!-- Generated from catalog/datasets/ssrb.yaml. Edit the YAML source. -->
# SSRB

[简体中文](ssrb.zh-CN.md)

Semi-structured retrieval benchmark combining exact field conditions with semantic requirements.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `auxiliary` |
| Primary category | `table_rag` |
| Tasks | evidence_retrieval, reasoning_retrieval |
| Modalities | text, table |
| Gold annotation levels | document |
| Evidence provenance | synthetic |
| Corpus / queries / answers | provided / provided / not_provided |
| Original data license | Apache-2.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The release separates structured-object corpus files, test queries and positive query-object qrels; nested or missing fields are part of the task.

Published scale: About 14M objects across 99 schemas and six domains; 8,485 test queries.
Format: JSONL.

## Ground truth and evaluation

LLMs generate objects and queries and judge pooled retrieval candidates; qrels identify relevant whole objects rather than cell-level evidence or generated answers.

Official metrics: recall_at_20, ndcg_at_10.

Protocol: Report in-schema and in-domain cross-schema retrieval separately, with macro averages across domains. Keep candidate pools and serialization fixed.

## When to use it

- Retrieval over heterogeneous structured records
- Joint numerical filters and semantic constraints

## Limitations and cautions

- Synthetic pooled qrels are not exhaustive human relevance judgments
- This is retrieval evaluation; answer generation requires a separate protocol

## Access and sources

- [Official resource](https://github.com/vec-ai/struct-ir)
- [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/631bbd89466337712564872840a401be-Abstract-Datasets_and_Benchmarks_Track.html)
- [Data](https://huggingface.co/datasets/vec-ai/struct-ir)
- dataset_card: [source](https://huggingface.co/datasets/vec-ai/struct-ir) — supports `data`, `ground_truth.levels`, `access.license`
- repository: [source](https://github.com/vec-ai/struct-ir) — supports `summary`, `classification`, `ground_truth`, `evaluation.evaluator`, `use`
- paper: [source](https://proceedings.neurips.cc/paper_files/paper/2025/file/631bbd89466337712564872840a401be-Paper-Datasets_and_Benchmarks_Track.pdf) — supports `evaluation.official_metrics`, `evaluation.protocol`, `data.size`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
