<!-- Generated from catalog/datasets/confrag.yaml. Edit the YAML source. -->
# ConfRAG

[简体中文](confrag.zh-CN.md)

Contradiction-aware QA benchmark requiring coverage of distinct viewpoints in supplied web references.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | long_form_qa, rag_robustness, attribution |
| Modalities | text |
| Gold annotation levels | document, fact_citation, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | HF card: CC BY 4.0; repository says dataset research use only and original web licenses apply |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Records contain web-page contents and URLs, contradiction flags, answer clusters and supporting reasons with website indices; the recommended release improves annotations.

Published scale: 1,814 questions; 57.2% exhibit contradictions according to the paper.
Format: JSONL.

## Ground truth and evaluation

LLM extraction and human review produce viewpoint clusters, reasons and website indices. These references are not exact sentence offsets or guarantees that a viewpoint is objectively true.

Official metrics: normalized_mutual_information, answer_coverage, reason_coverage, valid_partition_rate.

Protocol: Freeze the released page contexts and annotation version. Structured outputs are scored for clustering and keyword-based answer/reason matching; report validity separately.

## When to use it

- Contradictory multi-source answer synthesis
- Viewpoint and reason coverage

## Limitations and cautions

- Supplied web references test reasoning after retrieval; open-corpus retrieval needs its own protocol
- License statements differ between the dataset card and repository; resolve the applicable terms before use

## Access and sources

- [Official resource](https://github.com/XaiverYuan/ConfRAG)
- [Paper](https://aclanthology.org/2026.acl-long.11/)
- [Data](https://huggingface.co/datasets/OracleY/ConfRAG)
- dataset_card: [source](https://huggingface.co/datasets/OracleY/ConfRAG) — supports `summary`, `classification`, `data`, `ground_truth`, `evaluation.official_metrics`, `evaluation.protocol`, `access.license`, `use`
- repository: [source](https://github.com/XaiverYuan/ConfRAG) — supports `evaluation.evaluator`, `access.license`, `use.caveats`
- paper: [source](https://aclanthology.org/2026.acl-long.11.pdf) — supports `data.size`, `evaluation.official_metrics`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
