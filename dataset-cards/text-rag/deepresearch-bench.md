<!-- Generated from catalog/datasets/deepresearch-bench.yaml. Edit the YAML source. -->
# DeepResearch Bench (Du et al.)

[简体中文](deepresearch-bench.zh-CN.md)

Expert-authored open-web research tasks evaluated through adaptive report-quality criteria and citation support checks.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | agentic_search, long_form_qa, attribution |
| Modalities | text |
| Gold annotation levels | answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | external / provided / provided |
| Original data license | Apache-2.0 for the official Hugging Face report/annotation release; retrieved web sources retain their own terms. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The official repository supplies research prompts, reference/evaluation material and generated reports; its Hugging Face companion releases model reports and human evaluation annotations. RACE assesses report quality against references; FACT extracts statement-URL pairs and checks cited web support. Neither framework is a second dataset.

Published scale: 100 tasks across 22 fields, with 50 English and 50 Chinese prompts; 96,147 analyzed user queries are construction input, not the benchmark evaluation size.
Splits: Public evaluation task set; no training split is designated in the reference protocol.
Format: JSONL prompts, reference/model reports and evaluation annotations..

## Ground truth and evaluation

Expert-designed tasks are paired with report references and LLM-derived criteria; published human annotations support evaluator-consistency analysis. References include model-generated reports, not unique human gold answers. FACT verifies output citations at evaluation time rather than supplying exhaustive retrieval qrels.

Official metrics: RACE_overall, RACE_comprehensiveness, RACE_depth, RACE_instruction_following, RACE_readability, FACT_citation_accuracy, FACT_effective_citations.

Protocol: Report RACE and FACT separately. Pin reference, cleaner, judge and scraping pipeline; May 2026 changed the official RACE judge and September 2026 changed its cleaning model, so historical Gemini-based and newer GPT-based scores must not be pooled. Record agent retrieval budget and evaluation date; inaccessible cited pages affect FACT.

## When to use it

- Separating long-report synthesis from citation support
- Auditing quality versus search cost for deep-research agents

## Limitations and cautions

- This 100-task Du et al. benchmark is not FutureSearch's similarly named 91-task DeepResearchBench
- RACE is reference-relative and judge-dependent; FACT citation accuracy is not exhaustive evidence recall
- The Hugging Face companion contains reports and annotations; use the repository's query.jsonl for the actual task prompts

## Access and sources

- [Official resource](https://github.com/Ayanami0730/deep_research_bench)
- [Paper](https://proceedings.iclr.cc/paper_files/paper/2026/hash/465f22be10e07b301c6ed58f0472f704-Abstract-Conference.html)
- [Data](https://huggingface.co/datasets/muset-ai/DeepResearch-Bench-Dataset)
- paper: [source](https://proceedings.iclr.cc/paper_files/paper/2026/hash/465f22be10e07b301c6ed58f0472f704-Abstract-Conference.html) — supports `name`, `summary`, `data.size`, `classification.rag_role`
- paper: [source](https://arxiv.org/html/2506.11763) — supports `data.description`, `ground_truth.description`, `ground_truth.provenance`, `ground_truth.alternatives`, `evaluation.official_metrics`
- repository: [source](https://github.com/Ayanami0730/deep_research_bench) — supports `data.size`, `data.splits`, `data.format`, `evaluation.protocol`, `evaluation.evaluator`, `use.caveats`
- dataset_card: [source](https://huggingface.co/datasets/muset-ai/DeepResearch-Bench-Dataset) — supports `access.license`, `data.description`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
