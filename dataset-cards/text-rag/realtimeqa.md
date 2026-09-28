<!-- Generated from catalog/datasets/realtimeqa.yaml. Edit the YAML source. -->
# RealTime QA

Recurring current-events QA releases with dated questions and retrieval baselines.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_convertible` |
| Primary category | `text_rag` |
| Tasks | time_sensitive_qa |
| Modalities | text |
| Gold annotation levels | answer |
| Evidence provenance | human |
| Corpus / queries / answers | external / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The official platform releases roughly 30 questions per weekly round, historical question files, and Google Custom Search/DPR baseline retrieval results. Web and news source collections are external and change over time.


## Ground truth and evaluation

Dated answers support temporal QA, while released search results are baseline outputs rather than source-coordinate gold evidence for every round.

Official metrics: answer_accuracy.

Protocol: Identify the question week and answer cut-off; record whether the model saw contemporaneous or later web evidence. Do not pool weeks without controlling source availability.

## When to use it

- Time-aware RAG
- Testing changing factual answers

## Limitations and cautions

- No single permanent retrieval corpus
- Search-baseline outputs are not universal evidence labels

## Access and sources

- [Official resource](https://github.com/realtimeqa/realtimeqa_public)
- repository: [source](https://github.com/realtimeqa/realtimeqa_public) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
