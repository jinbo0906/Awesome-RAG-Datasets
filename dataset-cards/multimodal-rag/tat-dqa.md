<!-- Generated from catalog/datasets/tat-dqa.yaml. Edit the YAML source. -->
# TAT-DQA

[简体中文](tat-dqa.zh-CN.md)

Financial document-image QA combining table and text evidence with discrete numerical reasoning.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_convertible` |
| Primary category | `multimodal_rag` |
| Tasks | visual_qa, text_table_reasoning, table_qa |
| Modalities | text, image, table, layout |
| Gold annotation levels | span, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | CC-BY-4.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

An extension of TAT-QA with PDF documents, converted text blocks and boxes, QA, answer scales and derivations. The author repository states that test ground truth was released in January 2024.

Published scale: 16,558 questions over 2,758 documents and 3,067 pages; each supplied document has at most three pages.
Splits: Train, development and test.
Format: PDFs and JSON document blocks plus QA annotations..

## Ground truth and evaluation

QA annotations include answer forms, scales, derivations and OCR block-to-span mappings. Optional supporting facts are generated heuristically, while block boxes come from PDF extraction or OCR; neither is universal human-labeled table-cell or retrieval gold.

Official metrics: exact_match, F1.

Protocol: Use the official numeric and scale-aware scoring. Keep document blocks and operand mappings when adapting to retrieval; original short-document answering is not corpus-wide financial RAG.

## When to use it

- Numerical reasoning over document images
- Preserving table-text operands and source-block mappings

## Limitations and cautions

- TAT-QA and TAT-DQA are different releases
- Heuristic facts and OCR boxes need separate provenance from human QA

## Access and sources

- [Official resource](https://nextplusplus.github.io/TAT-DQA/)
- [Paper](https://arxiv.org/abs/2207.11871)
- [Data](https://github.com/NExTplusplus/TAT-DQA)
- official: [source](https://nextplusplus.github.io/TAT-DQA/) — supports `summary`, `data.description`, `data.size`, `data.splits`, `ground_truth.description`, `evaluation.official_metrics`, `access.license`
- repository: [source](https://github.com/NExTplusplus/TAT-DQA) — supports `data.description`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
