<!-- Generated from catalog/datasets/citerag.yaml. Edit the YAML source. -->
# CiteRAG (academic citation prediction)

[简体中文](citerag.zh-CN.md)

Academic reference recommendation at bibliography and citation-placeholder levels with a hierarchical scholarly retrieval corpus.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | citation_prediction, evidence_retrieval |
| Modalities | text |
| Gold annotation levels | document, answer |
| Evidence provenance | distant |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Introduced at WWW 2026 (arXiv first posted 2026-01-21). Task 1 predicts a paper's reference list from title/abstract; Task 2 predicts references at local placeholders. The author repository provides trainQA, test, a multi-volume corpus archive and separate retrieval/generation scripts.

Published scale: Paper reports 7,267 Task-1 instances, 8,541 Task-2 instances and 554,719 corpus papers; task instances are not all independent source papers or test-only examples.
Splits: Author trainQA and test directories; follow the paper's removal of test instances from the retrieval corpus and references/citation markers from input views.
Format: Per-example JSON and a multi-volume compressed hierarchical corpus..

## Ground truth and evaluation

Observed scholarly references provide target papers and ranked-list supervision. They are not exhaustive relevance judgments for every appropriate reference, nor proof that a generated claim is entailed by its citation.

Official metrics: Recall@k, MRR@k, NDCG@k, Hit@k, PACA@k, Citation_Diversity_Entropy, Hallucination_Rate.

Protocol: Separate retrieval from Task-1 list generation and Task-2 placeholder prediction. Paper section 5 defines PACA over all placeholders; released task2_metrics.py normalizes ranks only over matched predictions before article averaging. Task-1 code also allows 0.90 title similarity while Task-2 uses exact normalized titles. Pin the evaluator and report these differences rather than treating code and paper scores as identical.

## When to use it

- Comparing document-level and local-context scholarly retrieval
- Diagnosing missing or fabricated references in generated bibliographies

## Limitations and cautions

- Citation prediction is not ordinary answer-citation faithfulness evaluation
- Dataset redistribution terms were not confirmed from a dedicated data license
- Official paper and released metric aggregation have material differences

## Access and sources

- [Official resource](https://github.com/LQgdwind/CiteRAG)
- [Paper](https://doi.org/10.1145/3774904.3792075)
- [Data](https://github.com/LQgdwind/CiteRAG/tree/main/data)
- paper: [source](https://arxiv.org/abs/2601.14949) — supports `summary`, `data.description`, `data.size`, `access.paper`
- paper: [source](https://arxiv.org/html/2601.14949) — supports `data.splits`, `ground_truth.description`, `evaluation.official_metrics`, `evaluation.protocol`
- repository: [source](https://github.com/LQgdwind/CiteRAG) — supports `data.format`, `data.description`, `access.license`
- repository: [source](https://github.com/LQgdwind/CiteRAG/blob/main/eval/task1_metrics.py) — supports `evaluation.protocol`
- repository: [source](https://github.com/LQgdwind/CiteRAG/blob/main/eval/task2_metrics.py) — supports `evaluation.protocol`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
