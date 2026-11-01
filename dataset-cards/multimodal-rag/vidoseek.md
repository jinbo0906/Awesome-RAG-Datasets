<!-- Generated from catalog/datasets/vidoseek.yaml. Edit the YAML source. -->
# ViDoSeek

[简体中文](vidoseek.zh-CN.md)

Visual document retrieval and answer benchmark over a large PDF collection.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `rag_native` |
| Primary category | `multimodal_rag` |
| Tasks | page_retrieval, visual_qa |
| Modalities | text, image, table, layout |
| Gold annotation levels | page, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

ViDoRAG (EMNLP 2025) introduces the ViDoSeek dataset, not an independent dataset named after the method. Query records provide a reference answer and metadata including original file and reference page numbers; the official Hugging Face release also separates a refined SlideVQA variant.


## Ground truth and evaluation

Query metadata identifies reference pages, suitable for page-level retrieval scoring.

Official metrics: page_recall, answer_accuracy.

Protocol: Distinguish retrieved-page accuracy from final answer quality.

## When to use it

- Visual document RAG over many pages
- Iterative evidence retrieval

## Limitations and cautions

- Page labels do not by themselves specify exact figure or cell boundaries
- ViDoRAG is the method and paper name; keep ViDoSeek and SlideVQA-refined release variants distinct

## Access and sources

- [Official resource](https://github.com/Alibaba-NLP/ViDoRAG)
- [Paper](https://aclanthology.org/2025.emnlp-main.464/)
- [Data](https://huggingface.co/datasets/Qiuchen-Wang/ViDoSeek)
- repository: [source](https://github.com/Alibaba-NLP/ViDoRAG) — supports `summary`, `data.description`, `ground_truth.description`
- paper: [source](https://aclanthology.org/2025.emnlp-main.464/) — supports `data.description`, `use.caveats`, `access.paper`
- dataset_card: [source](https://huggingface.co/datasets/Qiuchen-Wang/ViDoSeek) — supports `access.data`, `data.description`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
