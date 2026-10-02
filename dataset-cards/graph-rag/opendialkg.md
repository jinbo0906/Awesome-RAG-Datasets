<!-- Generated from catalog/datasets/opendialkg.yaml. Edit the YAML source. -->
# OpenDialKG

[简体中文](opendialkg.zh-CN.md)

Human conversations paired with participant-annotated knowledge-graph walks and a released base graph.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_convertible` |
| Primary category | `graph_rag` |
| Tasks | conversational_qa, graph_reasoning |
| Modalities | graph, text |
| Gold annotation levels | graph_path, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | CC BY-NC 4.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The release includes dialogue CSV and entity/relation/triple files; dialogue contexts can serve as queries and subsequent utterances as responses.

Published scale: 13,802 sessions and 91,209 turns; base KG has 100,813 entities and 1,190,658 bidirectional triples.
Format: CSV with JSON actions and tab-separated KG triples.

## Ground truth and evaluation

Participants select paths connecting concepts across adjacent turns; intermediate entities need not appear in text, and paths are not unique factual-answer evidence sets.

Official metrics: entity_recall_at_k, human_response_preference.

Protocol: The original paper evaluates predicted response entities at k=1/3/5/10/25 and human naturalness preferences. Preserve in-domain versus cross-domain settings.

## When to use it

- Conversational graph walks with explicit supervision
- Graph reasoning across dialogue domains

## Limitations and cautions

- Entity prediction metrics are not full answer factuality or citation metrics
- The official repository is archived and does not provide a universal modern GraphRAG evaluator

## Access and sources

- [Official resource](https://github.com/facebookresearch/opendialkg)
- [Paper](https://aclanthology.org/P19-1081/)
- [Data](https://github.com/facebookresearch/opendialkg/tree/main/data)
- repository: [source](https://github.com/facebookresearch/opendialkg) — supports `summary`, `classification`, `data`, `ground_truth`, `access.license`, `use`
- paper: [source](https://aclanthology.org/P19-1081.pdf) — supports `evaluation`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
