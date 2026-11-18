<!-- Generated from catalog/suites/ragperf.yaml. Edit the YAML source. -->
# RAGPerf

[简体中文](ragperf.zh-CN.md)

System benchmark for RAG throughput, latency, resource use and answer quality, with a checked public static text protocol and a separate paper-only mixed-update experiment.

Review status: `source_checked`. This is a benchmark suite or protocol, not one standalone dataset.

## Indexed components

Component-level dataset cards have not yet been indexed. Use the official resource for the full list; this empty list does not mean the suite has no components.

## Protocol and interpretation

**Public static text workload.** Pin the linked author revision. Build the Linux C++20 monitoring extension and install the Python, vector database and model dependencies documented upstream. Use `python3 src/run_new.py --config config/lance_insert.yaml --msys-config config/monitor/example_config.yaml` for ingestion and index building, then switch `--config` to `config/lance_query.yaml` for retrieval and generation. Both configs need local database paths. The insert config expects a precomputed embedding pickle at an author-local path. To build your own input, enable embedding, disable embedding loading and keep the same encoder for ingestion and queries.

The text loader uses Wikimedia Wikipedia `20231101.en` and the query loader reads the first 512 queries and answers by default from `sentence-transformers/natural-questions` `train`. These external assets have their own terms. This is the public workload preset, with no separately indexed component variant or single fixed QA download. Pin the data revisions, sample size, models, index, hardware, batch size and query concurrency. Measure throughput, end-to-end and stage latency, and CPU/GPU and memory use. Text quality evaluation is off by default. If enabled, the public vLLM evaluator uses Ragas `LLMContextRecall`, `FactualCorrectness` and `AnswerAccuracy`. Record its settings and version separately from the paper's quality measures and from qrels-based recall. The author code is Apache-2.0. This catalog checked the entry point, configs and data sources without running the GPU pipeline.

**Concurrent updates in the paper.** Section 5.5 and Fig. 9 use LanceDB IVF-HNSW and Qwen-7B for 60 minutes with 50% queries and 50% document updates. The experiment varies uniform versus Zipfian access and a temporary flat index, and reports query latency, context recall and accuracy over time. The reviewed public revision supplies separate ingestion/query configs. The exact mixed workload configuration, versioned update QA and replay trace or equivalent generator remain unconfirmed. A custom update replay requires its own trace, labels and reporting. See the [selection guide](../guides/selecting-a-benchmark.md#evidence-and-update-protocols).

## Official sources

- [Official resource](https://github.com/platformxlab/RAGPerf/tree/49c9794895666d029a3c98a48afd872197d83b23)
- [Paper](https://www.vldb.org/pvldb/vol19/p3689-li.pdf)
- paper: [source](https://www.vldb.org/pvldb/vol19/p3689-li.pdf) — supports `name`, `summary`, `protocol`
- repository: [source](https://github.com/platformxlab/RAGPerf/blob/49c9794895666d029a3c98a48afd872197d83b23/src/run_new.py) — supports `protocol`
- repository: [source](https://github.com/platformxlab/RAGPerf/blob/49c9794895666d029a3c98a48afd872197d83b23/config/lance_insert.yaml) — supports `protocol`
- repository: [source](https://github.com/platformxlab/RAGPerf/blob/49c9794895666d029a3c98a48afd872197d83b23/config/lance_query.yaml) — supports `protocol`
- repository: [source](https://github.com/platformxlab/RAGPerf/blob/49c9794895666d029a3c98a48afd872197d83b23/src/datasetLoader/TextDatasetLoader.py) — supports `protocol`
- repository: [source](https://github.com/platformxlab/RAGPerf/blob/49c9794895666d029a3c98a48afd872197d83b23/src/RAGRequest/TextsRAGRequest.py) — supports `protocol`
- repository: [source](https://github.com/platformxlab/RAGPerf/blob/49c9794895666d029a3c98a48afd872197d83b23/src/evaluator/Ragasvllm.py) — supports `protocol`
- dataset_card: [source](https://huggingface.co/datasets/wikimedia/wikipedia) — supports `protocol`
- dataset_card: [source](https://huggingface.co/datasets/sentence-transformers/natural-questions) — supports `protocol`
- repository: [source](https://github.com/platformxlab/RAGPerf/blob/49c9794895666d029a3c98a48afd872197d83b23/LICENSE) — supports `protocol`
