<!-- Generated from catalog/datasets/oaks.yaml. Edit the YAML source. -->
# OAKS (Online Adaptation to Continual Knowledge Streams)

[简体中文](oaks.zh-CN.md)

Chronological streams with per-interval answers that expose how quickly a model adapts after a fact changes.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-18 |
| RAG role | `auxiliary` |
| Primary category | `text_rag` |
| Tasks | time_sensitive_qa, long_context_qa |
| Modalities | text |
| Gold annotation levels | sentence, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | Adobe Research License (academic research or teaching and noncommercial use) |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

OAKS-B provides synthetic narratives with many state changes. OAKS-N uses public-domain novel passages and multiple-choice questions. Replay each stream in order and reveal chunks only as they arrive.

Published scale: Pinned public files: OAKS-B 12 streams, 1,224 question IDs and 78,994 question–interval labels. OAKS-N 19 novels, 435 question IDs and 32,403 labels. The paper describes 39 novels and 870 questions.
Splits: Released OAKS-B streams and OAKS-N novels are separate conditions. Count repeated question IDs once when reporting unique questions.
Format: JSON with ordered chunks and question-to-answer maps indexed by chunk.

## Ground truth and evaluation

chunk_to_answer supplies the expected answer at each stream interval. Novel records store full option texts and option_sources links options to supporting sentences by interval. Acquisition is scored by answer state.

Official metrics: interval_accuracy, acquisition_latency_AL, distraction_susceptibility_DS, phase_miss_rate_PM.

Protocol: Score answers at each interval and macro-average by question. The paper separates errors before the first correct answer, errors after it and entirely missed phases. Record whether using the paper formula or the released script, which charges a wholly missed phase to latency. The RAG baseline filters precomputed neighbors to visible chunks.

## When to use it

- Replaying repeated fact changes and measuring the time steps to recover the correct state
- Comparing retrieval and online adaptation on the same chronological inputs

## Limitations and cautions

- Use the public novel subset denominator for released results
- Answer intervals are states and the novel support metadata is separate
- Report live index visibility delay separately if measuring it

## Access and sources

- [Official resource](https://github.com/adobe-research/OAKS)
- [Paper](https://aclanthology.org/2026.acl-long.1956/)
- [Data](https://github.com/adobe-research/OAKS/tree/0bbc4b3877eae5f9335f07c5e485aabf1d9136e9/data)
- paper: [source](https://aclanthology.org/2026.acl-long.1956.pdf) — supports `summary`, `classification`, `data.description`, `ground_truth`, `evaluation.official_metrics`, `evaluation.protocol`, `use`
- repository: [source](https://github.com/adobe-research/OAKS/tree/0bbc4b3877eae5f9335f07c5e485aabf1d9136e9/data) — supports `data.size`, `data.splits`, `data.format`, `ground_truth.description`, `access.data`
- repository: [source](https://github.com/adobe-research/OAKS/blob/0bbc4b3877eae5f9335f07c5e485aabf1d9136e9/LICENSE) — supports `access.license`
- repository: [source](https://github.com/kaistAI/OAKS/tree/c1a76e66b5b2276973ee8ee3de7063721e22a88f) — supports `evaluation.evaluator`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
