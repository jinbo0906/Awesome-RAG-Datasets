<!-- Generated from catalog/datasets/tabfact.yaml. Edit the YAML source. -->
# TabFact

Entailment or refutation of natural-language claims against Wikipedia tables.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_convertible` |
| Primary category | `table_rag` |
| Tasks | fact_verification, table_qa |
| Modalities | text, table |
| Evidence levels | table, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Claims are paired with individual tables and binary labels; the official page reports both 117,854 manually annotated statements and a 118,275 row-count total under different tabulations.


## Ground truth and evaluation

Entailed or refuted labels are gold; a supporting cell set is not natively guaranteed for every claim.

Official metrics: accuracy.

Protocol: A table retriever and table-level qrels must be specified to evaluate a RAG pipeline.

## When to use it

- Table-aware claim verification
- Semantic and symbolic inference

## Limitations and cautions

- The official README contains differing count presentations
- Native task supplies its table and is not open retrieval

## Access and sources

- [Official resource](https://github.com/wenhuchen/Table-Fact-Checking)
- repository: [source](https://github.com/wenhuchen/Table-Fact-Checking) — supports `summary`, `data.description`, `ground_truth.description`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
