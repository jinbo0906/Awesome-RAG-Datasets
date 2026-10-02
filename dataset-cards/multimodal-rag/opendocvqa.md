<!-- Generated from catalog/datasets/opendocvqa.yaml. Edit the YAML source. -->
# OpenDocVQA

[简体中文](opendocvqa.zh-CN.md)

VDocRAG's released open-domain document-image QA collection with pooled pages and relevant-image identifiers.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_native` |
| Primary category | `multimodal_rag` |
| Tasks | page_retrieval, visual_qa, multi_hop_qa |
| Modalities | text, image, table, chart, layout |
| Gold annotation levels | page, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | Per-source licenses; MHDocVQA/VisualMRC/SlideVQA QA use the NTT evaluation license. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Nine filtered collections combine DocVQA, InfographicVQA, VisualMRC, ChartQA, OpenWikiTable, DUDE, MPMQA, SlideVQA and new MHDocVQA. Official QA and corpus repositories are released separately.

Published scale: Approximately 43,000 QA pairs over 200,000 document images, including distractor pages.
Splits: Source-specific train/development and test configurations; ChartQA and SlideVQA are zero-shot test sources.
Format: Hugging Face QA records with query, answers and relevant_doc_ids; separate image corpus..

## Ground truth and evaluation

relevant_doc_ids identify relevant document images, including multiple images for MHDocVQA. Human source QA and newly constructed multi-hop questions coexist; uniform region, table-cell and minimal-span gold is not claimed.

Official metrics: nDCG@5, ANLS, relaxed_accuracy, F1.

Protocol: Distinguish source-specific single-pool and unified all-pool retrieval. Use nDCG@5 for retrieval and original source QA metrics; VDocRAG's reported generation uses the top three retrieved images.

## When to use it

- Open-domain page retrieval followed by visual answering
- Comparing separate source pools with a unified image corpus

## Limitations and cautions

- The corpus requires accepting terms and sharing contact information
- Filtered source QA and new MHDocVQA must retain their dataset identities

## Access and sources

- [Official resource](https://vdocrag.github.io/)
- [Paper](https://arxiv.org/abs/2504.09795)
- [Data](https://huggingface.co/datasets/NTT-hil-insight/OpenDocVQA)
- official: [source](https://vdocrag.github.io/) — supports `summary`, `data.size`, `use.best_for`
- dataset_card: [source](https://huggingface.co/datasets/NTT-hil-insight/OpenDocVQA) — supports `data.description`, `data.splits`, `data.format`, `ground_truth.description`, `access.license`
- dataset_card: [source](https://huggingface.co/datasets/NTT-hil-insight/OpenDocVQA-Corpus) — supports `access.gated`, `access.license`, `use.caveats`
- paper: [source](https://arxiv.org/html/2504.09795) — supports `evaluation.official_metrics`, `evaluation.protocol`, `ground_truth.provenance`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
