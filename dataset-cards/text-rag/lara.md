<!-- Generated from catalog/datasets/lara.yaml. Edit the YAML source. -->
# LaRA

[简体中文](lara.zh-CN.md)

Long-context QA benchmark comparing retrieval-augmented and full-context inference across books, papers and financial reports.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | long_context_qa, rag_robustness |
| Modalities | text |
| Gold annotation levels | answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown; repository code is MIT, source texts retain upstream rights |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Released 32k/128k context files and queries cover location, comparison, reasoning and hallucination tasks. Questions are constructed for the source context, rather than an unrestricted web corpus.

Published scale: 2,326 test cases across three context types and four QA tasks.
Format: JSON/JSONL.

## Ground truth and evaluation

Human-authored seed QA guides GPT-4o generation, with sampled manual validation and iterative prompt refinement; this does not mean every pair is independently human-authored. Reference answers do not establish exhaustive supporting spans or optimal chunk boundaries.

Official metrics: llm_judged_accuracy.

Protocol: Report context length, context type and task separately. Use the released RAG/full-context scripts with identical source texts and pin the judge model and prompt used by compute_score_llm.py.

## When to use it

- RAG versus long-context routing
- Context-length and task-dependent retrieval analysis

## Limitations and cautions

- LLM-based grading depends on the judge and prompt
- Answer correctness alone cannot validate a chunking boundary

## Access and sources

- [Official resource](https://github.com/Alibaba-NLP/LaRA)
- [Paper](https://proceedings.mlr.press/v267/li25dv.html)
- [Data](https://github.com/Alibaba-NLP/LaRA/tree/main/datasets)
- paper: [source](https://arxiv.org/html/2502.09977#S3.SS3) — supports `ground_truth.provenance`, `ground_truth.description`
- paper: [source](https://proceedings.mlr.press/v267/li25dv.html) — supports `summary`, `data.size`
- repository: [source](https://github.com/Alibaba-NLP/LaRA) — supports `data.description`, `ground_truth.description`, `evaluation.protocol`, `access.data`, `access.license`
- repository: [source](https://github.com/Alibaba-NLP/LaRA/blob/main/evaluation/compute_score_llm.py) — supports `evaluation.official_metrics`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
