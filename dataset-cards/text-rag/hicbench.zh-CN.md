<!-- Generated from catalog/datasets/hicbench.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# HiCBench

[English](hicbench.md)

面向分块研究，提供层级边界标注与证据密集型问答的 benchmark。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | evidence_retrieval, long_context_qa |
| 模态 | text, layout |
| 已发布真值标注层级 | section, paragraph, sentence, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

精选的 OHRBench 文档与层级标注、合成的高证据密度问题配对。


## 真值与评测

人工标注的多层级分块点与合成问答、相关证据来源同时存在，不能把两种标注混为一谈。

官方指标：chunking_quality, evidence_coverage, answer_quality。

评测协议：将来源层级标签与问答证据分开，并在不同上下文预算下测试。

## 适用场景

- 层级分块
- 比较不同 chunk 大小时的证据完整性

## 限制与注意事项

- 若声称可泛化，合成问题还需要独立的人工审查留出集

## 获取方式与来源

- [官方资源](https://github.com/TencentCloudADP/hichunk)
- [论文](https://aclanthology.org/2026.acl-long.1372/)
- paper：[来源](https://aclanthology.org/2026.acl-long.1372/) — 支持字段 `summary`、`data.description`、`ground_truth.description`
- repository：[来源](https://github.com/TencentCloudADP/hichunk) — 支持字段 `evaluation.protocol`、`access.official`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
