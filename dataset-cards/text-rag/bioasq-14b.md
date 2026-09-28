<!-- Generated from catalog/datasets/bioasq-14b.yaml. Edit the YAML source. -->
# BioASQ Task 14b (2026)

[简体中文](bioasq-14b.zh-CN.md)

Biomedical question answering challenge with article, snippet and answer supervision.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | evidence_retrieval, single_hop_qa, long_form_qa |
| Modalities | text |
| Gold annotation levels | document, span, answer |
| Evidence provenance | human |
| Corpus / queries / answers | external / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

BioASQ is a recurring challenge, not one timeless file. The official participant page lists 5,729 training questions for Task 14b (2026), with gold concepts, articles, snippets, exact answers and ideal answers. Source articles are external and downloads require registration.

Published scale: 5,729 training questions in BioASQ14 Task b; test releases are separate.

## Ground truth and evaluation

Gold article and snippet records provide retrieval supervision; exact and ideal answers support short-form and paragraph-length generation. Evidence identifiers and source versions must be preserved when materializing a corpus.

Official metrics: not confirmed.

Protocol: State challenge year and phase. Phase A scores retrieval and Phase B scores answers; do not mix the 2026 training size with another edition's test set or metrics.

## When to use it

- Biomedical retrieval plus answering
- Source-snippet evidence and exact-versus-ideal answers

## Limitations and cautions

- Registration is required for official downloads
- The external article corpus and yearly challenge rules must be pinned

## Access and sources

- [Official resource](https://participants-area.bioasq.org/datasets/)
- official: [source](https://participants-area.bioasq.org/datasets/) — supports `summary`, `data.description`, `data.size`, `ground_truth.description`, `access.gated`
- official: [source](https://www.bioasq.org/node/2) — supports `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
