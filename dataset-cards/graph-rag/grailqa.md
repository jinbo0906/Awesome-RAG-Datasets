<!-- Generated from catalog/datasets/grailqa.yaml. Edit the YAML source. -->
# GrailQA

Knowledge-base QA with executable logical forms and generalization splits.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_convertible` |
| Primary category | `graph_rag` |
| Tasks | graph_qa, graph_reasoning |
| Modalities | graph, text |
| Gold annotation levels | graph_path, answer |
| Evidence provenance | human |
| Corpus / queries / answers | external / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Questions map to Freebase answers and logical forms including SPARQL and S-expressions; reproducing retrieval requires a compatible Freebase snapshot.


## Ground truth and evaluation

Logical forms specify executable graph reasoning structure but are not necessarily a unique retrieved subgraph.

Official metrics: exact_match, answer_f1.

Protocol: Retain the original i.i.d., compositional and zero-shot splits and state the KB version.

## When to use it

- Graph reasoning generalization
- Logical-form-aware retrieval

## Limitations and cautions

- A KBQA logical form is not automatically a natural-language GraphRAG citation path

## Access and sources

- [Official resource](https://github.com/dki-lab/GrailQA)
- repository: [source](https://github.com/dki-lab/GrailQA) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
