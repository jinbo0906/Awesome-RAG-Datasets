<!-- Generated from catalog/datasets/mtrag-un.yaml. Edit the YAML source. -->
# MTRAG-UN

[简体中文](mtrag-un.zh-CN.md)

Multi-turn RAG tests of unanswerable, underspecified and non-standalone questions and clarification responses.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | conversational_qa, evidence_retrieval, rag_robustness, query_rewriting |
| Modalities | text |
| Gold annotation levels | paragraph, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Human conversations are converted into one challenging evaluation turn per conversation; some underspecified endings are stitched to existing conversations. At checking time, reference.jsonl exposes 507 tasks in ClapNQ, Cloud, FiQA and Govt. The author README still marks Banking/Telco corpora and associated tasks as coming soon, so the six-domain paper benchmark is not fully public.

Published scale: Paper reports 666 tasks from 666 conversations and over 2,800 conversation turns across six domains; the checked public reference file has 507 four-domain rows.
Splits: Evaluation benchmark; MTRAG is the separate training resource in SemEval-2026 MTRAGEval, not the same dataset.
Format: JSONL generation tasks and BEIR-format passage-retrieval qrels.

## Ground truth and evaluation

Reference passages, response targets, answerability and conversation-type labels support generation and clarification scoring. Qrels cover answerable/partially answerable turns (468 in the full paper benchmark), not all unanswerable or underspecified cases.

Official metrics: Recall@5, Recall@10, nDCG@5, nDCG@10, RB_llm, RB_alg, IDK_judge, RAGAS_faithfulness, underspecified_response_judge.

Protocol: Preserve history and contrast last-turn queries with query rewrites. Evaluate retrieval only on its eligible turns and condition generation scores on answerability; underspecified responses use their own judge. Report Reference and full-RAG conditions separately. Paper judges and the available four-domain release must not be silently replaced by the full six-domain scores.

## When to use it

- Distinguishing appropriate refusal from clarification
- Evaluating retrieval-query rewriting and difficult later conversation turns

## Limitations and cautions

- Two enterprise domains are not yet released according to the author README
- Count evaluation turns separately from conversations and full conversation turns
- Judge identity and answerability-conditioned scoring affect comparability with original MTRAG
- Repository software licensing does not establish one uniform license for every source corpus

## Access and sources

- [Official resource](https://github.com/IBM/mt-rag-benchmark/tree/main/mtragun-human)
- [Paper](https://aclanthology.org/2026.findings-acl.503/)
- [Data](https://github.com/IBM/mt-rag-benchmark/blob/main/mtragun-human/generation_tasks/reference.jsonl)
- paper: [source](https://aclanthology.org/2026.findings-acl.503.pdf) — supports `summary`, `classification`, `data.size`, `ground_truth`, `evaluation.official_metrics`, `evaluation.protocol`
- repository: [source](https://github.com/IBM/mt-rag-benchmark/blob/main/mtragun-human/README.md) — supports `data.description`, `data.corpus`, `data.format`, `access.license`, `access.gated`, `use`
- repository: [source](https://raw.githubusercontent.com/IBM/mt-rag-benchmark/main/mtragun-human/generation_tasks/reference.jsonl) — supports `data.size`, `data.queries`, `data.answers`, `data.description`
- repository: [source](https://github.com/IBM/mt-rag-benchmark) — supports `data.splits`
- repository: [source](https://github.com/IBM/mt-rag-benchmark/tree/main/scripts/evaluation) — supports `evaluation.evaluator`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
