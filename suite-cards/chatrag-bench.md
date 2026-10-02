<!-- Generated from catalog/suites/chatrag-bench.yaml. Edit the YAML source. -->
# ChatRAG Bench

[简体中文](chatrag-bench.zh-CN.md)

Conversational document QA suite derived from ten datasets, covering retrieval, tables, arithmetic and unanswerable questions.

Review status: `source_checked`. This is a benchmark suite or protocol, not one standalone dataset.

## Indexed components

- [doc2dial](../dataset-cards/text-rag/doc2dial.md)
- [qrecc](../dataset-cards/text-rag/qrecc.md)
- [topiocqa](../dataset-cards/text-rag/topiocqa.md)
- [sqa](../dataset-cards/table-rag/sqa.md)
- [convfinqa](../dataset-cards/table-rag/convfinqa.md)

## Protocol and interpretation

This catalog links five upstream source datasets, not all ten standardized evaluation configurations. The release also includes QuAC, INSCIT, CoQA, HybriDialogue and DoQA. Use the released ctxs/messages/answers and evaluation scripts; document whether context is supplied or retrieved. Report per-task scores and the average with and without HybriDialogue where training overlap applies; evaluate answerable/unanswerable detection separately. Converted splits and F1 settings are not interchangeable with upstream native evaluations. Original dataset licenses apply.

## Official sources

- [Official resource](https://huggingface.co/datasets/nvidia/ChatRAG-Bench)
- [Paper](https://arxiv.org/abs/2401.10225)
- dataset_card: [source](https://huggingface.co/datasets/nvidia/ChatRAG-Bench) — supports `summary`, `components`, `protocol`
