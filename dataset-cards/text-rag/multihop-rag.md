<!-- Generated from catalog/datasets/multihop-rag.yaml. Edit the YAML source. -->
# MultiHop-RAG

[简体中文](multihop-rag.zh-CN.md)

Open multi-document RAG QA with query types and supporting evidence labels.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | multi_hop_qa, evidence_retrieval |
| Modalities | text |
| Gold annotation levels | document, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The released knowledge base and question set include inference, comparison, temporal and null-answer cases.


## Ground truth and evaluation

Questions are associated with supporting evidence from multiple source documents.

Official metrics: retrieval_recall, answer_accuracy.

Protocol: Report null-answer cases separately from multi-hop answerable cases.

## When to use it

- Multi-document retrieval
- Temporal or comparative reasoning

## Limitations and cautions

- Supporting documents are not automatically minimal sufficient spans

## Access and sources

- [Official resource](https://github.com/yixuantt/MultiHop-RAG)
- [Paper](https://arxiv.org/abs/2401.15391)
- repository: [source](https://github.com/yixuantt/MultiHop-RAG) — supports `summary`, `data.description`, `ground_truth.description`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
