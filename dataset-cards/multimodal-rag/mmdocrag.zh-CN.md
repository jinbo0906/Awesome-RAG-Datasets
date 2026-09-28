<!-- Generated from catalog/datasets/mmdocrag.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# MMDocRAG

[English](mmdocrag.md)

多页多模态文档问答，包含跨模态证据链和摘录选择。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `multimodal_rag` |
| 任务 | page_retrieval, layout_retrieval, visual_qa, attribution |
| 模态 | text, image, table, chart, layout |
| 已发布真值标注层级 | page, quote, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

问题锚定于含文本和图像摘录的长文档，并配有刻意设计的困难负例摘录。

发布规模：项目发布版从 222 份长文档构建了 4,055 个问答对。

## 真值与评测

跨页、跨模态证据链支持摘录选择和带引用回答的评测。

官方指标：quote_selection_f1, answer_quality。

评测协议：将检索与摘录选择结果同多模态回答质量分开报告。

## 适用场景

- 跨页证据选择
- 文本与图像摘录整合
- 困难负例下的鲁棒性

## 限制与注意事项

- 部分构建过程使用生成问题和解析器衍生摘录；人工核验子集应单独报告

## 获取方式与来源

- [官方资源](https://mmdocrag.github.io/MMDocRAG/)
- [论文](https://arxiv.org/abs/2505.16470)
- [数据](https://github.com/MMDocRAG/MMDocRAG)
- official：[来源](https://mmdocrag.github.io/MMDocRAG/) — 支持字段 `summary`、`data.size`、`ground_truth.description`、`evaluation.protocol`
- paper：[来源](https://proceedings.neurips.cc/paper_files/paper/2025/file/1a93178950e92fd2e7b7448f7d68fd7d-Paper-Datasets_and_Benchmarks_Track.pdf) — 支持字段 `data.description`、`classification.modalities`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
