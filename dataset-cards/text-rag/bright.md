<!-- Generated from catalog/datasets/bright.yaml. Edit the YAML source. -->
# BRIGHT

A text retrieval benchmark where relevance depends on substantial reasoning.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `auxiliary` |
| Primary category | `text_rag` |
| Tasks | reasoning_retrieval, evidence_retrieval |
| Modalities | text |
| Evidence levels | document |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / not_provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Queries and candidate documents support reasoning-intensive retrieval evaluation.


## Ground truth and evaluation

Document-level relevance labels evaluate retrieval rather than answer generation.

Official metrics: ndcg_at_10.

Protocol: Use as a retrieval component test; add an answer protocol before calling it an end-to-end RAG benchmark.

## When to use it

- Reasoning-intensive retriever selection
- Out-of-domain retrieval stress tests

## Limitations and cautions

- No native answer-generation gold is specified in this catalog record

## Access and sources

- [Official resource](https://brightbenchmark.github.io/)
- [Paper](https://arxiv.org/abs/2407.12883)
- official: [source](https://brightbenchmark.github.io/) — supports `summary`, `classification.tasks`, `data.description`, `ground_truth.levels`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
