<!-- Generated from catalog/datasets/musique.yaml. Edit the YAML source. -->
# MuSiQue

Multi-hop questions composed from single-hop sources to require connected reasoning.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | multi_hop_qa, evidence_retrieval |
| Modalities | text |
| Gold annotation levels | paragraph, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | CC BY 4.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

MuSiQue-Ans and MuSiQue-Full differ in answerability; train, dev and test are distributed in official format.


## Ground truth and evaluation

Question decomposition and paragraph support can be used to test full-chain retrieval.

Official metrics: answer_em, answer_f1, support_f1.

Protocol: Compare Ans and Full separately.

## When to use it

- Connected multi-hop reasoning
- Evidence completeness under a fixed context budget

## Limitations and cautions

- Seed single-hop questions can overlap other training data; consult released leakage IDs

## Access and sources

- [Official resource](https://github.com/StonyBrookNLP/musique)
- [Paper](https://aclanthology.org/2022.tacl-1.31/)
- repository: [source](https://github.com/StonyBrookNLP/musique) — supports `summary`, `data.description`, `access.license`, `use.caveats`, `evaluation.evaluator`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
