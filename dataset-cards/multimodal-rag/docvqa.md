<!-- Generated from catalog/datasets/docvqa.yaml. Edit the YAML source. -->
# DocVQA (single-page)

[简体中文](docvqa.zh-CN.md)

Human-written extractive questions over individual scanned industry-document images.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_convertible` |
| Primary category | `multimodal_rag` |
| Tasks | visual_qa, page_retrieval |
| Modalities | text, image, layout |
| Gold annotation levels | answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The original task supplies one document image per question, with OCR and human answers. VDocRAG reuses a filtered subset for open-domain training; its OpenDocVQA protocol is a separate adaptation.

Published scale: About 50,000 questions over 12,767 document images.
Splits: Original train, validation and held-out test; test evaluation uses the challenge platform.
Format: Document images, question/answer JSON and OCR..

## Ground truth and evaluation

Answers are text spans in the supplied image, but answer strings are not universal gold OCR-span coordinates or corpus-wide retrieval qrels. The paired image can seed an explicitly defined page-retrieval adaptation.

Official metrics: ANLS.

Protocol: Preserve the original split and answer aliases. Report any pooling, query filtering and new qrels separately; single-page DocVQA, MP-DocVQA and OpenDocVQA are distinct settings.

## When to use it

- Visual document reading baselines
- Explicit page-pool retrieval adaptations

## Limitations and cautions

- Original questions assume the relevant image is supplied
- Challenge access and test-label availability differ from derivative mirrors

## Access and sources

- [Official resource](https://site.docvqa.org/datasets/docvqa)
- [Paper](https://openaccess.thecvf.com/content/WACV2021/papers/Mathew_DocVQA_A_Dataset_for_VQA_on_Document_Images_WACV_2021_paper.pdf)
- [Data](https://rrc.cvc.uab.es/?ch=17&com=downloads)
- official: [source](https://site.docvqa.org/datasets/docvqa) — supports `summary`, `data.description`, `data.size`, `access.data`, `access.gated`
- paper: [source](https://openaccess.thecvf.com/content/WACV2021/papers/Mathew_DocVQA_A_Dataset_for_VQA_on_Document_Images_WACV_2021_paper.pdf) — supports `ground_truth.description`, `evaluation.official_metrics`, `data.splits`
- paper: [source](https://arxiv.org/html/2504.09795) — supports `data.description`, `evaluation.protocol`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
