<!-- Generated from catalog/datasets/bamboogle.yaml. Edit the YAML source. -->
# Bamboogle

[简体中文](bamboogle.zh-CN.md)

Handwritten two-hop questions designed to defeat direct search snippets while composing facts available in Wikipedia.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_convertible` |
| Primary category | `text_rag` |
| Tasks | multi_hop_qa |
| Modalities | text |
| Gold annotation levels | answer |
| Evidence provenance | human |
| Corpus / queries / answers | external / provided / provided |
| Original data license | MIT |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The author release contains question-answer pairs; Wikipedia and live search are external resources. It does not bundle a fixed retrieval collection or per-hop evidence annotations.

Published scale: 125 manually written two-hop questions.

## Ground truth and evaluation

Authors provide final answers to compositional questions. The fact that both hops can be found in Wikipedia does not supply annotated passage IDs, supporting sentences or reference reasoning traces.

Official metrics: exact_match.

Protocol: Extract and score the final answer, and record the search or corpus snapshot. The original evaluation uses the full small benchmark without tuning prompts on it; report later subsets separately.

## When to use it

- Iterative search and question decomposition
- Varied two-hop factual questions

## Limitations and cautions

- The small sample limits statistical precision
- Its original search-snippet failure condition is time-dependent

## Access and sources

- [Official resource](https://github.com/ofirpress/self-ask)
- [Paper](https://aclanthology.org/2023.findings-emnlp.378/)
- repository: [source](https://github.com/ofirpress/self-ask) — supports `data.description`
- repository: [source](https://github.com/ofirpress/self-ask/blob/main/datasets/bamboogle.md) — supports `access.license`
- paper: [source](https://aclanthology.org/2023.findings-emnlp.378.pdf) — supports `summary`, `data.size`, `ground_truth.description`, `evaluation.official_metrics`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
