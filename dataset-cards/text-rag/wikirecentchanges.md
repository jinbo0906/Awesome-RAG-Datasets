<!-- Generated from catalog/datasets/wikirecentchanges.yaml. Edit the YAML source. -->
# WikiRecentChanges

[简体中文](wikirecentchanges.zh-CN.md)

Stable versus updated facts with true and counterfactual paragraphs for temporal context-memory conflict tests.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-01 |
| RAG role | `auxiliary` |
| Primary category | `text_rag` |
| Tasks | time_sensitive_qa, rag_robustness |
| Modalities | text |
| Gold annotation levels | answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The author repository publishes final mutable and stable CSVs with questions, answers, counterfactual answers, and true/counterfactual context paragraphs. Wikidata relations seed the facts; the native test supplies paragraphs rather than searching an open knowledge graph.

Published scale: Released mutable_final.csv has 2,330 rows and stable_final.csv has 2,381 rows, for 4,711 final examples; this differs from pre-filter seed-fact counts.
Splits: Mutable facts changed in 2025 versus stable facts; these are diagnostic strata, not train/test partitions.
Format: CSV plus dataset-reconstruction and evaluation scripts.

## Ground truth and evaluation

Wikidata-derived factual answers are paired with model-generated counterfactuals and paragraphs. True/counterfactual input conditions and stable/updated fact types enable controlled conflict tests; no native open-corpus relevance judgments or graph evidence paths are released as this task's gold.

Official metrics: OpenEval, answer_match, context_acceptance_rate, temporal_reasoning_detection.

Protocol: Cross fact type with no-context, true-context and counterfactual-context conditions, retaining model knowledge-cutoff and date prompts. Compare factual, counterfactual and closed-book answers separately. OpenEval uses a model judge, Match is a relaxed answer match, and the paper's context-acceptance rate is a marginal change against its specified baseline, not raw answer accuracy.

## When to use it

- Separating temporal conflict recognition from correct final decisions
- Testing reliance on generated evidence versus parametric memory

## Limitations and cautions

- The 2025 update target must be reconsidered for newer model cutoffs
- Supplied synthetic paragraphs do not evaluate retrieval or continuous index updates
- README sample.csv examples do not identify the actual released final CSV filenames
- No explicit dataset license was confirmed in the author repository

## Access and sources

- [Official resource](https://github.com/jwallat/knowledge-conflicts-mutability)
- [Paper](https://aclanthology.org/2026.findings-acl.103/)
- [Data](https://github.com/jwallat/knowledge-conflicts-mutability/tree/main/data/recent_changes)
- paper: [source](https://aclanthology.org/2026.findings-acl.103.pdf) — supports `summary`, `classification`, `ground_truth`, `evaluation.official_metrics`, `evaluation.protocol`, `use`
- repository: [source](https://github.com/jwallat/knowledge-conflicts-mutability) — supports `data.description`, `data.splits`, `data.format`, `data.corpus`, `access.license`, `access.gated`, `evaluation.evaluator`, `use.caveats`
- repository: [source](https://raw.githubusercontent.com/jwallat/knowledge-conflicts-mutability/main/data/recent_changes/mutable_final.csv) — supports `data.size`, `data.queries`, `data.answers`
- repository: [source](https://raw.githubusercontent.com/jwallat/knowledge-conflicts-mutability/main/data/recent_changes/stable_final.csv) — supports `data.size`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
