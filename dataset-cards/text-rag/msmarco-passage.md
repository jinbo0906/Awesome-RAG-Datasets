<!-- Generated from catalog/datasets/msmarco-passage.yaml. Edit the YAML source. -->
# MS MARCO Passage Ranking (v1)

Large-scale web passage retrieval with query-passage relevance judgments.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `auxiliary` |
| Primary category | `text_rag` |
| Tasks | evidence_retrieval |
| Modalities | text |
| Gold annotation levels | document |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / not_provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

This record covers the passage-ranking v1 variant, not the original MS MARCO generative QA task, document ranking or TREC Deep Learning track. The v1 collection has about 8.8 million passages, queries and sparse qrels.


## Ground truth and evaluation

Qrels identify relevant passages for ranking. They do not provide a complete set of all relevant passages or a reference generated answer in this ranking variant.

Official metrics: mrr_at_10.

Protocol: State v1 versus v2, train/dev/test split and full-retrieval versus reranking setting. Sparse judgments require caution when treating unjudged passages as negatives.

## When to use it

- Retriever training and ranking controls
- Large-scale passage indexing

## Limitations and cautions

- Retrieval-only variant is not an end-to-end answer benchmark
- Sparse qrels can undercount relevant evidence

## Access and sources

- [Official resource](https://microsoft.github.io/msmarco/)
- repository: [source](https://github.com/microsoft/msmarco/blob/master/Datasets.md) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.protocol`
- repository: [source](https://github.com/microsoft/MSMARCO-Passage-Ranking) — supports `evaluation.official_metrics`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
