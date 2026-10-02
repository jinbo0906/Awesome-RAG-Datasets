<!-- Generated from catalog/datasets/frames.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# FRAMES

[English](frames.md)

人工编写的多文档问题，同时评测事实回答、检索与推理。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | multi_hop_qa, time_sensitive_qa |
| 模态 | text |
| 已发布真值标注层级 | document, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | Apache-2.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

CSV 提供问题、参考答案、推理类型和支持的维基百科 URL；文章正文需要另外获取。

发布规模：824 个评测问题。
数据划分：只有一个测试划分，没有原生训练集。
格式：CSV。

## 真值与评测

标注者提供支持文章；URL 是文档级目标，不是句子偏移量，也不是唯一图路径。

官方指标：answer_accuracy, article_recall。

评测协议：论文比较无检索、BM25 检索、金标准文章及迭代检索。回答正确性由 LLM 评判；应固定维基百科快照与评判提示词。

## 适用场景

- 迭代检索与搜索规划
- 多文档时间与数值推理

## 限制与注意事项

- 维基百科 URL 不会冻结正文，应使用注明日期的语料快照
- 论文发表于 NAACL 2025，不能写成 ACL 主会论文

## 获取方式与来源

- [官方资源](https://huggingface.co/datasets/google/frames-benchmark)
- [论文](https://aclanthology.org/2025.naacl-long.243/)
- [数据](https://huggingface.co/datasets/google/frames-benchmark/tree/main)
- dataset_card：[来源](https://huggingface.co/datasets/google/frames-benchmark) — 支持字段 `data`、`ground_truth.levels`、`access.license`
- paper：[来源](https://aclanthology.org/2025.naacl-long.243.pdf) — 支持字段 `summary`、`classification`、`ground_truth`、`evaluation`、`use`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
