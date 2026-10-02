<!-- Generated from catalog/datasets/topiocqa.yaml. Edit the YAML source. -->
# TopiOCQA

[简体中文](topiocqa.zh-CN.md)

Open-domain conversational QA with topic switching, free-form answers and gold Wikipedia passages.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | conversational_qa, evidence_retrieval |
| Modalities | text |
| Gold annotation levels | paragraph, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | CC-BY-NC-SA-4.0 |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Author resources supply conversations, gold question-passage pairs, a Wikipedia corpus and its segmented retrieval version. Answers may be abstractive and absent as literal substrings of the supporting passage.

Published scale: The released retrieval setup uses approximately 25.7M Wikipedia passages.

## Ground truth and evaluation

Gold passages ground answers, including additional human answers used by the reader evaluator. Passage identities support retrieval scoring without assuming that an answer-string match identifies evidence.

Official metrics: Hits@k, exact_match, token_f1.

Protocol: Score retrieval against the supplied gold passages and generation with the official CoQA-style multi-reference evaluator. Retain conversation history and topic switches; label any externally generated question rewrites.

## When to use it

- Topic switches in conversational retrieval
- Abstractive answers grounded in retrieved passages

## Limitations and cautions

- Answer-string containment is insufficient for retrieval scoring
- Question rewrites in model resources should not be assumed to be original human annotations

## Access and sources

- [Official resource](https://mcgill-nlp.github.io/topiocqa/)
- [Paper](https://arxiv.org/abs/2110.00768)
- [Data](https://github.com/McGill-NLP/topiocqa)
- repository: [source](https://github.com/McGill-NLP/topiocqa) — supports `summary`, `data.description`, `data.size`, `ground_truth.description`, `evaluation.protocol`, `access.license`
- repository: [source](https://github.com/McGill-NLP/topiocqa/blob/main/evaluate_retriever.py) — supports `evaluation.official_metrics`
- repository: [source](https://github.com/McGill-NLP/topiocqa/blob/main/evaluate_reader.py) — supports `evaluation.official_metrics`, `ground_truth.alternatives`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
