<!-- Generated from catalog/datasets/narrativeqa.yaml. Edit the YAML source. -->
# NarrativeQA

Questions over books and screenplays with human answers and document-level links.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_convertible` |
| Primary category | `text_rag` |
| Tasks | long_context_qa, summarization |
| Modalities | text |
| Gold annotation levels | document, answer |
| Evidence provenance | human |
| Corpus / queries / answers | external / provided / provided |
| Original data license | Apache-2.0 repository; source stories have separate terms |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The release includes question-answer pairs, document metadata, Wikipedia summaries and links or download scripts for full stories.


## Ground truth and evaluation

Questions have reference answers but no native sentence-level supporting-fact map.

Official metrics: rouge_l, bleu, meteor.

Protocol: Disclose summary-versus-full-story setting and the exact story snapshot used.

## When to use it

- Long-document retrieval stress tests
- Story-level answer generation

## Limitations and cautions

- Not a native chunk-boundary gold standard
- Full story availability depends on source URLs and rights

## Access and sources

- [Official resource](https://github.com/google-deepmind/narrativeqa)
- [Paper](https://arxiv.org/abs/1712.07040)
- repository: [source](https://github.com/google-deepmind/narrativeqa) — supports `summary`, `data.description`, `ground_truth.description`, `access.license`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
