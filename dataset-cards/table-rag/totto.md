<!-- Generated from catalog/datasets/totto.yaml. Edit the YAML source. -->
# ToTTo

Controlled table-to-text generation from a given Wikipedia table and highlighted cells.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `auxiliary` |
| Primary category | `table_rag` |
| Tasks | table_to_text |
| Modalities | text, table |
| Gold annotation levels | table_cell, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / not_provided / provided |
| Original data license | CC BY-SA 3.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The official release has over 120,000 training examples. Each input includes table metadata, the table and highlighted cell coordinates; the target is an edited one-sentence description. Development and private test references and header-overlap subsets have separate protocols.


## Ground truth and evaluation

Highlighted cells identify the supplied conditioning evidence, and edited sentences are reference outputs. The cells are not retrieved from an open table collection in the native task.

Official metrics: not confirmed.

Protocol: Treat this as evidence-conditioned generation, not a retrieval benchmark. To evaluate TableRAG, add queries, a table corpus, qrels and a held-out split without exposing highlighted cells.

## When to use it

- Faithful generation from selected cells
- Testing whether header context survives evidence packaging

## Limitations and cautions

- No native retrieval query or candidate pool
- The highlighted cells are provided inputs rather than recovered evidence

## Access and sources

- [Official resource](https://github.com/google-research-datasets/totto)
- repository: [source](https://github.com/google-research-datasets/totto) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.protocol`, `access.license`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
