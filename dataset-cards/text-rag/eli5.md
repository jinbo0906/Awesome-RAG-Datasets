<!-- Generated from catalog/datasets/eli5.yaml. Edit the YAML source. -->
# ELI5

Explanatory long-form QA drawn from Reddit questions and answers with web support documents.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_convertible` |
| Primary category | `text_rag` |
| Tasks | long_form_qa, attribution |
| Modalities | text |
| Evidence levels | answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | external / provided / provided |
| Original data license | source content rights vary |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Official scripts reconstruct Reddit QA and CommonCrawl support documents; processed data are not hosted by the authors.


## Ground truth and evaluation

Web support documents are selected heuristically, not a human-annotated minimal citation set.

Official metrics: rouge_l.

Protocol: Record the Reddit and CommonCrawl snapshot; ALCE-ELI5 uses a separate BM25 retrieval bundle and citation evaluator.

## When to use it

- Long-form explanation generation
- Citation evaluation through ALCE

## Limitations and cautions

- Reconstruction requires substantial compute and upstream content access
- Support passages are heuristic rather than human gold

## Access and sources

- [Official resource](https://github.com/facebookresearch/ELI5)
- [Paper](https://arxiv.org/abs/1907.09190)
- repository: [source](https://github.com/facebookresearch/ELI5) — supports `summary`, `data.description`, `ground_truth.description`, `use.caveats`
- repository: [source](https://github.com/princeton-nlp/ALCE) — supports `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
