<!-- Generated from catalog/datasets/vidoseek.yaml. Edit the YAML source. -->
# ViDoSeek

Visual document retrieval and answer benchmark over a large PDF collection.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `multimodal_rag` |
| Tasks | page_retrieval, visual_qa |
| Modalities | text, image, table, layout |
| Evidence levels | page, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Query records provide a reference answer and metadata including original file and reference page numbers.


## Ground truth and evaluation

Query metadata identifies reference pages, suitable for page-level retrieval scoring.

Official metrics: page_recall, answer_accuracy.

Protocol: Distinguish retrieved-page accuracy from final answer quality.

## When to use it

- Visual document RAG over many pages
- Iterative evidence retrieval

## Limitations and cautions

- Page labels do not by themselves specify exact figure or cell boundaries

## Access and sources

- [Official resource](https://github.com/Alibaba-NLP/ViDoRAG)
- [Paper](https://arxiv.org/abs/2502.18017)
- repository: [source](https://github.com/Alibaba-NLP/ViDoRAG) — supports `summary`, `data.description`, `ground_truth.description`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
