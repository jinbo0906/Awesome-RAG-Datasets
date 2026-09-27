<!-- Generated from catalog/datasets/mp-docvqa.yaml. Edit the YAML source. -->
# MP-DocVQA

Multi-page document visual question answering with answer-page supervision.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_convertible` |
| Primary category | `multimodal_rag` |
| Tasks | page_retrieval, visual_qa |
| Modalities | text, image, layout |
| Evidence levels | page, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The challenge expands document-image QA to multi-page documents; official data and evaluation are hosted through the DocVQA/RRC challenge.


## Ground truth and evaluation

An answer page can score page selection, but does not establish a minimal region or cross-page evidence chain.

Official metrics: anls, page_accuracy.

Protocol: Distinguish closed-document page selection from open-corpus document retrieval and use the official challenge split.

## When to use it

- Page selection within one document
- OCR-versus-visual QA

## Limitations and cautions

- Not open multi-document retrieval by default
- Answer-page truth is not a question-specific bbox

## Access and sources

- [Official resource](https://rrc.cvc.uab.es/?ch=17&com=tasks)
- [Paper](https://arxiv.org/abs/2212.05935)
- official: [source](https://rrc.cvc.uab.es/?ch=17&com=tasks) — supports `summary`, `data.description`
- paper: [source](https://arxiv.org/abs/2212.05935) — supports `ground_truth.description`, `evaluation.official_metrics`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
