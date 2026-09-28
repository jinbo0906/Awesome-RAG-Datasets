<!-- Generated from catalog/datasets/metaqa.yaml. Edit the YAML source. -->
# MetaQA

Movie-domain knowledge-base QA with one-, two- and three-hop question variants.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_convertible` |
| Primary category | `graph_rag` |
| Tasks | graph_qa, graph_reasoning |
| Modalities | text, graph, audio |
| Gold annotation levels | answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The official release provides a movie knowledge base as subject-relation-object triples, question-answer splits by hop count, paraphrased question variants and optional audio questions. The graph QA track should be reported separately from the audio variant.


## Ground truth and evaluation

Answer entities are released; the KB and question templates expose intended hop complexity. Do not assume that every item supplies a unique annotated graph path or a cited text passage.

Official metrics: answer_accuracy.

Protocol: Fix the KB release, hop count and vanilla/paraphrased/audio variant. For a GraphRAG path task, add independently checked path or subgraph labels rather than deriving gold from a tested retriever.

## When to use it

- Controlled graph-hop reasoning
- KB-backed retriever ablations

## Limitations and cautions

- Template-derived questions differ from open-ended GraphRAG tasks
- Native release does not guarantee gold citation paths

## Access and sources

- [Official resource](https://github.com/yuyuz/MetaQA)
- repository: [source](https://github.com/yuyuz/MetaQA) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
