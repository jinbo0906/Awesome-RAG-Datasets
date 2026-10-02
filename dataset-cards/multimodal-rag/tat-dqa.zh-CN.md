<!-- Generated from catalog/datasets/tat-dqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# TAT-DQA

[English](tat-dqa.md)

结合表格与正文证据、要求离散数值推理的金融文档图像问答。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `multimodal_rag` |
| 任务 | visual_qa, text_table_reasoning, table_qa |
| 模态 | text, image, table, layout |
| 已发布真值标注层级 | span, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | CC-BY-4.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

TAT-QA 的文档图像扩展版本，提供 PDF、转换后的文字块和框、问答、答案尺度与计算式。作者仓库说明测试集真值于 2024 年 1 月公开。

发布规模：16,558 个问题，对应 2,758 份文档、3,067 页；每份已提供文档最多三页。
数据划分：训练集、开发集和测试集。
格式：PDFs and JSON document blocks plus QA annotations.。

## 真值与评测

问答标注含答案形式、尺度、计算式和 OCR 文本块到跨度的映射。可选支持事实由启发式方法生成，文本块框来自 PDF 提取或 OCR；它们都不是通用的人工表格单元格或检索真值。

官方指标：exact_match, F1。

评测协议：使用官方包含数值及尺度处理的评分。检索改造应保留文档块与操作数映射；原始短文档问答不能直接视为全语料金融 RAG。

## 适用场景

- 文档图像中的数值推理
- 保留表格—文本操作数和来源块映射

## 限制与注意事项

- TAT-QA 与 TAT-DQA 是不同版本
- 启发式事实与 OCR 框须和人工问答分别标明来源

## 获取方式与来源

- [官方资源](https://nextplusplus.github.io/TAT-DQA/)
- [论文](https://arxiv.org/abs/2207.11871)
- [数据](https://github.com/NExTplusplus/TAT-DQA)
- official：[来源](https://nextplusplus.github.io/TAT-DQA/) — 支持字段 `summary`、`data.description`、`data.size`、`data.splits`、`ground_truth.description`、`evaluation.official_metrics`、`access.license`
- repository：[来源](https://github.com/NExTplusplus/TAT-DQA) — 支持字段 `data.description`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
