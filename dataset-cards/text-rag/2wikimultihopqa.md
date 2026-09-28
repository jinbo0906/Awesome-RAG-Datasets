<!-- Generated from catalog/datasets/2wikimultihopqa.yaml. Edit the YAML source. -->
# 2WikiMultiHopQA

[简体中文](2wikimultihopqa.zh-CN.md)

Multi-hop Wikipedia QA with supporting facts and structured reasoning evidence.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | multi_hop_qa, evidence_retrieval |
| Modalities | text, graph |
| Gold annotation levels | sentence, graph_path, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Questions are built from Wikipedia text and Wikidata relations; use the official split and evidence format.


## Ground truth and evaluation

Released annotations include supporting sentences and evidence paths; the exact graph use depends on the evaluation configuration.

Official metrics: answer_em, answer_f1, supporting_fact_em, supporting_fact_f1.


## When to use it

- Multi-hop evidence chain retrieval
- Comparing text and graph-derived evidence

## Limitations and cautions

- Do not equate a generated reasoning path with a human-verified unique minimal evidence set

## Access and sources

- [Official resource](https://github.com/Alab-NII/2wikimultihop)
- [Paper](https://aclanthology.org/2020.coling-main.580/)
- repository: [source](https://github.com/Alab-NII/2wikimultihop) — supports `summary`, `data.description`, `ground_truth.levels`, `evaluation.official_metrics`
- paper: [source](https://aclanthology.org/2020.coling-main.580/) — supports `summary`, `classification.tasks`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
