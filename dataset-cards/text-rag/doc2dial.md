<!-- Generated from catalog/datasets/doc2dial.yaml. Edit the YAML source. -->
# Doc2Dial

[简体中文](doc2dial.zh-CN.md)

Goal-oriented information-seeking dialogues with document span grounding and agent response annotations.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_convertible` |
| Primary category | `text_rag` |
| Tasks | conversational_qa, evidence_retrieval |
| Modalities | text |
| Gold annotation levels | document, span, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Document files provide text, HTML, span offsets and section structure. Dialogue files link user and agent turns to a document and grounding references; later releases differ from the original paper version.


## Ground truth and evaluation

Human utterances reference span IDs in associated documents. Grounding spans, conditional/solution annotations and contextual titles have different roles; structural source spans are not universal optimal chunk boundaries.

Official metrics: span_exact_match, span_token_f1, mapped_span_exact_match, BLEU-1, BLEU-2, BLEU-3, BLEU-4.

Protocol: Report document retrieval, grounding prediction and response generation as separate tasks. Preserve span offsets, turn history, release version and inclusion of irrelevant turns; the original response task supplies document context.

## When to use it

- Document-grounded service dialogues
- Tracking span evidence through contextual follow-ups

## Limitations and cautions

- Release versions and irrelevant-turn settings change the evaluation
- A supplied-document response experiment does not measure open-corpus retrieval

## Access and sources

- [Official resource](https://doc2dial.github.io/data.html)
- [Paper](https://aclanthology.org/2020.emnlp-main.652/)
- official: [source](https://doc2dial.github.io/data.html) — supports `summary`, `data.description`, `ground_truth.description`
- official: [source](https://doc2dial.github.io/README.html) — supports `ground_truth.levels`, `evaluation.protocol`
- paper: [source](https://aclanthology.org/2020.emnlp-main.652.pdf) — supports `evaluation.official_metrics`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
