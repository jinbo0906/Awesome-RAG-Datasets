<!-- Generated from catalog/datasets/grbench.yaml. Edit the YAML source. -->
# GRBench (Graph-CoT)

[简体中文](grbench.zh-CN.md)

Human-written questions over ten text-attributed graphs, testing graph lookup, multi-hop and inductive reasoning.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `rag_native` |
| Primary category | `graph_rag` |
| Tasks | graph_qa, graph_reasoning, multi_hop_qa |
| Modalities | text, graph |
| Gold annotation levels | answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | Apache-2.0 for the HF QA release; original graph sources retain their own terms. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Released with Graph-CoT in Findings ACL 2024; reused in ACL 2025 Graph Counselor. QA files are on Hugging Face and graph environments are linked separately by the authors. This is not the later GraphRAG-Bench novel/medical release.

Published scale: 1,740 questions over ten graphs from five broad application domains, as reported by the introducing paper.
Splits: Ten domain configurations exposed as test data; easy, medium and hard reasoning strata are not train/dev/test splits.
Format: JSON questions and answers plus separately downloaded graph environments..

## Ground truth and evaluation

Manually designed questions and reference answers; graph availability and difficulty labels do not imply independently annotated minimal evidence paths or gold agent trajectories.

Official metrics: exact_match, BLEU, ROUGE, GPT4score.

Protocol: Pin each graph environment and its QA configuration. The original script reports string metrics and a GPT-4 answer judge; Graph Counselor's ROUGE-L/QwenScore experiments use a different judge and should not be pooled with the original GPT4score.

## When to use it

- Comparing iterative graph exploration with flat textual retrieval
- Testing transfer from lookup to relational and inductive questions

## Limitations and cautions

- GRBench and GraphRAG-Bench are distinct resources rather than aliases
- Answer judges do not measure source-path completeness
- QA and graph environments must be acquired together

## Access and sources

- [Official resource](https://github.com/PeterGriffinJin/Graph-CoT)
- [Paper](https://aclanthology.org/2024.findings-acl.11/)
- [Data](https://huggingface.co/datasets/PeterJinGo/GRBench)
- paper: [source](https://aclanthology.org/2024.findings-acl.11/) — supports `summary`, `data.description`, `data.size`, `ground_truth.provenance`
- dataset_card: [source](https://huggingface.co/datasets/PeterJinGo/GRBench) — supports `data.splits`, `data.format`, `access.license`, `ground_truth.description`
- repository: [source](https://github.com/PeterGriffinJin/Graph-CoT/blob/main/eval.py) — supports `evaluation.official_metrics`, `evaluation.protocol`
- paper: [source](https://aclanthology.org/2025.acl-long.1202/) — supports `data.description`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
