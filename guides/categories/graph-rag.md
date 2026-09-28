# Graph RAG: graph structure is not graph truth

[简体中文](graph-rag.zh-CN.md)

The [Graph RAG catalog section](../../README.md#graph-rag) deliberately keeps two settings apart. GraphRAG systems may *construct* a graph from prose and retrieve graph-linked context. Knowledge-base QA systems query an existing structured graph. Both are useful, but their gold annotations and failure modes differ.

| Setting | Inspect | Main caution |
|---|---|---|
| Graph construction plus RAG generation | [GraphRAG-Bench](../../dataset-cards/graph-rag/graphrag-bench.md) | A system-built edge is not an independently annotated gold evidence path |
| Existing KB reasoning | [GrailQA](../../dataset-cards/graph-rag/grailqa.md), [WebQuestionsSP](../../dataset-cards/graph-rag/webqsp.md), [MetaQA](../../dataset-cards/graph-rag/metaqa.md) | Logical forms, hop counts and answers do not automatically become citation subgraphs |
| Long-source global summarization | [Microsoft GraphRAG podcast corpus](../../catalog/corpora/ms-graphrag-podcasts.yaml) | Corpus and open-ended queries need an explicit answer/evidence evaluator |

For a GraphRAG benchmark, pin original source documents, graph-construction method/version, entity resolution, edge provenance, retrieval budget and answer evaluator. Report graph construction cost, source-node recall, path/edge correctness *when gold exists*, answer quality and citation validity separately. A model should not receive credit merely because its own generated graph agrees with itself. Multi-hop text QA can be a useful transfer test, but calling the original HotpotQA or MuSiQue release “native GraphRAG” would change their task identity.

The category is intentionally smaller than the number of papers that use graphs: methods, source corpora and benchmark datasets are different entities. See [dataset versus benchmark](../benchmark-vs-dataset.md) for the inclusion decision.
