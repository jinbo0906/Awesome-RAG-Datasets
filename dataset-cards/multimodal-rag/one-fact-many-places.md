<!-- Generated from catalog/datasets/one-fact-many-places.yaml. Edit the YAML source. -->
# One Fact, Many Places (MMLongBench-Red / MMDocRAG-Red)

[简体中文](one-fact-many-places.zh-CN.md)

A shared release of fact-level alternative evidence annotations for auditing document retrieval, citation and masking-based attribution.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-18 |
| RAG role | `auxiliary` |
| Primary category | `multimodal_rag` |
| Tasks | page_retrieval, evidence_retrieval, attribution |
| Modalities | text, image, table, chart, layout |
| Gold annotation levels | page, bbox, quote, fact_citation |
| Evidence provenance | mixed |
| Corpus / queries / answers | external / provided / external |
| Original data license | CC-BY-NC-4.0 (released data annotations) |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The October 2026 preprint augments subsets of MMLongBench-Doc and MMDocRAG. Its ancillary archive contains the two annotation files, alternative review versions, portable scorers and frozen outputs. MMLongBench-Red includes original answers. Use the upstream releases for full source and answer assets including PDFs and image candidates.

Published scale: 420 questions across two files. MMLongBench-Red has 220 (60 development and 160 test). MMDocRAG-Red has 200 (two samples of 80 and 120).
Splits: Relevant denominators are 208 applicable MMLongBench-Red questions (54 dev and 154 test) and 196 applicable MMDocRAG-Red questions. Freeze the original annotation files for published scores and name the review variant for sensitivity tests.
Format: JSONL annotations and Python scoring library in the arXiv ancillary 7z archive.

## Ground truth and evaluation

Page and quote instances are grouped by supporting fact. MMDocRAG-Red distinguishes strict, loose, combination and contextual quotes. MMLongBench-Red has conditional boxes in PDF points found by key strings and OCR. A model applied the annotation protocol and two human reviewers independently re-annotated 60 sampled questions.

Official metrics: evidence_aware_recall_at_k, redundancy_aware_quote_F1, set_level_masking_answer_survival.

Protocol: Compare page scoring under dataset, verified-gold and evidence-aware modes. State the exact Quote F1 variant and keep strict support, jointly necessary quotes and contextual mentions distinct. Measure masking against an all-annotated-instances condition at comparable granularity and report applicable counts.

## When to use it

- Measuring false retrieval misses and citation errors under single-location labels
- Testing whether masking one evidence region leaves a valid copy

## Limitations and cautions

- Images and PDFs require the upstream datasets
- OCR and text-layer search can undercount pixel-only copies
- Sparse boxes and sampled alternative locations do not constitute exhaustive source annotations

## Access and sources

- [Official resource](https://arxiv.org/abs/2610.26401)
- [Paper](https://arxiv.org/pdf/2610.26401)
- [Data](https://arxiv.org/src/2610.26401v1/anc/code-and-data.7z)
- paper: [source](https://arxiv.org/pdf/2610.26401) — supports `summary`, `classification`, `data.description`, `ground_truth`, `evaluation.official_metrics`, `evaluation.protocol`, `access.license`, `use`
- official: [source](https://arxiv.org/src/2610.26401v1/anc/code-and-data.7z) — supports `data.size`, `data.splits`, `data.format`, `ground_truth.provenance`, `access.data`, `access.license`, `evaluation.evaluator`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
