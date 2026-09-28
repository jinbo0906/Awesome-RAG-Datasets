<!-- Generated from catalog/datasets/heteqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# HeteQA

[English](heteqa.md)

与 TableRAG 方法一起提出的异构文本—表格问答数据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `table_rag` |
| 任务 | text_table_reasoning, table_qa |
| 模态 | text, table |
| 已发布真值标注层级 | table, paragraph, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

发布数据将问题与表格、正文混合证据配对，用于异构文档推理。


## 真值与评测

在把行或单元格坐标视为真值前，应先核查发布文件中的证据 ID。

官方指标：answer_accuracy。

评测协议：同时与表格感知检索和纯文本检索基线比较。

## 适用场景

- 混合表格与文本检索
- 测试与正文关联的表格运算

## 限制与注意事项

- 数据规模较小时应提供置信区间和外部留出集验证

## 获取方式与来源

- [官方资源](https://github.com/yxh-y/TableRAG)
- [论文](https://aclanthology.org/2025.emnlp-main.710/)
- repository：[来源](https://github.com/yxh-y/TableRAG) — 支持字段 `summary`、`data.description`、`evaluation.protocol`
- paper：[来源](https://aclanthology.org/2025.emnlp-main.710/) — 支持字段 `classification.tasks`、`use.best_for`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
