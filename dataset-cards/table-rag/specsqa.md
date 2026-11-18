<!-- Generated from catalog/datasets/specsqa.yaml. Edit the YAML source. -->
# SpecsQA

[简体中文](specsqa.zh-CN.md)

Semi-structured product QA testing exhaustive lists, multi-constraint filtering and cross-product comparisons.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-18 |
| RAG role | `rag_native` |
| Primary category | `table_rag` |
| Tasks | table_qa, text_table_reasoning |
| Modalities | text, table |
| Gold annotation levels | answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | CC-BY-ND-4.0 (data) |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

November 2025 Samsung UK snapshot with specification tables and product prose. SpecsQA supplies question categories, reference prose and product lists where available. DualGraph builds textual and symbolic graphs from the snapshot.

Published scale: 117 questions (counted in questions.json), 2,162 product pages over 26 categories (author release).
Splits: One evaluation set with inverse, multi-condition and reasoning/comparison questions. Keep the objective-only list subset distinct in results.
Format: Question JSON and split tar.xz raw HTML archive with parsing code.

## Ground truth and evaluation

Questions are manually curated and reference material includes product list targets, source hints and a preferred retrieval method. Some prose references use model generation from lists. These fields do not provide exhaustive per-question passage, cell or graph-path labels.

Official metrics: factual_correctness_F1, list_match_precision_recall_F1, pairwise_judge_win_rate, input_output_tokens.

Protocol: Run retrieval or symbolic lookup over the full snapshot. List Match extracts a predicted list using an LLM and computes set precision, recall and F1 against available list targets. Score factual correctness and pairwise output quality separately, and report indexing and query token use.

## When to use it

- Comparing semantic retrieval and exact structured filtering
- Testing complete product enumeration across documents

## Limitations and cautions

- Results refer to a single vendor snapshot
- List extraction and judging introduce model dependence
- The checked release includes system code and data but no confirmed standalone scorer

## Access and sources

- [Official resource](https://github.com/corneliocristina/DualGraphRAG)
- [Paper](https://aclanthology.org/2026.findings-emnlp.1319/)
- [Data](https://github.com/corneliocristina/DualGraphRAG/tree/main/SpecsQA)
- paper: [source](https://aclanthology.org/2026.findings-emnlp.1319/) — supports `summary`, `classification`
- paper: [source](https://arxiv.org/html/2605.27164) — supports `evaluation.official_metrics`, `evaluation.protocol`, `use`
- repository: [source](https://raw.githubusercontent.com/corneliocristina/DualGraphRAG/main/SpecsQA/README.md) — supports `data`, `ground_truth.description`, `access.data`, `access.license`
- repository: [source](https://github.com/corneliocristina/DualGraphRAG/blob/main/SpecsQA/questions.json) — supports `data.size`, `ground_truth`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
