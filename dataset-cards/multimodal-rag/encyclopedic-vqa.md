<!-- Generated from catalog/datasets/encyclopedic-vqa.yaml. Edit the YAML source. -->
# Encyclopedic-VQA (E-VQA)

[简体中文](encyclopedic-vqa.zh-CN.md)

Fine-grained visual knowledge QA with a controlled Wikipedia knowledge base and evidence-section identifiers.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_native` |
| Primary category | `multimodal_rag` |
| Tasks | visual_qa, multimodal_retrieval, multi_hop_qa |
| Modalities | text, image |
| Gold annotation levels | document, section, quote, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

CSV question/answer records link iNaturalist and Google Landmarks images to a released WikiWeb2M-derived knowledge-base JSON. Image pixels are acquired separately; Google Lens test retrieval outputs are also released.

Published scale: About 221,000 unique QA pairs and one million image-question-answer samples.
Splits: Train, validation and test, with question type and seen/unseen Wikipedia-entity indicators.
Format: QA CSV, knowledge-base JSON and separately sourced images..

## Ground truth and evaluation

Wikipedia URLs and evidence_section_id locate support, including two consecutive sources for two-hop questions. Evidence strings exist only for templated questions; not every item has a literal quote or visual-region annotation.

Official metrics: BEM_answer_accuracy.

Protocol: Use the released BEM evaluator and question-type handling, including multi-answer cases. Preserve Wikipedia URL keys and knowledge-base sections; do not equate later M2KR retrieval conversions with the original protocol.

## When to use it

- Image-conditioned retrieval of encyclopedia evidence
- Evaluating section grounding and multi-hop visual knowledge

## Limitations and cautions

- Knowledge-base and query image pixels require separate upstream downloads
- Quote support is limited to templated questions

## Access and sources

- [Official resource](https://github.com/google-research/google-research/tree/master/encyclopedic_vqa)
- [Paper](https://arxiv.org/abs/2306.09224)
- [Data](https://github.com/google-research/google-research/blob/master/encyclopedic_vqa/README.md)
- repository: [source](https://github.com/google-research/google-research/blob/master/encyclopedic_vqa/README.md) — supports `summary`, `data.description`, `data.size`, `data.splits`, `ground_truth.description`, `evaluation.official_metrics`, `evaluation.protocol`
- paper: [source](https://arxiv.org/abs/2306.09224) — supports `classification.rag_role`, `ground_truth.provenance`, `use.best_for`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
