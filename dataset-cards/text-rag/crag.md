<!-- Generated from catalog/datasets/crag.yaml. Edit the YAML source. -->
# CRAG

Time-aware factual QA benchmark with web results and mock knowledge APIs for RAG.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | single_hop_qa, multi_hop_qa |
| Modalities | text, graph |
| Gold annotation levels | answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | CC BY-NC 4.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Questions span five domains and eight categories; released retrieval content includes web search results and mock APIs.


## Ground truth and evaluation

Gold and alternative answers are provided; retrieved pages are candidate context rather than gold supporting spans.

Official metrics: correctness_with_abstention.

Protocol: Official scoring distinguishes correct answers, missing answers and incorrect answers.

## When to use it

- Temporal factual retrieval
- Abstention and error-cost analysis

## Limitations and cautions

- Search results are not relevance judgments; do not treat every returned page as supporting evidence

## Access and sources

- [Official resource](https://github.com/facebookresearch/CRAG)
- [Paper](https://arxiv.org/abs/2406.04744)
- repository: [source](https://github.com/facebookresearch/CRAG) — supports `summary`, `data.description`, `evaluation.protocol`, `access.license`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
