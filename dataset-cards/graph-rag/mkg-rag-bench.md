<!-- Generated from catalog/datasets/mkg-rag-bench.yaml. Edit the YAML source. -->
# MKG-RAG-Bench

[简体中文](mkg-rag-bench.zh-CN.md)

Retrieval of text and image-bearing knowledge graph triples with a downstream answer task derived from the same triples.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-18 |
| RAG role | `rag_native` |
| Primary category | `graph_rag` |
| Tasks | evidence_retrieval, multimodal_retrieval, graph_qa |
| Modalities | graph, text, image |
| Gold annotation levels | graph_triplet, answer |
| Evidence provenance | synthetic |
| Corpus / queries / answers | external / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The general G split is built from MarKG and the medical M split from MedMKG. The release includes triple JSONL, separate text and multimodal query files and TSV qrels. Obtain upstream image assets to run the full visual conditions. Some medical image paths refer to MIMIC-CXR-JPG.

Published scale: G has 48,908/6,113/6,115 train/validation/test queries and 25,517 triples. M has 4,781/597/599 queries and 18,468 triples. Test query counts were checked in the release.
Splits: Train, validation and test per domain with a shared corpus within each domain. Record which query types and which candidate triple modalities are allowed.
Format: JSONL for queries and triple records, TSV for qrels, external image files.

## Ground truth and evaluation

Question generation masks entities or relations from selected graph triples. Qrels identify supporting triples and answers are derived from the masked elements. Triple targets do not establish multi-hop path completeness.

Official metrics: nDCG_at_k, precision_at_k, recall_at_k, EM, token_F1, Contains_at_1, BLEU_1.

Protocol: Score ranked triples using the qrels and hold the query/candidate modality configuration fixed. The generation experiment feeds top five retrieved triples to GPT-5 and reports lexical answer measures alongside a generation-only baseline.

## When to use it

- Testing the contribution of images to graph triple retrieval
- Separating graph retrieval and answer quality under controlled modality conditions

## Limitations and cautions

- Images need upstream distributions and may require credentialed access
- The paper license does not establish benchmark or image terms
- Triple-derived QA does not measure extraction of a graph from raw documents

## Access and sources

- [Official resource](https://github.com/XiaochenWang-PSU/MKG-RAG-Bench)
- [Paper](https://doi.org/10.1145/3770855.3817570)
- [Data](https://github.com/XiaochenWang-PSU/MKG-RAG-Bench/tree/34a1b5d96fbcaf92eac0c478f41ca6ce972b437e)
- paper: [source](https://arxiv.org/html/2606.26458) — supports `summary`, `classification`, `data.description`, `data.size`, `ground_truth`, `evaluation.official_metrics`, `evaluation.protocol`, `use`
- repository: [source](https://github.com/XiaochenWang-PSU/MKG-RAG-Bench/tree/34a1b5d96fbcaf92eac0c478f41ca6ce972b437e) — supports `data`, `access.data`, `evaluation.evaluator`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
