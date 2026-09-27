<!-- Generated from catalog/datasets/qasper.yaml. Edit the YAML source. -->
# QASPER

Information-seeking questions grounded in full NLP research papers with evidence annotations.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | long_context_qa, evidence_retrieval |
| Modalities | text |
| Evidence levels | paragraph, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Questions target full-text research papers; answers include extractive, abstractive, yes/no and unanswerable cases.


## Ground truth and evaluation

Answer annotations identify supporting evidence spans or paragraphs in the paper.

Official metrics: answer_f1, evidence_f1.


## When to use it

- Long-document evidence localization
- Section-aware chunking

## Limitations and cautions

- Evidence annotations are tied to the dataset text extraction and may not map directly to PDF coordinates

## Access and sources

- [Official resource](https://allenai.org/data/qasper)
- [Paper](https://arxiv.org/abs/2105.03011)
- [Data](https://huggingface.co/datasets/allenai/qasper)
- repository: [source](https://github.com/allenai/qasper-led-baseline) — supports `summary`, `evaluation.official_metrics`, `ground_truth.description`
- paper: [source](https://arxiv.org/abs/2105.03011) — supports `data.description`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
