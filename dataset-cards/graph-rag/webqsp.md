<!-- Generated from catalog/datasets/webqsp.yaml. Edit the YAML source. -->
# WebQuestionsSP

[简体中文](webqsp.zh-CN.md)

Natural-language questions over Freebase with answers and SPARQL semantic parses.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_convertible` |
| Primary category | `graph_rag` |
| Tasks | graph_qa, graph_reasoning |
| Modalities | text, graph |
| Gold annotation levels | graph_path, answer |
| Evidence provenance | human |
| Corpus / queries / answers | external / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Microsoft distributes questions, semantic parses and an evaluator; 4,737 questions have full SPARQL parses and 1,073 have partial annotations.


## Ground truth and evaluation

Executable SPARQL parses identify graph operations, but are not necessarily unique retrieved subgraphs or citation paths.

Official metrics: answer_f1.

Protocol: Specify Freebase snapshot and distinguish full-parse from partial-annotation examples.

## When to use it

- Knowledge-graph question answering
- Semantic-parse-guided retrieval

## Limitations and cautions

- Reproducing results depends on a compatible Freebase snapshot
- GraphRAG citation evidence requires additional annotation

## Access and sources

- [Official resource](https://www.microsoft.com/en-us/download/details.aspx?id=52763)
- official: [source](https://www.microsoft.com/en-us/download/details.aspx?id=52763) — supports `summary`, `data.description`, `ground_truth.description`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
