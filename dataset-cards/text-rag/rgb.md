<!-- Generated from catalog/datasets/rgb.yaml. Edit the YAML source. -->
# RGB

Bilingual fixed-context RAG stress test for noise, abstention, integration and counterfactual documents.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `auxiliary` |
| Primary category | `text_rag` |
| Tasks | rag_robustness, single_hop_qa, multi_hop_qa |
| Modalities | text |
| Gold annotation levels | answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | not_provided / provided / provided |
| Original data license | CC BY-NC-SA 4.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The repository supplies English and Chinese questions with fixed positive and negative passages, plus separate integration and counterfactual files. A March 2024 refined release corrected some passages and answers; the files do not define one open retrieval corpus.

Format: JSON.

## Ground truth and evaluation

Reference answers and scenario-specific context labels support controlled robustness tests. They are not immutable source-document spans or human-verified optimal chunks.

Official metrics: accuracy, rejection_rate, error_detection_rate, error_correction_rate.

Protocol: Pin original versus refined files, language, noise_rate and passage_num. Evaluate negative rejection and counterfactual detection with their distinct upstream scripts; do not report these as retrieval recall.

## When to use it

- Robustness to distracting passages
- Abstention under insufficient context
- Cross-document integration

## Limitations and cautions

- Fixed passages do not benchmark an open-corpus retriever
- The refined release changes passages and some answers

## Access and sources

- [Official resource](https://github.com/chen700564/RGB)
- [Paper](https://arxiv.org/abs/2309.01431)
- repository: [source](https://github.com/chen700564/RGB) — supports `summary`, `data.description`, `evaluation.official_metrics`, `evaluation.protocol`, `access.license`
- paper: [source](https://arxiv.org/abs/2309.01431) — supports `classification.tasks`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
