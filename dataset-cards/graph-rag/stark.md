<!-- Generated from catalog/datasets/stark.yaml. Edit the YAML source. -->
# STaRK (textual and relational retrieval)

[简体中文](stark.zh-CN.md)

Entity retrieval over semi-structured knowledge bases, requiring joint satisfaction of textual and relational constraints.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `auxiliary` |
| Primary category | `graph_rag` |
| Tasks | reasoning_retrieval, evidence_retrieval |
| Modalities | text, graph |
| Gold annotation levels | document |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / not_provided |
| Original data license | CC-BY-4.0 for the HF query release; underlying knowledge-base sources retain their terms. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

NeurIPS 2024 Datasets and Benchmarks release with Amazon, MAG and Prime knowledge bases. Relevant node IDs are retrieval targets, not reference natural-language answers. ACL 2026 ARK evaluates adaptive lexical search and graph-neighborhood exploration on these resources.

Published scale: Current HF synthesized-all configurations have 9,100 / 13,323 / 11,204 rows for Amazon / MAG / Prime; human-generated sets have 81 / 84 / 98 queries. These are not test-only counts.
Splits: Use the loader's official train/val/test index files; test-0.1 and human_generated_eval are separate evaluation settings. HF's synthesized_all_split combines native splits.
Format: QA CSV, split indices and processed semi-structured knowledge bases through the stark-qa loader..

## Ground truth and evaluation

Positive entity/node IDs identify relevant retrieval objects (document here means an addressable node record). Synthetic queries and separate human queries have different origins; no free-form answer or minimal supporting graph path is claimed.

Official metrics: Hit@1, Hit@5, Recall@20, MRR.

Protocol: Rank eligible candidate nodes, not arbitrary text chunks; retain all positive node IDs. Pin the SKB, split indices and candidate types. ARK's training-free comparisons and teacher-trajectory distillation are distinct experiments; its trajectories are not native STaRK gold.

## When to use it

- Separating entity retrieval from answer generation
- Budgeted graph traversal under textual and relational constraints

## Limitations and cautions

- Do not confuse this STaRK with unrelated same-name dialogue or agent methods
- All-split row counts must not be presented as test sizes
- Source node relevance is not a gold natural-language citation chain

## Access and sources

- [Official resource](https://github.com/snap-stanford/stark)
- [Paper](https://papers.nips.cc/paper_files/paper/2024/hash/e607b1419e9ae7cd5cb5b5bb60c2ad5c-Abstract-Datasets_and_Benchmarks_Track.html)
- [Data](https://huggingface.co/datasets/snap-stanford/stark)
- paper: [source](https://papers.nips.cc/paper_files/paper/2024/hash/e607b1419e9ae7cd5cb5b5bb60c2ad5c-Abstract-Datasets_and_Benchmarks_Track.html) — supports `summary`, `data.description`, `ground_truth.provenance`
- dataset_card: [source](https://huggingface.co/datasets/snap-stanford/stark) — supports `data.format`, `access.license`, `ground_truth.description`
- dataset_card: [source](https://datasets-server.huggingface.co/size?dataset=snap-stanford/stark) — supports `data.size`
- repository: [source](https://github.com/snap-stanford/stark) — supports `data.splits`, `evaluation.protocol`
- paper: [source](https://aclanthology.org/2026.acl-long.714.pdf) — supports `evaluation.official_metrics`, `evaluation.protocol`, `data.description`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
