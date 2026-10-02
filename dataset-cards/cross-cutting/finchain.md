<!-- Generated from catalog/datasets/finchain.yaml. Edit the YAML source. -->
# FinChain

[简体中文](finchain.zh-CN.md)

Auxiliary financial reasoning benchmark with executable symbolic templates and verifiable intermediate calculations.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `auxiliary` |
| Primary category | `cross_cutting` |
| Tasks | single_hop_qa |
| Modalities | text, equation |
| Gold annotation levels | answer |
| Evidence provenance | synthetic |
| Corpus / queries / answers | not_provided / provided / provided |
| Original data license | Apache-2.0 for original code and executable templates |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Released Python templates generate financial problems, gold intermediate values and executable traces; no document retrieval corpus or relevance labels are supplied.

Published scale: 58 topics across 12 domains; five templates per topic and ten seeds yield 2,900 paper evaluation cases.
Format: Executable Python templates and generated problem/trace records.

## Ground truth and evaluation

Executable symbolic templates define final values and intermediate calculations; these are reasoning targets rather than source-document citations.

Official metrics: chaineval, final_answer_correctness, rouge_2, rouge_l, bertscore.

Protocol: Use fixed templates, seeds and step extraction; the paper selects DTWNormGate with final-answer correctness and numerical tolerance 0.05. This is a reasoning component test.

## When to use it

- Verifying numerical reasoning after retrieval
- Separating final-answer correctness from intermediate calculation quality

## Limitations and cautions

- No native RAG retrieval task is released
- New template seeds do not alone eliminate model exposure to problem patterns

## Access and sources

- [Official resource](https://github.com/mbzuai-nlp/finchain)
- [Paper](https://aclanthology.org/2026.acl-long.662/)
- [Data](https://github.com/mbzuai-nlp/finchain/tree/main/data/templates)
- repository: [source](https://github.com/mbzuai-nlp/finchain) — supports `summary`, `classification`, `data`, `ground_truth`, `access.license`, `evaluation.evaluator`, `use`
- paper: [source](https://aclanthology.org/2026.acl-long.662.pdf) — supports `evaluation.official_metrics`, `evaluation.protocol`, `data.size`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
