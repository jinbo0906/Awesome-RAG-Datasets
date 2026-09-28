<!-- Generated from catalog/datasets/t2-ragbench.yaml. Edit the YAML source. -->
# T²-RAGBench

[简体中文](t2-ragbench.zh-CN.md)

Financial-document RAG benchmark combining prose, tables and numerical reasoning.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `table_rag` |
| Tasks | text_table_reasoning, table_qa |
| Modalities | text, table |
| Gold annotation levels | answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Built from FinQA, ConvFinQA and TAT-DQA style financial document QA; PDF and structured contexts require explicit version selection.

Published scale: Project site reports 23,088 triples; the original paper abstract reports 32,908. Treat these as different release or counting scopes until reconciled.

## Ground truth and evaluation

Question-context-answer triples are released; exact table-cell evidence coverage needs release-specific inspection.

Official metrics: answer_accuracy.

Protocol: State the downloaded release and source-document conversion when comparing systems.

## When to use it

- Numerical reasoning across prose and tables
- Testing financial-document retrieval

## Limitations and cautions

- Paper and live project page disagree on total triples; do not combine results across unverified versions

## Access and sources

- [Official resource](https://t2ragbench.demo.hcds.uni-hamburg.de/)
- [Paper](https://arxiv.org/abs/2506.12071)
- [Data](https://huggingface.co/datasets/G4KMU/t2-ragbench)
- official: [source](https://t2ragbench.demo.hcds.uni-hamburg.de/) — supports `summary`, `data.description`, `data.size`
- paper: [source](https://arxiv.org/abs/2506.12071) — supports `data.size`, `classification.tasks`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
