<!-- Generated from catalog/datasets/tempo.yaml. Edit the YAML source. -->
# TEMPO

[简体中文](tempo.zh-CN.md)

Cross-period reasoning and step-wise retrieval over a dated Stack Exchange document collection.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | time_sensitive_qa, evidence_retrieval, multi_hop_qa |
| Modalities | text |
| Gold annotation levels | document, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Hugging Face configurations release documents, query examples with gold_ids/gold_answers, step-specific gold documents and model-reasoning query variants. Human-selected posts and LLM-assisted temporal annotation support both document retrieval and the paper's downstream QA experiment.

Published scale: 1,730 queries, 3,976 retrieval steps and 1,654,055 documents across 13 Stack Exchange domains.
Splits: Domain-named evaluation splits; reasoning-augmented queries are variants, not independent test questions.
Format: Hugging Face Parquet.

## Ground truth and evaluation

gold_ids and step-level mappings identify relevant documents; gold_answers retain reference answer text. Temporal intent, anchors and plan annotations are model-assisted with sampled human review, not exhaustive human verification of every temporal judgment.

Official metrics: nDCG@10, temporal_precision_at_k, temporal_relevance_at_k, temporal_coverage_at_k, ndcg_full_coverage_at_k, answer_correctness_0_100.

Protocol: Keep domain, original versus reasoning-augmented query and query-to-document versus step-wise retrieval separate. The author run.py excludes each query's negative_ids from ranking; retaining them is a stricter full-corpus adaptation, not the same leaderboard protocol. Temporal metrics use model judgments. Table 6/Appendix G.3 use a fixed generator and a 0–100 reference-coverage judge, including no-retrieval and gold-document controls.

## When to use it

- Testing whether retrieved evidence spans required periods
- Evaluating step-wise temporal evidence coverage separately from final QA

## Limitations and cautions

- HF metadata specifies CC BY 4.0 while the data card notes CC BY-SA upstream Stack Exchange content; applicable terms need checking
- Filtering negative_ids changes the candidate universe and must be reported
- Model-judged temporal completeness is not independently exhaustive evidence gold
- The January 2026 author preprint is not assigned an unverified conference venue

## Access and sources

- [Official resource](https://tempo-bench.github.io/)
- [Paper](https://arxiv.org/abs/2601.09523)
- [Data](https://huggingface.co/datasets/tempo26/Tempo)
- paper: [source](https://arxiv.org/html/2601.09523) — supports `summary`, `classification`, `data.size`, `ground_truth`, `evaluation.official_metrics`, `evaluation.protocol`, `use`
- dataset_card: [source](https://huggingface.co/datasets/tempo26/Tempo) — supports `data.description`, `data.splits`, `data.format`, `data.corpus`, `data.queries`, `data.answers`, `access.data`, `access.license`, `access.gated`
- repository: [source](https://github.com/tempo-bench/Tempo/blob/main/run.py) — supports `evaluation.protocol`, `use.caveats`
- repository: [source](https://github.com/tempo-bench/Tempo/blob/main/temporal_metrics.py) — supports `evaluation.evaluator`, `evaluation.official_metrics`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
