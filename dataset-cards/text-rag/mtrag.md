<!-- Generated from catalog/datasets/mtrag.yaml. Edit the YAML source. -->
# MTRAG (human)

[简体中文](mtrag.zh-CN.md)

Human-authored multi-turn RAG conversations with retrieval and generation tasks over four corpora.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | conversational_qa, evidence_retrieval |
| Modalities | text |
| Gold annotation levels | paragraph, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The human release contains 110 reviewed conversations averaging 7.7 turns and 842 turn-level evaluation tasks. ClapNQ, Cloud, FiQA and Govt corpora are separate; synthetic MTRAG and MTRAG-UN are different releases, not part of this record.


## Ground truth and evaluation

The conversations include reference passages, passage relevance and responses. Retrieval tasks are provided in BEIR format for answerable and partial turns; unanswerable turns require a distinct evaluation treatment.

Official metrics: not confirmed.

Protocol: Keep conversation history, domain and turn order intact. Compare reference, reference+RAG and full-RAG settings separately; only the last setting lets retrieval misses affect generation.

## When to use it

- Follow-up and underspecified queries
- Retrieval errors across dialogue turns
- Multi-domain RAG

## Limitations and cautions

- Do not count 842 turn-level tasks as 842 independent conversations
- Synthetic and UN variants have distinct provenance and protocols

## Access and sources

- [Official resource](https://github.com/IBM/mt-rag-benchmark)
- [Paper](https://arxiv.org/abs/2501.03468)
- repository: [source](https://github.com/IBM/mt-rag-benchmark) — supports `summary`, `data.description`, `ground_truth.description`
- repository: [source](https://github.com/IBM/mt-rag-benchmark/blob/main/mtrag-human/README.md) — supports `data.description`, `evaluation.protocol`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
