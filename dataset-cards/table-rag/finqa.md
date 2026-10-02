<!-- Generated from catalog/datasets/finqa.yaml. Edit the YAML source. -->
# FinQA

[简体中文](finqa.zh-CN.md)

Financial numerical QA with supporting text/table facts and executable reasoning programs.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_convertible` |
| Primary category | `table_rag` |
| Tasks | table_qa, text_table_reasoning, evidence_retrieval |
| Modalities | text, table |
| Gold annotation levels | sentence, table, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | MIT |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

JSON examples include pre/post-table text, a report table, a question, gold supporting fact indices, a reasoning program and its execution answer.

Splits: Train/dev/public test contain references; private test questions omit gold references.
Format: JSON.

## Ground truth and evaluation

gold_inds selects supporting text sentences and serialized table rows; programs supervise numerical operations. These row targets are not original PDF cell coordinates.

Official metrics: execution_accuracy, program_accuracy.

Protocol: Run retrieval plus program generation for challenge submissions. Gold retrieval inputs are for diagnostics; distinguish public from private test and use corrected table-row serialization.

## When to use it

- Retrieval before financial computation
- Executable answer and program supervision

## Limitations and cautions

- The native candidate context is supplied; full-report retrieval is an additional conversion
- The repository documents earlier serialization bugs that leaked retrieval labels

## Access and sources

- [Official resource](https://github.com/czyssrs/FinQA)
- [Paper](https://aclanthology.org/2021.emnlp-main.300/)
- [Data](https://github.com/czyssrs/FinQA/tree/main/dataset)
- repository: [source](https://github.com/czyssrs/FinQA) — supports `summary`, `classification`, `data`, `ground_truth`, `evaluation`, `access.license`, `use`
- paper: [source](https://aclanthology.org/2021.emnlp-main.300/) — supports `ground_truth.provenance`, `access.paper`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
