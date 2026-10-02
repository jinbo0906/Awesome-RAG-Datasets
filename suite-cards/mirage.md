<!-- Generated from catalog/suites/mirage.yaml. Edit the YAML source. -->
# MIRAGE (medical RAG)

[简体中文](mirage.zh-CN.md)

Medical RAG suite of 7,663 questions from five QA datasets, evaluated zero-shot with question-only retrieval.

Review status: `source_checked`. This is a benchmark suite or protocol, not one standalone dataset.

## Indexed components

- [medqa](../dataset-cards/text-rag/medqa.md)
- [medmcqa](../dataset-cards/text-rag/medmcqa.md)
- [pubmedqa](../dataset-cards/text-rag/pubmedqa.md)

## Protocol and interpretation

Use the released benchmark.json: MMLU-Med (1,089), MedQA-US four-option test (1,273), MedMCQA dev (4,183), context-removed PubMedQA* test (500), and BioASQ yes/no test questions from 2019–2023 (618). Linked cards describe three upstream datasets; the other two exact subsets are not separately indexed. BioASQ-Y/N is not BioASQ14b. Retrieve using questions without answer options, keep the MedRAG corpus/retriever snapshot fixed, and report per-task and average answer accuracy. Retrieved snippet IDs are system outputs, not gold evidence judgments. Findings ACL 2024 is the publication venue; do not call it an ACL main-conference paper.

## Official sources

- [Official resource](https://github.com/gzxiong/MIRAGE)
- [Paper](https://aclanthology.org/2024.findings-acl.372/)
- repository: [source](https://github.com/gzxiong/MIRAGE) — supports `summary`, `components`, `protocol`
- paper: [source](https://aclanthology.org/2024.findings-acl.372/) — supports `protocol`
