<!-- Generated from catalog/datasets/m3docvqa.yaml. Edit the YAML source. -->
# M3DocVQA

Open-domain visual document QA over a multi-page multi-document PDF collection.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `multimodal_rag` |
| Tasks | page_retrieval, visual_qa |
| Modalities | text, image, table, chart |
| Evidence levels | page, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The M3DocRAG project releases an open-domain collection exceeding 3,000 PDFs and 40,000 pages.


## Ground truth and evaluation

Relevance is evaluated at document or page level before visual answer generation.

Official metrics: retrieval_recall, answer_accuracy.

Protocol: Preserve PDF identity and page numbers; do not conflate closed-domain MP-DocVQA with open-domain M3DocVQA.

## When to use it

- Open-domain multi-page retrieval
- Visual evidence missed by OCR

## Limitations and cautions

- The source repository was archived in July 2026; record the exact snapshot used

## Access and sources

- [Official resource](https://github.com/bloomberg/m3docrag)
- [Paper](https://arxiv.org/abs/2411.04952)
- repository: [source](https://github.com/bloomberg/m3docrag) — supports `summary`, `data.description`, `ground_truth.description`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
