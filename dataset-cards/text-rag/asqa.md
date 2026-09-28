<!-- Generated from catalog/datasets/asqa.yaml. Edit the YAML source. -->
# ASQA

Ambiguous factoid questions with long answers and disambiguating short-answer pairs.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_convertible` |
| Primary category | `text_rag` |
| Tasks | long_form_qa, attribution |
| Modalities | text |
| Gold annotation levels | answer |
| Evidence provenance | human |
| Corpus / queries / answers | external / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Questions and long-form answers are accompanied by extractive QA pairs; ALCE distributes a retrieval-results adaptation.


## Ground truth and evaluation

Reference answers cover multiple interpretations; native citation links to source passages are not equivalent to the ALCE adaptation.

Official metrics: rouge, qa_accuracy.

Protocol: If using ALCE retrieved passages, report its retrieval snapshot and citation scoring separately.

## When to use it

- Ambiguity-aware long-form answer coverage
- Citation evaluation through ALCE

## Limitations and cautions

- Original ASQA and ALCE-ASQA are distinct evaluation settings

## Access and sources

- [Official resource](https://github.com/google-research/language/tree/master/language/asqa)
- dataset_card: [source](https://github.com/tensorflow/datasets/blob/master/docs/catalog/asqa.md) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.official_metrics`
- repository: [source](https://github.com/princeton-nlp/ALCE) — supports `data.description`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
