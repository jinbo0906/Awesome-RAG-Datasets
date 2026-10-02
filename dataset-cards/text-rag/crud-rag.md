<!-- Generated from catalog/datasets/crud-rag.yaml. Edit the YAML source. -->
# CRUD-RAG

[简体中文](crud-rag.zh-CN.md)

Chinese RAG benchmark covering continuation, question answering, summarization and text correction.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | single_hop_qa, multi_hop_qa, summarization, rag_robustness |
| Modalities | text |
| Gold annotation levels | answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The release contains merged task data, the paper's selected experiment subset and more than 80K news documents used as the retrieval database.

Format: JSON and text documents.

## Ground truth and evaluation

Task references support generation and correction scoring; the release is not claimed to provide a universal sentence-level supporting-evidence set.

Official metrics: bleu, rouge, bertscore, ragquesteval.

Protocol: Select the released experiment subset and report the task, chunking, top-k and model prompts. RAGQuestEval requires a question-generation/answering model.

## When to use it

- Chinese news RAG beyond short QA
- Comparing generation tasks under one retrieval corpus

## Limitations and cautions

- Reference style and prompting affect lexical metrics
- The repository citation identifies ACM TOIS; do not relabel its arXiv version as a conference paper

## Access and sources

- [Official resource](https://github.com/IAAR-Shanghai/CRUD_RAG)
- [Paper](https://doi.org/10.1145/3701228)
- [Data](https://github.com/IAAR-Shanghai/CRUD_RAG/tree/main/data)
- repository: [source](https://github.com/IAAR-Shanghai/CRUD_RAG) — supports `summary`, `classification`, `data`, `ground_truth`, `evaluation`, `access.paper`, `use`
- paper: [source](https://arxiv.org/html/2401.17043v3) — supports `ground_truth.provenance`, `evaluation.official_metrics`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
