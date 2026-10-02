<!-- Generated from catalog/datasets/infographicvqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# InfographicVQA

[English](infographicvqa.md)

需要联合理解信息图文字、图形、布局和数值信息的视觉问答。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `multimodal_rag` |
| 任务 | visual_qa, page_retrieval |
| 模态 | text, image, chart, layout |
| 已发布真值标注层级 | answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

人工编写的问答关联网络信息图图像，并提供 OCR。VisRAG 与 VDocRAG 通过过滤问题、汇集图像构造检索设置；这些子集不能替代原始数据集。

发布规模：30,035 个问题，对应 5,485 张图像。
数据划分：训练集 23,946 题，验证集 2,801 题，测试集 3,288 题。
格式：Infographic images, OCR and QA annotations.。

## 真值与评测

发布参考答案与图像关联。OCR 布局属于输入数据，不是通用的人工答案框或原生开放域检索相关性真值。

官方指标：ANLS。

评测协议：原生问答使用原始挑战划分。使用 VisRAG 或 OpenDocVQA 时，须先说明过滤后的查询、图像候选池和检索指标，再比较结果。

## 适用场景

- 包含空间与数值推理的信息图阅读
- 比较视觉检索与基于 OCR 的检索改造

## 限制与注意事项

- 原始任务已经给出相关图像
- 原始划分与过滤后的 RAG 划分规模明显不同

## 获取方式与来源

- [官方资源](https://site.docvqa.org/datasets/infographicvqa)
- [论文](https://arxiv.org/abs/2104.12756)
- [数据](https://rrc.cvc.uab.es/?ch=17&com=downloads)
- official：[来源](https://site.docvqa.org/datasets/infographicvqa) — 支持字段 `summary`、`data.description`、`access.data`
- paper：[来源](https://arxiv.org/abs/2104.12756) — 支持字段 `classification.modalities`、`data.size`、`data.splits`、`ground_truth.description`、`evaluation.official_metrics`
- paper：[来源](https://arxiv.org/html/2504.09795) — 支持字段 `data.description`、`evaluation.protocol`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
