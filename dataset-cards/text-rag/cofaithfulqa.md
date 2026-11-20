<!-- Generated from catalog/datasets/cofaithfulqa.yaml. Edit the YAML source. -->
# CoFaithfulQA

[简体中文](cofaithfulqa.zh-CN.md)

Supplied-evidence QA for measuring whether LLMs follow accurate passages that conflict with their closed-book answers.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-20 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | single_hop_qa, multi_hop_qa, rag_robustness |
| Modalities | text |
| Gold annotation levels | answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | Hub dataset card: MIT. Paper Appendix A.2 states academic research distribution. Source dataset terms are listed in Appendix A.1. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Six public JSONL files from HotpotQA, NewsQA, Natural Questions, SearchQA, SQuAD and TriviaQA. A row includes a question, supplied context, reference answers, the construction model's closed-book answer and its frequency. The release supplies per-question passages for given-evidence evaluation.

Splits: The Hub labels the public files train. The authors document those files for evaluation and report different deduplicated counts in the paper.
Format: JSONL.

## Ground truth and evaluation

The reference answer and supporting passage come from the source QA data. The construction pipeline identifies stable closed-book answers through repeated sampling and uses multiple models to verify conflicts. The release provides no independent open-corpus retrieval judgments.

Official metrics: context_recall, memory_recall, memorization_ratio.

Protocol: Supply each model with the same question and context and use the normalization in Section 5. Record the data revision, subset, prompting and scoring settings. Context recall and memory recall score answers against different references, and memorization ratio is MemR / (MemR + ConR).

## When to use it

- Measuring answer faithfulness when correct supplied evidence conflicts with model memory
- Comparing context recall and memory recall under fixed evidence

## Limitations and cautions

- Conflict selection depends on the construction model and its closed-book answer
- Evaluate open-corpus retrieval separately
- Dataset card and paper describe different distribution terms

## Access and sources

- [Official resource](https://huggingface.co/datasets/chengpingan/CoFaithfulQA)
- [Paper](https://doi.org/10.52202/085713-3356)
- [Data](https://huggingface.co/datasets/chengpingan/CoFaithfulQA/tree/main)
- paper: [source](https://arxiv.org/html/2502.15543v4#S4) — supports `summary`, `classification.tasks`, `ground_truth`
- paper: [source](https://arxiv.org/html/2502.15543v4#S5) — supports `evaluation.official_metrics`, `evaluation.protocol`
- paper: [source](https://arxiv.org/html/2502.15543v4#A1.SS2) — supports `access.license`, `use.caveats`
- dataset_card: [source](https://huggingface.co/datasets/chengpingan/CoFaithfulQA) — supports `classification.languages`, `data`, `ground_truth.alternatives`, `access.official`, `access.data`, `access.license`
- paper: [source](https://doi.org/10.52202/085713-3356) — supports `access.paper`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
