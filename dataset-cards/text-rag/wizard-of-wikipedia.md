<!-- Generated from catalog/datasets/wizard-of-wikipedia.yaml. Edit the YAML source. -->
# Wizard of Wikipedia

[简体中文](wizard-of-wikipedia.zh-CN.md)

Human knowledge-grounded conversations with retrieved Wikipedia candidates and selected supporting sentences.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | conversational_qa, evidence_retrieval |
| Modalities | text |
| Gold annotation levels | sentence, answer |
| Evidence provenance | human |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Raw dialogues include conversation topics, user/wizard utterances, retrieved passages and checked knowledge. Supplied retrieval candidates support the native task; replacing them with a full Wikipedia index requires a separately specified setting.

Splits: Training, validation and test resources distinguish seen-topic and unseen-topic evaluation.

## Ground truth and evaluation

Wizard turns include a checked_sentence and checked_passage identifying the knowledge selected by the annotator, plus the written response. Selected knowledge need not enumerate every sentence that could support an acceptable reply.

Official metrics: knowledge_accuracy, response_f1, perplexity, human_rating.

Protocol: Report seen and unseen topics separately and distinguish knowledge selection from response generation; retain the native candidate pool when reproducing its knowledge-selection setting.

## When to use it

- Knowledge-grounded conversational responses
- Generalization to unseen conversation topics

## Limitations and cautions

- Selected sentences are not exhaustive alternative evidence sets
- Native retrieved candidates differ from unrestricted Wikipedia retrieval

## Access and sources

- [Official resource](https://parl.ai/projects/wizard_of_wikipedia/)
- [Paper](https://arxiv.org/abs/1811.01241)
- official: [source](https://parl.ai/projects/wizard_of_wikipedia/) — supports `summary`, `data.description`, `data.splits`, `ground_truth.description`, `evaluation.official_metrics`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
