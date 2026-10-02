<!-- Generated from catalog/suites/longbench.yaml. Edit the YAML source. -->
# LongBench (v1)

[简体中文](longbench.zh-CN.md)

Bilingual long-context suite with 21 tasks, including QA, summarization, few-shot learning, synthetic retrieval and code completion.

Review status: `source_checked`. This is a benchmark suite or protocol, not one standalone dataset.

## Indexed components

- [narrativeqa](../dataset-cards/text-rag/narrativeqa.md)
- [qasper](../dataset-cards/text-rag/qasper.md)
- [hotpotqa](../dataset-cards/text-rag/hotpotqa.md)
- [2wikimultihopqa](../dataset-cards/text-rag/2wikimultihopqa.md)
- [musique](../dataset-cards/text-rag/musique.md)
- [triviaqa](../dataset-cards/text-rag/triviaqa.md)

## Protocol and interpretation

The linked components are upstream source datasets, not the exact LongBench reprocessed subsets; this is a partial component index. Use THUDM/LongBench test files and per-task metrics together, distinguishing LongBench-E length-balanced variants. Retrieval-based context compression is a documented comparison, but the suite has no universal gold chunk boundaries. LongBench v2 is a separate release and is cataloged as its own dataset.

## Official sources

- [Official resource](https://github.com/THUDM/LongBench/tree/main/LongBench)
- [Paper](https://aclanthology.org/2024.acl-long.172/)
- repository: [source](https://github.com/THUDM/LongBench/tree/main/LongBench) — supports `summary`, `components`, `protocol`
