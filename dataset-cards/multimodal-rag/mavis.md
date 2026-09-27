<!-- Generated from catalog/datasets/mavis.yaml. Edit the YAML source. -->
# MAVIS

Visual-question benchmark for long answers with fact-level citations to multimodal documents.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `multimodal_rag` |
| Tasks | visual_qa, attribution, long_form_qa |
| Modalities | text, image |
| Evidence levels | document, fact_citation, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Input image and question are paired with multimodal retrieval corpus and cited long-form answers.

Published scale: 157K visual QA instances reported by the authors.

## Ground truth and evaluation

Fact-level answer citations reference supporting multimodal documents.

Official metrics: groundedness, completeness, relevance, fluency.

Protocol: Separate image-document groundedness from text-document groundedness.

## When to use it

- Fact-level multimodal citation
- Long-form grounded answer generation

## Limitations and cautions

- Document-level citations are not necessarily bbox-level evidence annotations

## Access and sources

- [Official resource](https://github.com/seokwon99/MAVIS)
- [Paper](https://ojs.aaai.org/index.php/AAAI/article/view/40585)
- [Data](https://huggingface.co/datasets/seokwon99/MAVIS)
- repository: [source](https://github.com/seokwon99/MAVIS) — supports `summary`, `data.description`, `evaluation.official_metrics`
- paper: [source](https://ojs.aaai.org/index.php/AAAI/article/view/40585) — supports `data.size`, `ground_truth.description`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
