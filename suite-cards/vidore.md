<!-- Generated from catalog/suites/vidore.yaml. Edit the YAML source. -->
# ViDoRe

[简体中文](vidore.zh-CN.md)

Versioned visual-document benchmark family; v3 extends retrieval relevance to grounding and reference-answer evaluation.

Review status: `source_checked`. This is a benchmark suite or protocol, not one standalone dataset.

## Indexed components

Component-level dataset cards have not yet been indexed. Use the official resource for the full list; this empty list does not mean the suite has no components.

## Protocol and interpretation

Keep v1/v2 retrieval settings separate from v3. The January 2026 v3 paper reports 10 datasets, approximately 26,000 pages and 3,099 human-verified base queries in six languages, with relevance, bounding-box grounding and reference-answer annotations. Eight datasets are public and two are held out; these are not ten openly downloadable components. Current single-retriever evaluation uses MTEB for v1-v3. The author repository now maintains complex retrieval-pipeline evaluation on v3, including OCR/chunking/reranking, nDCG@10, recall and optional indexing/search cost. Its retrieval score is not the paper's model-judged answer correctness or grounding score. Record language, version, public/private subset and evaluator. Components remain unindexed as separate variant cards; consult each dataset's terms rather than applying the code's MIT license to source documents.

## Official sources

- [Official resource](https://github.com/illuin-tech/vidore-benchmark)
- [Paper](https://arxiv.org/abs/2601.08620)
- repository: [source](https://github.com/illuin-tech/vidore-benchmark) — supports `summary`, `protocol`
- paper: [source](https://arxiv.org/html/2601.08620) — supports `summary`, `protocol`
- official: [source](https://huggingface.co/collections/vidore/vidore-benchmark-v3) — supports `protocol`
