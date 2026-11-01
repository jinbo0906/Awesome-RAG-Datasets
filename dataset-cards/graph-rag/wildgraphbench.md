<!-- Generated from catalog/datasets/wildgraphbench.yaml. Edit the YAML source. -->
# WildGraphBench

[简体中文](wildgraphbench.zh-CN.md)

GraphRAG evaluation over long external references, separating single-fact QA, multi-fact aggregation and statement-level summarization.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `rag_native` |
| Primary category | `graph_rag` |
| Tasks | single_hop_qa, multi_hop_qa, summarization |
| Modalities | text, graph |
| Gold annotation levels | document, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | Apache-2.0 for the released benchmark; third-party reference documents retain their original rights. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Findings ACL 2026 benchmark built from Wikipedia articles and their heterogeneous external references. Index reference_pages rather than the Wikipedia article used to construct gold. Questions, reference URLs, source texts and summary statements are released by topic.

Published scale: Current repository/HF release has 1,197 questions (667 single-fact, 191 multi-fact, 339 summary) across 12 topics; the paper abstract reports 1,100. These versions must not be silently equated.
Splits: Twelve topic-named HF splits are evaluation partitions, not twelve independent train/test tasks.
Format: Question JSONL, source text files and reference metadata; optional statement files..

## Ground truth and evaluation

Wikipedia citation-linked statements seed model-assisted QA and summary construction. ref_urls supplies question-level source references and gold_statements supplies summary targets; neither guarantees per-fact minimal source spans or gold graph edges.

Official metrics: single_fact_accuracy, multi_fact_accuracy, statement_precision, statement_recall, statement_f1.

Protocol: Paper sections 3.5/4.1 separate LLM-judged QA accuracy from summary statement matching; the default judge is gpt-5-mini. Hold construction/answer models and retrieval budgets constant; the reported 1,200-token chunks with 100-token overlap are baseline settings, not gold chunk boundaries. Never index the gold Wikipedia summary article as retrieval evidence.

## When to use it

- Testing evidence aggregation beyond short curated passages
- Comparing fine-detail retention and global summarization in GraphRAG

## Limitations and cautions

- Current release and paper abstract have different question counts
- Constructed graph edges are not independent gold paths
- Reference URLs and model-judged statement matches do not certify source-coordinate evidence completeness

## Access and sources

- [Official resource](https://github.com/BstWPY/WildGraphBench)
- [Paper](https://aclanthology.org/2026.findings-acl.679/)
- [Data](https://huggingface.co/datasets/Bstwpy/WildGraphBench)
- paper: [source](https://aclanthology.org/2026.findings-acl.679/) — supports `summary`, `data.description`, `data.size`
- dataset_card: [source](https://huggingface.co/datasets/Bstwpy/WildGraphBench) — supports `data.size`, `data.splits`, `data.format`, `access.license`, `ground_truth.description`
- repository: [source](https://github.com/BstWPY/WildGraphBench) — supports `data.description`, `evaluation.protocol`, `data.size`
- paper: [source](https://arxiv.org/html/2602.02053) — supports `ground_truth.provenance`, `evaluation.official_metrics`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
