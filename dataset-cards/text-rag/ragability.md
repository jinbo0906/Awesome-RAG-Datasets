<!-- Generated from catalog/datasets/ragability.yaml. Edit the YAML source. -->
# Ragability Corpus

[简体中文](ragability.zh-CN.md)

Handcrafted fictional-entity contexts that isolate inter-context contradiction detection and appropriate refusal.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `auxiliary` |
| Primary category | `text_rag` |
| Tasks | rag_robustness, time_sensitive_qa |
| Modalities | text |
| Gold annotation levels | answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | CC-BY-SA-4.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

A small seed corpus supplies four context variants, content questions, context-conditioned short and long answers, and reasoning-type labels. Fantasy entities, dates and numbers are manually substituted into selected WikiContradict cases. The accompanying Ragability library constructs controlled prompt combinations; it is a separate tool, not another dataset.

Published scale: 53 released CSV seed rows based on 43 selected source context pairs; the paper's experiment generates 1,060 test prompts per evaluated model.
Splits: One Hugging Face train-named seed table; generated prompt combinations are not independent train/test splits.
Format: CSV seed data plus a Python prompt-generation and checking library.

## Ground truth and evaluation

Manually constructed contexts and answers specify answerable, contradictory and insufficient conditions. Contradictory or insufficient context combinations can require refusal. Context snippets are supplied inputs, not qrels for a larger corpus or optimal segmentation labels.

Official metrics: contradiction_identification, correct_answer_all, refusal_not_answerable, correct_answer_answerable.

Protocol: Generate the specified context combinations and retain prompt hints, answerability, reasoning type and context ordering. The paper uses 20 prompts per seed and reverses two-context orders; larger context sets do not enumerate every permutation. Semantic correctness and refusal depend on a checker model, so pin its identity rather than interpreting checker agreement as human gold.

## When to use it

- Separating conflict identification from content answering and refusal
- Controlled tests without relying on memorized real-world entities

## Limitations and cautions

- The small constructed seed set is not a representative live retrieval distribution
- Generated prompt counts must not be reported as unique questions or documents
- A contradiction warning can improve contradictory cases while harming non-contradictory cases
- Supplied contexts do not measure retrieval effectiveness

## Access and sources

- [Official resource](https://huggingface.co/datasets/ofai/RagabilityCorpus)
- [Paper](https://aclanthology.org/2026.lrec-1.182/)
- [Data](https://huggingface.co/datasets/ofai/RagabilityCorpus)
- paper: [source](https://aclanthology.org/2026.lrec-1.182.pdf) — supports `summary`, `classification`, `data.description`, `data.size`, `ground_truth`, `evaluation.official_metrics`, `evaluation.protocol`, `use`
- dataset_card: [source](https://huggingface.co/datasets/ofai/RagabilityCorpus) — supports `data.corpus`, `data.queries`, `data.answers`, `data.splits`, `data.format`, `data.size`, `access.license`, `access.gated`
- repository: [source](https://github.com/OFAI/python-ragability) — supports `evaluation.evaluator`, `data.description`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
