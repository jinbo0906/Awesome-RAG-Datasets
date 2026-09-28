<!-- Generated from catalog/datasets/chartqa.yaml. Edit the YAML source. -->
# ChartQA

Chart-image question answering with human and generated questions plus optional chart-element boxes.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_convertible` |
| Primary category | `multimodal_rag` |
| Tasks | visual_qa, table_qa |
| Modalities | image, chart, table |
| Gold annotation levels | bbox, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The official full release includes chart images, QA, underlying tables and element annotations; train_human and train_augmented have different origins.


## Ground truth and evaluation

Element boxes are available in the full version, but are not necessarily per-question minimal evidence boxes.

Official metrics: relaxed_accuracy.

Protocol: For retrieval experiments construct a chart corpus and state whether underlying tables or element boxes are exposed.

## When to use it

- Chart perception and numerical reasoning
- Visual-versus-table ablations

## Limitations and cautions

- Native task supplies a chart; it is not open-corpus RAG
- SVG-derived boxes can be noisy or missing

## Access and sources

- [Official resource](https://github.com/vis-nlp/ChartQA)
- [Paper](https://aclanthology.org/2022.findings-acl.177/)
- repository: [source](https://github.com/vis-nlp/ChartQA) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.protocol`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
