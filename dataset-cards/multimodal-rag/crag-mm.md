<!-- Generated from catalog/datasets/crag-mm.yaml. Edit the YAML source. -->
# CRAG-MM

[简体中文](crag-mm.zh-CN.md)

Wearable-oriented image-grounded single- and multi-turn RAG with mock image-KG and web retrieval, abstention and conversation-level scoring.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `rag_native` |
| Primary category | `multimodal_rag` |
| Tasks | visual_qa, conversational_qa, multimodal_retrieval, rag_robustness |
| Modalities | text, image, graph |
| Gold annotation levels | answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | CC-BY-NC-4.0 stated by the author project; source images and retrieved material can retain separate rights. |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The KDD Cup 2025 challenge release includes single-turn and multi-turn questions, images or source URLs, reference answers and versioned image/web search indices. It is distinct from the earlier text-only CRAG dataset, not a renamed copy.

Published scale: Paper Table 3 reports 6,462 single-turn questions and 1,956 multi-turn conversations; these totals are not the size of each public split.
Splits: Current Hugging Face packages expose validation and public_test. The single-turn splits contain 1,938 and 1,936 rows; multi-turn splits contain 586 and 587 conversation rows respectively, checked on 2026-11-01. Challenge-private data remains separate.
Format: Hugging Face Parquet with session-level turns and answers, image fields and separately versioned search indices..

## Ground truth and evaluation

Annotators create and check answers; multi-turn seeds also use model-generated conversations. Gold answers and query/image metadata are provided, but mock retrieval output is not exhaustive evidence qrels or a minimal cross-source proof chain.

Official metrics: accuracy, missing_rate, hallucination_rate, truthfulness_score, mean_multi_turn_conversation_score.

Protocol: Fix the task's permitted image-KG/web sources and index/API versions. Score correct, abstained and wrong answers as +1, 0 and -1. Multi-turn scoring averages session scores with an early-stop rule after two failed turns; pin the evaluator because README, paper and implementation can differ on whether abstention triggers stopping. Freeze images and source snapshots rather than treating dynamism labels as live knowledge updates.

## When to use it

- Image-plus-external-knowledge dialogue with abstention
- Comparing single-source and image-plus-web RAG under realistic visual degradation

## Limitations and cautions

- KDD Cup participation does not make the introducing preprint a KDD main-track paper
- Some image assets are URLs rather than embedded binaries
- Data-card prose can lag public_test release and evaluator behavior; pin revisions
- Correct answers do not establish complete cross-source evidence retrieval

## Access and sources

- [Official resource](https://github.com/facebookresearch/CRAG-MM)
- [Paper](https://arxiv.org/abs/2510.26160)
- [Data](https://huggingface.co/crag-mm-2025)
- paper: [source](https://arxiv.org/html/2510.26160) — supports `summary`, `data.size`, `ground_truth.provenance`, `evaluation.protocol`, `use.caveats`
- repository: [source](https://github.com/facebookresearch/CRAG-MM) — supports `data.description`, `data.format`, `access.license`, `ground_truth.description`
- dataset_card: [source](https://huggingface.co/datasets/crag-mm-2025/crag-mm-single-turn-public) — supports `data.splits`, `access.gated`, `use.caveats`
- dataset_card: [source](https://huggingface.co/datasets/crag-mm-2025/crag-mm-multi-turn-public) — supports `data.splits`, `access.gated`
- repository: [source](https://github.com/facebookresearch/CRAG-MM/blob/main/evaluation/README.md) — supports `evaluation.official_metrics`, `evaluation.protocol`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
