<!-- Generated from catalog/datasets/timelyqabench.yaml. Edit the YAML source. -->
# TimelyQABench

[简体中文](timelyqabench.zh-CN.md)

Korean QA and document relevance for policies that retain almost identical wording across successive amendments.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-18 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | time_sensitive_qa, evidence_retrieval |
| Modalities | text |
| Gold annotation levels | document, answer |
| Evidence provenance | synthetic |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The TimelyRAG preprint releases four synthetic Korean QA domains with overlapping document versions and temporally invalid hard negatives. Query and document times constrain which version applies.

Published scale: Four domain releases have 3,000 QA records and 30,000 corpus documents each. Total: 12,000 QA records and 120,000 documents.
Splits: Four domain evaluation sets. Each query runs against its domain corpus.
Format: ZIP with domain JSONL files containing QA and documents linked by global IDs.

## Ground truth and evaluation

Gold IDs mark document versions supporting the answer under the query's temporal conditions. The JSONL stores insertion times. Event times are expressed in text rather than separate event-time fields.

Official metrics: nDCG@10, MAP@10, Recall@10, Hit@10, judged_win_tie_loss.

Protocol: Measure document ranking in each domain against released qrels. The paper uses GPT-5 pairwise judgments for correctness and temporal validity with the same generator on both sides. State which timestamps are available at retrieval time and reserve oracle filtering for an upper bound.

## When to use it

- Testing retrieval of the applicable version among near-duplicate policy documents
- Comparing semantic retrieval and time-aware reranking

## Limitations and cautions

- Policies and question pairs are synthetic
- The native protocol ranks a fixed versioned corpus and does not measure update propagation
- Document IDs do not specify clause-level evidence coordinates

## Access and sources

- [Official resource](https://github.com/kaist-dmlab/TimelyRAG)
- [Paper](https://arxiv.org/abs/2609.11572)
- [Data](https://github.com/kaist-dmlab/TimelyRAG/blob/5213a0c1743f23fd52a258005c3887aaf7e8cd0f/datasets.zip)
- paper: [source](https://arxiv.org/html/2609.11572) — supports `summary`, `classification`, `data.description`, `ground_truth`, `evaluation`, `use`
- repository: [source](https://github.com/kaist-dmlab/TimelyRAG/blob/5213a0c1743f23fd52a258005c3887aaf7e8cd0f/datasets.zip) — supports `data.size`, `data.splits`, `data.format`, `access.data`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
