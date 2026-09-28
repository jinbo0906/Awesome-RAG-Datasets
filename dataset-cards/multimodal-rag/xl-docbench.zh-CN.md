<!-- Generated from catalog/datasets/xl-docbench.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# XL-DocBench

[English](xl-docbench.md)

在超长文档上进行专家核验问答，提供证据页与摘录。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `multimodal_rag` |
| 任务 | long_context_qa, page_retrieval, evidence_retrieval |
| 模态 | text, image, table, layout |
| 已发布真值标注层级 | page, quote, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

发布版引用公开来源文档 URL，而非打包全部 PDF；包含单文档和跨文档问答。

发布规模：共 1,519 个问题，其中 1,354 个单文档、165 个跨文档问题；对应 331 条文档记录。

## 真值与评测

可回答样本包含人工标注的证据页面和带来源定位信息的证据摘录。

官方指标：answer_accuracy, evidence_retrieval。

评测协议：比较解析器或分块器前，应先获取并固定带版本的来源 PDF。

## 适用场景

- 超长文档检索
- 跨文档证据定位

## 限制与注意事项

- 外部文档 URL 可能漂移；复现需要固定快照及哈希

## 获取方式与来源

- [官方资源](https://officeintelligence.github.io/xl-docbench/)
- [数据](https://huggingface.co/datasets/anonymous12123/XL-DocBench)
- dataset_card：[来源](https://huggingface.co/datasets/anonymous12123/XL-DocBench) — 支持字段 `data.description`、`data.size`、`ground_truth.description`
- official：[来源](https://officeintelligence.github.io/xl-docbench/) — 支持字段 `summary`、`use.best_for`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
