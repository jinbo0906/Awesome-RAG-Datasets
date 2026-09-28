<!-- Generated from catalog/datasets/wikitablequestions.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# WikiTableQuestions

[English](wikitablequestions.md)

针对已提供的半结构化维基百科 HTML 表格提出的复杂问题。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `table_rag` |
| 任务 | table_qa |
| 模态 | text, table |
| 已发布真值标注层级 | table, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

每题与维基百科表格及答案配对；官方评测器检查答案指称结果。


## 真值与评测

提供表格和答案，但不保证有最小支持单元格集合或开放表格检索 qrel。

官方指标：denotation_accuracy。

评测协议：做表格检索时，应构建固定表格语料及 qrels，且不能在输入中泄露配对表格。

## 适用场景

- 检索后的表格推理
- 答案指称结果评测

## 限制与注意事项

- 原生任务直接提供表格，不是开放表格检索 benchmark

## 获取方式与来源

- [官方资源](https://github.com/ppasupat/WikiTableQuestions)
- repository：[来源](https://github.com/ppasupat/WikiTableQuestions) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
