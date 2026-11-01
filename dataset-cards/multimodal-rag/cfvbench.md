<!-- Generated from catalog/datasets/cfvbench.yaml. Edit the YAML source. -->
# CFVBench

[简体中文](cfvbench.zh-CN.md)

Fine-grained video RAG over chart-heavy reports, news and tutorials, with separate visual and transcript-derived answer keypoints.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `rag_native` |
| Primary category | `multimodal_rag` |
| Tasks | video_qa, multimodal_retrieval, multi_hop_qa |
| Modalities | text, video, audio, chart, table |
| Gold annotation levels | document, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | CC-BY-4.0 for author annotations; raw videos have separate academic/non-commercial/no-redistribution terms and upstream copyrights. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The author repository releases per-video QA JSON and links a video archive. Questions distinguish visual, transcript-only and multimodal keypoints; source-video folders identify associated videos.

Published scale: 599 videos; the paper reports 5,360 QA pairs while the current repository README reports 5,363.
Splits: Published evaluation collection; no separate official training split was confirmed.
Format: MP4 archive and per-video multiQA, tsingleQA and vsingleQA JSON..

## Ground truth and evaluation

Model-generated and manually checked questions have answers and keypoints; multiQA separates keypoints.video and keypoints.text. Here document denotes the associated video ID. Public QA samples inspected do not expose question-specific start/end intervals, despite timestamp extraction in the construction pipeline.

Official metrics: Recall@1, Recall@3, Recall@5, Recall@10, video_keypoint_recall, text_keypoint_recall, keypoint_precision, keypoint_f1, ROUGE-L, semantic_similarity, LLM_Likert_score.

Protocol: Report video retrieval hits separately from generated-answer keypoint coverage. Match paper and code revisions, judge model, frame sampling, ASR/OCR and retrieval budget. The paper uses semantic similarity and model ratings in addition to lexical/keypoint measures; current code supports configurable similarity backends and heuristic keypoint matching, so its settings must be recorded.

## When to use it

- Testing whether retrieved video preserves transient chart or interface details
- Separating visual and transcript evidence coverage

## Limitations and cautions

- Paper and repository counts differ by three QA pairs
- Video association and answer keypoints are not released fine-grained temporal qrels
- Video access and redistribution differ from annotation licensing
- Judge and similarity-backend changes can alter scores without changing the RAG system

## Access and sources

- [Official resource](https://github.com/CQU-MM-Intelligent-Lab/CFVBENCH)
- [Paper](https://doi.org/10.1145/3774904.3792726)
- [Data](https://github.com/CQU-MM-Intelligent-Lab/CFVBENCH/tree/main/Bench)
- paper: [source](https://arxiv.org/html/2510.09266) — supports `summary`, `data.size`, `ground_truth.provenance`, `evaluation.official_metrics`, `evaluation.protocol`
- repository: [source](https://github.com/CQU-MM-Intelligent-Lab/CFVBENCH) — supports `data.description`, `data.size`, `data.format`, `access.license`, `use.caveats`
- repository: [source](https://github.com/CQU-MM-Intelligent-Lab/CFVBENCH/blob/main/Bench/-3h4Xt9No9o/multiQA.json) — supports `ground_truth.levels`, `ground_truth.description`
- repository: [source](https://github.com/CQU-MM-Intelligent-Lab/CFVBENCH/blob/main/videorag/evaluate/evaluate.py) — supports `evaluation.protocol`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
