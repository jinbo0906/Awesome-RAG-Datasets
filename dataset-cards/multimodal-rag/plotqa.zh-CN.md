<!-- Generated from catalog/datasets/plotqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# PlotQA

[English](plotqa.md)

基于科学绘图模板生成的问题，覆盖开放词汇标签与计算得到的数值答案。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `multimodal_rag` |
| 任务 | visual_qa, table_qa |
| 模态 | text, image, chart, table |
| 已发布真值标注层级 | bbox, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | CC-BY-4.0 for data; MIT for code. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

图像根据现实数据绘制，问题模板来自众包。发布版本含图像标注和两个问答版本；VisRAG 使用过滤后汇集图像的检索改造。

发布规模：224,377 张绘图；问答 v1 有 8,190,674 对，v2 有 28,952,641 对。
数据划分：原始训练集、验证集和测试集，各自提供独立版本的问答文件。
格式：PNG plots, plot annotations and QA JSON.。

## 真值与评测

问答结构包含 image_index；当答案直接出现在图中时提供 answer_bbox。计算答案可能没有框；绘图对象标注与针对问题的证据及检索相关性真值不同。

官方指标：answer_accuracy。

评测协议：固定问答版本与数值答案容差。原始问答已提供绘图，应将 VisRAG 的过滤、候选池和检索分数与原生绘图回答准确率分别报告。

## 适用场景

- 数值图表阅读与开放词汇回答
- 有条件答案框评测和明确的检索转换

## 限制与注意事项

- 计算答案通常没有对应的可见答案框
- 问答 v1、v2 与规模小得多的 VisRAG 改造属于不同协议

## 获取方式与来源

- [官方资源](https://github.com/NiteshMethani/PlotQA)
- [论文](https://arxiv.org/abs/1909.00997)
- [数据](https://github.com/NiteshMethani/PlotQA/blob/master/PlotQA_Dataset.md)
- repository：[来源](https://github.com/NiteshMethani/PlotQA) — 支持字段 `summary`、`data.description`、`data.size`、`access.license`
- repository：[来源](https://github.com/NiteshMethani/PlotQA/blob/master/PlotQA_Dataset.md) — 支持字段 `data.size`、`data.splits`、`data.format`、`ground_truth.description`
- paper：[来源](https://arxiv.org/abs/1909.00997) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`
- paper：[来源](https://proceedings.iclr.cc/paper_files/paper/2025/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf) — 支持字段 `data.description`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
