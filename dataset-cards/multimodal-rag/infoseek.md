<!-- Generated from catalog/datasets/infoseek.yaml. Edit the YAML source. -->
# InfoSeek

[简体中文](infoseek.zh-CN.md)

Knowledge-intensive visual QA over OVEN images and Wikipedia-derived information.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_convertible` |
| Primary category | `multimodal_rag` |
| Tasks | visual_qa, multimodal_retrieval |
| Modalities | text, image |
| Gold annotation levels | answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The project releases image-linked questions, accepted answer aliases, KB mappings and a roughly six-million-entry Wikipedia text resource. Images derive from OVEN and must be acquired separately; the original QA and M2KR retrieval adaptation are distinct protocols.


## Ground truth and evaluation

Answers and equivalent forms are provided. Released mappings can support a retrieval adaptation, but a universal human-labeled minimal evidence page or image region is not claimed.

Official metrics: answer_accuracy.

Protocol: State the image, Wikipedia and question versions. For RAG experiments, disclose how the knowledge candidate pool and qrels are built; do not import M2KR's qrels as native InfoSeek gold.

## When to use it

- Knowledge-dependent visual questions
- Retrieval adaptation with external Wikipedia text

## Limitations and cautions

- Image acquisition has separate upstream dependencies
- Native QA does not guarantee question-specific visual-region evidence

## Access and sources

- [Official resource](https://github.com/open-vision-language/infoseek)
- [Paper](https://arxiv.org/abs/2302.11713)
- repository: [source](https://github.com/open-vision-language/infoseek) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
