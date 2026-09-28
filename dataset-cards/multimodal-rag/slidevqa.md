<!-- Generated from catalog/datasets/slidevqa.yaml. Edit the YAML source. -->
# SlideVQA

Multi-image slide-deck QA with evidence-page selection and document layout boxes.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `multimodal_rag` |
| Tasks | page_retrieval, visual_qa |
| Modalities | text, image, layout, chart |
| Gold annotation levels | page, bbox, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The source reports 14,484 QA pairs across slide decks and 890,945 layout bounding boxes; the Hugging Face package excludes OCR and bbox data.


## Ground truth and evaluation

QA records identify evidence_pages and answers; bbox files label slide layout objects, but those boxes are not automatically question-specific evidence.

Official metrics: evidence_selection, answer_accuracy.

Protocol: Evaluate evidence-page selection separately from answer generation and disclose whether OCR and bbox files are used.

## When to use it

- Cross-slide evidence retrieval
- Layout-aware visual QA

## Limitations and cautions

- Layout boxes must not be mistaken for per-question gold regions
- Some upstream slide URLs are unavailable

## Access and sources

- [Official resource](https://github.com/nttmdlab-nlp/SlideVQA)
- repository: [source](https://github.com/nttmdlab-nlp/SlideVQA) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.protocol`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
