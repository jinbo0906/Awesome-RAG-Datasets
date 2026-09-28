<!-- Generated from catalog/datasets/slidevqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# SlideVQA

[English](slidevqa.md)

多图像幻灯片问答，提供证据页选择和文档版面边界框。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `multimodal_rag` |
| 任务 | page_retrieval, visual_qa |
| 模态 | text, image, layout, chart |
| 已发布真值标注层级 | page, bbox, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

来源报告跨幻灯片的 14,484 个问答对和 890,945 个版面边界框；Hugging Face 数据包不含 OCR 与边界框数据。


## 真值与评测

问答记录给出 evidence_pages 和答案；边界框文件标注幻灯片版面对象，但这些框并非自动对应每题的证据。

官方指标：evidence_selection, answer_accuracy。

评测协议：分别评测证据页选择与回答生成，并说明是否使用 OCR 和边界框文件。

## 适用场景

- 跨幻灯片证据检索
- 感知版面的视觉问答

## 限制与注意事项

- 不能把版面框误当作逐题金标准区域
- 部分上游幻灯片 URL 已不可用

## 获取方式与来源

- [官方资源](https://github.com/nttmdlab-nlp/SlideVQA)
- repository：[来源](https://github.com/nttmdlab-nlp/SlideVQA) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.protocol`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
