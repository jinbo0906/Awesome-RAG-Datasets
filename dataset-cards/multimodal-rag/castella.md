<!-- Generated from catalog/datasets/castella.yaml. Edit the YAML source. -->
# CASTELLA

[简体中文](castella.zh-CN.md)

Human-annotated audio moment retrieval with sound descriptions and potentially multiple time intervals in long recordings.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-18 |
| RAG role | `auxiliary` |
| Primary category | `multimodal_rag` |
| Tasks | evidence_retrieval, multimodal_retrieval |
| Modalities | audio, text |
| Gold annotation levels | time_interval |
| Evidence provenance | human |
| Corpus / queries / answers | external / provided / not_provided |
| Original data license | CC-BY-4.0 for the annotation release. Source audio availability and terms vary. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Given a recording and a local description, find matching moments within 1–5 minutes of audio. The repository provides English and Japanese annotations, source IDs, download tools and links to extracted features.

Published scale: 1,862 recordings (1,009 train, 213 validation and 640 test). Pinned EN and JA JSON each store 2,182/352/1,347 local caption rows and 6,157/973/4,175 time pairs. The num_moments totals (2,208/357/1,361) differ from row counts.
Splits: Native train, validation and test. The paper's localization experiment excludes 242 recordings without local captions. Challenge adaptations may use different protocols.
Format: JSON with YouTube IDs, local captions and timestamp pairs, plus separately hosted features.

## Ground truth and evaluation

Each local caption has human-annotated start and end seconds at one-second resolution. Multiple intervals can match a single caption, and intervals may include nearby context.

Official metrics: Recall1_at_tIoU_0.5, Recall1_at_tIoU_0.7, mAP_at_tIoU_0.5, mAP_at_tIoU_0.75, mean_mAP_over_tIoU_thresholds.

Protocol: Report within-recording localization using the paper's temporal IoU thresholds. Document split and feature versions as well as which source waveforms were available. QA generation requires a separate adaptation.

## When to use it

- Testing acoustic evidence localization independently of speech transcription
- Evaluating retrieval of repeated events within a long audio recording

## Limitations and cautions

- The corpus must be obtained separately for waveform evaluation
- Localization labels support a component evaluation without QA reference answers
- One-second annotation resolution limits precision at short durations

## Access and sources

- [Official resource](https://github.com/line/CASTELLA)
- [Paper](https://arxiv.org/abs/2511.15131)
- [Data](https://github.com/line/CASTELLA/tree/9b592efe898e6452631dcea001033009762fe36a/json)
- official: [source](https://research.lycorp.co.jp/en/publications/2663) — supports `summary`, `classification`, `data.size`
- paper: [source](https://arxiv.org/html/2511.15131v2) — supports `data.description`, `data.splits`, `ground_truth`, `evaluation.official_metrics`, `evaluation.protocol`, `use`
- repository: [source](https://github.com/line/CASTELLA/tree/9b592efe898e6452631dcea001033009762fe36a/json) — supports `data.size`, `data.format`, `access.data`, `ground_truth.description`
- repository: [source](https://github.com/line/CASTELLA) — supports `access.license`, `evaluation.evaluator`
- official: [source](https://zenodo.org/records/17412176) — supports `data.description`, `data.format`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
