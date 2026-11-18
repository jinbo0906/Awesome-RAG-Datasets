<!-- Generated from catalog/datasets/query-robustness.yaml. Edit the YAML source. -->
# Query Robustness (How You Ask Matters)

[简体中文](query-robustness.zh-CN.md)

Paired answer-preserving query variations for evaluating how adaptive RAG changes its answers, retrieval strategy and cost.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-18 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | rag_robustness, retrieval_routing |
| Modalities | text |
| Gold annotation levels | answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | external / provided / provided |
| Original data license | CC-BY-SA-4.0 (released variation data) |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

EMNLP 2026 benchmark draws from six existing QA datasets and groups each original with six machine-generated form variations and up to two human rewrites. The RAG setup uses external Wikipedia passages from DPR.

Published scale: Pinned release has 3,000 originals, 18,000 machine variants and 1,183 nonempty human rewrites for 597 base rows (22,183 forms including originals).
Splits: Six evaluation configurations of 500 original rows each. The HF viewer's automatic train label differs from the test.jsonl file naming and intended evaluation use.
Format: JSONL with original_question, answers, human rewrite and surface-variation columns.

## Ground truth and evaluation

Answer targets are shared with each original. Pairs are designed to preserve intent while varying formality, readability, syntax or errors. The release does not label a unique correct retrieval decision for each question.

Official metrics: answer_accuracy, InAccuracy, semantic_answer_consistency, retrieval_calls, LLM_calls, normalized_cost_deviation, retrieval_decision_robustness.

Protocol: Pair each variant with its original in the same retrieval and model environment. InAccuracy checks whether an answer contains a gold string. Compare changes in correctness, semantic answer consistency, retrieval routing and call counts separately. Keep originals and their variants together in any derived split.

## When to use it

- Detecting needless route changes for semantically equivalent queries
- Measuring answer-robustness and cost tradeoffs for adaptive retrieval

## Limitations and cautions

- Forms sharing an original are repeated measurements
- MIT applies to the baseline overlays while the dataset and Wikipedia terms are separate
- Route changes diagnose instability and require counterfactual evaluation to establish whether they were beneficial

## Access and sources

- [Official resource](https://huggingface.co/datasets/YunahJang/query-robustness)
- [Paper](https://aclanthology.org/2026.emnlp-main.2156/)
- [Data](https://huggingface.co/datasets/YunahJang/query-robustness/tree/48bbc43c76a4581ab2f62331e455a1f37d9e1482)
- paper: [source](https://aclanthology.org/2026.emnlp-main.2156.pdf) — supports `summary`, `classification`, `data.description`, `ground_truth`, `evaluation.official_metrics`, `evaluation.protocol`, `use`
- dataset_card: [source](https://huggingface.co/datasets/YunahJang/query-robustness/tree/48bbc43c76a4581ab2f62331e455a1f37d9e1482) — supports `data.size`, `data.splits`, `data.format`, `access.data`, `access.license`
- repository: [source](https://github.com/YunahJang/AdaptiveRAG-Robustness/tree/c9a5bfc8d10957baa006bbe24dc05b8e8f842b10) — supports `evaluation.evaluator`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
