<!-- Generated from catalog/datasets/clapnq.yaml. Edit the YAML source. -->
# CLAP NQ

[简体中文](clapnq.zh-CN.md)

Long-form RAG answers grounded in non-contiguous sentences of Natural Questions passages.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | long_form_qa, evidence_retrieval |
| Modalities | text |
| Gold annotation levels | sentence, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | Apache-2.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The official release includes annotated QA, original Wikipedia documents and retrieval-formatted data; answerable and unanswerable examples are represented.


## Ground truth and evaluation

Selected passage sentences ground a concise cohesive answer; many answers require non-adjacent sentences.

Official metrics: retrieval_recall, answer_quality.

Protocol: Keep the source sentence identifiers through passage reconstruction; the official test answers are withheld.

## When to use it

- Chunking across non-contiguous evidence
- Long-form grounded answers

## Limitations and cautions

- Official test labels require the upstream evaluation process

## Access and sources

- [Official resource](https://github.com/primeqa/clapnq)
- [Paper](https://arxiv.org/abs/2404.02103)
- repository: [source](https://github.com/primeqa/clapnq) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.protocol`, `access.license`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
