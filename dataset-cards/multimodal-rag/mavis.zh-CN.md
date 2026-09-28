<!-- Generated from catalog/datasets/mavis.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# MAVIS

[English](mavis.md)

面向长篇回答的视觉问答 benchmark，提供多模态文档的事实级引用。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `multimodal_rag` |
| 任务 | visual_qa, attribution, long_form_qa |
| 模态 | text, image |
| 已发布真值标注层级 | document, fact_citation, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

输入图像和问题与多模态检索语料、带引用的长篇回答配对。

发布规模：作者报告了 15.7 万个视觉问答样本。

## 真值与评测

回答中的事实级引用指向提供支持的多模态文档。

官方指标：groundedness, completeness, relevance, fluency。

评测协议：分别评测图像文档与文本文档对回答的支持程度。

## 适用场景

- 事实级多模态引用
- 生成有依据的长篇回答

## 限制与注意事项

- 文档级引用不一定提供边界框级证据标注

## 获取方式与来源

- [官方资源](https://github.com/seokwon99/MAVIS)
- [论文](https://ojs.aaai.org/index.php/AAAI/article/view/40585)
- [数据](https://huggingface.co/datasets/seokwon99/MAVIS)
- repository：[来源](https://github.com/seokwon99/MAVIS) — 支持字段 `summary`、`data.description`、`evaluation.official_metrics`
- paper：[来源](https://ojs.aaai.org/index.php/AAAI/article/view/40585) — 支持字段 `data.size`、`ground_truth.description`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
