<!-- Generated from catalog/datasets/unidoc-bench.yaml. Edit the YAML source. -->
# UniDoc-Bench

[简体中文](unidoc-bench.zh-CN.md)

Document-centric multimodal RAG with linked text, table and figure evidence and controlled comparison of retrieval paradigms.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `rag_native` |
| Primary category | `multimodal_rag` |
| Tasks | page_retrieval, visual_qa, multi_hop_qa, attribution |
| Modalities | text, image, table, chart, layout |
| Gold annotation levels | page, figure, fact_citation, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | CC-BY-NC-4.0 with an additional author notice against developing competing models; consult LICENSE.txt and source-document rights. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Eight domain PDF archives accompany QA with source metadata and selected text/image evidence. The GitHub filtered JSON and Hugging Face Parquet expose different schemas and should be mapped explicitly.

Published scale: The paper evaluates 1,600 QA pairs over approximately 70,000 PDF pages; current Hugging Face configuration and size API expose eight domain splits of 200 rows each. Its README body instead claims 1,742 pairs, an unresolved documentation inconsistency.
Splits: Eight domain-named evaluation splits in the current Hugging Face default configuration; not the single test split claimed in its README body.
Format: Domain PDF archives, QA JSON and domain-split Hugging Face Parquet..

## Ground truth and evaluation

QA records link used chunks and figures through chunk_used metadata and list supporting facts. References can be mapped to source pages; they are not universal question-specific bounding boxes. QA is model-synthesized with human checking, whose extent differs across publication and release descriptions.

Official metrics: Precision@10, Recall@10, answer_completeness, faithfulness.

Protocol: Compare text-only, image-only, fusion and joint retrieval using the same candidate corpus, prompts and budget. Map retrieved chunks/pages to original file and page for retrieval scoring; partial page overlap can inflate recall. Use the specified model judge for factual completeness and faithfulness, recording revision and evaluator rather than substituting generic Ragas defaults.

## When to use it

- Comparing multimodal retrieval under a shared candidate pool
- Studying evidence completeness across text and figures

## Limitations and cautions

- Hugging Face README claims 1742 examples in one test split but its configured domain splits total 1600; inspect actual files rather than inferring a new release
- Published abstract and Hugging Face card report 20 percent human validation while a revised preprint claims full validation; pin the version
- Page-overlap matches do not certify complete fine-grained evidence
- Release terms contain an additional model-use notice beyond the named Creative Commons license

## Access and sources

- [Official resource](https://github.com/SalesforceAIResearch/UniDoc-Bench)
- [Paper](https://aclanthology.org/2026.findings-emnlp.534/)
- [Data](https://huggingface.co/datasets/Salesforce/UniDoc-Bench)
- paper: [source](https://aclanthology.org/2026.findings-emnlp.534/) — supports `name`, `summary`, `data.size`, `ground_truth.provenance`, `use.caveats`
- paper: [source](https://arxiv.org/html/2510.03663) — supports `ground_truth.description`, `evaluation.official_metrics`, `evaluation.protocol`, `use.caveats`
- dataset_card: [source](https://huggingface.co/datasets/Salesforce/UniDoc-Bench) — supports `data.size`, `data.splits`, `data.format`, `access.data`, `access.gated`, `use.caveats`
- official: [source](https://datasets-server.huggingface.co/size?dataset=Salesforce%2FUniDoc-Bench) — supports `data.size`, `data.splits`, `use.caveats`
- repository: [source](https://github.com/SalesforceAIResearch/UniDoc-Bench/blob/main/data/QA/filtered/finance.json) — supports `data.description`, `ground_truth.levels`, `ground_truth.description`
- official: [source](https://github.com/SalesforceAIResearch/UniDoc-Bench/blob/main/LICENSE.txt) — supports `access.license`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
