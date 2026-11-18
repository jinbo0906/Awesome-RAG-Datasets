<!-- Generated from catalog/datasets/mmdocrag.yaml. Edit the YAML source. -->
# MMDocRAG

[简体中文](mmdocrag.zh-CN.md)

Multi-page multimodal document QA with cross-modal evidence chains and quote selection.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-18 |
| RAG role | `rag_native` |
| Primary category | `multimodal_rag` |
| Tasks | page_retrieval, layout_retrieval, visual_qa, attribution |
| Modalities | text, image, table, chart, layout |
| Gold annotation levels | page, quote, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | The Hugging Face release is tagged Apache-2.0. The paper Appendix G limits new question, evidence and answer annotations to academic and noncommercial research unless the authors give written permission. Check both terms before reuse. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The official Hugging Face release provides PDF/image archives and question JSONL with 15-quote and 20-quote candidate settings. Inputs include gold and hard-negative text and image quotes.

Published scale: The paper reports 4,055 QA pairs from 222 documents, of which 2,503 are cross-modal.
Splits: The paper specifies 2,055 development and 2,000 evaluation questions. The 15-quote and 20-quote evaluation files are alternative candidate settings for the evaluation questions.

## Ground truth and evaluation

Match question-local `gold_quotes` IDs to `text_quotes` and `img_quotes`, then map each quote to its document, `page_id` and `layout_id`. The records provide short and interleaved answers. Use `evidence_modality_type` to find questions that use more than one modality.

Official metrics: quote_selection_f1, BLEU, ROUGE-L, answer_quality.

Protocol: For supplied-context quote selection, use the matching `evaluation_15.jsonl` or `evaluation_20.jsonl` and the author `eval_all.py`. The scorer matches predicted and gold quote IDs, and the separate `eval_llm_judge.py` scores interleaved answers. Pin the candidate setting, input mode and judge. Report retrieval from the source documents separately from given-candidate selection. Use the selection guide's complete-set diagnostic with explicit fact-to-quote mappings when studying evidence fragmentation.

## When to use it

- Cross-page evidence selection
- Text-image quote integration
- Hard-negative robustness

## Limitations and cautions

- Supplied 15/20-quote selection and retrieval from the source document expose different candidate pools.
- Released quote IDs indicate support. Ordered dependency edges and exhaustive sets of alternative evidence require additional annotation.

## Access and sources

- [Official resource](https://mmdocrag.github.io/MMDocRAG/)
- [Paper](https://arxiv.org/abs/2505.16470)
- [Data](https://huggingface.co/datasets/MMDocIR/MMDocRAG/tree/04b58dbc5c6c4955291124eed411b09114728061)
- official: [source](https://mmdocrag.github.io/MMDocRAG/) — supports `summary`, `data.size`, `ground_truth.description`, `evaluation.protocol`
- paper: [source](https://proceedings.neurips.cc/paper_files/paper/2025/file/1a93178950e92fd2e7b7448f7d68fd7d-Paper-Datasets_and_Benchmarks_Track.pdf) — supports `data.description`, `classification.modalities`
- paper: [source](https://arxiv.org/html/2505.16470) — supports `data.size`, `data.splits`, `access.license`, `use.caveats`
- dataset_card: [source](https://huggingface.co/datasets/MMDocIR/MMDocRAG/tree/04b58dbc5c6c4955291124eed411b09114728061) — supports `access.data`, `access.license`, `data.description`, `data.splits`
- official: [source](https://datasets-server.huggingface.co/first-rows?dataset=MMDocIR%2FMMDocRAG&config=default&split=test) — supports `ground_truth.description`
- repository: [source](https://github.com/MMDocRAG/MMDocRAG/blob/2fd7505c6a576376b4a92aafaff6d87494765bb7/eval_all.py) — supports `evaluation.official_metrics`, `evaluation.protocol`
- repository: [source](https://github.com/MMDocRAG/MMDocRAG/blob/2fd7505c6a576376b4a92aafaff6d87494765bb7/eval_llm_judge.py) — supports `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
