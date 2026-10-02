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

## Recent-paper extensions

[ComplexWebQuestions](../../dataset-cards/graph-rag/complexwebquestions.md) and [KQA Pro](../../dataset-cards/graph-rag/kqa-pro.md) extend existing-KB semantic parsing and compositional reasoning coverage. [OpenDialKG](../../dataset-cards/graph-rag/opendialkg.md) supplies participant-selected conversational graph paths; these paths are supervision for dialogue transitions, not unique proof graphs for every response. [MINTQA](../../dataset-cards/graph-rag/mintqa.md) adds new and long-tail knowledge, subquestions and linked KG resources; generated fact chains and answer containment must be assessed separately.

The [paper index](../recent-paper-index.md) links ACL 2025 KG-Agent's exact datasets and ICML 2025 HippoRAG 2's text-QA conversion. [mmRAG](../../dataset-cards/text-rag/mmrag.md) tests routing/retrieval over serialized graph, table and text records; its fixed-chunk qrels do not become native graph-path gold.
