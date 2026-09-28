<!-- Generated from catalog/datasets/qasper.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# QASPER

[English](qasper.md)

以完整 NLP 研究论文为来源、带证据标注的信息寻求型问题。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | long_context_qa, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | paragraph, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

问题针对研究论文全文；答案包含抽取式、生成式、是/否及不可回答案例。


## 真值与评测

答案标注指出论文中的支持性证据片段或段落。

官方指标：answer_f1, evidence_f1。


## 适用场景

- 长文档证据定位
- 感知章节结构的分块

## 限制与注意事项

- 证据标注绑定到数据集的文本抽取结果，未必能直接映射回 PDF 坐标

## 获取方式与来源

- [官方资源](https://allenai.org/data/qasper)
- [论文](https://arxiv.org/abs/2105.03011)
- [数据](https://huggingface.co/datasets/allenai/qasper)
- repository：[来源](https://github.com/allenai/qasper-led-baseline) — 支持字段 `summary`、`evaluation.official_metrics`、`ground_truth.description`
- paper：[来源](https://arxiv.org/abs/2105.03011) — 支持字段 `data.description`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
