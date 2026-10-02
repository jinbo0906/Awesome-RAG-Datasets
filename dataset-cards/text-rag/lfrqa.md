<!-- Generated from catalog/datasets/lfrqa.yaml. Edit the YAML source. -->
# LFRQA / RAG-QA Arena

[简体中文](lfrqa.zh-CN.md)

Human-written long answers and document citations for cross-domain retrieval-augmented QA.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | long_form_qa, attribution |
| Modalities | text |
| Gold annotation levels | document, fact_citation, answer |
| Evidence provenance | human |
| Corpus / queries / answers | external / provided / provided |
| Original data license | Apache-2.0 for the project; underlying corpus terms apply separately |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

LFRQA extends RobustQA with long-form answers; download the underlying raw documents and passages through RobustQA. Citation-annotated files are a separate revised release.

Published scale: The EMNLP 2024 paper reports about 26K queries across seven domains; citation-release counts differ.
Format: JSONL.

## Ground truth and evaluation

The citation release maps faithful_answer_w_citation and citation_numbers to annotated gold doc_id values; these are document references rather than character spans.

Official metrics: win_rate, win_plus_tie_rate, elo_rating.

Protocol: RAG-QA Arena compares generated answers against LFRQA or other systems with a fixed LLM judge. Record the annotation version, retrieved-passage count and judge model.

## When to use it

- Long-form cross-domain answer comparison
- Document citation and answer-quality evaluation

## Limitations and cautions

- The Arena evaluator is a protocol while LFRQA is the dataset
- The official repository provides new annotations; its license does not replace upstream corpus terms

## Access and sources

- [Official resource](https://github.com/awslabs/rag-qa-arena)
- [Paper](https://aclanthology.org/2024.emnlp-main.249/)
- [Data](https://github.com/awslabs/rag-qa-arena/tree/main/data)
- paper: [source](https://aclanthology.org/2024.emnlp-main.249/) — supports `summary`, `classification`, `data.size`
- repository: [source](https://github.com/awslabs/rag-qa-arena) — supports `data.description`, `data.format`, `ground_truth`, `evaluation`, `access.license`, `use`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
