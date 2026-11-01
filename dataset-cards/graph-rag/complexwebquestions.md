<!-- Generated from catalog/datasets/complexwebquestions.yaml. Edit the YAML source. -->
# ComplexWebQuestions 1.1

[简体中文](complexwebquestions.zh-CN.md)

Complex compositional QA over Freebase or retrieved web snippets with decomposition supervision.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `rag_convertible` |
| Primary category | `graph_rag` |
| Tasks | graph_qa, multi_hop_qa |
| Modalities | graph, text |
| Gold annotation levels | graph_path, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | external / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Version 1.1 publishes complex questions, SPARQL, answers and decomposed-question supervision; KB experiments use Freebase while web experiments retrieve snippets.

Splits: Use the corrected version 1.1 partition; version 1.0 has a documented split problem.
Format: JSON.

## Ground truth and evaluation

Generated compositional queries and human-paraphrased questions supply logical-form supervision; retrieved web snippets are candidate evidence, not gold sentence-level citations.

Official metrics: precision_at_1.

Protocol: Use the official answer scorer and version 1.1 split. Declare whether answering uses web retrieval or the documented Freebase snapshot; later KBQA papers may report additional metrics.

## When to use it

- Question decomposition and compositional KBQA
- Comparing graph and web retrieval routes

## Limitations and cautions

- Use Freebase snapshot freebase-rdf-2015-08-02-00-00 for original KB reconstruction
- Logical forms do not establish unique minimal retrieved subgraphs
- The former project homepage returned 404 on 2026-11-01; the canonical link now points to author code and corrected version-1.1 data availability must be checked separately

## Access and sources

- [Official resource](https://github.com/alontalmor/WebAsKB)
- [Paper](https://aclanthology.org/N18-1059/)
- repository: [source](https://github.com/alontalmor/WebAsKB) — supports `summary`, `data.format`, `evaluation.protocol`, `access.official`, `use.caveats`
- paper: [source](https://aclanthology.org/N18-1059/) — supports `ground_truth`, `evaluation.official_metrics`, `use.best_for`
- paper: [source](https://arxiv.org/abs/1807.09623) — supports `data.splits`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
