<!-- Generated from catalog/datasets/frames.yaml. Edit the YAML source. -->
# FRAMES

[简体中文](frames.zh-CN.md)

Human-written multi-document questions evaluating factual answers, retrieval and reasoning together.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | multi_hop_qa, time_sensitive_qa |
| Modalities | text |
| Gold annotation levels | document, answer |
| Evidence provenance | human |
| Corpus / queries / answers | external / provided / provided |
| Original data license | Apache-2.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The CSV supplies questions, reference answers, reasoning types and supporting Wikipedia URLs; article text must be obtained separately.

Published scale: 824 evaluation questions.
Splits: One test split; no native training split.
Format: CSV.

## Ground truth and evaluation

Annotators identify supporting articles; URLs are document targets, not sentence offsets or a unique graph path.

Official metrics: answer_accuracy, article_recall.

Protocol: The paper compares no retrieval, BM25 retrieval, oracle articles and iterative retrieval. Answer correctness uses an LLM autorater; fix the Wikipedia snapshot and judge prompt.

## When to use it

- Iterative retrieval and search planning
- Multi-document temporal and numerical reasoning

## Limitations and cautions

- Wikipedia URLs do not freeze source content; reproduce a dated corpus snapshot
- NAACL 2025 publication should not be described as an ACL main-conference paper

## Access and sources

- [Official resource](https://huggingface.co/datasets/google/frames-benchmark)
- [Paper](https://aclanthology.org/2025.naacl-long.243/)
- [Data](https://huggingface.co/datasets/google/frames-benchmark/tree/main)
- dataset_card: [source](https://huggingface.co/datasets/google/frames-benchmark) — supports `data`, `ground_truth.levels`, `access.license`
- paper: [source](https://aclanthology.org/2025.naacl-long.243.pdf) — supports `summary`, `classification`, `ground_truth`, `evaluation`, `use`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
