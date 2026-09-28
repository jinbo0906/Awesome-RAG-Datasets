<!-- Generated from catalog/datasets/hicbench.yaml. Edit the YAML source. -->
# HiCBench

[简体中文](hicbench.zh-CN.md)

A chunking-focused benchmark with hierarchical boundary annotations and evidence-dense QA.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | evidence_retrieval, long_context_qa |
| Modalities | text, layout |
| Gold annotation levels | section, paragraph, sentence, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Curated documents from OHRBench are paired with hierarchy annotations and synthesized evidence-intensive questions.


## Ground truth and evaluation

Human-labeled multilevel chunking points coexist with synthesized QA and associated evidence sources.

Official metrics: chunking_quality, evidence_coverage, answer_quality.

Protocol: Keep source hierarchy labels separate from QA evidence and test across context budgets.

## When to use it

- Hierarchical chunking
- Evidence completeness across chunk sizes

## Limitations and cautions

- Synthesized questions need an independent human-audited holdout for claims of generalization

## Access and sources

- [Official resource](https://github.com/TencentCloudADP/hichunk)
- [Paper](https://aclanthology.org/2026.acl-long.1372/)
- paper: [source](https://aclanthology.org/2026.acl-long.1372/) — supports `summary`, `data.description`, `ground_truth.description`
- repository: [source](https://github.com/TencentCloudADP/hichunk) — supports `evaluation.protocol`, `access.official`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
