<!-- Generated from catalog/datasets/legalbench-rag.yaml. Edit the YAML source. -->
# LegalBench-RAG

[简体中文](legalbench-rag.zh-CN.md)

Legal retrieval benchmark scoring precise text snippets against character-range annotations.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `auxiliary` |
| Primary category | `text_rag` |
| Tasks | evidence_retrieval |
| Modalities | text |
| Gold annotation levels | document, span |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / not_provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The downloadable benchmark supplies a text corpus and queries with snippet targets derived from ContractNLI, CUAD, MAUD and PrivacyQA; a retrieval target is not a free-form answer reference.

Published scale: The paper reports 6,858 query/snippet examples over more than 79M corpus characters.
Format: Text files and JSON benchmark files.

## Ground truth and evaluation

Each target identifies a corpus file and a character range. Expert upstream annotations are transformed into retrieval cases with LLM assistance.

Official metrics: character_precision_at_k, character_recall_at_k.

Protocol: Preserve file paths and original character offsets when chunking. Report k and full versus mini release; the official benchmark evaluates retrieval.

## When to use it

- Legal chunking and precise evidence retrieval
- Character-level retrieval coverage

## Limitations and cautions

- No native answer-generation scoring is established by this retrieval release
- Check the terms of the four upstream legal datasets before regeneration

## Access and sources

- [Official resource](https://github.com/zeroentropy-ai/legalbenchrag)
- [Paper](https://arxiv.org/abs/2408.10343)
- repository: [source](https://github.com/zeroentropy-ai/legalbenchrag) — supports `summary`, `classification`, `data.description`, `data.format`, `ground_truth`, `evaluation`, `use`
- paper: [source](https://arxiv.org/html/2408.10343v1) — supports `data.size`, `evaluation.official_metrics`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
