<!-- Generated from catalog/datasets/tabfact.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# TabFact

[English](tabfact.md)

判断自然语言主张是否得到维基百科表格蕴含或反驳的数据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `table_rag` |
| 任务 | fact_verification, table_qa |
| 模态 | text, table |
| 已发布真值标注层级 | table, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

主张与单张表格及二元标签配对；官方页面分别给出 117,854 条人工标注陈述和 118,275 行的总数，统计口径不同。


## 真值与评测

蕴含或反驳标签是真值；原生数据不保证每条主张都有支持性单元格集合。

官方指标：accuracy。

评测协议：若要评测 RAG 流水线，须明确表格检索器和表格级 qrels。

## 适用场景

- 感知表格的主张核查
- 语义与符号推理

## 限制与注意事项

- 官方 README 使用不同计数口径
- 原生任务直接提供表格而非开放检索

## 获取方式与来源

- [官方资源](https://github.com/wenhuchen/Table-Fact-Checking)
- repository：[来源](https://github.com/wenhuchen/Table-Fact-Checking) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
