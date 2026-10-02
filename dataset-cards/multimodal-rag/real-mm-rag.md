<!-- Generated from catalog/datasets/real-mm-rag.yaml. Edit the YAML source. -->
# REAL-MM-RAG

[简体中文](real-mm-rag.zh-CN.md)

Document-page retrieval over similar IBM financial and technical materials, with three levels of query rephrasing.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `auxiliary` |
| Primary category | `multimodal_rag` |
| Tasks | page_retrieval, multimodal_retrieval, rag_robustness |
| Modalities | text, image, table, chart, layout |
| Gold annotation levels | page, answer |
| Evidence provenance | synthetic |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | CDLA-Permissive-2.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Four author-released subsets cover FinReport, FinSlides, TechReport and TechSlides. Parquet rows embed pages with image_filename, query, three rephrased queries and a generated answer; null-query rows preserve distractor pages. The official benchmark evaluates retrieval rather than answer generation.

Published scale: Paper Table S1 reports 8,604 pages across 163 documents and 4,553 base queries, each with four phrasing versions.
Splits: Four test subsets; proposed FinTab and rephrased ColPali training data are separate resources.
Format: Hugging Face Parquet with embedded page images and nullable query/answer fields..

## Ground truth and evaluation

Generated queries are linked to image_filename. A VLM checks other pages, retaining queries deemed answerable only from their original page. Generated answers aid construction; labels are not human-exhaustive gold, and no question-specific region or cell coordinates are supplied.

Official metrics: nDCG@5, Recall@1, Recall@5.

Protocol: Deduplicate the page corpus by image_filename, keep null-query distractors, and evaluate each subset and phrasing level separately. Table 2 uses level 3; Table 3 compares levels 0–3. Chunking adaptations must retain page identity; generated answers do not establish an official QA metric.

## When to use it

- Retrieval robustness under semantic query rephrasing
- Comparing text chunks and page images on similar table-heavy documents

## Limitations and cautions

- Model-generated and model-verified relevance can still contain false negatives
- Hugging Face row counts are not unique-page or non-null-query counts
- Page-level gold cannot directly score fine-grained chunk or cell localization

## Access and sources

- [Official resource](https://navvewas.github.io/REAL-MM-RAG/)
- [Paper](https://aclanthology.org/2025.acl-long.1528/)
- [Data](https://huggingface.co/collections/ibm-research/real-mm-rag-bench)
- official: [source](https://navvewas.github.io/REAL-MM-RAG/) — supports `summary`, `classification.rag_role`, `data.description`, `evaluation.protocol`
- paper: [source](https://aclanthology.org/2025.acl-long.1528.pdf) — supports `data.size`, `data.splits`, `ground_truth.description`, `ground_truth.provenance`, `evaluation.official_metrics`, `use.caveats`
- dataset_card: [source](https://huggingface.co/datasets/ibm-research/REAL-MM-RAG_FinReport) — supports `data.description`, `data.format`, `access.license`, `access.gated`, `evaluation.protocol`
- dataset_card: [source](https://huggingface.co/datasets/ibm-research/REAL-MM-RAG_FinSlides) — supports `data.description`, `access.license`
- dataset_card: [source](https://huggingface.co/datasets/ibm-research/REAL-MM-RAG_TechReport) — supports `data.description`, `access.license`
- dataset_card: [source](https://huggingface.co/datasets/ibm-research/REAL-MM-RAG_TechSlides) — supports `data.description`, `access.license`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
