<!-- Generated from catalog/datasets/qampari.yaml. Edit the YAML source. -->
# QAMPARI

Open-domain QA where each question has many answers supported by multiple paragraphs.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_convertible` |
| Primary category | `text_rag` |
| Tasks | multi_hop_qa, long_form_qa, evidence_retrieval |
| Modalities | text |
| Gold annotation levels | paragraph, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | external / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Questions are built using Wikipedia knowledge-graph and table relations, then linked to supporting paragraphs; ALCE packages retrieval outputs for citation experiments.


## Ground truth and evaluation

Answer entities and supporting paragraphs are released; paragraph alignment uses automatic construction and question-answer validation.

Official metrics: answer_f1, citation_quality.

Protocol: Distinguish the original answer-set task from ALCE citation-conditioned evaluation.

## When to use it

- Multi-answer evidence coverage
- Citation completeness under distributed evidence

## Limitations and cautions

- No single paragraph necessarily covers every correct answer
- The original corpus snapshot must be specified

## Access and sources

- [Official resource](https://arxiv.org/abs/2205.12665)
- paper: [source](https://arxiv.org/abs/2205.12665) — supports `summary`, `data.description`, `ground_truth.description`
- repository: [source](https://github.com/princeton-nlp/ALCE) — supports `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
