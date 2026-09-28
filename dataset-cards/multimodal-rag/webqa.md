<!-- Generated from catalog/datasets/webqa.yaml. Edit the YAML source. -->
# WebQA

Multimodal web QA requiring retrieval of relevant snippets and images before answer generation.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `multimodal_rag` |
| Tasks | multimodal_retrieval, multi_hop_qa, visual_qa |
| Modalities | text, image |
| Gold annotation levels | document, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The benchmark offers restricted and full retrieval settings over web snippets and images; question categories distinguish text- and image-based evidence.


## Ground truth and evaluation

Relevant source snippets/images support source-retrieval scoring and natural-language answer assessment; no universal within-image bbox gold is claimed.

Official metrics: source_retrieval_f1, answer_quality.

Protocol: Do not mix restricted and full retrieval scores; disclose availability of large pre-extracted image features.

## When to use it

- Joint web image-text retrieval
- Multimodal multi-hop answers

## Limitations and cautions

- Some hosted feature files require a request or may be unavailable
- Source IDs are coarser than image-region evidence

## Access and sources

- [Official resource](https://webqna.github.io/)
- [Paper](https://arxiv.org/abs/2109.00590)
- [Data](https://github.com/WebQnA/WebQA_Baseline)
- official: [source](https://webqna.github.io/) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.official_metrics`
- repository: [source](https://github.com/WebQnA/WebQA_Baseline) — supports `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
