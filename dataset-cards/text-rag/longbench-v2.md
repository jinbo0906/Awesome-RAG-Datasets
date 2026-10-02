<!-- Generated from catalog/datasets/longbench-v2.yaml. Edit the YAML source. -->
# LongBench v2

[简体中文](longbench-v2.zh-CN.md)

Human-authored multiple-choice benchmark for deep reasoning over realistic long documents, conversations, repositories and structured data.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_convertible` |
| Primary category | `text_rag` |
| Tasks | long_context_qa |
| Modalities | text |
| Gold annotation levels | answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | MIT |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Each record supplies a long context, four options and a correct option. The native task is long-context understanding; the released code also supports a top-N retrieved-context RAG comparison.

Published scale: 503 questions across six task categories; context lengths range from 8k to 2M words.
Splits: The Hugging Face split named train contains the evaluation release; do not treat it as a training set for leaderboard evaluation.
Format: JSON.

## Ground truth and evaluation

The answer key identifies A/B/C/D. The published record format does not provide query-level supporting spans, qrels or optimal segmentation boundaries.

Official metrics: accuracy.

Protocol: Separate direct, CoT, no-context and RAG settings. Report difficulty, task and length groups; specify top-N, chunking and retrieval configuration for a RAG run.

## When to use it

- Long-context versus retrieval comparisons
- Answer-quality stress tests beyond extractive lookup

## Limitations and cautions

- No native supporting-span supervision for chunking
- Multiple-choice accuracy can reflect reasoning or memorization rather than retrieval success

## Access and sources

- [Official resource](https://longbench2.github.io/)
- [Paper](https://aclanthology.org/2025.acl-long.183/)
- [Data](https://huggingface.co/datasets/zai-org/LongBench-v2)
- paper: [source](https://aclanthology.org/2025.acl-long.183/) — supports `summary`, `data.size`, `ground_truth.provenance`
- repository: [source](https://github.com/THUDM/LongBench) — supports `data.description`, `data.splits`, `ground_truth.description`, `evaluation.protocol`
- dataset_card: [source](https://huggingface.co/datasets/zai-org/LongBench-v2) — supports `access.license`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
