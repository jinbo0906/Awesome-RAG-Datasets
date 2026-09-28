# Taxonomy, entities and review status

[简体中文](taxonomy.zh-CN.md)

This catalog separates a **dataset** (records/examples), a **suite** (a selection plus evaluation protocol), a **corpus** (a versioned source collection), a **task** (a capability), and a **paper** (a publication). A benchmark is the data plus an evaluation contract, not necessarily another data object; see [dataset versus benchmark](benchmark-vs-dataset.md). A paper using a dataset does not create a new dataset. A suite variant may alter corpus, qrels or scoring and must not silently replace the original.

## RAG role

| Role | Operational criterion | Typical mistake |
|---|---|---|
| `rag_native` | Released query, source pool, answer and retrieval/evidence protocol allow retrieval and answer evaluation | Assuming a supplied context is open retrieval |
| `rag_convertible` | QA or VQA exists, but a source pool, qrels, evidence map or retrieval split must be built | Calling the adaptation an official benchmark |
| `auxiliary` | Measures a useful component, such as retrieval or factuality, without full answer evaluation | Claiming IR NDCG is end-to-end RAG quality |
| `out_of_scope` | Retrieval's contribution cannot be isolated with available data | Adding a general knowledge quiz as RAG gold |

Roles are judgments made by this catalog, not claims by dataset authors. A record's card explains the missing pieces. In particular, BEIR and M-BEIR are retrieval suites; a high retrieval score does not certify a grounded answer. Natural Questions in its native candidate-page setting is not identical to open-domain Natural Questions.

## Evidence granularity

The `ground_truth.levels` field describes **released annotations**, not what could be inferred by an LLM. `answer` is not evidence. `response_span` is an error/support annotation on a generated response; `span` is a coordinate in source material. They must not be exchanged. A layout `bbox` may mark every chart element but not identify which element answers a particular question. A graph logical form may encode computation without identifying a minimal natural-language citation path. Multiple accepted evidence sets should remain alternatives rather than be flattened into one union.

The primary categories—text, multimodal, graph, table and cross-cutting RAG—are navigation aids. Tasks and modalities remain independent tags. A table in a PDF may legitimately involve table, image and layout modalities while keeping one primary category. `GraphRAG` here means graph representation or graph-grounded retrieval is central; merely asking a multi-hop text question does not make the original dataset a native graph benchmark.

## Review ladder

`discovered` confirms only identity. `screened` confirms entity type and plausible use from an upstream resource. `source_checked` means key fields have field-level primary sources and a check date; it **does not** mean the data downloaded or the evaluator reproduced. `reproduced` requires a documented loader/evaluator run. `verified` additionally requires independent review. `deprecated` means a known upstream replacement or withdrawal, not merely an inactive GitHub repository. Unknown licenses stay `unknown` and are never inferred from a model repository's code license.

The catalog is deliberately conservative: source-checked descriptions may still contain author-reported facts, access may change, and unlisted variants may exist. A contribution should upgrade a specific field with evidence rather than promote the whole entry on appearance alone.

## Field interpretation

- `data.corpus/queries/answers`: `provided`, `external`, `not_provided` or `unknown`; `external` means retrieval or reconstruction is needed from another source.
- `ground_truth.provenance`: annotation origin; `mixed` includes workflows with human and synthetic or distant steps.
- `ground_truth.alternatives`: whether multiple acceptable evidence/answer sets are explicit, only implicit, or undocumented.
- `access.license`: original dataset terms, not this repository's license. Code, data, images and source documents can have different licenses.
- `sources[].fields`: exactly which claims an official page, paper, repository or data card supports.

Do not compare counts without a unit, version, split and source. A “question,” “QA pair,” “page,” “PDF,” “table,” “retrieval candidate” and “annotation” are different denominators. For example, a project page and paper abstract can publish different QA counts; the card should retain the discrepancy and identify the chosen release.
