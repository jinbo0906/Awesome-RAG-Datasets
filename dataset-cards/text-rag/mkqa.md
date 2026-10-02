<!-- Generated from catalog/datasets/mkqa.yaml. Edit the YAML source. -->
# MKQA

[简体中文](mkqa.zh-CN.md)

Passage-independent factual QA annotations aligned across 26 languages from the same Natural Questions queries.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_convertible` |
| Primary category | `text_rag` |
| Tasks | single_hop_qa, rag_robustness |
| Modalities | text |
| Gold annotation levels | answer |
| Evidence provenance | human |
| Corpus / queries / answers | not_provided / provided / provided |
| Original data license | CC-BY-SA-3.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

New passage-independent answers are collected for sampled Natural Questions queries, then questions and answers are human-translated. Text, entity, binary and unanswerable labels are supplied without a native retrieval corpus.

Published scale: 10K aligned queries across 26 languages, yielding 260K language-specific QA pairs.

## Ground truth and evaluation

Typed answers include acceptable aliases and, where possible, Wikidata QIDs. These identifiers enable answer alignment but are not gold supporting documents or spans.

Official metrics: exact_match, token_f1.

Protocol: Use the official language-specific normalization and no-answer thresholds. The official macro-average requires all 26 languages; disclose answerability filters and any externally chosen RAG corpus.

## When to use it

- Aligned multilingual answer quality
- Cross-language retrieval conversions

## Limitations and cautions

- No native passage-relevance gold is supplied
- Answerable-only subsets and partial-language averages change the protocol

## Access and sources

- [Official resource](https://github.com/apple-aiml-research/ml-mkqa)
- [Paper](https://aclanthology.org/2021.tacl-1.82/)
- repository: [source](https://github.com/apple-aiml-research/ml-mkqa) — supports `summary`, `data.description`, `data.size`, `ground_truth.description`, `evaluation.official_metrics`, `evaluation.protocol`, `access.license`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
