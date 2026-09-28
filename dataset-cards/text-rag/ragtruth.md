<!-- Generated from catalog/datasets/ragtruth.yaml. Edit the YAML source. -->
# RAGTruth

[简体中文](ragtruth.zh-CN.md)

Human-annotated response-side hallucination spans over several RAG-style generation tasks.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `auxiliary` |
| Primary category | `text_rag` |
| Tasks | hallucination_detection, attribution |
| Modalities | text |
| Gold annotation levels | response_span |
| Evidence provenance | human |
| Corpus / queries / answers | not_provided / provided / not_provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The release pairs source_info.jsonl with response.jsonl; each source elicits six model responses. The official repository reports 17,790 generated responses across QA, summarization and data-to-text. A generated response is a model output, not a gold answer.

Format: JSONL.

## Ground truth and evaluation

Annotators mark start/end offsets of unsupported spans in model responses, with label type and metadata. These response offsets are not source-evidence coordinates or retrieval qrels.

Official metrics: not confirmed.

Protocol: Join responses to source_info by source_id, preserve train/test split and annotation version, and score hallucination detection separately from answer correctness or retrieval.

## When to use it

- Token- or span-level hallucination detection
- Diagnosing unsupported claims

## Limitations and cautions

- Not an end-to-end retrieval benchmark
- Does not supply a human gold answer for every generated response

## Access and sources

- [Official resource](https://github.com/ParticleMedia/RAGTruth)
- [Paper](https://arxiv.org/abs/2401.00396)
- repository: [source](https://github.com/ParticleMedia/RAGTruth) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
