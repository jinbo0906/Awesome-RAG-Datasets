<!-- Generated from catalog/datasets/ragbench.yaml. Edit the YAML source. -->
# RAGBench

[简体中文](ragbench.zh-CN.md)

RAG evaluation collection with responses and fine-grained support labels over retrieved context.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | attribution, fact_verification |
| Modalities | text |
| Gold annotation levels | sentence, fact_citation, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | CC BY 4.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The hosted release has 12 subsets with questions, retrieved documents, generated responses and sentence-level support annotations.


## Ground truth and evaluation

Response sentences and document sentences are linked by support keys; this evaluates response adherence and context utilization.

Official metrics: adherence, relevance, utilization, completeness.

Protocol: Treat released retrieved documents as a fixed context pool unless an external corpus is separately reconstructed.

## When to use it

- Answer groundedness diagnostics
- Sentence-level support attribution

## Limitations and cautions

- Mixed-source and model-assisted annotations should not be called a fully human gold standard

## Access and sources

- [Official resource](https://huggingface.co/datasets/galileo-ai/ragbench)
- [Paper](https://arxiv.org/abs/2407.11005)
- dataset_card: [source](https://huggingface.co/datasets/galileo-ai/ragbench) — supports `summary`, `data.description`, `ground_truth.description`, `access.license`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
