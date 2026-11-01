<!-- Generated from catalog/suites/m4-rag.yaml. Edit the YAML source. -->
# M4-RAG

[简体中文](m4-rag.zh-CN.md)

Multilingual and multicultural retrieval-augmented VQA over CVQA and WorldCuisines with separate Wikipedia source pools.

Review status: `source_checked`. This is a benchmark suite or protocol, not one standalone dataset.

## Indexed components

Component-level dataset cards have not yet been indexed. Use the official resource for the full list; this empty list does not mean the suite has no components.

## Protocol and interpretation

The CVPR 2026 paper introduces a RAG evaluation protocol over CVQA and WorldCuisines, reporting more than 80,000 image-question pairs across 42 languages, 56 dialects/registers and 189 countries. These converted components are not separately indexed in this catalog. Obtain QA/images from the two upstream datasets, not from the M4-RAG corpus-only Hugging Face repository. Its current metadata lists 306,794 CVQA-domain and 223,468 WorldCuisines-domain Wikipedia article records; the split named train is a source-corpus split, not supervised QA training. Use the separate evaluation scripts and specified multiple-choice/open-ended answer scoring, reporting language, prompt, retrieval and oracle-caption conditions. Answer-string containment in retrieved chunks is a diagnostic, not independently annotated evidence qrels. The corpus card specifies CC-BY-SA-4.0; QA, images and code retain separate terms. Do not equate this suite with newly created native QA or exhaustive cross-language relevance judgments.

## Official sources

- [Official resource](https://github.com/davidanugraha/M4-RAG)
- [Paper](https://openaccess.thecvf.com/content/CVPR2026/html/Anugraha_M4-RAG_A_Massive-Scale_Multilingual_Multi-Cultural_Multimodal_RAG_CVPR_2026_paper.html)
- paper: [source](https://openaccess.thecvf.com/content/CVPR2026/html/Anugraha_M4-RAG_A_Massive-Scale_Multilingual_Multi-Cultural_Multimodal_RAG_CVPR_2026_paper.html) — supports `name`, `summary`, `protocol`
- repository: [source](https://github.com/davidanugraha/M4-RAG) — supports `protocol`
- dataset_card: [source](https://huggingface.co/datasets/davidanugraha/M4-RAG) — supports `protocol`
- repository: [source](https://github.com/davidanugraha/M4-RAG/blob/main/src/evaluation/eval_cvqa.py) — supports `protocol`
