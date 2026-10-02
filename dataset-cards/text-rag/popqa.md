<!-- Generated from catalog/datasets/popqa.yaml. Edit the YAML source. -->
# PopQA

[简体中文](popqa.zh-CN.md)

Entity-centric factual questions with answer aliases, Wikidata identities and Wikipedia popularity metadata.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_convertible` |
| Primary category | `text_rag` |
| Tasks | single_hop_qa, evidence_retrieval |
| Modalities | text |
| Gold annotation levels | answer |
| Evidence provenance | distant |
| Corpus / queries / answers | external / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Questions are constructed from entity relations; the release includes aliases and popularity metadata, while retrieval experiments use separately obtained passages or retrieval results.

Published scale: Approximately 14K QA pairs.
Splits: The author-hosted Hugging Face release has a test split; later training or long-tail subsets are separate experiment choices.

## Ground truth and evaluation

Wikidata relations and object aliases define acceptable answers; entity IDs and page-view counts do not annotate supporting text passages.

Official metrics: answer_accuracy.

Protocol: The original code marks a generation correct when it contains an accepted answer alias with supported case variants; this is not strict normalized exact match. Report any popularity filter and external corpus snapshot.

## When to use it

- Long-tail factual knowledge
- Adaptive retrieval versus parametric answering

## Limitations and cautions

- Popularity-filtered subsets are not the complete dataset
- No native passage relevance or supporting-span annotations are claimed

## Access and sources

- [Official resource](https://github.com/AlexTMallen/adaptive-retrieval)
- [Paper](https://aclanthology.org/2023.acl-long.546/)
- [Data](https://huggingface.co/datasets/akariasai/PopQA)
- repository: [source](https://github.com/AlexTMallen/adaptive-retrieval) — supports `summary`, `data.description`, `data.size`, `ground_truth.description`
- dataset_card: [source](https://huggingface.co/datasets/akariasai/PopQA) — supports `data.splits`, `ground_truth.alternatives`
- repository: [source](https://github.com/AlexTMallen/adaptive-retrieval/blob/main/run_model.py) — supports `evaluation.official_metrics`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
