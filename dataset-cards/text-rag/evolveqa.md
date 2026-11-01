<!-- Generated from catalog/datasets/evolveqa.yaml. Edit the YAML source. -->
# evolveQA

[简体中文](evolveqa.zh-CN.md)

Cutoff-aligned knowledge probes that distinguish current, outdated and incorrect answers across evolving facts.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `auxiliary` |
| Primary category | `text_rag` |
| Tasks | time_sensitive_qa |
| Modalities | text |
| Gold annotation levels | answer |
| Evidence provenance | synthetic |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | CC-BY-NC-ND-4.0; the author README limits the release to academic/scientific reproducibility and prohibits model training. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The October 2026 author release contains timestamped AWS updates, Azure changes and WHO Disease Outbreak News sources alongside generated QA records. Questions have open-ended, multiple-choice and paired verifiable formats, with entity/concept/attribute metadata and an answer date. Native experiments probe parametric knowledge without retrieval; raw sources are not a released open-RAG relevance or citation evaluation protocol.

Published scale: At release revision 2deea4042935b44b06c19c6dfed19ce25d928887, 18 cutoff-specific JSON files contain 4,967 records and 937 distinct domain/question_id keys. The latest cutoff alone has 922 records (550 AWS, 203 Azure and 169 WHO).
Splits: Six knowledge-cutoff conditions from August 2023 to August 2024, not independent train/test partitions; question IDs recur across cutoff files.
Format: JSON question arrays plus domain-organized raw source data.

## Ground truth and evaluation

Model-generated reference answers and option/yes-no targets are aligned with the selected cutoff. A human sample audits construction quality, not every released label. Entity/concept/attribute fields and recent_answer_date do not provide question-specific document qrels or evidence spans.

Official metrics: accuracy, verifiable_qa_hard_accuracy, outdated_response_rate.

Protocol: Match the model's knowledge cutoff to the selected condition and keep probing formats separate. Hard accuracy requires both true- and false-eliciting variants of a fact to be correct. For open-ended answers the paper's judge uses current and historical answers to classify correct/current, outdated or incorrect; ORR is lower-is-better. Any retrieval adaptation must separately define its source snapshot, relevance labels and evidence/citation metrics.

## When to use it

- Cutoff-aligned parametric-knowledge controls for RAG experiments
- Separating obsolete answers from wholly incorrect answers

## Limitations and cautions

- Native scores do not evaluate retrieval or continuous knowledge-base updates
- The six historical cutoff conditions do not measure knowledge current in November 2026
- Repeated question IDs and multiple probing formats must not be counted as independent questions
- Public availability does not remove the stated no-training and restricted-use terms

## Access and sources

- [Official resource](https://github.com/amazon-science/evolveQA)
- [Paper](https://aclanthology.org/2026.emnlp-main.2373/)
- [Data](https://github.com/amazon-science/evolveQA/tree/main/evolveQA-benchmark)
- paper: [source](https://aclanthology.org/2026.emnlp-main.2373.pdf) — supports `summary`, `classification`, `ground_truth`, `evaluation.official_metrics`, `evaluation.protocol`, `use.best_for`
- repository: [source](https://github.com/amazon-science/evolveQA) — supports `data.description`, `data.corpus`, `data.queries`, `data.answers`, `data.splits`, `data.format`, `access.data`, `access.license`, `access.gated`, `use.caveats`
- repository: [source](https://github.com/amazon-science/evolveQA/tree/2deea4042935b44b06c19c6dfed19ce25d928887/evolveQA-benchmark) — supports `data.size`
- repository: [source](https://github.com/amazon-science/evolveQA/blob/main/LICENSE) — supports `access.license`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
