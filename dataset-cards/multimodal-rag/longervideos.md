<!-- Generated from catalog/datasets/longervideos.yaml. Edit the YAML source. -->
# LongerVideos

[简体中文](longervideos.zh-CN.md)

Long-video collection-level open-ended questions for comparative generation evaluation, without released reference answers or temporal relevance judgments.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `auxiliary` |
| Primary category | `multimodal_rag` |
| Tasks | video_qa, long_form_qa, summarization |
| Modalities | text, video, audio |
| Gold annotation levels | not documented |
| Evidence provenance | unknown |
| Corpus / queries / answers | external / provided / not_provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

VideoRAG's author release groups YouTube URLs, topic descriptions and open questions by collection. Users obtain the original videos and build their own frame, ASR and retrieval representations; released questions do not include reference_answer or evidence intervals.

Published scale: 22 collections, 164 videos, 602 queries and approximately 134.6 hours in the author overview.
Splits: Evaluation collections; no native training split or question-specific answer-gold split confirmed.
Format: Collection-indexed JSON with video_url, description, questions and type; external videos..

## Ground truth and evaluation

The inspected dataset.json supplies question IDs and text but no reference answers, temporal qrels or independently labeled cross-video proof chains. Collection membership defines available context, not a per-question relevance annotation.

Official metrics: pairwise_win_rate, Comprehensiveness, Empowerment, Trustworthiness, Depth, Density, Overall_Score.

Protocol: Follow VideoRAG's model-judged comparison prompts and aggregation scripts. Pairwise evaluation reverses answer order and repeated judgments are aggregated; quantitative scores use the specified rating criteria. Pin the comparator, judge, video availability, processing cost and retrieval budget. Preference wins are not reference-answer accuracy or retrieval recall.

## When to use it

- Stress-testing generation over hours of thematically grouped video
- Studying comparative answer quality and indexing cost

## Limitations and cautions

- No released gold answers or temporal qrels in the inspected question file
- YouTube availability and upstream rights can change
- Framework licensing does not establish a separate dataset or video license
- A generated comparison score cannot certify factual evidence completeness

## Access and sources

- [Official resource](https://github.com/HKUDS/VideoRAG)
- [Paper](https://doi.org/10.1145/3770854.3783944)
- [Data](https://github.com/HKUDS/VideoRAG/blob/main/VideoRAG-algorithm/longervideos/dataset.json)
- repository: [source](https://github.com/HKUDS/VideoRAG) — supports `summary`, `data.size`, `use.caveats`
- repository: [source](https://github.com/HKUDS/VideoRAG/blob/main/VideoRAG-algorithm/longervideos/dataset.json) — supports `data.description`, `data.format`, `data.answers`, `ground_truth.levels`, `ground_truth.description`
- paper: [source](https://arxiv.org/html/2502.01549) — supports `evaluation.official_metrics`, `evaluation.protocol`, `use.best_for`
- repository: [source](https://github.com/HKUDS/VideoRAG/tree/main/VideoRAG-algorithm/reproduce) — supports `evaluation.protocol`, `evaluation.evaluator`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
