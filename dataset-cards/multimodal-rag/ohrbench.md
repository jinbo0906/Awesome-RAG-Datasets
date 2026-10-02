<!-- Generated from catalog/datasets/ohrbench.yaml. Edit the YAML source. -->
# OHRBench

[简体中文](ohrbench.zh-CN.md)

Document RAG benchmark isolating how OCR semantic and formatting errors affect evidence retrieval and answer generation.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_native` |
| Primary category | `multimodal_rag` |
| Tasks | rag_robustness, evidence_retrieval, visual_qa |
| Modalities | text, image, table, chart, equation, layout |
| Gold annotation levels | page, quote, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown; HF metadata says CC BY 4.0, but author copyright statement restricts research use and prohibits commercial use |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Releases PDFs, human-verified structured page data, qas_v2.json, OCR outputs and semantic/formatting perturbations. The native pipeline extracts a textual knowledge base from document images, rather than requiring a vision-only generator.

Published scale: 8,561 document-page images and 8,498 QA pairs across seven domains in the ICCV 2025 paper.
Format: PDF/JSON/text.

## Ground truth and evaluation

Questions retain source-page and supporting-content mappings; human-verified page transcription provides an OCR reference. Transcription correctness and QA supporting content are different labels and are not optimal segmentation boundaries.

Official metrics: ocr_edit_distance, evidence_lcs, answer_f1.

Protocol: Report OCR edit distance, retrieval evidence inclusion via longest common subsequence (LCS), gold-context generation and full RAG separately. Pin OCR version, perturbation severity and QA release; group results by text, table, formula, chart and reading-order tasks. LCS evidence inclusion is not document Recall@K.

## When to use it

- Tracing OCR errors through the RAG pipeline
- Chunking evaluation under structured-document corruption

## Limitations and cautions

- Corrupted source text requires remapping evidence to the canonical page content
- Good OCR or answer F1 alone does not prove cross-modal evidence completeness
- License metadata and research-only copyright statement differ; consult author terms and source-document rights

## Access and sources

- [Official resource](https://github.com/opendatalab/OHR-Bench)
- [Paper](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_OCR_Hinders_RAG_Evaluating_the_Cascading_Impact_of_OCR_on_ICCV_2025_paper.html)
- [Data](https://huggingface.co/datasets/opendatalab/OHR-Bench)
- repository: [source](https://github.com/opendatalab/OHR-Bench#copyright-statement) — supports `access.license`, `use.caveats`
- dataset_card: [source](https://huggingface.co/datasets/opendatalab/OHR-Bench) — supports `access.license`
- paper: [source](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_OCR_Hinders_RAG_Evaluating_the_Cascading_Impact_of_OCR_on_ICCV_2025_paper.html) — supports `summary`, `data.size`
- repository: [source](https://github.com/opendatalab/OHR-Bench) — supports `data.description`, `ground_truth.description`, `evaluation.protocol`, `access.data`
- paper: [source](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_OCR_Hinders_RAG_Evaluating_the_Cascading_Impact_of_OCR_on_ICCV_2025_paper.pdf) — supports `evaluation.official_metrics`
- paper: [source](https://arxiv.org/html/2412.02592v4) — supports `evaluation.official_metrics`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
