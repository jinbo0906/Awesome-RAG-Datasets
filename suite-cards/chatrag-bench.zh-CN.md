<!-- Generated from catalog/suites/chatrag-bench.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# ChatRAG Bench

[English](chatrag-bench.md)

由十个数据集改造的会话式文档问答套件，覆盖检索、表格、算术推理和不可回答问题。

审查状态：`source_checked`。这是评测套件或协议，不是单一独立数据集。

## 已收录的组成数据集

- [doc2dial](../dataset-cards/text-rag/doc2dial.zh-CN.md)
- [qrecc](../dataset-cards/text-rag/qrecc.zh-CN.md)
- [topiocqa](../dataset-cards/text-rag/topiocqa.zh-CN.md)
- [sqa](../dataset-cards/table-rag/sqa.zh-CN.md)
- [convfinqa](../dataset-cards/table-rag/convfinqa.zh-CN.md)

## 协议与结果解释

本目录链接五个原始来源数据集，并非全部十个标准化评测配置；发布版本还含 QuAC、INSCIT、CoQA、HybriDialogue 和 DoQA。使用发布的 ctxs/messages/answers 和评分脚本，注明上下文是给定还是检索所得。有训练重叠时分别报告含与不含 HybriDialogue 的平均分，并单独评测可回答与不可回答判断。改造版划分及 F1 设置不能与上游原生评测互换，许可沿用各原始数据集。

## 官方来源

- [官方资源](https://huggingface.co/datasets/nvidia/ChatRAG-Bench)
- [论文](https://arxiv.org/abs/2401.10225)
- dataset_card：[来源](https://huggingface.co/datasets/nvidia/ChatRAG-Bench) — 支持字段 `summary`、`components`、`protocol`
