<!-- Generated from catalog/datasets/quality.yaml. Edit the YAML source. -->
# QuALITY

Multiple-choice long-document comprehension over articles and stories.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_convertible` |
| Primary category | `text_rag` |
| Tasks | long_context_qa |
| Modalities | text |
| Evidence levels | document, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | article-specific terms |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Examples contain an article, four answer options, a gold label and annotation metadata; a harder subset is identified by timed human performance.


## Ground truth and evaluation

Gold answer labels are human-validated; the native release does not provide a minimal supporting span for every question.

Official metrics: accuracy, hard_subset_accuracy.

Protocol: Report full and difficult subsets separately; constructing retrieval chunks is an adaptation.

## When to use it

- Long-context reasoning with retrieval adaptation

## Limitations and cautions

- QuALITY means long-input QA; it is not a product-quality dataset
- No native evidence-span gold

## Access and sources

- [Official resource](https://github.com/nyu-mll/quality)
- [Paper](https://aclanthology.org/2022.naacl-main.391/)
- repository: [source](https://github.com/nyu-mll/quality) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.official_metrics`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
