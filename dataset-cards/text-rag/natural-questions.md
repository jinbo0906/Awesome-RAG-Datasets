<!-- Generated from catalog/datasets/natural-questions.yaml. Edit the YAML source. -->
# Natural Questions

[简体中文](natural-questions.zh-CN.md)

Search-query questions paired with Wikipedia pages and long or short answer annotations.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_convertible` |
| Primary category | `text_rag` |
| Tasks | single_hop_qa, evidence_retrieval |
| Modalities | text |
| Gold annotation levels | span, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Each example includes a question and a candidate Wikipedia page; an open-corpus index must be defined separately for retrieval experiments.


## Ground truth and evaluation

Long answers identify an HTML region and short answers identify one or more text spans; some examples have no answer.

Official metrics: long_answer_f1, short_answer_f1.

Protocol: Preserve byte and HTML coordinates when converting to clean text or chunks.

## When to use it

- Source-coordinate evidence coverage
- Answerable and unanswerable QA

## Limitations and cautions

- The native task supplies a candidate page rather than an open-corpus retrieval protocol

## Access and sources

- [Official resource](https://github.com/google-research-datasets/natural-questions)
- repository: [source](https://github.com/google-research-datasets/natural-questions) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.official_metrics`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
