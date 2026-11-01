<!-- Generated from catalog/datasets/enterpriserag-bench.yaml. Edit the YAML source. -->
# EnterpriseRAG-Bench

[简体中文](enterpriserag-bench.zh-CN.md)

Synthetic company-internal retrieval and QA with dense distractors, conflicting records, completeness queries and absent information.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | multi_hop_qa, evidence_retrieval, rag_robustness |
| Modalities | text |
| Gold annotation levels | document, answer |
| Evidence provenance | synthetic |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | MIT (HF dataset card); record the corpus release separately from the code version. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Public arXiv release dated 2026-05-05, simulating one company across nine source types such as Slack, email, tickets and wikis. The author dataset card supplies questions, expected_doc_ids, gold_answer and answer_facts; documents are provided separately. This is synthetic enterprise data, not a disclosure of real internal communications.

Published scale: More than 500,000 documents and 500 core questions in ten categories; another 100 metadata-dependent questions are excluded from the core leaderboard.
Splits: HF questions/test and documents/test are two configurations, not disjoint training/test corpora; freeze the specific release and gold set.
Format: HF Parquet configurations, JSONL questions and released document archives..

## Ground truth and evaluation

LLM-generated questions, answers, atomic facts and pooled document IDs follow human-in-the-loop corpus scaffolding. High-Level and Info-Not-Found categories have no gold document IDs. Authors treat other gold sets as revisable, not exhaustive human qrels or fact-to-source citation mappings.

Official metrics: Overall_Score, Answer_Correctness, Answer_Completeness, Document_Recall, Invalid_Extra_Docs.

Protocol: Submit question_id, answer and document_ids. Overall Score averages per-question binary correctness times completeness; invalid extra documents is lower-is-better. Preserve no-answer/high-level handling, judge model and whether corrections were applied. Do not compare corrected gold with the initial leaderboard gold as one fixed test; report each release separately.

## When to use it

- Testing coherent cross-document retrieval in noisy enterprise sources
- Studying missing information and gold-set incompleteness at corpus scale

## Limitations and cautions

- Synthetic realism is not validation on private production data
- Atomic answer facts are not minimal source spans
- Gold corrections and judge changes affect score comparability

## Access and sources

- [Official resource](https://github.com/onyx-dot-app/EnterpriseRAG-Bench)
- [Paper](https://arxiv.org/abs/2605.05253)
- [Data](https://huggingface.co/datasets/onyx-dot-app/EnterpriseRAG-Bench)
- paper: [source](https://arxiv.org/abs/2605.05253) — supports `summary`, `data.description`, `data.size`
- dataset_card: [source](https://huggingface.co/datasets/onyx-dot-app/EnterpriseRAG-Bench) — supports `data.splits`, `data.format`, `access.license`, `evaluation.official_metrics`, `evaluation.protocol`
- repository: [source](https://github.com/onyx-dot-app/EnterpriseRAG-Bench) — supports `data.size`, `ground_truth.description`
- paper: [source](https://arxiv.org/html/2605.05253) — supports `ground_truth.provenance`, `ground_truth.description`, `evaluation.protocol`
- repository: [source](https://github.com/onyx-dot-app/EnterpriseRAG-Bench/blob/main/answer_evaluation/README.md) — supports `evaluation.official_metrics`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
