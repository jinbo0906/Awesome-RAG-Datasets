<!-- Generated from catalog/datasets/arxivqa.yaml. Edit the YAML source. -->
# ArXivQA

[简体中文](arxivqa.zh-CN.md)

GPT-4V-generated multiple-choice scientific-figure QA used for multimodal instruction training and retrieval adaptations.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_convertible` |
| Primary category | `multimodal_rag` |
| Tasks | visual_qa, multimodal_retrieval |
| Modalities | text, image, chart, equation |
| Gold annotation levels | answer |
| Evidence provenance | synthetic |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The Multimodal ArXiv project releases figures with generated questions, options, labels and rationales. VisRAG constructs an independently filtered retrieval evaluation from these question-figure associations.

Published scale: 100,000 released QA examples.
Splits: The original Hugging Face package has a train container; retrieval-specific evaluation splits are derivative protocols.
Format: JSON QA and figure-image archive..

## Ground truth and evaluation

Generated labels and rationales supervise figure answering. Paired figures can seed retrieval positives, but rationales are not human evidence boxes or native exhaustive corpus relevance judgments.

Official metrics: multiple_choice_accuracy.

Protocol: Treat the original release primarily as training data; label any held-out construction explicitly. For VisRAG, follow its converted queries, figure pool and retrieval/generation scoring instead of assuming a native RAG test set.

## When to use it

- Scientific-figure instruction training
- Explicit figure-retrieval adaptations

## Limitations and cautions

- Synthetic labels and rationales require independent error auditing
- Project page says CC-BY-NC-4.0 research-only while the current data card says CC-BY-SA-4.0

## Access and sources

- [Official resource](https://mm-arxiv.github.io/)
- [Paper](https://aclanthology.org/2024.acl-long.775/)
- [Data](https://huggingface.co/datasets/MMInstruction/ArxivQA)
- official: [source](https://mm-arxiv.github.io/) — supports `summary`, `data.description`, `ground_truth.provenance`, `use.caveats`
- dataset_card: [source](https://huggingface.co/datasets/MMInstruction/ArxivQA) — supports `data.size`, `data.splits`, `data.format`, `ground_truth.description`, `use.caveats`
- paper: [source](https://proceedings.iclr.cc/paper_files/paper/2025/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf) — supports `data.description`, `evaluation.official_metrics`, `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
