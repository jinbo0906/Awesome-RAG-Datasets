<!-- Generated from catalog/datasets/raguard.yaml. Edit the YAML source. -->
# RAGuard

[简体中文](raguard.zh-CN.md)

Political fact-checking benchmark testing RAG against naturally misleading Reddit retrievals.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | fact_verification, rag_robustness |
| Modalities | text |
| Gold annotation levels | document, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | MIT |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Separate claims and documents CSVs contain binary verdicts, document IDs, Reddit text and supporting/misleading/unrelated labels.

Published scale: 2,648 claims and 16,331 documents.
Format: CSV.

## Ground truth and evaluation

Verdicts derive from PolitiFact; document labels describe their effect on an annotating LLM, not universally true or false passages or minimal evidence.

Official metrics: accuracy.

Protocol: Compare zero-context, full-corpus RAG and oracle associated-document settings; distinguish RAG-1/RAG-5 and oracle-all/oracle-misleading. Invalid class outputs count as errors.

## When to use it

- Robustness to misleading real-world retrievals
- Retrieval versus zero-context fact-checking

## Limitations and cautions

- Misleadingness is relative to model behavior and the political domain
- Load the two CSVs separately; the default Hugging Face viewer reports incompatible columns

## Access and sources

- [Official resource](https://huggingface.co/datasets/UCSC-IRKM/RAGuard)
- [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ed25c00ff6900989116d3ba5d607d33d-Abstract-Datasets_and_Benchmarks_Track.html)
- [Data](https://huggingface.co/datasets/UCSC-IRKM/RAGuard/tree/main)
- dataset_card: [source](https://huggingface.co/datasets/UCSC-IRKM/RAGuard) — supports `data.description`, `data.format`, `access.license`, `use.caveats`
- paper: [source](https://arxiv.org/html/2502.16101v5) — supports `summary`, `classification`, `data.size`, `ground_truth`, `evaluation`, `use.best_for`
- paper: [source](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ed25c00ff6900989116d3ba5d607d33d-Abstract-Datasets_and_Benchmarks_Track.html) — supports `access.paper`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
