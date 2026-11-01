<!-- Generated from catalog/datasets/browsecomp.yaml. Edit the YAML source. -->
# BrowseComp

[简体中文](browsecomp.zh-CN.md)

Live-web browsing questions with short reference answers, testing persistent search for obscure multi-step facts.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `rag_native` |
| Primary category | `text_rag` |
| Tasks | agentic_search, multi_hop_qa |
| Modalities | text |
| Gold annotation levels | answer |
| Evidence provenance | human |
| Corpus / queries / answers | external / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

Human trainers construct hard-to-locate factual questions for agents using web search and browsing. The public reference loader reads obfuscated questions and answers from an author-hosted CSV; it does not provide a fixed web corpus.

Published scale: 1,266 evaluation questions; the paper's separate human verification campaign covers 1,255 problems.
Splits: Public test release; BrowseComp-Plus is a separate fixed-corpus adaptation, not the same evaluation setting.
Format: Obfuscated CSV with an author-provided reference loader..

## Ground truth and evaluation

Trainers supply short, intended-to-be-unambiguous answers. This release does not establish exhaustive document qrels, source spans or gold browsing trajectories.

Official metrics: accuracy, calibration_error.

Protocol: Use the paper's answer-equivalence judge and confidence-calibration protocol; report browsing tools, search provider, date and inference budget. Do not equate answer accuracy with evidence recall. The archived reference grader requires version-specific inspection before use; it has not been reproduced here.

## When to use it

- Persistent multi-step web search under a controlled budget
- Comparing live-web agents against fixed-corpus BrowseComp-Plus

## Limitations and cautions

- No fixed source corpus or retrieval qrels; web and search-provider drift affect reproducibility
- Original authors request that benchmark examples not be published in plaintext; no question or answer examples are mirrored here
- The simple-evals code is MIT but a separate data license was not confirmed; its README says active updates ended in July 2025

## Access and sources

- [Official resource](https://openai.com/index/browsecomp/)
- [Paper](https://arxiv.org/abs/2504.12516)
- [Data](https://openaipublic.blob.core.windows.net/simple-evals/browse_comp_test_set.csv)
- official: [source](https://openai.com/index/browsecomp/) — supports `summary`, `data.description`, `data.size`, `ground_truth.description`, `ground_truth.provenance`, `use.caveats`
- paper: [source](https://arxiv.org/html/2504.12516) — supports `classification.rag_role`, `evaluation.official_metrics`, `evaluation.protocol`
- repository: [source](https://github.com/openai/simple-evals/blob/main/browsecomp_eval.py) — supports `data.format`, `data.splits`, `access.data`, `evaluation.evaluator`, `evaluation.protocol`
- repository: [source](https://github.com/openai/simple-evals) — supports `access.license`, `use.caveats`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
