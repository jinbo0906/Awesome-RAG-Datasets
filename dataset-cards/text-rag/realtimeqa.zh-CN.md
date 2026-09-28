<!-- Generated from catalog/datasets/realtimeqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# RealTime QA

[English](realtimeqa.md)

定期发布的时事问答，包含带日期的问题和检索基线。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `text_rag` |
| 任务 | time_sensitive_qa |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

官方平台每周发布约 30 个问题、历史问题文件，以及 Google Custom Search/DPR 基线检索结果；网页和新闻来源位于外部且持续变化。


## 真值与评测

带日期的答案可用于时间敏感问答；发布的搜索结果是基线输出，而非每轮都有的来源坐标证据真值。

官方指标：answer_accuracy。

评测协议：标明问题所属周和答案截止时间，并记录模型看到的是同期还是更晚的网页证据；不控制来源可用性时不要合并不同周的结果。

## 适用场景

- 时间敏感 RAG
- 测试会变化的事实答案

## 限制与注意事项

- 不存在单一永久不变的检索语料
- 搜索基线输出不是通用证据标签

## 获取方式与来源

- [官方资源](https://github.com/realtimeqa/realtimeqa_public)
- repository：[来源](https://github.com/realtimeqa/realtimeqa_public) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
