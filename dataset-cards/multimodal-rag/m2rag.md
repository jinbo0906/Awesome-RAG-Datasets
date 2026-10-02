<!-- Generated from catalog/datasets/m2rag.yaml. Edit the YAML source. -->
# M²RAG

[简体中文](m2rag.zh-CN.md)

Released multi-task open-domain multimodal RAG data adapted from WebQA and Factify.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_native` |
| Primary category | `multimodal_rag` |
| Tasks | visual_qa, fact_verification, multimodal_retrieval |
| Modalities | text, image |
| Gold annotation levels | answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | WebQA CC0-1.0 and Factify MIT as stated in paper Appendix A.1; repository code MIT; upstream image terms also apply. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Four tasks cover image captioning, multimodal QA, multimodal fact verification and image reranking. The author repository links task files and a multipart image archive; QA and captioning use WebQA, while verification uses Factify.

Published scale: Each task has 3,000 test queries; the first three also have 3,000 training queries, with task-specific corpora.
Splits: Author-defined train and test; Factify evaluation is sampled from its validation set.
Format: Task-specific data folders and image TSV/archive assets..

## Ground truth and evaluation

Task targets include captions, QA answers, three-way verification labels and reference images. Annotation and retrieval relevance vary by task; this record does not claim universal paragraph or image-region evidence.

Official metrics: BERTScore, ROUGE-L, CIDEr, accuracy, F1, FID.

Protocol: Use the task-specific corpus and metric: captioning/QA use text-generation metrics, verification uses accuracy/F1, and image reranking uses FID. Report top-k context and avoid merging unlike task scores without a stated aggregation.

## When to use it

- Testing multimodal retrieved-context utilization across tasks
- Comparing retrieval-augmented instruction tuning with vanilla RAG

## Limitations and cautions

- M²RAG is distinct from M2KR and M2RAG interleaved-answer systems
- FID for reranking is not a standard query-level relevance metric

## Access and sources

- [Official resource](https://github.com/NEUIR/M2RAG)
- [Paper](https://arxiv.org/abs/2502.17297)
- [Data](https://huggingface.co/datasets/whalezzz/M2RAG)
- paper: [source](https://arxiv.org/html/2502.17297) — supports `summary`, `data.description`, `data.size`, `data.splits`, `ground_truth.description`, `evaluation.official_metrics`, `evaluation.protocol`, `access.license`
- repository: [source](https://github.com/NEUIR/M2RAG) — supports `data.description`, `data.format`, `access.data`, `use.best_for`
- dataset_card: [source](https://huggingface.co/datasets/whalezzz/M2RAG) — supports `access.data`, `data.description`, `data.format`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
