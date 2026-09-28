<!-- Generated from catalog/datasets/mmdocrag.yaml. Edit the YAML source. -->
# MMDocRAG

Multi-page multimodal document QA with cross-modal evidence chains and quote selection.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `multimodal_rag` |
| Tasks | page_retrieval, layout_retrieval, visual_qa, attribution |
| Modalities | text, image, table, chart, layout |
| Gold annotation levels | page, quote, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Questions are grounded in long documents with text and image quotes plus deliberately difficult negative quotes.

Published scale: 4,055 QA pairs from 222 long documents in the project release.

## Ground truth and evaluation

Cross-page and cross-modal evidence chains support quote-selection and cited-answer evaluation.

Official metrics: quote_selection_f1, answer_quality.

Protocol: Report retrieval and quote selection separately from multimodal answer quality.

## When to use it

- Cross-page evidence selection
- Text-image quote integration
- Hard-negative robustness

## Limitations and cautions

- Part of the construction uses generated questions and parser-derived quotes; report human-verified subset separately

## Access and sources

- [Official resource](https://mmdocrag.github.io/MMDocRAG/)
- [Paper](https://arxiv.org/abs/2505.16470)
- [Data](https://github.com/MMDocRAG/MMDocRAG)
- official: [source](https://mmdocrag.github.io/MMDocRAG/) — supports `summary`, `data.size`, `ground_truth.description`, `evaluation.protocol`
- paper: [source](https://proceedings.neurips.cc/paper_files/paper/2025/file/1a93178950e92fd2e7b7448f7d68fd7d-Paper-Datasets_and_Benchmarks_Track.pdf) — supports `data.description`, `classification.modalities`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
