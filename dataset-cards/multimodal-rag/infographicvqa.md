<!-- Generated from catalog/datasets/infographicvqa.yaml. Edit the YAML source. -->
# InfographicVQA

[简体中文](infographicvqa.zh-CN.md)

Visual questions requiring joint reading of infographic text, graphics, layout and numerical information.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_convertible` |
| Primary category | `multimodal_rag` |
| Tasks | visual_qa, page_retrieval |
| Modalities | text, image, chart, layout |
| Gold annotation levels | answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Human-authored QA pairs are linked to web-sourced infographic images and provided OCR. VisRAG and VDocRAG filter questions and pool images for retrieval; those released subsets do not replace the original dataset.

Published scale: 30,035 questions over 5,485 images.
Splits: 23,946 train, 2,801 validation and 3,288 test questions.
Format: Infographic images, OCR and QA annotations..

## Ground truth and evaluation

Reference answers and image associations are provided. OCR layout is input data, not a universal human-labeled answer box or native open-domain retrieval relevance set.

Official metrics: ANLS.

Protocol: Use original challenge splits for native QA. For VisRAG or OpenDocVQA, state the filtered query set, candidate image pool and retrieval metric before comparing scores.

## When to use it

- Reading infographics with spatial and numeric reasoning
- Comparing visual retrieval with OCR-based retrieval adaptations

## Limitations and cautions

- The original task supplies the relevant image
- Original and filtered RAG splits have substantially different sizes

## Access and sources

- [Official resource](https://site.docvqa.org/datasets/infographicvqa)
- [Paper](https://arxiv.org/abs/2104.12756)
- [Data](https://rrc.cvc.uab.es/?ch=17&com=downloads)
- official: [source](https://site.docvqa.org/datasets/infographicvqa) — supports `summary`, `data.description`, `access.data`
- paper: [source](https://arxiv.org/abs/2104.12756) — supports `classification.modalities`, `data.size`, `data.splits`, `ground_truth.description`, `evaluation.official_metrics`
- paper: [source](https://arxiv.org/html/2504.09795) — supports `data.description`, `evaluation.protocol`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
