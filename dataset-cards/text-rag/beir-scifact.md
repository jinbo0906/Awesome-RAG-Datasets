<!-- Generated from catalog/datasets/beir-scifact.yaml. Edit the YAML source. -->
# SciFact (BEIR variant)

Scientific claim-to-abstract retrieval as packaged for the BEIR zero-shot IR suite.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `auxiliary` |
| Primary category | `text_rag` |
| Tasks | fact_verification, evidence_retrieval |
| Modalities | text |
| Evidence levels | document |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / not_provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The BEIR package supplies corpus, queries and document-level relevance judgments for scientific claims; this record is the BEIR variant, not the original SciFact claim-verification package.


## Ground truth and evaluation

BEIR qrels identify relevant abstracts, not an answer-generation gold standard.

Official metrics: ndcg_at_10, map_at_k, recall_at_k.

Protocol: Use BEIR test qrels and fixed corpus; add a separate answer task before claiming end-to-end RAG.

## When to use it

- Scientific retriever comparisons
- Corpus-query-qrels schema demonstration

## Limitations and cautions

- Retrieval-only auxiliary; no native generated-answer evaluation

## Access and sources

- [Official resource](https://github.com/beir-cellar/beir)
- repository: [source](https://github.com/beir-cellar/beir) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.official_metrics`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
