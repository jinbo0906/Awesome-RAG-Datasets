<!-- Generated from catalog/datasets/a-okvqa.yaml. Edit the YAML source. -->
# A-OKVQA

[简体中文](a-okvqa.zh-CN.md)

Knowledge-intensive visual questions with direct answers, multiple-choice labels and human rationales.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_convertible` |
| Primary category | `multimodal_rag` |
| Tasks | visual_qa, multimodal_retrieval |
| Modalities | text, image |
| Gold annotation levels | answer |
| Evidence provenance | human |
| Corpus / queries / answers | not_provided / provided / provided |
| Original data license | Apache-2.0 for the official repository; COCO images retain separate upstream terms. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Crowdsourced questions over COCO 2017 images require world knowledge and scene reasoning. The official v1.0 package includes answer choices, direct answers and rationales; it does not supply a fixed external knowledge pool.

Published scale: Approximately 25,000 questions.
Splits: Train, validation and test; held-out test predictions use the official leaderboard.
Format: QA JSON; COCO 2017 images downloaded separately..

## Ground truth and evaluation

Correct choices, direct-answer variants and free-text rationales supervise answering and explanation. A rationale is not a retrieved passage identifier or a human-verified external citation.

Official metrics: multiple_choice_accuracy, direct_answer_VQA_accuracy.

Protocol: Report multiple-choice and direct-answer scores separately. Apply the official direct-answer eligibility filter and matching rules; disclose knowledge retrieval, corpus versions and rationale-derived supervision.

## When to use it

- Knowledge retrieval combined with scene reasoning
- Comparing direct answers and multiple-choice reasoning

## Limitations and cautions

- Human rationales are not retrieval relevance gold
- The dataset is a distinct successor with no shared OK-VQA question-image pairs

## Access and sources

- [Official resource](https://github.com/allenai/aokvqa)
- [Paper](https://arxiv.org/abs/2206.01718)
- [Data](https://prior-datasets.s3.us-east-2.amazonaws.com/aokvqa/aokvqa_v1p0.tar.gz)
- repository: [source](https://github.com/allenai/aokvqa) — supports `summary`, `data.description`, `data.size`, `data.splits`, `ground_truth.description`, `evaluation.protocol`, `access.data`
- repository: [source](https://github.com/allenai/aokvqa/blob/main/evaluation/eval_predictions.py) — supports `evaluation.official_metrics`
- repository: [source](https://github.com/allenai/aokvqa/blob/main/LICENSE) — supports `access.license`
- official: [source](https://okvqa.allenai.org/download.html) — supports `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
