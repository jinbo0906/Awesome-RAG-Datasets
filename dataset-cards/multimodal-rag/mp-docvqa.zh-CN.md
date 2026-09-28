<!-- Generated from catalog/datasets/mp-docvqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# MP-DocVQA

[English](mp-docvqa.md)

附答案所在页面监督信号的多页文档视觉问答数据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `multimodal_rag` |
| 任务 | page_retrieval, visual_qa |
| 模态 | text, image, layout |
| 已发布真值标注层级 | page, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

挑战赛将文档图像问答扩展到多页文档；官方数据和评测通过 DocVQA/RRC 挑战平台提供。


## 真值与评测

答案页面可评测页面选择，但不能据此建立最小区域或跨页证据链真值。

官方指标：anls, page_accuracy。

评测协议：区分单文档内的页面选择与开放语料中的文档检索，并使用官方挑战赛划分。

## 适用场景

- 单文档内页面选择
- 比较 OCR 与视觉问答

## 限制与注意事项

- 默认并非开放式多文档检索
- 答案页面真值不是针对问题的边界框

## 获取方式与来源

- [官方资源](https://rrc.cvc.uab.es/?ch=17&com=tasks)
- [论文](https://arxiv.org/abs/2212.05935)
- official：[来源](https://rrc.cvc.uab.es/?ch=17&com=tasks) — 支持字段 `summary`、`data.description`
- paper：[来源](https://arxiv.org/abs/2212.05935) — 支持字段 `ground_truth.description`、`evaluation.official_metrics`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
