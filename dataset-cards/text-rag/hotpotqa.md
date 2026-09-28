<!-- Generated from catalog/datasets/hotpotqa.yaml. Edit the YAML source. -->
# HotpotQA

Wikipedia multi-hop QA with sentence-level supporting facts and answer labels.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | multi_hop_qa, evidence_retrieval |
| Modalities | text |
| Gold annotation levels | sentence, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | CC BY-SA 4.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Distractor and full-wiki settings have different retrieval pools; preserve the selected setting when comparing results.

Format: JSON.

## Ground truth and evaluation

Supporting facts identify a Wikipedia title and zero-based sentence index; answers are evaluated separately.

Official metrics: answer_em, answer_f1, supporting_fact_em, supporting_fact_f1, joint_em, joint_f1.

Protocol: Report distractor and full-wiki results separately.

## When to use it

- Multi-document evidence assembly
- Query-independent chunking evaluated against sentence coordinates

## Limitations and cautions

- A supporting sentence is not a unique optimal chunk boundary
- Distractor context is not equivalent to open-corpus retrieval

## Access and sources

- [Official resource](https://hotpotqa.github.io/)
- [Paper](https://arxiv.org/abs/1809.09600)
- [Data](https://hotpotqa.github.io/)
- repository: [source](https://github.com/hotpotqa/hotpot) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.official_metrics`, `access.license`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
