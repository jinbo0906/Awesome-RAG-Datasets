<!-- Generated from catalog/datasets/feverous.yaml. Edit the YAML source. -->
# FEVEROUS

[简体中文](feverous.zh-CN.md)

Open-domain fact verification over Wikipedia sentences and table cells.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `table_rag` |
| Tasks | fact_verification, evidence_retrieval, text_table_reasoning |
| Modalities | text, table |
| Gold annotation levels | sentence, table_cell, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Released claims are labeled Supports, Refutes or Not Enough Info against Wikipedia pages containing prose and tables.

Published scale: 87,026 verified claims in the full dataset; smaller study subsets must be identified separately.

## Ground truth and evaluation

Up to three evidence sets may contain sentence, cell, header, caption or list-item IDs with structural context.

Official metrics: label_accuracy, feverous_score.

Protocol: Evaluate complete evidence set and verdict jointly.

## When to use it

- Text-table evidence fusion
- Cell and header preservation
- Alternative evidence-set scoring

## Limitations and cautions

- A verdict-only score hides failed cell retrieval; retain structural context for cell IDs

## Access and sources

- [Official resource](https://fever.ai/dataset/feverous.html)
- [Paper](https://arxiv.org/abs/2106.05707)
- [Data](https://huggingface.co/datasets/fever/feverous)
- repository: [source](https://github.com/Raldir/FEVEROUS) — supports `summary`, `data.size`, `ground_truth.description`, `evaluation.protocol`
- dataset_card: [source](https://huggingface.co/datasets/fever/feverous) — supports `ground_truth.alternatives`, `classification.modalities`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
