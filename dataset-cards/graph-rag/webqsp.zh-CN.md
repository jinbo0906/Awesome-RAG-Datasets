<!-- Generated from catalog/datasets/webqsp.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# WebQuestionsSP

[English](webqsp.md)

面向 Freebase 的自然语言问题，含答案与 SPARQL 语义解析。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `graph_rag` |
| 任务 | graph_qa, graph_reasoning |
| 模态 | text, graph |
| 已发布真值标注层级 | graph_path, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

微软发布问题、语义解析和评测器；4,737 个问题有完整 SPARQL 解析，另有 1,073 个问题仅部分标注。


## 真值与评测

可执行 SPARQL 解析定义图操作，但不一定是唯一的已检索子图或引用路径。

官方指标：answer_f1。

评测协议：指明 Freebase 快照，并区分完整解析与部分标注样本。

## 适用场景

- 知识图谱问答
- 语义解析引导的检索

## 限制与注意事项

- 复现结果依赖兼容的 Freebase 快照
- GraphRAG 引用证据需要额外标注

## 获取方式与来源

- [官方资源](https://www.microsoft.com/en-us/download/details.aspx?id=52763)
- official：[来源](https://www.microsoft.com/en-us/download/details.aspx?id=52763) — 支持字段 `summary`、`data.description`、`ground_truth.description`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
