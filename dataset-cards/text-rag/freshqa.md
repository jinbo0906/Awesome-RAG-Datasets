<!-- Generated from catalog/datasets/freshqa.yaml. Edit the YAML source. -->
# FreshQA

Versioned question answering data for facts that change or emerged after model training.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_convertible` |
| Primary category | `text_rag` |
| Tasks | time_sensitive_qa, single_hop_qa |
| Modalities | text |
| Gold annotation levels | answer |
| Evidence provenance | human |
| Corpus / queries / answers | not_provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The authors maintain dated spreadsheet snapshots and an evaluator. Questions and accepted answers are refreshed over time; the release is not one immutable retrieval corpus.


## Ground truth and evaluation

Answer judgments are versioned with the question sheet, not anchored to stable passage coordinates. A source-document snapshot and temporal relevance labels would be an adaptation.

Official metrics: accuracy.

Protocol: Freeze a dated FreshQA sheet and evaluation mode before comparing systems. Record search date, retrieved pages and their capture dates so time-varying answers are not evaluated anachronistically.

## When to use it

- Freshness-aware answer evaluation
- Temporal retrieval protocol design

## Limitations and cautions

- Changing answer keys prevent cross-date score comparison
- No native frozen source pool or evidence spans

## Access and sources

- [Official resource](https://github.com/freshllms/freshqa)
- [Paper](https://arxiv.org/abs/2310.03214)
- repository: [source](https://github.com/freshllms/freshqa) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
