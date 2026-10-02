<!-- Generated from catalog/datasets/nomiracl.yaml. Edit the YAML source. -->
# NoMIRACL

[简体中文](nomiracl.zh-CN.md)

Multilingual RAG relevance assessment with passage sets containing either no relevant passage or at least one.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `auxiliary` |
| Primary category | `text_rag` |
| Tasks | evidence_retrieval, rag_robustness |
| Modalities | text |
| Gold annotation levels | paragraph |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / not_provided |
| Original data license | Apache-2.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The release supplies queries, relevance labels and up to ten annotated passages per query, with relevant and non-relevant subsets in 18 languages. It evaluates binary relevance assessment rather than answer-text correctness.

Splits: Development and test, each separated into relevant and non-relevant subsets.

## Ground truth and evaluation

Human passage judgments determine whether any supplied context is relevant. Non-relevant sets contain only judged non-relevant passages; relevant sets contain at least one judged relevant passage. Reference answer strings are not the native labels.

Official metrics: hallucination_rate, error_rate.

Protocol: Report both subsets separately. Hallucination rate is FP/(FP+TN) on non-relevant sets; error rate is FN/(FN+TP) on relevant sets. These measure context relevance recognition, not factual accuracy of arbitrary generated answers.

## When to use it

- Multilingual abstention under retrieval misses
- Balancing false confidence and missed relevant evidence

## Limitations and cautions

- Its hallucination-rate label describes a binary assessment protocol
- Supplied top-k contexts do not evaluate full-corpus retrieval recall

## Access and sources

- [Official resource](https://github.com/project-miracl/nomiracl)
- [Paper](https://aclanthology.org/2024.findings-emnlp.730/)
- [Data](https://huggingface.co/datasets/miracl/nomiracl)
- repository: [source](https://github.com/project-miracl/nomiracl) — supports `summary`, `ground_truth.description`, `evaluation.official_metrics`, `evaluation.protocol`
- dataset_card: [source](https://huggingface.co/datasets/miracl/nomiracl) — supports `data.description`, `data.splits`, `access.license`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
