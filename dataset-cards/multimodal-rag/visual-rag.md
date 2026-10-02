<!-- Generated from catalog/datasets/visual-rag.yaml. Edit the YAML source. -->
# Visual-RAG

[简体中文](visual-rag.zh-CN.md)

Fine-grained natural-organism questions with human-verified clue-image relevance for text-to-image RAG.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_native` |
| Primary category | `multimodal_rag` |
| Tasks | visual_qa, multimodal_retrieval |
| Modalities | text, image |
| Gold annotation levels | document, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | external / provided / provided |
| Original data license | CC-BY-NC-4.0 for annotations; iNaturalist images retain individual upstream licenses. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The official v2 JSONL provides text questions, answer variants, scientific names and per-image binary clue labels. Images are acquired from iNaturalist 2021; the native evaluation searches a species-specific subset.

Published scale: 374 questions in corrected v2 annotations; native per-query pools contain about 200–300 species images.
Splits: Evaluation annotations; no native training split.
Format: v2_anno.jsonl and upstream iNaturalist image files..

## Ground truth and evaluation

Model-proposed questions and image labels undergo human verification. Released binary labels identify clue images and accepted answers; there is no uniform within-image evidence box.

Official metrics: Recall@k, nDCG@k, Hit@k, Hit_Count@k, LLM_judged_answer_accuracy, ROUGE, gCUE.

Protocol: Use corrected v2 labels and the documented species-specific corpus. Separate no-image, gold-clue, non-clue, top-k RAG and one-in-k settings; pin judge model and distinguish ACL 2026 gold-injected selection pools.

## When to use it

- Text-to-image retrieval of fine-grained visual clues
- Isolating clue utilization from retrieval failure

## Limitations and cautions

- v1 contained invalid questions and image labels that were corrected in v2
- Images are not redistributed and the native pool is narrower than the full iNaturalist corpus

## Access and sources

- [Official resource](https://github.com/visual-rag/visual-rag)
- [Paper](https://arxiv.org/abs/2502.16636)
- [Data](https://github.com/visual-rag/visual-rag/blob/main/v2_anno.jsonl)
- repository: [source](https://github.com/visual-rag/visual-rag) — supports `summary`, `data.description`, `data.size`, `data.format`, `ground_truth.description`, `use.caveats`
- paper: [source](https://arxiv.org/html/2502.16636) — supports `ground_truth.provenance`, `evaluation.official_metrics`, `evaluation.protocol`, `data.splits`, `access.license`
- paper: [source](https://aclanthology.org/2026.acl-long.1620/) — supports `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
