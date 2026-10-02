<!-- Generated from catalog/datasets/medqa.yaml. Edit the YAML source. -->
# MedQA

[简体中文](medqa.zh-CN.md)

Medical licensing-exam multiple-choice QA with multilingual subsets and reference materials used in medical RAG evaluations.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_convertible` |
| Primary category | `text_rag` |
| Tasks | single_hop_qa |
| Modalities | text |
| Gold annotation levels | answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown for source exam/textbook content; repository code is MIT |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The author repository links QA splits and reference textbook material. MIRAGE selects the US English four-option test subset; native MedQA also has other language and option-count settings.

Format: JSONL.

## Ground truth and evaluation

Correct option labels supervise exam answering. Reference textbooks are candidate knowledge sources, not query-level supporting-document or citation judgments.

Official metrics: accuracy.

Protocol: Name the language, option count and split. In MIRAGE use the 1,273-question US four-option subset, retrieve using only the question, and keep the selected corpus snapshot fixed.

## When to use it

- Medical-domain retrieval-augmented exam answering
- Comparing corpus/retriever combinations through MIRAGE

## Limitations and cautions

- Answer labels do not identify which retrieved source supports the answer
- Original language/option variants and MIRAGE-US are not interchangeable

## Access and sources

- [Official resource](https://github.com/jind11/MedQA)
- [Paper](https://arxiv.org/abs/2009.13081)
- [Data](https://github.com/jind11/MedQA)
- repository: [source](https://github.com/jind11/MedQA) — supports `summary`, `data.description`, `data.corpus`, `ground_truth.description`, `access.data`, `access.license`
- repository: [source](https://github.com/gzxiong/MIRAGE) — supports `evaluation.official_metrics`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
