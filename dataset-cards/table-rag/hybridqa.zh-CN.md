<!-- Generated from catalog/datasets/hybridqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# HybridQA

[English](hybridqa.md)

结合维基百科表格行与链接段落证据的多跳问答数据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `table_rag` |
| 任务 | table_qa, text_table_reasoning |
| 模态 | table, text |
| 已发布真值标注层级 | table, paragraph, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

问题要求在固定发布语料中查找表格，再结合所链接的正文段落推理。


## 真值与评测

表格与链接段落之间的关联支持跨结构推理协议。

官方指标：answer_em, answer_f1。

评测协议：分别比较检索与回答阶段，并保留表格到段落的链接。

## 适用场景

- 表格—文本证据关联
- 跨结构多跳推理

## 限制与注意事项

- 将表格展平为纯文本可能丢失行与表头的关联

## 获取方式与来源

- [官方资源](https://github.com/wenhuchen/HybridQA)
- [论文](https://aclanthology.org/2020.findings-emnlp.91/)
- repository：[来源](https://github.com/wenhuchen/HybridQA) — 支持字段 `summary`、`data.description`、`ground_truth.description`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
