<!-- Generated from catalog/datasets/pubhealth.yaml. Edit the YAML source. -->
# PUBHEALTH

Public-health claim verification with journalist explanations and source metadata.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-09-28 |
| RAG role | `rag_convertible` |
| Primary category | `text_rag` |
| Tasks | fact_verification, evidence_retrieval |
| Modalities | text |
| Gold annotation levels | answer |
| Evidence provenance | human |
| Corpus / queries / answers | not_provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The official v1.0 TSV release has 12,279 rows across train, dev and test; the paper describes an earlier approximately 11.8K-claim version. Records include claim, date, main evidence text, evidence-source URLs and label, but not one frozen retrievable source corpus.

Published scale: 12,279 claims in the repository v1.0 release; paper counts describe an earlier version.

## Ground truth and evaluation

Fact-check labels and explanations are supplied. Source URLs and main evidence text are useful grounding leads, but no stable document/character offsets are guaranteed for open retrieval.

Official metrics: label_accuracy.

Protocol: Pin the TSV release and acquisition dates. A RAG experiment must build a licensed, dated document collection and define source matching without leaking fact-check explanations.

## When to use it

- Domain-specific claim verification
- Time-aware evidence-source analysis

## Limitations and cautions

- The released TSV is not a complete frozen retrieval corpus
- Repository and paper report different version counts

## Access and sources

- [Official resource](https://github.com/neemakot/Health-Fact-Checking/tree/master/data)
- [Paper](https://arxiv.org/abs/2010.09926)
- repository: [source](https://github.com/neemakot/Health-Fact-Checking/blob/master/data/README.md) — supports `summary`, `data.description`, `data.size`, `ground_truth.description`
- paper: [source](https://arxiv.org/abs/2010.09926) — supports `data.description`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
