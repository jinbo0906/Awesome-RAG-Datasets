<!-- Generated from catalog/datasets/temprageval.yaml. Edit the YAML source. -->
# TempRAGEval

[简体中文](temprageval.zh-CN.md)

Answer-preserving temporal perturbations with manually located Wikipedia evidence for time-sensitive RAG.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | time_sensitive_qa, evidence_retrieval, rag_robustness |
| Modalities | text |
| Gold annotation levels | sentence, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | external / provided / provided |
| Original data license | Apache-2.0 in query-release metadata; external Wikipedia/ATLAS corpus retains upstream terms. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

SituatedQA and TimeQA questions are manually rewritten with more demanding temporal conditions while preserving their answers. The query release is separate from the ATLAS December 2021 English Wikipedia corpus of 33.1 million text chunks used in the paper.

Published scale: Paper reports 1,000 evidence-annotated test examples; rows with an empty time_relation are excluded by the author protocol.
Splits: Test benchmark with SituatedQA-derived and TimeQA-derived strata; report original and perturbed question results separately.
Format: CSV test file on Hugging Face plus external ATLAS text corpus.

## Ground truth and evaluation

Annotators provide up to two supporting sentences. A retrieved chunk counts as evidence if it contains either sentence, so the evidence metric is an any-support hit, not complete multi-sentence evidence coverage. Answers and source questions originate from differently constructed source datasets.

Official metrics: answer_recall_at_k, gold_evidence_recall_at_k, exact_match, token_f1.

Protocol: Use the pinned Wikipedia/ATLAS corpus, exclude empty time_relation rows and score chunks rather than the system's extracted sentences. Answer-containing recall and annotated-evidence recall are different measures: incidental answer mentions can inflate the former, while unannotated valid passages can reduce the latter. MRAG is the introducing method, not a separate dataset.

## When to use it

- Diagnosing semantic similarity without temporal validity
- Testing retrieval and QA sensitivity to answer-preserving date changes

## Limitations and cautions

- HF API marks access as auto-gated; query files were not downloaded in this audit
- Sentence anchors are not optimal chunk-boundary annotations or exhaustive qrels
- Historical temporal reasoning does not by itself test continuous knowledge-base updates
- The paper is Findings EMNLP 2025; its December 2024 preprint date is a different publication milestone

## Access and sources

- [Official resource](https://github.com/siyue-zhang/MRAG)
- [Paper](https://aclanthology.org/2025.findings-emnlp.167/)
- [Data](https://huggingface.co/datasets/siyue/TempRAGEval)
- paper: [source](https://aclanthology.org/2025.findings-emnlp.167.pdf) — supports `summary`, `classification`, `data.description`, `data.size`, `ground_truth`, `evaluation.official_metrics`, `use`
- repository: [source](https://github.com/siyue-zhang/MRAG) — supports `data.corpus`, `data.splits`, `ground_truth.description`, `evaluation.protocol`, `evaluation.evaluator`, `access.data`
- dataset_card: [source](https://huggingface.co/api/datasets/siyue/TempRAGEval) — supports `data.format`, `access.license`, `access.gated`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
