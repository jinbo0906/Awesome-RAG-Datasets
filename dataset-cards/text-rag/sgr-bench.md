<!-- Generated from catalog/datasets/sgr-bench.yaml. Edit the YAML source. -->
# SGR-Bench (paper-linked release)

[简体中文](sgr-bench.zh-CN.md)

State-gated web retrieval tasks requiring source discovery, filter/scope control and complete structured answers.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | agentic_search, multi_hop_qa |
| Modalities | text, table |
| Gold annotation levels | answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | external / provided / provided |
| Original data license | CC-BY-4.0 for released task data; external source websites retain their own terms. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The paper-linked PKUAIWeb release pairs goal-oriented and constraint-guided prompts over the same information needs. Records include output schemas, reference answers, state/dependency metadata and review rubrics; actual data sources remain live specialized websites.

Published scale: 100 task formulations, comprising 50 goal/constraint pairs, across six source families and 12 public data ecosystems in the paper.
Splits: 50 goal and 50 constraint English records; aligned Chinese per-task files are provided. These are paired evaluation formulations, not independent train/test splits.
Format: Hugging Face JSONL splits and per-task JSON files..

## Ground truth and evaluation

LLM-assisted drafting and expert validation produce ordered-table reference answers, narrow canonicalization rules and retrieval-state annotations. The release does not give exhaustive per-action gold trajectories; table-shaped answers are not source-cell coordinates.

Official metrics: exact_match, Item-F1, Row-F1, P.O.A..

Protocol: Fix the paper-linked 100-record release. Give agents the declared task prompt/output format and report whether reference entry URLs are revealed. Canonicalize without repairing missing facts, align row keys, and score individual fields, complete rows and shared-row order separately. The paper's main table uses Item-F1, Row-F1 and P.O.A.; release instructions also specify exact match. Root-cause trace review is separate from deterministic answer metrics.

## When to use it

- Testing retrieval-state preservation rather than only relevant-site discovery
- Diagnosing locally correct fields but incomplete structured answers

## Limitations and cautions

- Paired prompts share answers and must not be treated as independent information needs
- Public website changes and system-specific tools affect reproducibility
- This entry pins the original paper-linked release; larger similarly named releases require separate provenance and version checks

## Access and sources

- [Official resource](https://huggingface.co/datasets/PKUAIWeb/SGR-BENCH)
- [Paper](https://arxiv.org/abs/2605.22219)
- [Data](https://huggingface.co/datasets/PKUAIWeb/SGR-BENCH)
- paper: [source](https://arxiv.org/html/2605.22219) — supports `summary`, `classification.rag_role`, `data.size`, `ground_truth.description`, `ground_truth.provenance`, `evaluation.official_metrics`, `evaluation.protocol`
- dataset_card: [source](https://huggingface.co/datasets/PKUAIWeb/SGR-BENCH) — supports `data.description`, `data.splits`, `data.format`, `evaluation.protocol`, `access.license`, `access.gated`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
