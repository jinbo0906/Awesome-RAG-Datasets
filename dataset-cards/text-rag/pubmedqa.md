<!-- Generated from catalog/datasets/pubmedqa.yaml. Edit the YAML source. -->
# PubMedQA

[简体中文](pubmedqa.zh-CN.md)

Biomedical research QA that predicts yes, no or maybe from a PubMed abstract, with labeled, unlabeled and artificial subsets.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_convertible` |
| Primary category | `text_rag` |
| Tasks | single_hop_qa, fact_verification |
| Modalities | text |
| Gold annotation levels | answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown; PubMed abstract rights depend on upstream content |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Native examples supply a question, abstract context and conclusion-derived long answer. MIRAGE's PubMedQA* removes the given context from the 500 expert-labeled test questions and uses external retrieval instead.

Published scale: 1,000 expert-labeled, 61.2k unlabeled and 211.3k artificially generated instances; the unlabeled subset lacks gold decisions.
Format: JSON.

## Ground truth and evaluation

Final yes/no/maybe decisions are the scored target, with expert labels in PQA-L and synthetic labels in PQA-A. The supplied abstract is task context, not an exhaustive open-corpus relevance judgment.

Official metrics: accuracy, macro_f1.

Protocol: Report the selected subset and supervision regime. Native abstract-conditioned QA and MIRAGE's context-removed PubMedQA* evaluate different tasks; accuracy/F1 must not be treated as retrieval recall.

## When to use it

- Biomedical abstract-conditioned QA
- Context-removed medical RAG comparison via MIRAGE

## Limitations and cautions

- Source abstracts and reference conclusions must not leak into context-removed evaluation
- Different label provenances require separate reporting

## Access and sources

- [Official resource](https://pubmedqa.github.io/)
- [Paper](https://aclanthology.org/D19-1259/)
- [Data](https://github.com/pubmedqa/pubmedqa)
- official: [source](https://pubmedqa.github.io/) — supports `summary`, `data.size`
- repository: [source](https://github.com/pubmedqa/pubmedqa) — supports `data.description`, `ground_truth.description`, `ground_truth.provenance`
- repository: [source](https://github.com/pubmedqa/pubmedqa/blob/master/evaluation.py) — supports `evaluation.official_metrics`
- repository: [source](https://github.com/gzxiong/MIRAGE) — supports `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
