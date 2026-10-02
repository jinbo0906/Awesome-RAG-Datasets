<!-- Generated from catalog/datasets/ambigqa.yaml. Edit the YAML source. -->
# AmbigQA / AmbigNQ

[简体中文](ambigqa.zh-CN.md)

Ambiguous Natural Questions annotated with multiple interpretations, acceptable answers and disambiguated questions.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_convertible` |
| Primary category | `text_rag` |
| Tasks | single_hop_qa |
| Modalities | text |
| Gold annotation levels | answer |
| Evidence provenance | human |
| Corpus / queries / answers | external / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The core AmbigNQ annotations provide questions and alternative single-answer or multiple-QA outputs. Author resources include separate Wikipedia databases and a later semi-oracle evidence-article package, which should be identified when used.

Splits: Public train and development annotations; test evaluation follows the upstream submission process.

## Ground truth and evaluation

Multiple acceptable outputs contain answer aliases and question rewrites. Viewed page titles and annotation search queries are incomplete metadata, not exhaustive retrieval gold or permitted test inputs.

Official metrics: F1 answer, F1 edit-f1, F1 bleu1, F1 bleu2, F1 bleu3, F1 bleu4.

Protocol: Score answer coverage and disambiguation separately with the official evaluator; label semi-oracle evidence experiments and preserve alternative annotations.

## When to use it

- Covering multiple valid interpretations
- Distinguishing answer coverage from disambiguation quality

## Limitations and cautions

- Semi-oracle evidence changes the retrieval task
- Annotation metadata must not be treated as system input

## Access and sources

- [Official resource](https://github.com/shmsw25/AmbigQA)
- [Paper](https://arxiv.org/abs/2004.10645)
- repository: [source](https://github.com/shmsw25/AmbigQA) — supports `summary`, `data.description`, `data.splits`, `ground_truth.description`, `evaluation.protocol`
- repository: [source](https://github.com/shmsw25/AmbigQA/blob/main/ambigqa_evaluate_script.py) — supports `evaluation.official_metrics`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
