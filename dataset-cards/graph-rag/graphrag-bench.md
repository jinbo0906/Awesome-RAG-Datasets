<!-- Generated from catalog/datasets/graphrag-bench.yaml. Edit the YAML source. -->
# GraphRAG-Bench

[简体中文](graphrag-bench.zh-CN.md)

Domain benchmark comparing graph-based RAG across factual and contextual generation tasks.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `rag_native` |
| Primary category | `graph_rag` |
| Tasks | graph_reasoning, single_hop_qa, summarization |
| Modalities | text, graph |
| Gold annotation levels | answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Released novel and medical tracks evaluate fact retrieval, complex reasoning, contextual summarization and creative generation. The dataset was released in 2025; the author repository reports ICLR 2026 acceptance. This is distinct from the ten-graph GRBench introduced by Graph-CoT.


## Ground truth and evaluation

Reference answers and task-level evaluation are published; a universal gold graph path is not claimed here.

Official metrics: accuracy, rouge_l, coverage, factual_score.

Protocol: Separate graph construction cost and retrieval effects from generation quality. Fact retrieval and complex reasoning report accuracy/ROUGE-L; summarization reports accuracy/coverage; creative generation additionally uses factual score. Fix task-specific judges and budgets rather than presenting one answer metric as gold path retrieval.

## When to use it

- Comparing GraphRAG with text RAG
- Studying which task types benefit from graph structure

## Limitations and cautions

- The graph may be constructed by the evaluated method; generated graph edges are not gold evidence paths

## Access and sources

- [Official resource](https://github.com/GraphRAG-Bench/GraphRAG-Benchmark)
- [Paper](https://arxiv.org/abs/2506.05690)
- repository: [source](https://github.com/GraphRAG-Bench/GraphRAG-Benchmark) — supports `summary`, `data.description`, `evaluation.official_metrics`
- repository: [source](https://github.com/GraphRAG-Bench/GraphRAG-Benchmark) — supports `data.description`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
