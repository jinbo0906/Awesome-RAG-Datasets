<!-- Generated from catalog/datasets/fever.yaml. Edit the YAML source. -->
# FEVER

Wikipedia-based claim verification with labeled supporting sentence sets.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | fact_verification, evidence_retrieval |
| Modalities | text |
| Gold annotation levels | sentence, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Claims are labeled Supports, Refutes or Not Enough Info against a fixed Wikipedia snapshot.


## Ground truth and evaluation

Evidence sets of Wikipedia sentences support or refute verifiable claims.

Official metrics: label_accuracy, fever_score.

Protocol: FEVER score requires both a correct label and complete evidence for supported or refuted claims.

## When to use it

- Sentence-level evidence retrieval
- Testing complete evidence-set coverage

## Limitations and cautions

- NEI cases do not have a positive gold evidence set

## Access and sources

- [Official resource](https://fever.ai/dataset/fever.html)
- [Paper](https://aclanthology.org/N18-1074/)
- paper: [source](https://aclanthology.org/N18-1074/) — supports `summary`, `data.description`, `ground_truth.description`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
