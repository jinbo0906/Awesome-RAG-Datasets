<!-- Generated from catalog/datasets/harp-audio.yaml. Edit the YAML source. -->
# HARP Audio QA (SongEval / MedMosaic)

[简体中文](harp-audio.zh-CN.md)

Recording-local audio retrieval and QA with song comparison and contrastive speech versus acoustic symptom questions.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-18 |
| RAG role | `rag_native` |
| Primary category | `multimodal_rag` |
| Tasks | audio_qa, evidence_retrieval, multimodal_retrieval |
| Modalities | audio, text |
| Gold annotation levels | time_interval, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | external / provided / provided |
| Original data license | MIT for queries and checkpoints per release notice. Source audio terms differ (SongEval CC-BY-NC-SA-4.0 and MedMosaic CC-BY-4.0). |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The September 2026 HARP paper evaluates retrieval within a specified long recording. Public question and metadata files cover music comparisons and simulated consultations. Obtain the respective audio assets upstream and use the author preparation scripts.

Published scale: 712 released questions. SongEval has 500 questions over 50 medleys (200 audio cue, 150 time and 150 position prompts). MedMosaic has 212 questions over 106 consultations (106 reported and 106 exhibited symptom prompts).
Splits: Two public evaluation tracks with no separate train split in the question files. Emotion is a third paper track requiring separate MSP license and local reconstruction.
Format: JSONL questions and song metadata with external audio.

## Ground truth and evaluation

Music questions identify two songs whose filenames and recording IDs join to start/end times for whole song instances and expert aesthetic scores. MedMosaic publishes yes/no answers and judging metadata without per-question supporting temporal intervals.

Official metrics: retrieval_hit_rate, judged_answer_accuracy, judged_rationale_accuracy.

Protocol: Score the fraction of required evidence retrieved where it can be resolved. The answer and rationale use model judgments. The released evaluator falls back to factuality alone for audio-only rationale scoring. Report track, retrieval modality, oracle condition and judge separately.

## When to use it

- Testing retrieval of multiple audio clips within one recording
- Comparing transcript retrieval with acoustic evidence retrieval

## Limitations and cautions

- Song intervals cover whole songs and do not localize the shortest justification
- Public track counts exclude MSP emotion (426 in the paper versus 466 in repository preparation notes)
- Long-recording search is scoped to the specified recording

## Access and sources

- [Official resource](https://github.com/chinjouli/harp)
- [Paper](https://arxiv.org/abs/2609.14116)
- [Data](https://huggingface.co/cjli/harp/tree/68f6baf120e7b0fa4627e6f6a15789498e676d97)
- paper: [source](https://arxiv.org/html/2609.14116) — supports `summary`, `classification`, `data.description`, `data.splits`, `ground_truth`, `evaluation.official_metrics`, `evaluation.protocol`, `use`
- official: [source](https://huggingface.co/cjli/harp/tree/68f6baf120e7b0fa4627e6f6a15789498e676d97) — supports `data.size`, `data.format`, `access.data`, `access.license`, `ground_truth.description`
- repository: [source](https://github.com/chinjouli/harp/blob/fea0bf987c92caff0be755d22ab27fa2423f3571/dataset/process_gt_music.py) — supports `ground_truth.description`, `evaluation.protocol`
- repository: [source](https://github.com/chinjouli/harp/blob/fea0bf987c92caff0be755d22ab27fa2423f3571/evaluate/README.md) — supports `evaluation.evaluator`, `evaluation.protocol`
- repository: [source](https://github.com/chinjouli/harp/blob/main/dataprep/emotion/README.md) — supports `data.splits`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
