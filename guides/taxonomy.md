# Taxonomy, entities and review status

[简体中文](taxonomy.zh-CN.md)

This catalog separates a **dataset** (records/examples), a **suite** (a selection plus evaluation protocol), a **corpus** (a versioned source collection), a **task** (a capability), and a **paper** (a publication). A benchmark is the data plus an evaluation contract, not necessarily another data object; see [dataset versus benchmark](benchmark-vs-dataset.md). A paper using a dataset does not create a new dataset. A suite variant may alter corpus, qrels or scoring and must not silently replace the original.

## RAG role

| Role | Operational criterion | Typical mistake |
|---|---|---|
| `rag_native` | Released queries, answer targets or rubrics, and an official source/tool environment support retrieval-augmented answer evaluation | Assuming a supplied context is open retrieval |
| `rag_convertible` | QA or VQA exists, but a source pool, qrels, evidence map or retrieval split must be built | Calling the adaptation an official benchmark |
| `auxiliary` | Measures a useful component, such as retrieval or factuality, without full answer evaluation | Claiming IR NDCG is end-to-end RAG quality |
| `out_of_scope` | Retrieval's contribution cannot be isolated with available data | Adding a general knowledge quiz as RAG gold |

Roles are judgments made by this catalog, not claims by dataset authors. A record's card explains the missing pieces. In particular, BEIR and M-BEIR are retrieval suites; a high retrieval score does not certify a grounded answer. Natural Questions in its native candidate-page setting is not identical to open-domain Natural Questions.

## Evidence granularity

The `ground_truth.levels` field describes **released annotations**, not what could be inferred by an LLM. `answer` is not evidence. `response_span` is an error/support annotation on a generated response; `span` is a coordinate in source material. They must not be exchanged. A layout `bbox` may mark every chart element but not identify which element answers a particular question. A graph logical form may encode computation without identifying a minimal natural-language citation path. Multiple accepted evidence sets should remain alternatives rather than be flattened into one union.

The primary categories—text, multimodal, graph, table and cross-cutting RAG—are navigation aids. Tasks and modalities remain independent tags. A table in a PDF may legitimately involve table, image and layout modalities while keeping one primary category. `GraphRAG` here means graph representation or graph-grounded retrieval is central; merely asking a multi-hop text question does not make the original dataset a native graph benchmark.

`rubric` identifies released output-assessment requirements, as in [DeepResearch Bench II](../dataset-cards/text-rag/deepresearch-bench-ii.md); `response_preference` identifies chosen/rejected response orderings, as in [RAG-RewardBench](../dataset-cards/text-rag/rag-rewardbench.md). Both are non-source annotations: neither is a reference source span, retrieval qrel or complete evidence chain. Judge-extracted evidence in a generated report is also not original-source gold.

## November 2026 classification assessment

Retain the five primary categories and existing paths. New search-agent, temporal and trust evaluations cross source representations; adding them beside text/image/graph/table would mix capability with representation and duplicate entries. Video fits `multimodal_rag` plus the existing `video` modality; generating a table-shaped answer does not make [SGR-Bench](../dataset-cards/text-rag/sgr-bench.md) Table RAG.

| Dimension | Where it is recorded | Maintenance rule |
|---|---|---|
| Primary source representation | `primary_category`, optional `secondary_categories` | One primary location; secondary links do not create duplicate records |
| Evaluated capability | `tasks` | Reuse existing tags; add `agentic_search`, `citation_prediction`, `response_preference` for the demonstrated gaps |
| Source media | `modalities` | Video/audio are media, not synonyms for agentic search |
| Domain and language | `domains`, `languages` | Enterprise, medicine and multilingual coverage are independent facets |
| Evaluation environment and version | `evaluation.protocol`, `data.splits`, `sources` | Distinguish live web/fixed corpus, supplied context, snapshot, tool budgets and judge revisions |
| Released annotation type | `ground_truth` | Distinguish source coordinates, answers, rubrics and preferences; never infer absent time intervals or graph paths |

The [capability routes](selecting-a-benchmark.md#capability-routes) provide a human-readable index across these facets without another taxonomy or duplicate catalog. A method that constructs a graph from HotpotQA does not relocate the native dataset into the graph category. [GRBench](../dataset-cards/graph-rag/grbench.md) and [GraphRAG-Bench](../dataset-cards/graph-rag/graphrag-bench.md) are genuinely different releases; ViDoRAG/ViDoSeek is a method/data naming distinction, not two datasets.

### November 18 annotation and task additions

Three new levels describe released source annotations. `chunk` addresses the upstream segmentation. `graph_triplet` identifies a knowledge graph triple. `time_interval` identifies start and end positions in media. Cards specify the track, split or mapping that supplies each level. Document validity dates remain time metadata. The interval label is reserved for positions in media.

Use the five existing categories to organize source representations. Acoustic resources use multimodal RAG and the `audio` modality. Image-bearing knowledge graphs use graph RAG with multimodal as a secondary category. The new `audio_qa` and `retrieval_routing` tags describe tasks, with selection routes for sequential replay, applicable-version retrieval and process diagnostics.

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
