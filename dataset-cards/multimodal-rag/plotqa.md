<!-- Generated from catalog/datasets/plotqa.yaml. Edit the YAML source. -->
# PlotQA

[简体中文](plotqa.zh-CN.md)

Template-generated QA over scientific plots with open-vocabulary labels and computed numerical answers.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_convertible` |
| Primary category | `multimodal_rag` |
| Tasks | visual_qa, table_qa |
| Modalities | text, image, chart, table |
| Gold annotation levels | bbox, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | CC-BY-4.0 for data; MIT for code. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Plots are rendered from real-world data, with question templates derived from crowdsourcing. The release includes image annotations and two QA versions; VisRAG uses a filtered, pooled-image retrieval adaptation.

Published scale: 224,377 plots; QA v1 has 8,190,674 pairs and v2 has 28,952,641 pairs.
Splits: Original train, validation and test with separate versioned QA files.
Format: PNG plots, plot annotations and QA JSON..

## Ground truth and evaluation

The QA schema has image_index and an answer_bbox when the answer appears in the plot. Computed answers need not have a box; plot-level object annotations are distinct from question-specific evidence and retrieval qrels.

Official metrics: answer_accuracy.

Protocol: Fix QA version and numerical-answer tolerance. Original QA supplies the plot; report VisRAG's filtering, candidate pool and retrieval scores separately from native plot-answering accuracy.

## When to use it

- Numeric chart reading and open-vocabulary answers
- Conditional answer-box evaluation and explicit retrieval conversion

## Limitations and cautions

- Computed answers often do not correspond to a visible answer box
- QA v1/v2 and the much smaller VisRAG adaptation are different protocols

## Access and sources

- [Official resource](https://github.com/NiteshMethani/PlotQA)
- [Paper](https://arxiv.org/abs/1909.00997)
- [Data](https://github.com/NiteshMethani/PlotQA/blob/master/PlotQA_Dataset.md)
- repository: [source](https://github.com/NiteshMethani/PlotQA) — supports `summary`, `data.description`, `data.size`, `access.license`
- repository: [source](https://github.com/NiteshMethani/PlotQA/blob/master/PlotQA_Dataset.md) — supports `data.size`, `data.splits`, `data.format`, `ground_truth.description`
- paper: [source](https://arxiv.org/abs/1909.00997) — supports `evaluation.official_metrics`, `evaluation.protocol`
- paper: [source](https://proceedings.iclr.cc/paper_files/paper/2025/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf) — supports `data.description`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
