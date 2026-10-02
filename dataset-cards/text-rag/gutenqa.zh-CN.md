<!-- Generated from catalog/datasets/gutenqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# GutenQA

[English](gutenqa.md)

叙事书籍问答数据，提供含答案的原文子串与多种切分格式，用于比较分块及检索。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | long_context_qa, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | quote, answer |
| 证据标注来源 | synthetic |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | MIT dataset card; underlying books retain Project Gutenberg terms |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

Project Gutenberg 书籍以段落、递归、语义、命题和 LumberChunker 格式发布。问题记录包含书籍标识、答案和 Chunk Must Contain 子串，用于跨切分方式匹配证据。

发布规模：100 本叙事书籍共 3,000 个问答对，每本书 30 对。
格式：Parquet。

## 真值与评测

含答案子串将证据锚定在书籍内。发布的分块 ID 对应某种切分，不是独立人工标注的最优切分点。

官方指标：dcg_at_k, recall_at_k。

评测协议：使用书籍内检索池及发布的子串匹配方法，报告所选 k 下的 DCG 与 Recall（论文使用 1/2/5/10/20）。论文的回答生成实验另用四本自传、280 个问题，不是发布的 100 本书、3,000 题 GutenQA 集。新生成协议需单独说明；比较分块方法时固定段落语料和上下文预算。

## 适用场景

- 利用稳定的答案子串锚点比较切分方案
- 叙事文档内的证据检索

## 限制与注意事项

- 以 LumberChunker 构建数据可能偏向其切分分布
- 稀疏的含答案证据不能衡量所有语义边界质量

## 获取方式与来源

- [官方资源](https://github.com/joaodsmarques/LumberChunker)
- [论文](https://aclanthology.org/2024.findings-emnlp.377/)
- [数据](https://huggingface.co/datasets/LumberChunker/GutenQA)
- repository：[来源](https://github.com/joaodsmarques/LumberChunker) — 支持字段 `data.description`、`data.size`、`ground_truth.description`
- paper：[来源](https://aclanthology.org/2024.findings-emnlp.377.pdf) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`、`ground_truth.provenance`
- dataset_card：[来源](https://huggingface.co/datasets/LumberChunker/GutenQA) — 支持字段 `access.license`、`access.data`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
