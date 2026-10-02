<!-- Generated from catalog/datasets/saferag.yaml. Edit the YAML source. -->
# SafeRAG

[简体中文](saferag.zh-CN.md)

Chinese RAG security benchmark with silver noise, inter-context conflicts, soft advertisements and denial-of-service contexts.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | rag_robustness, evidence_retrieval |
| Modalities | text |
| Gold annotation levels | sentence, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The repository releases clean and attack-augmented knowledge bases plus task-specific question/context files. News-based questions and golden contexts are generated with LLM assistance and manually checked and revised.

Format: Text/JSON.

## Ground truth and evaluation

Golden contexts and correct/incorrect propositions support task-specific scoring. They are selected evidence sentences, not an annotation of every valid segmentation of the original news articles.

Official metrics: f1_correct, f1_incorrect, f1_avg, attack_success_rate, retrieval_accuracy.

Protocol: Fix the attack type, injection stage, attack ratio and retrieval window. Distinguish attacks on indexing, retrieved context and filtered context; do not combine their scores into a clean-retrieval score. The reported attack failure rate AFR is 1-ASR, so higher AFR and lower attack success rate mean better defense.

## When to use it

- Chinese RAG robustness under injected contexts
- Comparing retrieval and filtering defenses at different stages

## Limitations and cautions

- Task-specific constructed attacks do not represent an unrestricted live threat distribution
- Gold evidence sentences are not unique chunk boundary gold

## Access and sources

- [Official resource](https://github.com/IAAR-Shanghai/SafeRAG)
- [Paper](https://aclanthology.org/2025.acl-long.230/)
- [Data](https://github.com/IAAR-Shanghai/SafeRAG/tree/main/nctd_datasets)
- paper: [source](https://aclanthology.org/2025.acl-long.230.pdf) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.official_metrics`
- repository: [source](https://github.com/IAAR-Shanghai/SafeRAG) — supports `data.corpus`, `access.data`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
