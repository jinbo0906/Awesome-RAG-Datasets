<!-- Generated from catalog/datasets/triviaqa.yaml. Edit the YAML source. -->
# TriviaQA

[简体中文](triviaqa.zh-CN.md)

Trivia questions with answer aliases and independently collected Wikipedia and web evidence documents.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_convertible` |
| Primary category | `text_rag` |
| Tasks | single_hop_qa, evidence_retrieval |
| Modalities | text |
| Gold annotation levels | document, answer |
| Evidence provenance | distant |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | Apache-2.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The reading-comprehension release supplies question-associated evidence documents; the unfiltered release retains questions whose retrieved documents may not contain an answer. A shared open-domain retrieval index is a separate experimental choice.

Published scale: Over 650K question-answer-evidence triples; about 95K QA pairs in the reading-comprehension release and 110K in the unfiltered release.

## Ground truth and evaluation

Answer aliases support answer scoring. Evidence documents are collected independently and largely associated through distant supervision; their inclusion does not establish human-annotated support spans or an exhaustive relevance set.

Official metrics: exact_match, token_f1.

Protocol: Keep Wikipedia/web, filtered/unfiltered and verified-subset settings distinct; score against the official answer aliases.

## When to use it

- Open-domain factual QA
- Comparing answer-alias scoring with retrieval coverage

## Limitations and cautions

- Question-associated evidence is not a ready-made shared retrieval index
- Distant evidence labels are not gold chunk boundaries

## Access and sources

- [Official resource](https://nlp.cs.washington.edu/triviaqa/)
- [Paper](https://aclanthology.org/P17-1147/)
- official: [source](https://nlp.cs.washington.edu/triviaqa/) — supports `summary`, `data.description`, `data.size`, `ground_truth.description`
- repository: [source](https://github.com/mandarjoshi90/triviaqa) — supports `access.license`, `evaluation.protocol`
- repository: [source](https://github.com/mandarjoshi90/triviaqa/blob/master/evaluation/triviaqa_evaluation.py) — supports `evaluation.official_metrics`, `ground_truth.alternatives`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
