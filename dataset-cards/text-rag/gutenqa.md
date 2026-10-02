<!-- Generated from catalog/datasets/gutenqa.yaml. Edit the YAML source. -->
# GutenQA

[简体中文](gutenqa.zh-CN.md)

Narrative-book QA with answer-containing substrings and multiple released segmentation formats for chunking and retrieval comparison.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | long_context_qa, evidence_retrieval |
| Modalities | text |
| Gold annotation levels | quote, answer |
| Evidence provenance | synthetic |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | MIT dataset card; underlying books retain Project Gutenberg terms |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Project Gutenberg books are released in paragraph, recursive, semantic, proposition and LumberChunker formats. Question records include book identity, answers and a Chunk Must Contain substring for matching evidence across segmentations.

Published scale: 3,000 QA pairs from 100 narrative books, with 30 QA pairs per book.
Format: Parquet.

## Ground truth and evaluation

The answer-containing substring anchors evidence within a book. Released chunk IDs identify a particular segmentation, not independently annotated optimal human cut points.

Official metrics: dcg_at_k, recall_at_k.

Protocol: Use book-level retrieval pools and the released substring matching procedure; report DCG and Recall at the selected k (the paper uses 1/2/5/10/20). The paper's answer-generation experiment uses a separate four-autobiography, 280-question evaluation, not the released 100-book/3,000-question GutenQA set. A new generation protocol must be documented separately. Fix the paragraph corpus and context budget when comparing chunkers.

## When to use it

- Comparing segmentation with a stable answer substring anchor
- In-document narrative evidence retrieval

## Limitations and cautions

- Construction using LumberChunker can favor its segmentation distribution
- Sparse answer-containing evidence does not measure all semantic boundary quality

## Access and sources

- [Official resource](https://github.com/joaodsmarques/LumberChunker)
- [Paper](https://aclanthology.org/2024.findings-emnlp.377/)
- [Data](https://huggingface.co/datasets/LumberChunker/GutenQA)
- repository: [source](https://github.com/joaodsmarques/LumberChunker) — supports `data.description`, `data.size`, `ground_truth.description`
- paper: [source](https://aclanthology.org/2024.findings-emnlp.377.pdf) — supports `evaluation.official_metrics`, `evaluation.protocol`, `ground_truth.provenance`
- dataset_card: [source](https://huggingface.co/datasets/LumberChunker/GutenQA) — supports `access.license`, `access.data`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
