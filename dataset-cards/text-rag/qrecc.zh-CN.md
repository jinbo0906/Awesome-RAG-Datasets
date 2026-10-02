<!-- Generated from catalog/datasets/qrecc.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# QReCC

[English](qrecc.md)

开放域多轮问答，提供人工问题改写、答案与来源 URL，并发布网页检索集合。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | conversational_qa, query_rewriting, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | document, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | CC-BY-SA-3.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

对话扩展自 QuAC、TREC CAsT 和 Natural Questions。每轮包含上下文、独立问题改写、答案及来源 URL；语料约有 1,000 万个网页，分成 5,400 万个段落。

发布规模：约 1.4 万段对话与 8.1 万个问答对。

## 真值与评测

人工改写和答案链接到来源网页。原始检索评测器可通过答案重合度阈值判断段落相关性，不应将其描述为完整的人工段落相关性标注。

官方指标：MRR, Recall@k, exact_match, token_f1。

评测协议：保留对话顺序，区分金标准改写与模型改写。报告原始检索的答案重合度阈值，或替换 qrels 的来源，并单独评测回答质量。

## 适用场景

- 依赖上下文的问题改写
- 分析多轮对话中的检索与回答错误

## 限制与注意事项

- 来源 URL 不构成完整的段落级相关性真值
- 使用金标准改写的检索与端到端多轮问答属于不同设置

## 获取方式与来源

- [官方资源](https://github.com/apple-aiml-research/ml-qrecc)
- [论文](https://aclanthology.org/2021.naacl-main.44/)
- repository：[来源](https://github.com/apple-aiml-research/ml-qrecc) — 支持字段 `summary`、`data.description`、`data.size`、`ground_truth.description`、`access.license`
- repository：[来源](https://github.com/apple-aiml-research/ml-qrecc/blob/main/utils/evaluate_retrieval.py) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`
- repository：[来源](https://github.com/apple-aiml-research/ml-qrecc/blob/main/utils/evaluate_qa.py) — 支持字段 `evaluation.official_metrics`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
