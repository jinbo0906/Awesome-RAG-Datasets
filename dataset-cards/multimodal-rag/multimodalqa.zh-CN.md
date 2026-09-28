<!-- Generated from catalog/datasets/multimodalqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# MultiModalQA

[English](multimodalqa.md)

需要联合推理文本、表格和图像的问题，提供支持上下文 ID。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `multimodal_rag` |
| 任务 | multi_hop_qa, text_table_reasoning, visual_qa |
| 模态 | text, table, image |
| 已发布真值标注层级 | document, table, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

发布版包含 29,918 个样本，以及独立的文本、表格和图像上下文文件；测试集答案及支持上下文未公开。


## 真值与评测

支持上下文条目标明来源文档 ID 和模态部分，包括中间答案上下文；不能据此假定有统一的边界框或单元格真值。

官方指标：answer_em, answer_f1。

评测协议：将上下文检索与最终回答分开测量，并保留支持上下文 ID 及隐藏测试集协议。

## 适用场景

- 跨模态多跳推理
- 汇集文本—表格—图像证据

## 限制与注意事项

- 来源级标签不能识别每个相关单元格或图像区域

## 获取方式与来源

- [官方资源](https://github.com/allenai/multimodalqa)
- [论文](https://arxiv.org/abs/2104.06039)
- repository：[来源](https://github.com/allenai/multimodalqa) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
