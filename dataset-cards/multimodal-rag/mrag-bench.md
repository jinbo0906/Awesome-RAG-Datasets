<!-- Generated from catalog/datasets/mrag-bench.yaml. Edit the YAML source. -->
# MRAG-Bench

[简体中文](mrag-bench.zh-CN.md)

Vision-centric RAG questions with gold supporting images and multiple-choice answers across nine scenarios.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_native` |
| Primary category | `multimodal_rag` |
| Tasks | visual_qa, multimodal_retrieval |
| Modalities | text, image |
| Gold annotation levels | document, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | CC-BY-4.0 for the Hugging Face release; upstream image-source terms may also apply. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The author release provides an image corpus and QA. Its Hugging Face test package embeds the query image, gt_images and five retrieved_images with four answer choices, enabling both oracle and retrieved-context evaluation.

Published scale: 1,353 human-annotated questions and 16,130 corpus images.
Splits: Test benchmark; no native training split.
Format: Hugging Face Parquet with images and an author-hosted corpus archive..

## Ground truth and evaluation

gt_images identify supporting images and answer_choice gives the correct option. These are image-level supports, not object boxes or a guarantee that every useful image in an enlarged corpus is exhaustively labeled.

Official metrics: multiple_choice_accuracy, Recall@5.

Protocol: Separate no-RAG, retrieved-RAG and gold-image-RAG settings; most native comparisons use five images. A fixed candidate pool that injects gold images, as in the ACL 2026 utility-selection study, is a separate selection protocol.

## When to use it

- Measuring how retrieved visual knowledge changes answers
- Comparing gold image use with imperfect retrieval

## Limitations and cautions

- Published at ICLR 2025; the 2024 arXiv date is not its conference year
- Oracle or gold-injected candidate pools must be distinguished from corpus retrieval

## Access and sources

- [Official resource](https://mragbench.github.io/)
- [Paper](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ee46288ab2aaf5c6e53aebebe719712c-Abstract-Conference.html)
- [Data](https://huggingface.co/datasets/uclanlp/MRAG-Bench)
- official: [source](https://mragbench.github.io/) — supports `summary`, `data.size`, `evaluation.official_metrics`, `evaluation.protocol`
- dataset_card: [source](https://huggingface.co/datasets/uclanlp/MRAG-Bench) — supports `data.description`, `data.splits`, `data.format`, `ground_truth.description`, `access.license`
- paper: [source](https://aclanthology.org/2026.acl-long.1620/) — supports `evaluation.protocol`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
