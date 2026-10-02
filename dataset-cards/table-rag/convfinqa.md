<!-- Generated from catalog/datasets/convfinqa.yaml. Edit the YAML source. -->
# ConvFinQA

[简体中文](convfinqa.zh-CN.md)

Conversational financial QA with linked numerical programs and answers for each turn.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_convertible` |
| Primary category | `table_rag` |
| Tasks | conversational_qa, text_table_reasoning |
| Modalities | text, table |
| Gold annotation levels | sentence, table, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | MIT |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The release supplies conversation-level and turn-level formats with tables, surrounding text, dialogue_break, turn_program and exe_ans_list.

Published scale: 3,892 conversations containing 14,115 questions.
Splits: Conversation-level train/dev/test have 3,037/421/434 examples; the released test provides reports and conversations while scoring references remain hidden.
Format: JSON in data.zip.

## Ground truth and evaluation

Per-turn programs and execution answers specify numerical dependencies; gold_ind identifies supporting facts in labeled splits. These are not source PDF cell coordinates.

Official metrics: execution_accuracy, program_accuracy.

Protocol: Retain turn order and conversation boundaries. Score with the official execution/program evaluator and state whether prior-turn programs or answers are gold or predicted.

## When to use it

- Conversational numerical reasoning after retrieval
- Prior-turn result dependencies

## Limitations and cautions

- Conversation synthesis and annotation build on FinQA; avoid source-report leakage across custom splits
- The released table/text context does not establish open-corpus retrieval performance

## Access and sources

- [Official resource](https://github.com/czyssrs/ConvFinQA)
- [Paper](https://aclanthology.org/2022.emnlp-main.421/)
- [Data](https://github.com/czyssrs/ConvFinQA/blob/main/data.zip)
- repository: [source](https://github.com/czyssrs/ConvFinQA) — supports `summary`, `classification`, `data.description`, `data.splits`, `data.format`, `ground_truth`, `evaluation`, `access.license`, `use`
- paper: [source](https://aclanthology.org/2022.emnlp-main.421/) — supports `data.size`, `ground_truth.provenance`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
