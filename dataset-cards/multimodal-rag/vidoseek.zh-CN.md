<!-- Generated from catalog/datasets/vidoseek.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# ViDoSeek

[English](vidoseek.md)

在大型 PDF 集合上评测视觉文档检索与回答的数据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `multimodal_rag` |
| 任务 | page_retrieval, visual_qa |
| 模态 | text, image, table, layout |
| 已发布真值标注层级 | page, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

查询记录提供参考答案、原始文件及参考页码等元数据。


## 真值与评测

查询元数据标识参考页面，可用于页面级检索评分。

官方指标：page_recall, answer_accuracy。

评测协议：将找回页面的准确性与最终回答质量区分开。

## 适用场景

- 跨大量页面的视觉文档 RAG
- 迭代式证据检索

## 限制与注意事项

- 页面标签本身不指定精确图形或单元格边界

## 获取方式与来源

- [官方资源](https://github.com/Alibaba-NLP/ViDoRAG)
- [论文](https://arxiv.org/abs/2502.18017)
- repository：[来源](https://github.com/Alibaba-NLP/ViDoRAG) — 支持字段 `summary`、`data.description`、`ground_truth.description`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
