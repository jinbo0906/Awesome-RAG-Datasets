<!-- Generated from catalog/datasets/redqa.yaml. Edit the YAML source. -->
# RedQA (RARE)

[简体中文](redqa.zh-CN.md)

Multi-hop QA with groups of interchangeable text chunks that support each required fact in high-similarity corpora.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-18 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | evidence_retrieval, multi_hop_qa |
| Modalities | text |
| Gold annotation levels | chunk, answer |
| Evidence provenance | synthetic |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

RARE is the construction framework. RedQA releases questions, answers, a fixed chunk corpus and grouped evidence. The authors construct the three high-overlap domains from financial reports, legal material and patents. General-Wiki is a separately reprocessed HotpotQA-based comparison.

Published scale: 645 finance, 605 legal and 480 patent questions (1,730 total), plus 688 General-Wiki comparison questions. The four released corpora contain 3,281, 4,090, 3,339 and 3,218 chunks respectively.
Splits: Four evaluation files by domain and control condition. Use the released question groups and compare by hop depth.
Format: JSON with corpus, queries, gold_chunk_ids and gold_chunk_groups.

## Ground truth and evaluation

Each group lists chunks judged by the construction pipeline to support the same required atomic fact. A complete retrieval result intersects every group. The IDs address the published segmentation.

Official metrics: Coverage@10, PerfRecall@10, group_nDCG@10, group_MRR, judged_answer_accuracy.

Protocol: Coverage averages the fraction of fact groups hit. PerfRecall requires all groups hit for a question and appears as perfect_match@k in code. Group nDCG and MRR use their released implementations. The paper also compares judged answer accuracy with and without retrieval.

## When to use it

- Separating partial retrieval from full fact coverage
- Measuring how duplicate evidence competes with complementary evidence

## Limitations and cautions

- The annotations refer to fixed upstream chunks so different chunkers require a fresh mapping to source evidence
- Equivalence judgments are model-assisted and can miss valid alternatives
- The repository MIT license does not settle source-corpus rights

## Access and sources

- [Official resource](https://github.com/gkswns0531/RARE)
- [Paper](https://aclanthology.org/2026.acl-long.923/)
- [Data](https://github.com/gkswns0531/RARE/tree/7d5e6749d8a2dc38e1c0c8ba21bc1cc43e4d76cd/dataset)
- paper: [source](https://aclanthology.org/2026.acl-long.923/) — supports `summary`, `classification`
- paper: [source](https://arxiv.org/html/2604.19047) — supports `data.description`, `ground_truth`, `evaluation.official_metrics`, `evaluation.protocol`, `use`
- repository: [source](https://github.com/gkswns0531/RARE/tree/7d5e6749d8a2dc38e1c0c8ba21bc1cc43e4d76cd/dataset) — supports `data.size`, `data.splits`, `data.format`, `access.data`
- repository: [source](https://raw.githubusercontent.com/gkswns0531/RARE/master/evaluation/metrics.py) — supports `evaluation.evaluator`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
