<!-- Generated from catalog/datasets/squad.yaml. Edit the YAML source. -->
# SQuAD 2.0

[简体中文](squad.zh-CN.md)

Wikipedia paragraph reading comprehension combining extractive questions with adversarial unanswerable questions.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_convertible` |
| Primary category | `text_rag` |
| Tasks | single_hop_qa, rag_robustness |
| Modalities | text |
| Gold annotation levels | span, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | CC-BY-SA-4.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Each example supplies a reading passage and questions; answerable questions have answer spans, while unanswerable questions require abstention. This record uses version 2.0 rather than a separate 1.1 entry.

Published scale: Version 2.0 combines about 100K version-1.1 questions with over 50K adversarial unanswerable questions.
Splits: Public training and development sets; official test data are withheld.

## Ground truth and evaluation

Crowdworkers annotate answer text and character positions in the supplied paragraph; empty answers represent unanswerability in that paragraph, not in all possible external documents.

Official metrics: exact_match, token_f1.

Protocol: Use the version-2 evaluator and no-answer handling. A RAG conversion must define the retrieval pool and preserve source offsets; supplied paragraphs are not open-corpus retrieval results.

## When to use it

- Answer extraction from retrieved contexts
- Context-specific abstention

## Limitations and cautions

- Native evaluation supplies the paragraph
- SQuAD 1.1 and 2.0 scores follow different answerability settings

## Access and sources

- [Official resource](https://rajpurkar.github.io/SQuAD-explorer/)
- [Paper](https://arxiv.org/abs/1806.03822)
- official: [source](https://rajpurkar.github.io/SQuAD-explorer/) — supports `summary`, `data.description`, `data.size`, `data.splits`, `ground_truth.description`, `evaluation.official_metrics`, `evaluation.protocol`, `access.license`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
