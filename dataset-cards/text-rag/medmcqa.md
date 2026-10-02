<!-- Generated from catalog/datasets/medmcqa.yaml. Edit the YAML source. -->
# MedMCQA

[简体中文](medmcqa.zh-CN.md)

Indian medical entrance-exam multiple-choice QA with explanations, subjects and topic metadata, used as a component of MIRAGE.

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
| Corpus / queries / answers | not_provided / provided / provided |
| Original data license | MIT in author repository; consult source-question terms |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Question records contain four options, a correct option, explanations and subject/topic fields. A fixed medical retrieval corpus must be supplied for RAG; an explanation is not a source document.

Format: JSON.

## Ground truth and evaluation

Correct-option labels and explanatory text do not supply source-document relevance or supporting-span coordinates.

Official metrics: accuracy.

Protocol: Use upstream split labels as documented; MIRAGE uses 4,183 development questions rather than the native held-out test set. Report the RAG corpus and question-only retrieval configuration.

## When to use it

- Medical multiple-choice generation with external retrieval
- MIRAGE component comparisons

## Limitations and cautions

- Requires a separately specified retrieval corpus and evidence mapping
- MIRAGE development evaluation must not be reported as native test performance

## Access and sources

- [Official resource](https://medmcqa.github.io/)
- [Paper](https://proceedings.mlr.press/v174/pal22a.html)
- [Data](https://github.com/medmcqa/medmcqa)
- repository: [source](https://github.com/medmcqa/medmcqa) — supports `summary`, `data.description`, `ground_truth.description`, `access.data`
- repository: [source](https://github.com/medmcqa/medmcqa/blob/main/LICENSE.md) — supports `access.license`
- repository: [source](https://github.com/gzxiong/MIRAGE) — supports `evaluation.official_metrics`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
