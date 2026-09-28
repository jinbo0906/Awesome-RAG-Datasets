<!-- Generated from catalog/datasets/m3docvqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# M3DocVQA

[English](m3docvqa.md)

面向多页、多文档 PDF 集合的开放域视觉文档问答数据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `multimodal_rag` |
| 任务 | page_retrieval, visual_qa |
| 模态 | text, image, table, chart |
| 已发布真值标注层级 | page, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

M3DocRAG 项目发布的开放域集合包含超过 3,000 份 PDF 和 40,000 页。


## 真值与评测

先在文档或页面层级评测相关性，再进行视觉回答生成。

官方指标：retrieval_recall, answer_accuracy。

评测协议：保留 PDF 身份与页码；不要把封闭域 MP-DocVQA 与开放域 M3DocVQA 混为一谈。

## 适用场景

- 开放域多页检索
- 发现 OCR 遗漏的视觉证据

## 限制与注意事项

- 来源仓库于 2026 年 7 月归档；应记录所用的准确快照

## 获取方式与来源

- [官方资源](https://github.com/bloomberg/m3docrag)
- [论文](https://arxiv.org/abs/2411.04952)
- repository：[来源](https://github.com/bloomberg/m3docrag) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
