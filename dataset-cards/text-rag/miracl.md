<!-- Generated from catalog/datasets/miracl.yaml. Edit the YAML source. -->
# MIRACL

[简体中文](miracl.zh-CN.md)

Native-speaker passage relevance judgments for same-language Wikipedia retrieval across 18 languages.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `auxiliary` |
| Primary category | `text_rag` |
| Tasks | evidence_retrieval |
| Modalities | text |
| Gold annotation levels | paragraph |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / not_provided |
| Original data license | Apache-2.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Author resources provide language-specific Wikipedia passage corpora, queries and positive/negative relevance judgments. Native queries and corpora share a language; this is not automatically cross-lingual retrieval or generated-answer evaluation.

Published scale: The paper reports about 78K queries and over 726K relevance judgments across 18 languages.
Splits: Splits vary by language; the German and Yoruba surprise evaluation languages do not have training data.

## Ground truth and evaluation

Native speakers label relevance of identified retrieval passages. Passages retain article titles and article/passage IDs; qrels do not provide reference answers or annotate optimal new chunk boundaries.

Official metrics: nDCG@10, Recall@100.

Protocol: Preserve language-specific corpus versions, splits and passage IDs, and score against the official qrels. Add an independent answer protocol before calling an experiment end-to-end RAG.

## When to use it

- Multilingual retrieval component evaluation
- Comparing retrieval across high- and low-resource languages

## Limitations and cautions

- The native task has no generated-answer reference
- Query/qrels licensing does not replace upstream Wikipedia corpus terms

## Access and sources

- [Official resource](https://github.com/project-miracl/miracl)
- [Paper](https://aclanthology.org/2023.tacl-1.63/)
- [Data](https://huggingface.co/datasets/miracl/miracl)
- repository: [source](https://github.com/project-miracl/miracl) — supports `summary`, `data.description`, `ground_truth.description`
- paper: [source](https://aclanthology.org/2023.tacl-1.63/) — supports `data.size`
- paper: [source](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00595/117438/MIRACL-A-Multilingual-Retrieval-Dataset-Covering) — supports `evaluation.official_metrics`, `evaluation.protocol`
- dataset_card: [source](https://huggingface.co/datasets/miracl/miracl) — supports `access.license`, `ground_truth.alternatives`
- dataset_card: [source](https://huggingface.co/datasets/miracl/miracl/discussions/1) — supports `data.splits`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
