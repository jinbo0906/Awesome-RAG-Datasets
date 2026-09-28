<!-- Generated from catalog/datasets/ragbench.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# RAGBench

[English](ragbench.md)

包含生成回答和细粒度上下文支持标签的 RAG 评测集合。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | attribution, fact_verification |
| 模态 | text |
| 已发布真值标注层级 | sentence, fact_citation, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | CC BY 4.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

托管版本含 12 个子集，提供问题、已检索文档、生成回答和句子级支持标注。


## 真值与评测

通过支持关系键连接回答句子与文档句子，可评测回答对上下文的遵循与利用。

官方指标：adherence, relevance, utilization, completeness。

评测协议：除非另行重建外部语料，否则应把发布的检索文档视为固定上下文池。

## 适用场景

- 回答依据诊断
- 句子级支持关系归因

## 限制与注意事项

- 混合来源及模型辅助标注不能称为完全人工的金标准

## 获取方式与来源

- [官方资源](https://huggingface.co/datasets/galileo-ai/ragbench)
- [论文](https://arxiv.org/abs/2407.11005)
- dataset_card：[来源](https://huggingface.co/datasets/galileo-ai/ragbench) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`access.license`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
