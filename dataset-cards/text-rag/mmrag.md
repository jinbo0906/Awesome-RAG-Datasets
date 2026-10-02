<!-- Generated from catalog/datasets/mmrag.yaml. Edit the YAML source. -->
# mmRAG (text, tables and knowledge graphs)

[简体中文](mmrag.zh-CN.md)

Integrated RAG release with queries and relevance judgments over unified text representations of prose, tables and knowledge graphs.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | evidence_retrieval, single_hop_qa, graph_qa, table_qa |
| Modalities | text, table, graph |
| Gold annotation levels | document, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown; source datasets retain their own terms |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Derives questions and retrievable records from NQ, TriviaQA, OTT-QA, TAT-QA, ComplexWebQuestions and WebQSP. Tables and KG facts are converted to documents and split into non-overlapping 512-token chunks; this is not an image-text benchmark such as M2RAG.

Format: JSON.

## Ground truth and evaluation

Pooled 512-token chunks receive LLM relevance grades 0/1/2; dataset-level relevance is derived for routing. The catalog document level denotes these addressable retrieval records, not original whole-document qrels. Labels do not supervise graph paths or alternative chunk boundaries.

Official metrics: ndcg_at_k, map_at_k, hits_at_k.

Protocol: Use the released 512-token chunks, judgments and splits together. Rechunking requires evidence remapping or new relevance judgments, not reuse of old chunk IDs. The retrieval script reports NDCG, MAP and Hits at 1/3/5; report routing and answer generation separately. Pin LLM annotation and grading configurations when reconstructing the benchmark.

## When to use it

- Routing between text/table/KG sources
- Component-level relevance evaluation across heterogeneous representations

## Limitations and cautions

- LLM judgments and incomplete pooling are not exhaustive human evidence gold
- Graphs and tables are serialized; image-layout reasoning is outside the native protocol

## Access and sources

- [Official resource](https://github.com/nju-websoft/mmRAG)
- [Paper](https://arxiv.org/abs/2505.11180)
- [Data](https://huggingface.co/datasets/Askio/mmrag_benchmark)
- paper: [source](https://arxiv.org/html/2505.11180v1) — supports `data.description`, `ground_truth.description`, `evaluation.protocol`
- repository: [source](https://github.com/nju-websoft/mmRAG) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.protocol`, `access.data`
- repository: [source](https://github.com/nju-websoft/mmRAG/blob/main/mmrag_experiments/eval.py) — supports `evaluation.official_metrics`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
