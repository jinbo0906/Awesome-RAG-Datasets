<!-- Generated from catalog/datasets/or-quac.yaml. Edit the YAML source. -->
# OR-QuAC

[简体中文](or-quac.zh-CN.md)

QuAC conversations adapted to open retrieval with CANARD question rewrites and a Wikipedia passage collection.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | conversational_qa, query_rewriting, evidence_retrieval |
| Modalities | text |
| Gold annotation levels | paragraph, span, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | CC-BY-SA-4.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Author resources provide the passage collection, derived qrels, train/dev/test examples and QuAC-format dev/test references. The dataset aggregates QuAC dialogue, CANARD standalone rewrites and Wikipedia passages.


## Ground truth and evaluation

Answer spans originate in human QuAC annotations; passage qrels are derived from those gold contexts and are explicitly partial, because other passages may also answer a question.

Official metrics: answer_f1, HEQ-Q, HEQ-D, MRR, retrieval_recall.

Protocol: Preserve original dialogue histories and QuAC answer references, and evaluate retrieval separately from reader quality. Do not assume preprocessed dev/test evidence fields always include gold passages.

## When to use it

- Conversational retrieval and reader pipelines
- Comparing standalone rewrites with history-aware retrieval

## Limitations and cautions

- Derived passage relevance judgments are incomplete
- Retrieval-independent gold-context QA does not measure end-to-end performance

## Access and sources

- [Official resource](https://github.com/prdwb/orconvqa-release)
- [Paper](https://ciir-publications.cs.umass.edu/getpdf.php?id=1386)
- repository: [source](https://github.com/prdwb/orconvqa-release) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.protocol`, `access.license`
- paper: [source](https://ciir-publications.cs.umass.edu/getpdf.php?id=1386) — supports `evaluation.official_metrics`
- repository: [source](https://github.com/prdwb/orconvqa-release/blob/master/scorer.py) — supports `evaluation.official_metrics`
- repository: [source](https://github.com/prdwb/orconvqa-release/blob/master/train_pipeline.py) — supports `evaluation.official_metrics`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
