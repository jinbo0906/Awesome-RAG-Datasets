<!-- Generated from catalog/datasets/multidoc2dial.yaml. Edit the YAML source. -->
# MultiDoc2Dial

[简体中文](multidoc2dial.zh-CN.md)

Goal-oriented dialogues whose grounding documents change across turns, with retrieval and agent response generation tasks.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | conversational_qa, evidence_retrieval |
| Modalities | text |
| Gold annotation levels | document, span, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The release supplies documents and dialogues across four domains. Turn references contain document and span IDs, allowing the relevant document to change as the conversation moves between sub-goals.

Splits: The v1.0 data readme documents training and validation files and a dummy test file; shared-task releases need separate identification.

## Ground truth and evaluation

Human agent utterances are associated with grounding references containing doc_id and id_sp. Empty references cover specified unanswerable or irrelevant turns; precondition/solution labels are described as fuzzy annotations.

Official metrics: document_Recall@k, passage_Recall@k, exact_match, token_f1, BLEU.

Protocol: Evaluate retrieval at document and passage levels separately from response generation; retain turn history and document/span mappings when changing segmentation.

## When to use it

- Conversational retrieval with changing documents
- Comparing document and passage evidence coverage

## Limitations and cautions

- A dummy test file is not a labeled evaluation set
- Publisher-card license metadata and licensing prose disagree; confirm the applicable data license

## Access and sources

- [Official resource](https://doc2dial.github.io/multidoc2dial/)
- [Paper](https://aclanthology.org/2021.emnlp-main.498/)
- [Data](https://github.com/IBM/multidoc2dial)
- official: [source](https://doc2dial.github.io/multidoc2dial/) — supports `summary`, `data.description`
- official: [source](https://doc2dial.github.io/multidoc2dial/data_readme.html) — supports `data.splits`, `ground_truth.description`, `ground_truth.levels`
- repository: [source](https://github.com/IBM/multidoc2dial) — supports `evaluation.official_metrics`, `evaluation.protocol`
- dataset_card: [source](https://huggingface.co/datasets/IBM/multidoc2dial) — supports `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
