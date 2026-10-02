<!-- Generated from catalog/datasets/rag-igbench.yaml. Edit the YAML source. -->
# RAG-IGBench

[简体中文](rag-igbench.zh-CN.md)

Open-domain RAG benchmark for producing interleaved text-and-image answers from retrieved social-platform content.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_native` |
| Primary category | `multimodal_rag` |
| Tasks | long_form_qa, attribution, multimodal_retrieval |
| Modalities | text, image |
| Gold annotation levels | answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Samples contain a query, retrieved documents, image URLs, category, split and reference answer with document citations and image indices. The release primarily fixes per-query retrieved context, rather than exposing full social-platform search.

Published scale: The paper reports 6,057 source queries; the bilingual Hugging Face package displays about 12,100 rows.
Splits: Read each row's split field; the Hugging Face viewer groups the bilingual package under a container named train.
Format: Chinese JSONL and English JSON with retrieved text and external image URLs..

## Ground truth and evaluation

Model-assisted reference answers are manually checked and retain selected image indices and document references. Retrieved contexts are candidate inputs, not exhaustive relevance judgments or minimal human evidence sets.

Official metrics: ROUGE-1, modified_edit_distance, Kendall_score, CLIP_score, alignment_score.

Protocol: Keep image IDs and order, use author metric definitions, and report language and row-level split. Cache permitted source images and record missing URLs; translation pairs should not be counted as independent source questions.

## When to use it

- Evaluating image selection and placement in generated answers
- Comparing text quality with image-text consistency

## Limitations and cautions

- Paper Appendix C says dataset CC-BY-4.0 while the current Hugging Face card says Apache-2.0
- External social-platform images can disappear and retain upstream rights

## Access and sources

- [Official resource](https://github.com/USTC-StarTeam/RAG-IGBench)
- [Paper](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b0a4b3e384b4554e65a47ad1f6b0310a-Abstract-Datasets_and_Benchmarks_Track.html)
- [Data](https://huggingface.co/datasets/Muyi13/RAG-IGBench)
- paper: [source](https://proceedings.neurips.cc/paper_files/paper/2025/file/b0a4b3e384b4554e65a47ad1f6b0310a-Paper-Datasets_and_Benchmarks_Track.pdf) — supports `summary`, `data.size`, `ground_truth.description`, `evaluation.official_metrics`, `use.caveats`
- repository: [source](https://github.com/USTC-StarTeam/RAG-IGBench) — supports `data.description`, `data.format`, `evaluation.protocol`
- dataset_card: [source](https://huggingface.co/datasets/Muyi13/RAG-IGBench) — supports `data.description`, `data.size`, `data.splits`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
