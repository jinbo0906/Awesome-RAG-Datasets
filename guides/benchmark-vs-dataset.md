# Dataset, benchmark, suite, corpus and evaluator

These words overlap in paper titles, but they answer different questions. A **dataset** is a released collection of examples, labels or source assets. A **benchmark** is an evaluation contract: the task, allowed input and source pool, split, gold labels, metric, evaluator and comparison rules. A dataset becomes usable *as a benchmark* only when those decisions are specified. A paper may call both the data and the protocol by one name; this catalog records the data once and describes its native protocol in the same card. It does not create an extra object merely to repeat the name.

| Object | What must be specified | Example | Catalog location |
|---|---|---|---|
| Dataset | Examples, labels, source relationships, version and access | [RAGTruth](../dataset-cards/text-rag/ragtruth.md) has source/response pairs and hallucination spans | `catalog/datasets/` |
| Benchmark protocol | Task, input and permitted evidence, split, metric and evaluator | [RGB](../dataset-cards/text-rag/rgb.md) tests fixed-context robustness at chosen noise rate and passage count | `evaluation` on a dataset; suite `protocol` when shared |
| Suite | Multiple datasets or task variants under a shared comparison protocol | [BEIR](../suite-cards/beir.md) unifies retrieval evaluations; [ALCE](../suite-cards/alce.md) adapts three long-form QA datasets for citations | `catalog/suites/` |
| Corpus | Versioned source collection, which may support several benchmarks | [KILT Wikipedia](../catalog/corpora/kilt-wikipedia-2019.yaml) is a fixed source snapshot; podcast transcripts are a [GraphRAG corpus](../catalog/corpora/ms-graphrag-podcasts.yaml) | `catalog/corpora/` |
| Evaluator or framework | Software that calculates or organizes scores | [Ragas](https://docs.ragas.io/en/stable/concepts/metrics/overview/) offers metrics; it is not itself a fixed question corpus | Outside the dataset catalog |
| Paper | Publication introducing, reprocessing or evaluating an object | A retrieval paper may use a QA dataset without making it a native RAG dataset | `catalog/papers/` |

The distinction is operational. [MS MARCO Passage Ranking](../dataset-cards/text-rag/msmarco-passage.md) has a corpus, queries and sparse qrels, so it can benchmark a retriever, but its ranking variant has no generated-answer gold. It is an `auxiliary` RAG component, not an end-to-end answer benchmark. [ToTTo](../dataset-cards/table-rag/totto.md) supplies highlighted cells *as input* for generation; it does not test finding those cells. [MTRAG](../dataset-cards/text-rag/mtrag.md) includes corpora, retrieval tasks, dialogue answers and separate reference/full-RAG settings, allowing failure at retrieval and generation to be distinguished.

## Decision rule for new entries

1. Is there a canonical release with examples or source assets? If no, a method name alone is not a dataset.
2. Is there a fixed or explicitly time-indexed source pool, query and answer/evidence relation? If not, state what a RAG adaptation must build; do not call the original task end-to-end RAG.
3. Is the object a versioned bundle of component datasets and shared scoring? If yes, create a suite and link component *variants* only when those variants are documented. Do not equate an original dataset with a reprocessed suite subset.
4. Are labels on the **source** or on the **generated response**? `span` and `response_span` are different. An answer label alone cannot score evidence retrieval.
5. Does a different corpus, split, evaluator or exposure of gold context change what the system may see? If yes, report a separate benchmark setting or version; scores are not directly interchangeable.

The primary categories in the README classify source representation—text, multimodal, graph or table. QA, verification, retrieval, conversation and citation are **tasks**; medical, finance and legal are **domains**. These are orthogonal facets, not additional mutually exclusive top-level categories. See the [taxonomy](taxonomy.md) and [selection guide](selecting-a-benchmark.md) for how to use them.
