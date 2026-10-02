<!-- Generated from catalog/datasets/qrecc.yaml. Edit the YAML source. -->
# QReCC

[简体中文](qrecc.zh-CN.md)

Open-domain conversational QA with human question rewrites, answers and source URLs over a released web collection.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | conversational_qa, query_rewriting, evidence_retrieval |
| Modalities | text |
| Gold annotation levels | document, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | CC-BY-SA-3.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Conversations extend QuAC, TREC CAsT and Natural Questions. Each turn includes context, a standalone rewrite, an answer and its source URL; the collection contains about 10M web pages segmented into 54M passages.

Published scale: Approximately 14K conversations and 81K question-answer pairs.

## Ground truth and evaluation

Human rewrites and answers are linked to source web pages. The original retrieval evaluator can determine passage relevance through answer-overlap thresholds; this should not be described as exhaustive human passage relevance annotation.

Official metrics: MRR, Recall@k, exact_match, token_f1.

Protocol: Preserve dialogue order and distinguish gold rewrites from predicted rewrites. Report the original retrieval answer-overlap threshold or the provenance of replacement qrels, and score answer quality separately.

## When to use it

- Context-dependent question rewriting
- Retrieval and answer errors across dialogue turns

## Limitations and cautions

- Source URLs do not establish complete passage-level relevance
- Gold-rewrite retrieval and end-to-end conversational QA are different settings

## Access and sources

- [Official resource](https://github.com/apple-aiml-research/ml-qrecc)
- [Paper](https://aclanthology.org/2021.naacl-main.44/)
- repository: [source](https://github.com/apple-aiml-research/ml-qrecc) — supports `summary`, `data.description`, `data.size`, `ground_truth.description`, `access.license`
- repository: [source](https://github.com/apple-aiml-research/ml-qrecc/blob/main/utils/evaluate_retrieval.py) — supports `evaluation.official_metrics`, `evaluation.protocol`
- repository: [source](https://github.com/apple-aiml-research/ml-qrecc/blob/main/utils/evaluate_qa.py) — supports `evaluation.official_metrics`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
