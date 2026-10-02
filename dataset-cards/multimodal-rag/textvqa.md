<!-- Generated from catalog/datasets/textvqa.yaml. Edit the YAML source. -->
# TextVQA

[简体中文](textvqa.zh-CN.md)

Visual QA requiring recognition and reasoning about text embedded in natural-scene images.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_convertible` |
| Primary category | `multimodal_rag` |
| Tasks | visual_qa |
| Modalities | text, image |
| Gold annotation levels | answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | CC-BY-4.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Questions and ten-answer annotations are paired with OpenImages photographs. Version 0.5.1 updates Rosetta OCR tokens without changing version 0.5 questions or images.

Published scale: 45,336 questions: 34,602 train, 5,000 validation and 5,734 test.
Splits: Official v0.5.1 train, validation and test-std.
Format: Image files, QA JSON and separate OCR JSON..

## Ground truth and evaluation

Human answer variants support VQA scoring. Rosetta token boxes are machine-produced OCR inputs, not question-specific evidence-region gold or native retrieval relevance labels.

Official metrics: VQA_accuracy.

Protocol: Fix the OCR version and account for OpenImages rotation metadata. Native evaluation supplies the query image; a retrieval experiment must define its additional corpus, relevance labels and answer protocol.

## When to use it

- Scene-text reading and OCR robustness
- Visual answer-generation component evaluation

## Limitations and cautions

- The native task has no external-knowledge retrieval pool or qrels
- OCR boxes do not certify which region supports an answer

## Access and sources

- [Official resource](https://textvqa.org/)
- [Paper](https://arxiv.org/abs/1904.08920)
- [Data](https://textvqa.org/dataset/)
- official: [source](https://textvqa.org/dataset/) — supports `summary`, `data.description`, `data.size`, `data.splits`, `ground_truth.description`, `access.license`
- official: [source](https://textvqa.org/challenge/) — supports `evaluation.official_metrics`, `evaluation.protocol`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
