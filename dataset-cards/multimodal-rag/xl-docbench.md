<!-- Generated from catalog/datasets/xl-docbench.yaml. Edit the YAML source. -->
# XL-DocBench

Expert-verified QA over extra-long documents with evidence pages and snippets.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `multimodal_rag` |
| Tasks | long_context_qa, page_retrieval, evidence_retrieval |
| Modalities | text, image, table, layout |
| Gold annotation levels | page, quote, answer |
| Evidence provenance | human |
| Corpus / queries / answers | external / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The release references public source document URLs rather than bundling every PDF; it includes single- and cross-document QA.

Published scale: 1,519 questions: 1,354 single-document and 165 cross-document; 331 document records.

## Ground truth and evaluation

Answerable cases include human evidence pages and evidence snippets with source locators.

Official metrics: answer_accuracy, evidence_retrieval.

Protocol: Materialize versioned source PDFs before comparing parsers or chunkers.

## When to use it

- Very long document retrieval
- Cross-document evidence localization

## Limitations and cautions

- External document URLs can drift; a reproducible snapshot and hashes are necessary

## Access and sources

- [Official resource](https://officeintelligence.github.io/xl-docbench/)
- [Data](https://huggingface.co/datasets/anonymous12123/XL-DocBench)
- dataset_card: [source](https://huggingface.co/datasets/anonymous12123/XL-DocBench) — supports `data.description`, `data.size`, `ground_truth.description`
- official: [source](https://officeintelligence.github.io/xl-docbench/) — supports `summary`, `use.best_for`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
