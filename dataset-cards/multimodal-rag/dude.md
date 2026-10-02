<!-- Generated from catalog/datasets/dude.yaml. Edit the YAML source. -->
# DUDE

[简体中文](dude.zh-CN.md)

Multi-page document QA with varied answer forms, domains and optional answer-region annotations.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_convertible` |
| Primary category | `multimodal_rag` |
| Tasks | visual_qa, page_retrieval, long_context_qa |
| Modalities | text, image, layout, table |
| Gold annotation levels | page, bbox, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | CC-BY-4.0 for the author-linked dataset loader; source documents retain their upstream terms. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The official release contains PDFs, QA annotations and alternative OCR engines. The author-linked loader supports the public ground truth; OpenDocVQA creates a separately filtered open-domain version.

Splits: Train, validation and test; use the named public ground-truth release rather than assuming every competition package exposes labels.
Format: PDF documents, JSON annotations and OCR in provider-specific or DUE format..

## Ground truth and evaluation

The loader exposes answers, accepted variants and answers_page_bounding_boxes with page coordinates. Boxes may be absent, and abstract or unanswerable items do not imply a localized supporting region.

Official metrics: ANLS.

Protocol: Preserve answer type, empty answers, page numbering and OCR configuration. ANLS uses the official threshold; open-domain retrieval adaptations must disclose their pool and filtered queries.

## When to use it

- Page selection and long-document answering
- Testing varied answer forms and available answer regions

## Limitations and cautions

- Answer boxes are not present for every question
- OCR outputs and the filtered OpenDocVQA protocol are separate versions

## Access and sources

- [Official resource](https://github.com/duchallenge-team/dude)
- [Paper](https://openaccess.thecvf.com/content/ICCV2023/html/Van_Landeghem_Document_Understanding_Dataset_and_Evaluation_DUDE_ICCV_2023_paper.html)
- [Data](https://huggingface.co/datasets/jordyvl/DUDE_loader)
- repository: [source](https://github.com/duchallenge-team/dude) — supports `summary`, `data.description`, `data.format`, `use.caveats`
- dataset_card: [source](https://huggingface.co/datasets/jordyvl/DUDE_loader/blob/main/DUDE_loader.py) — supports `data.splits`, `ground_truth.levels`, `ground_truth.description`, `access.license`
- repository: [source](https://github.com/Jordy-VL/DUDEeval) — supports `evaluation.official_metrics`, `evaluation.protocol`
- paper: [source](https://arxiv.org/html/2504.09795) — supports `data.description`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
