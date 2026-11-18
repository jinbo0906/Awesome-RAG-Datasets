<!-- Generated from catalog/datasets/ragcap-bench.yaml. Edit the YAML source. -->
# RAGCap-Bench

[简体中文](ragcap-bench.zh-CN.md)

Multiple-choice process diagnostics for planning, evidence extraction, grounded reasoning and noise robustness in search agents.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-11-18 |
| RAG role | `auxiliary` |
| Primary category | `text_rag` |
| Tasks | agentic_search, rag_robustness |
| Modalities | text |
| Gold annotation levels | answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | not_provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

AACL 2026 Long paper turns intermediate execution outputs from deep-research workflows into controlled choice tasks. The release supplies questions with context/options and prompts for six sub-capabilities.

Published scale: 255 released items in six task CSVs. Planning divergence/convergence 25/51, evidence extraction 69, grounded reasoning 53, noise abstention/reliability 37/20.
Splits: One evaluation collection partitioned by sub-capability. Keep prompt conditions separate.
Format: CSV with multiple-choice items and Python prompt definitions.

## Ground truth and evaluation

Correct choices are curated from intermediate traces and error-guided or template-based alternatives. The localized choice task examines one aspect of an agent step with context supplied.

Official metrics: exact_match, option_F1.

Protocol: Parse selected options and score option-set exact match and macro F1 by task under the specified bare or informative prompt. The separate WebThinker experiments report downstream pass@1 on BrowseComp and other web QA benchmarks.

## When to use it

- Probing which intermediate tasks fail before end-to-end runs
- Comparing model capability under matched supplied contexts

## Limitations and cautions

- Multiple-choice scores do not directly measure free-form planning or tool execution
- Logs serve as construction inputs without a released open retrieval index
- The repository publishes prompt definitions without a standalone scorer

## Access and sources

- [Official resource](https://github.com/jingru-lin/RAGCap-Bench)
- [Paper](https://aclanthology.org/2026.aacl-long.245/)
- [Data](https://github.com/jingru-lin/RAGCap-Bench/tree/99ed0d915cb2816a1182ef1a2a85a45d6fb6afde/data)
- paper: [source](https://aclanthology.org/2026.aacl-long.245.pdf) — supports `summary`, `classification`, `data.description`, `ground_truth`, `evaluation.official_metrics`, `evaluation.protocol`, `use`
- repository: [source](https://github.com/jingru-lin/RAGCap-Bench/tree/99ed0d915cb2816a1182ef1a2a85a45d6fb6afde/data) — supports `data.size`, `data.splits`, `data.format`, `access.data`
- repository: [source](https://github.com/jingru-lin/RAGCap-Bench/tree/main/prompts) — supports `evaluation.protocol`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
