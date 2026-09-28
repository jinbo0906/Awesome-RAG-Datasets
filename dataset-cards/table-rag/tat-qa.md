<!-- Generated from catalog/datasets/tat-qa.yaml. Edit the YAML source. -->
# TAT-QA

Financial QA over a provided hybrid context of report tables and surrounding text.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_convertible` |
| Primary category | `table_rag` |
| Tasks | table_qa, text_table_reasoning |
| Modalities | text, table |
| Gold annotation levels | table_cell, span, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | CC BY 4.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The official release contains 16,552 questions across 2,757 table-and-text contexts from financial reports.


## Ground truth and evaluation

Questions include derivation and answer-from metadata; model-specific heuristic facts and mappings are a separate derived representation.

Official metrics: em, f1.

Protocol: Do not treat supplied context as an open retrieval test without constructing a separate source-document corpus and split.

## When to use it

- Text-cell evidence fusion
- Numerical reasoning after retrieval

## Limitations and cautions

- Native context is supplied
- Heuristic TagOp mappings are not original human evidence labels

## Access and sources

- [Official resource](https://github.com/NExTplusplus/TAT-QA)
- [Paper](https://aclanthology.org/2021.acl-long.254/)
- repository: [source](https://github.com/NExTplusplus/TAT-QA) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.protocol`, `access.license`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
