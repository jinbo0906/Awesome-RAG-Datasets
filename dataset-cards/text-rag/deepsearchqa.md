<!-- Generated from catalog/datasets/deepsearchqa.yaml. Edit the YAML source. -->
# DeepSearchQA

[简体中文](deepsearchqa.zh-CN.md)

Multi-step web research with single or exhaustive set answers, penalizing premature stopping and extraneous guesses.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | agentic_search, multi_hop_qa |
| Modalities | text |
| Gold annotation levels | answer |
| Evidence provenance | human |
| Corpus / queries / answers | external / provided / provided |
| Original data license | Apache-2.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Google's December 2025 release provides hand-crafted causal-chain information-seeking prompts across 17 fields. The released fields are problem, problem_category, answer and answer_type; the web remains the external evidence environment.

Published scale: 900 prompts; the official card reports that 65% require set answers.
Splits: Single eval split; answer_type is evaluation metadata and must not be given to the agent at inference.
Format: CSV, loadable through Hugging Face Datasets..

## Ground truth and evaluation

Reference answers enumerate target items rather than relevant pages or browsing actions. An LLM judge matches semantic answer equivalents before set scoring; correct answer membership does not prove a supported citation or a complete source chain.

Official metrics: answer_set_F1, answer_precision, answer_recall, fully_correct_rate, fully_incorrect_rate, correct_with_extraneous_answers_rate.

Protocol: Macro-average per-prompt answer-set F1 as the primary ranking metric and report strict fully-correct success separately. Deduplicate answer items and use semantic matching; the paper uses Gemini 2.5 Flash as judge. Record web/search configuration, judge version and budget; missing items and extra guesses must both affect scores.

## When to use it

- Measuring exhaustive collection and stopping decisions in web research
- Distinguishing high answer recall from fully correct answer sets

## Limitations and cautions

- Answer-level precision and recall are not document-retrieval qrels
- Live source availability and judge behavior can change across runs
- Most set-answer tasks require complete membership rather than one plausible supporting fact

## Access and sources

- [Official resource](https://huggingface.co/datasets/google/deepsearchqa)
- [Paper](https://storage.googleapis.com/deepmind-media/DeepSearchQA/DeepSearchQA_benchmark_paper.pdf)
- [Data](https://huggingface.co/datasets/google/deepsearchqa)
- dataset_card: [source](https://huggingface.co/datasets/google/deepsearchqa) — supports `summary`, `classification`, `data`, `ground_truth.description`, `access.license`, `access.gated`, `evaluation.evaluator`
- paper: [source](https://storage.googleapis.com/deepmind-media/DeepSearchQA/DeepSearchQA_benchmark_paper.pdf) — supports `data.description`, `ground_truth.provenance`, `evaluation.official_metrics`, `evaluation.protocol`, `use.caveats`
- official: [source](https://blog.google/innovation-and-ai/technology/developers-tools/deep-research-agent-gemini-api/) — supports `data.description`, `use.best_for`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
