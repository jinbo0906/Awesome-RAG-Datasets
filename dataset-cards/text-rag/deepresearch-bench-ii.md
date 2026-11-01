<!-- Generated from catalog/datasets/deepresearch-bench-ii.yaml. Edit the YAML source. -->
# DeepResearch Bench II

[简体中文](deepresearch-bench-ii.zh-CN.md)

Expert-report-grounded rubrics measuring information recall, analysis and presentation in deep-research reports.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | agentic_search, long_form_qa, attribution |
| Modalities | text |
| Gold annotation levels | rubric |
| Evidence provenance | mixed |
| Corpus / queries / answers | external / provided / provided |
| Original data license | Per-task data terms follow DATA_LICENSE and each record's source license; 129 tasks CC-BY-4.0, two CC-BY-NC-4.0 and one CC0, not the Apache-2.0 code license. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

tasks_and_rubrics.jsonl supplies prompts and content-bearing assessment rubrics derived from expert articles through LLM extraction, revision and human/expert review. Agents research the web and write reports; reference articles and forbidden-reference rules are evaluation material, not oracle context for the agent.

Published scale: 132 released tasks across 22 domains, with 66 English and 66 Chinese tasks and 9,430 rubrics; the October 2026 leaderboard excludes tasks 112 and 114, leaving 130 eligible tasks.
Splits: Released evaluation set; retain all 132 records for archival accounting and report the exact scored task IDs, valid-result count and exclusions.
Format: JSONL tasks/rubrics; evaluated Markdown or DOCX reports are parsed to text by the current pipeline..

## Ground truth and evaluation

Released binary content rubrics encode factual or inferential output requirements, not source-coordinate qrels or a unique reference report. The current judge uses 1 for supported satisfaction, 0 for absence, and -1 for reliance on blocked references; evidence strings locate text in the generated report, not original-source evidence gold.

Official metrics: total, inforecall, analysis, presentation, blocked_rate.

Protocol: The aggregator measures the fraction of rubric items scored 1 and separately the blocked-reference fraction, then averages available task results. Fix judged task IDs, denominator and judge branch; the official evaluator migrated in August 2026 and October scoring excludes two tasks. Do not compare 132-task historical scores with 130-task current scores or treat rubric success as document recall.

## When to use it

- Diagnosing missing information versus weak analysis or presentation
- Designing independently verifiable fine-grained report rubrics

## Limitations and cautions

- Source-article leakage and blocked-reference use must be assessed separately from writing quality
- Current repository parsing ignores embedded report images; support for file formats is not multimodal retrieval gold
- License and score eligibility vary by task; preserve per-task metadata rather than assigning a blanket license or denominator

## Access and sources

- [Official resource](https://github.com/imlrz/DeepResearch-Bench-II)
- [Paper](https://arxiv.org/abs/2601.08536)
- [Data](https://github.com/imlrz/DeepResearch-Bench-II/blob/main/tasks_and_rubrics.jsonl)
- paper: [source](https://arxiv.org/html/2601.08536) — supports `name`, `summary`, `data.description`, `data.size`, `ground_truth.provenance`, `use.best_for`
- repository: [source](https://github.com/imlrz/DeepResearch-Bench-II) — supports `data.splits`, `data.format`, `ground_truth.description`, `evaluation.protocol`, `use.caveats`
- repository: [source](https://github.com/imlrz/DeepResearch-Bench-II/blob/main/aggregate_scores.py) — supports `evaluation.official_metrics`, `evaluation.protocol`
- repository: [source](https://github.com/imlrz/DeepResearch-Bench-II/blob/main/DATA_LICENSE) — supports `access.license`
- repository: [source](https://github.com/imlrz/DeepResearch-Bench-II/blob/main/tasks_and_rubrics.jsonl) — supports `data.size`, `ground_truth.levels`, `ground_truth.description`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
