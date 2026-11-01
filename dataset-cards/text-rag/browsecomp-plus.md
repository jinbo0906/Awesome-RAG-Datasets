<!-- Generated from catalog/datasets/browsecomp-plus.yaml. Edit the YAML source. -->
# BrowseComp-Plus

[简体中文](browsecomp-plus.zh-CN.md)

Fixed-corpus deep-search evaluation separating retrieval quality, evidence collection, answer correctness and search effort.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | agentic_search, multi_hop_qa, evidence_retrieval |
| Modalities | text |
| Gold annotation levels | document, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | MIT for the official Hugging Face release; original web-source terms may also apply. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

An independently released BrowseComp adaptation adds a frozen web corpus, human-verified evidence documents, answer-bearing gold documents and mined hard negatives. Query and judgment fields are obfuscated; the official repository supplies de-obfuscation and retrieval/agent evaluation tools.

Published scale: 830 test queries and 100,195 corpus documents in the official Hugging Face release.
Splits: Query/judgment test split; the separate corpus repository uses a split called train, which is the retrieval pool rather than agent training supervision.
Format: Hugging Face Parquet and author-provided JSONL/TSV conversion..

## Ground truth and evaluation

evidence_docs support the reasoning chain; gold_docs semantically contain the final answer. Model-assisted collection is followed by human verification. These two judgment sets are not interchangeable, and document relevance does not specify optimal chunk cuts.

Official metrics: accuracy, evidence_recall, search_calls, calibration_error, Recall@5, Recall@100, Recall@1000, nDCG@10.

Protocol: Keep the fixed corpus and designated evidence/gold qrels. Report agent answer accuracy, evidence-document coverage across calls, calls and calibration separately from retriever-only metrics. The project uses GPT-4.1 for answer judging; pin grader, search interface and budgets rather than mixing live-web BrowseComp scores.

## When to use it

- Disentangling retriever and agent contributions
- Comparing iterative evidence acquisition with single-pass retrieval

## Limitations and cautions

- Derived from only part of BrowseComp; scores are not native BrowseComp scores
- Obfuscation discourages leakage but is not access control; never expose benchmark labels to the evaluated agent
- Relevant documents are coarser than minimal complete evidence spans or unique reasoning paths

## Access and sources

- [Official resource](https://texttron.github.io/BrowseComp-Plus/)
- [Paper](https://aclanthology.org/2026.acl-long.1023/)
- [Data](https://huggingface.co/datasets/Tevatron/browsecomp-plus)
- paper: [source](https://aclanthology.org/2026.acl-long.1023/) — supports `name`, `summary`, `classification.rag_role`, `use.caveats`
- dataset_card: [source](https://huggingface.co/datasets/Tevatron/browsecomp-plus) — supports `data.description`, `data.size`, `data.splits`, `data.format`, `ground_truth.description`, `ground_truth.provenance`, `access.license`
- official: [source](https://texttron.github.io/BrowseComp-Plus/) — supports `evaluation.official_metrics`, `evaluation.protocol`, `ground_truth.description`
- repository: [source](https://github.com/texttron/BrowseComp-Plus) — supports `data.description`, `data.splits`, `evaluation.protocol`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
