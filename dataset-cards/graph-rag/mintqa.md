<!-- Generated from catalog/datasets/mintqa.yaml. Edit the YAML source. -->
# MINTQA

[简体中文](mintqa.zh-CN.md)

Wikidata-based multi-hop RAG QA separating new versus old and popular versus long-tail knowledge.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_native` |
| Primary category | `graph_rag` |
| Tasks | multi_hop_qa, graph_reasoning, time_sensitive_qa |
| Modalities | graph, text |
| Gold annotation levels | graph_path, answer |
| Evidence provenance | synthetic |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | MIT |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

POP and TI releases supply main/sub-questions, answers, hop labels, fact chains and facts; the author-linked MintQA-KG release provides the retrieval KB.

Published scale: MINTQA-POP has 17,887 questions; MINTQA-TI has 10,479 questions.
Splits: Two test subsets; report results by knowledge type and hop count.
Format: JSONL.

## Ground truth and evaluation

Question-generation chains and sub-answers are explicitly released; they are constructed from Wikidata facts and do not certify unique paths in the entire KB.

Official metrics: answer_containment_accuracy.

Protocol: The paper checks whether a gold answer occurs in lowercased predicted text. Separate parametric, direct retrieval and decomposition/retrieval settings; fix the KB version and linearization.

## When to use it

- Decomposition and retrieval decisions across knowledge familiarity
- Multi-hop fact-chain retrieval

## Limitations and cautions

- Newness is defined by dated Wikidata snapshots rather than today's freshness
- Dataset files are released but the repository says full project code is still being organized

## Access and sources

- [Official resource](https://github.com/probe2/multi-hop)
- [Paper](https://aclanthology.org/2026.acl-long.18/)
- [Data](https://huggingface.co/datasets/probejie/MINTQA)
- repository: [source](https://github.com/probe2/multi-hop) — supports `data`, `ground_truth.levels`, `use.caveats`
- dataset_card: [source](https://huggingface.co/Sp1der/MintQA-KG/tree/main) — supports `data.corpus`, `data.description`
- paper: [source](https://arxiv.org/html/2412.17032v3) — supports `summary`, `classification`, `ground_truth`, `evaluation`, `access.license`, `use`
- paper: [source](https://aclanthology.org/2026.acl-long.18.pdf) — supports `evaluation`, `access.license`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
