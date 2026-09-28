<!-- Generated from catalog/datasets/mmdocir.yaml. Edit the YAML source. -->
# MMDocIR

Long-document multimodal retrieval benchmark with human page and layout evidence labels.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `auxiliary` |
| Primary category | `multimodal_rag` |
| Tasks | page_retrieval, layout_retrieval |
| Modalities | text, image, table, equation, layout |
| Gold annotation levels | page, layout, bbox |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Evaluation data covers 313 long documents; expert questions have page and layout evidence, while a larger bootstrapped collection supports training.

Published scale: Evaluation: 1,658 expert questions; 2,107 page labels; 2,638 layout labels.

## Ground truth and evaluation

Annotators select evidence pages and MinerU-derived layout elements; manually add missed regions.

Official metrics: recall_at_k.

Protocol: Page retrieval and layout retrieval are separate tasks.

## When to use it

- Measuring evidence fragmentation across pages and regions
- Visual versus OCR retrieval

## Limitations and cautions

- The layout labels depend partly on a parser; keep original page coordinates and parser version
- Project page and paper differ on question count; pin the release used

## Access and sources

- [Official resource](https://mmdocrag.github.io/MMDocIR/)
- [Paper](https://arxiv.org/abs/2501.08828)
- [Data](https://huggingface.co/MMDocIR)
- official: [source](https://mmdocrag.github.io/MMDocIR/) — supports `summary`, `data.description`, `data.size`, `ground_truth.description`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
