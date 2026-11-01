<!-- Generated from catalog/datasets/rag-rewardbench.yaml. Edit the YAML source. -->
# RAG-RewardBench

[简体中文](rag-rewardbench.zh-CN.md)

Chosen/rejected response pairs for evaluating reward models on RAG-specific preference judgments.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `auxiliary` |
| Primary category | `text_rag` |
| Tasks | response_preference, rag_robustness, attribution |
| Modalities | text |
| Gold annotation levels | response_preference |
| Evidence provenance | synthetic |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | Apache-2.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Records contain retrieved references inside prompt, question, chosen/reject candidate responses, generating-model names and subset labels. Six retrievers and 24 answer models diversify the construction; this is a fixed-context response-comparison dataset, not an open retrieval corpus.

Published scale: 1,485 preference pairs; the release derives from 18 source RAG subsets and adds RAG-specific comparison scenarios.
Splits: Hugging Face names the sole split train, but the introducing paper uses it as an evaluation benchmark; do not assume an independent held-out split exists.
Format: JSON with prompt, question, chosen, reject, model and subset fields.

## Ground truth and evaluation

The released target is the preference ordering chosen over reject, not a reference QA answer or a source-evidence span. An ensemble of model judges scores candidate responses and filters low-consensus pairs; human preference checks assess sampled agreement rather than making every released pair a human annotation.

Official metrics: pairwise_preference_accuracy.

Protocol: Score the chosen response above the rejected response under the same supplied references. For generative judges, swap candidate order, evaluate twice and average accuracy to reduce positional bias. Report scenario/subset results before the aggregate. Multi-hop reasoning, fine-grained citation, abstention and conflict robustness are preference conditions, not four independently labeled retrieval benchmarks.

## When to use it

- Selecting reward models or response judges for grounded generation
- Testing whether preference scorers notice citation errors and inappropriate refusal

## Limitations and cautions

- Model-generated preferences can inherit consensus and judge biases
- High pairwise accuracy is not end-to-end retrieval or answer accuracy
- The public GitHub repository links data and paper but does not itself provide a complete evaluator implementation
- The 2024 preprint and Findings ACL 2025 publication are different milestones

## Access and sources

- [Official resource](https://github.com/jinzhuoran/RAG-RewardBench)
- [Paper](https://aclanthology.org/2025.findings-acl.877/)
- [Data](https://huggingface.co/datasets/jinzhuoran/RAG-RewardBench)
- paper: [source](https://aclanthology.org/2025.findings-acl.877.pdf) — supports `summary`, `classification`, `data.size`, `ground_truth`, `evaluation`, `use`
- dataset_card: [source](https://huggingface.co/datasets/jinzhuoran/RAG-RewardBench) — supports `data.description`, `data.corpus`, `data.queries`, `data.answers`, `data.splits`, `data.format`, `access.license`, `access.gated`
- repository: [source](https://github.com/jinzhuoran/RAG-RewardBench) — supports `access.data`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
