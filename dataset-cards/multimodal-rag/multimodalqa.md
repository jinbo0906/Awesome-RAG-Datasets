<!-- Generated from catalog/datasets/multimodalqa.yaml. Edit the YAML source. -->
# MultiModalQA

[简体中文](multimodalqa.zh-CN.md)

Questions requiring joint reasoning over text, tables and images with supporting-context IDs.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `multimodal_rag` |
| Tasks | multi_hop_qa, text_table_reasoning, visual_qa |
| Modalities | text, table, image |
| Gold annotation levels | document, table, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The release contains 29,918 examples plus separate text, table and image context files; test answers and supporting contexts are withheld.


## Ground truth and evaluation

Supporting-context entries identify source document IDs and modality parts, including intermediate-answer contexts; no uniform bbox or cell gold is asserted.

Official metrics: answer_em, answer_f1.

Protocol: Measure context retrieval and final answer separately; preserve supporting-context IDs and withheld-test protocol.

## When to use it

- Cross-modal multi-hop reasoning
- Text-table-image evidence collection

## Limitations and cautions

- Source-level labels do not identify every relevant table cell or image region

## Access and sources

- [Official resource](https://github.com/allenai/multimodalqa)
- [Paper](https://arxiv.org/abs/2104.06039)
- repository: [source](https://github.com/allenai/multimodalqa) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
