<!-- Generated from catalog/datasets/chartqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# ChartQA

[English](chartqa.md)

图表图像问答，结合人工与生成问题，并可使用图表元素边界框。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `multimodal_rag` |
| 任务 | visual_qa, table_qa |
| 模态 | image, chart, table |
| 已发布真值标注层级 | bbox, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

官方完整版本含图表图像、问答、底层表格和元素标注；train_human 与 train_augmented 的来源不同。


## 真值与评测

完整版本有元素边界框，但它们不一定是逐题的最小证据区域。

官方指标：relaxed_accuracy。

评测协议：若用于检索实验，应构建图表语料，并说明底层表格或元素框是否对系统可见。

## 适用场景

- 图表感知与数值推理
- 视觉与表格表示的消融比较

## 限制与注意事项

- 原生任务直接给出图表，并非开放语料 RAG
- 从 SVG 得到的边界框可能有噪声或缺失

## 获取方式与来源

- [官方资源](https://github.com/vis-nlp/ChartQA)
- [论文](https://aclanthology.org/2022.findings-acl.177/)
- repository：[来源](https://github.com/vis-nlp/ChartQA) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.protocol`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
