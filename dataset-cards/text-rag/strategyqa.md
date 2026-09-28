<!-- Generated from catalog/datasets/strategyqa.yaml. Edit the YAML source. -->
# StrategyQA

[简体中文](strategyqa.zh-CN.md)

Implicit multi-step yes/no QA with decompositions and paragraph evidence for each reasoning step.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | multi_hop_qa, evidence_retrieval |
| Modalities | text |
| Gold annotation levels | paragraph, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The paper describes 2,780 questions. The authors publish a Wikipedia paragraph corpus and a separate index recipe; their code repository's 90/10 train/dev partition is an unofficial split of the official training data.


## Ground truth and evaluation

Questions have yes/no answers, decomposed subquestions and evidence paragraphs for the reasoning steps. These paragraph labels are not unique optimal chunk boundaries.

Official metrics: answer_accuracy, paragraph_recall_at_10.

Protocol: Report official split versus author-code 90/10 split explicitly, and preserve question-level and step-level retrieval denominators when using paragraph evidence.

## When to use it

- Implicit multi-step retrieval
- Completeness of paragraph evidence

## Limitations and cautions

- Answer labels alone cannot score retrieval
- Reconstructed indexes and unofficial splits change comparability

## Access and sources

- [Official resource](https://github.com/eladsegal/strategyqa)
- [Paper](https://aclanthology.org/2021.tacl-1.21/)
- paper: [source](https://aclanthology.org/2021.tacl-1.21/) — supports `summary`, `data.description`, `ground_truth.description`
- repository: [source](https://github.com/eladsegal/strategyqa) — supports `data.description`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
