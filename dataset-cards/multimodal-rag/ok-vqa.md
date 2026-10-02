<!-- Generated from catalog/datasets/ok-vqa.yaml. Edit the YAML source. -->
# OK-VQA

[简体中文](ok-vqa.zh-CN.md)

Outside-knowledge visual QA whose images alone do not contain enough information to answer.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_convertible` |
| Primary category | `multimodal_rag` |
| Tasks | visual_qa, multimodal_retrieval |
| Modalities | text, image |
| Gold annotation levels | answer |
| Evidence provenance | human |
| Corpus / queries / answers | not_provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The release supplies question/answer annotations and links to COCO input images, without a fixed external knowledge corpus. NoteMR uses it with passage retrieval in CVPR 2025; M2KR defines another adaptation.

Published scale: 14,055 questions, each with five human reference answers.
Splits: Official train and test; v1.1 updates answer stemming, not questions or images.
Format: VQA-format question and annotation JSON; COCO images acquired separately..

## Ground truth and evaluation

Accepted answer strings are provided, but the original release does not identify gold Wikipedia passages or supporting image regions. Later retrieval supervision must be attributed to its own construction.

Official metrics: VQA_accuracy.

Protocol: Use the official answer normalization and fix v1.1 labels. Document the external corpus and retrieval supervision; scores from different knowledge pools or M2KR conversions are not interchangeable.

## When to use it

- Knowledge retrieval conditioned on image and question
- Comparing external knowledge with model-only answering

## Limitations and cautions

- Native annotations provide answers rather than passage-level retrieval gold
- COCO image terms are separate from QA annotations

## Access and sources

- [Official resource](https://okvqa.allenai.org/)
- [Paper](https://arxiv.org/abs/1906.00067)
- [Data](https://okvqa.allenai.org/download.html)
- official: [source](https://okvqa.allenai.org/) — supports `summary`, `data.size`, `ground_truth.description`
- official: [source](https://okvqa.allenai.org/download.html) — supports `data.description`, `data.splits`, `data.format`, `evaluation.protocol`
- paper: [source](https://arxiv.org/abs/1906.00067) — supports `evaluation.official_metrics`, `classification.rag_role`
- repository: [source](https://github.com/Jorffy/NoteMR) — supports `data.description`, `use.best_for`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
