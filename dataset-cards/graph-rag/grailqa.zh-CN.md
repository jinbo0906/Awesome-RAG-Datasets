<!-- Generated from catalog/datasets/grailqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# GrailQA

[English](grailqa.md)

提供可执行逻辑形式与泛化能力划分的知识库问答数据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `graph_rag` |
| 任务 | graph_qa, graph_reasoning |
| 模态 | graph, text |
| 已发布真值标注层级 | graph_path, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

问题映射到 Freebase 答案及 SPARQL、S 表达式等逻辑形式；复现检索需要兼容的 Freebase 快照。


## 真值与评测

逻辑形式指定可执行的图推理结构，但不一定对应唯一的已检索子图。

官方指标：exact_match, answer_f1。

评测协议：保留原有的独立同分布、组合泛化和零样本划分，并说明知识库版本。

## 适用场景

- 图推理泛化测试
- 感知逻辑形式的检索

## 限制与注意事项

- 知识库问答逻辑形式不会自动成为自然语言 GraphRAG 的引用路径

## 获取方式与来源

- [官方资源](https://github.com/dki-lab/GrailQA)
- repository：[来源](https://github.com/dki-lab/GrailQA) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
