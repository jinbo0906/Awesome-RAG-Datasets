<!-- Generated from catalog/datasets/sqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# Sequential Question Answering (SQA)

[English](sqa.md)

在已提供的维基百科 HTML 表格上进行的连续对话式问答。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `table_rag` |
| 任务 | conversational_qa, table_qa |
| 模态 | text, table |
| 已发布真值标注层级 | table_cell, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

微软研究院将 2,022 个 WikiTableQuestions 问题扩展为 6,066 组序列、17,553 个相互关联的问题。 原生任务直接提供表格；若用于 TableRAG 评测，还须定义开放式表格索引与检索负例。

发布规模：1.0 版本有 6,066 组序列和 17,553 个问题。

## 真值与评测

答案关联到单元格位置，可检查表内证据，但没有提供从多表语料检索表格的 qrel。

官方指标：answer_accuracy。

评测协议：保留问题顺序和对话上下文，并将给定表格的原生任务与自建表格检索阶段分开报告。

## 适用场景

- 多轮表格推理
- 单元格级答案定位

## 限制与注意事项

- 原始任务直接提供表格
- 在构建检索 chunks 前应按表格与问答序列划分

## 获取方式与来源

- [官方资源](https://www.microsoft.com/en-us/download/details.aspx?id=54253)
- official：[来源](https://www.microsoft.com/en-us/download/details.aspx?id=54253) — 支持字段 `summary`、`data.description`、`data.size`、`ground_truth.description`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
