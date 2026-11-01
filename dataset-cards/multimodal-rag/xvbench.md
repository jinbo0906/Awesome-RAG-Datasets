<!-- Generated from catalog/datasets/xvbench.yaml. Edit the YAML source. -->
# XVBench

[简体中文](xvbench.zh-CN.md)

Video-corpus RAG questions with explicit supporting clip filenames, targeting visual detail retention during iterative retrieval and reasoning.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `rag_native` |
| Primary category | `multimodal_rag` |
| Tasks | video_qa, multimodal_retrieval, long_context_qa |
| Modalities | text, video |
| Gold annotation levels | document, answer |
| Evidence provenance | synthetic |
| Corpus / queries / answers | external / provided / provided |
| Original data license | CC-BY-4.0 for annotations; obtain source videos under HowTo100M and upstream video terms. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

VimRAG introduces a HowTo100M-derived evaluation set. The official release provides query, gt, video_name and reference clip filenames; videos must be obtained separately and split using the provided fixed-duration preprocessing script.

Published scale: The released test JSONL contains 497 questions; 138 reference multiple clips, but none of their listed reference sets spans multiple source-video IDs in the inspected release.
Splits: One public test split; VimRAG training data and its approximately 200k-item merged evaluation corpus are separate experimental assets.
Format: JSONL plus a video splitting shell script; external HowTo100M videos..

## Ground truth and evaluation

gt contains the target answer and reference lists addressable supporting video clips. Here document denotes a clip, not an entire original video. Clip names and the default 60-second segmentation allow reconstruction, but do not provide minimal temporal intervals or exhaustive alternative evidence sets.

Official metrics: model_judged_answer_accuracy.

Protocol: VimRAG Section 4.1 and Table 2 report binary model-judged answer correctness; Appendix B specifies Qwen3-Max and Appendix J the judge prompt. Record corpus composition and reconstruct exact clip naming before retrieval. Clip-reference analysis is possible, but no additional ranking metric is claimed as an official reported score.

## When to use it

- Testing retention of supporting video clips in iterative RAG
- Comparing visual-memory compression against answer correctness

## Limitations and cautions

- The cross-video benchmark label does not guarantee each question needs multiple distinct source videos
- The full merged corpus in the paper is not the 497-row annotation release
- Source-video retrieval and exact preprocessing are required
- Supporting clip names are coarser than optimal temporal boundaries

## Access and sources

- [Official resource](https://huggingface.co/datasets/Alibaba-NLP/xvbench)
- [Paper](https://arxiv.org/abs/2602.12735)
- [Data](https://huggingface.co/datasets/Alibaba-NLP/xvbench/tree/main)
- paper: [source](https://arxiv.org/html/2602.12735) — supports `summary`, `ground_truth.provenance`, `evaluation.official_metrics`, `evaluation.protocol`, `data.splits`
- dataset_card: [source](https://huggingface.co/datasets/Alibaba-NLP/xvbench) — supports `data.description`, `data.size`, `data.splits`, `data.format`, `access.license`, `access.gated`, `ground_truth.description`, `use.caveats`
- official: [source](https://huggingface.co/datasets/Alibaba-NLP/xvbench/blob/main/xvbench.jsonl) — supports `data.size`, `ground_truth.levels`, `use.caveats`
- official: [source](https://huggingface.co/datasets/Alibaba-NLP/xvbench/blob/main/split_video.sh) — supports `ground_truth.description`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
