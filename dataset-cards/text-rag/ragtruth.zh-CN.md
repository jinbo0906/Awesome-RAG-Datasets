<!-- Generated from catalog/datasets/ragtruth.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# RAGTruth

[English](ragtruth.md)

在多种 RAG 式生成任务上，以人工标注生成回答中的幻觉片段。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `auxiliary` |
| 主分类 | `text_rag` |
| 任务 | hallucination_detection, attribution |
| 模态 | text |
| 已发布真值标注层级 | response_span |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | not_provided / provided / not_provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

发布版将 source_info.jsonl 与 response.jsonl 配对，每个来源产生六条模型回答。 官方仓库报告问答、摘要和数据到文本任务中共 17,790 条生成回答。生成回答是模型输出， 不是金标准答案。

格式：JSONL。

## 真值与评测

标注者记录模型回答中无来源支持片段的起止偏移、标签类型和元数据；这些回答偏移不是来源证据坐标或检索 qrels。

官方指标：尚未确认。

评测协议：按 source_id 关联回答与 source_info，保留训练/测试划分和标注版本；幻觉检测应与答案正确性或检索分开评分。

## 适用场景

- 词元或片段级幻觉检测
- 诊断缺乏依据的主张

## 限制与注意事项

- 不是端到端检索 benchmark
- 并非每条生成回答都有人工金标准答案

## 获取方式与来源

- [官方资源](https://github.com/ParticleMedia/RAGTruth)
- [论文](https://arxiv.org/abs/2401.00396)
- repository：[来源](https://github.com/ParticleMedia/RAGTruth) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
