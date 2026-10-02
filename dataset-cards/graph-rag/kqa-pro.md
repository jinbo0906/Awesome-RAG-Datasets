<!-- Generated from catalog/datasets/kqa-pro.yaml. Edit the YAML source. -->
# KQA Pro

[简体中文](kqa-pro.zh-CN.md)

Complex knowledge-base QA with explicit KoPL programs and SPARQL queries over a provided Wikidata subset.

| Field | Value |
|---|---|
| Catalog status | `source_checked` |
| Source checked on | 2026-10-02 |
| RAG role | `rag_convertible` |
| Primary category | `graph_rag` |
| Tasks | graph_qa, graph_reasoning |
| Modalities | graph, text |
| Gold annotation levels | graph_path, answer |
| Evidence provenance | mixed |
| Corpus / queries / answers | provided / provided / provided |
| Original data license | unknown |

`source_checked` means the cited fields were reviewed against upstream sources; it does not imply that the dataset was downloaded or its evaluator reproduced.

## Data and construction

The official download contains kb.json and train/val/test files; questions include executable KoPL and SPARQL supervision.

Published scale: 117,970 questions.
Format: JSON.

## Ground truth and evaluation

Composed programs and SPARQL define operations over the KB; crowdsourcing paraphrases the questions. A program may use comparison or set operations rather than a simple linear gold path.

Official metrics: answer_accuracy.

Protocol: Execute or compare answers on the released KB and official split; report reasoning-skill categories and whether gold programs or topic entities are available.

## When to use it

- Compositional graph reasoning and program execution
- Diagnostics by reasoning skill

## Limitations and cautions

- KoPL/SPARQL supervision is not automatically a natural-language GraphRAG citation path
- Keep the released Wikidata subset rather than silently replacing it with a live graph

## Access and sources

- [Official resource](https://github.com/shijx12/KQAPro_Baselines)
- [Paper](https://aclanthology.org/2022.acl-long.422/)
- repository: [source](https://github.com/shijx12/KQAPro_Baselines) — supports `data.description`, `data.format`
- paper: [source](https://aclanthology.org/2022.acl-long.422.pdf) — supports `summary`, `classification`, `data.size`, `ground_truth`, `evaluation`, `use`

Original dataset licenses and access terms are set by their owners. A catalog entry does not grant redistribution rights.
