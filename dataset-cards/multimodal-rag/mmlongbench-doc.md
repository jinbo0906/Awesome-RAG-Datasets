<!-- Generated from catalog/datasets/mmlongbench-doc.yaml. Edit the YAML source. -->
# MMLongBench-Doc

Long PDF document QA with evidence-page and modality-source annotations.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_convertible` |
| Primary category | `multimodal_rag` |
| Tasks | long_context_qa, page_retrieval, visual_qa |
| Modalities | text, image, table, chart, layout |
| Evidence levels | page, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The repository releases PDF documents and QA records containing doc_id, question, answer, evidence_pages and evidence_sources; the 2025 release revised some QAs.


## Ground truth and evaluation

Evidence pages and modality-source labels locate support, but no universal question-specific region/cell coordinates are supplied.

Official metrics: answer_f1.

Protocol: State dataset revision and whether document pages are retrieved or all supplied to the model.

## When to use it

- Long visual document context
- Cross-page evidence collection

## Limitations and cautions

- Original evaluation is long-context VQA; a page-retrieval protocol is an adaptation
- QA revisions require version pinning

## Access and sources

- [Official resource](https://github.com/mayubo2333/MMLongBench-Doc)
- repository: [source](https://github.com/mayubo2333/MMLongBench-Doc) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
