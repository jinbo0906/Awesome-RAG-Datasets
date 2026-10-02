<!-- Generated from catalog/datasets/mrag-bench.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# MRAG-Bench

[English](mrag-bench.md)

覆盖九种场景、提供金标准支持图像和选择题答案的视觉中心 RAG 数据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_native` |
| 主分类 | `multimodal_rag` |
| 任务 | visual_qa, multimodal_retrieval |
| 模态 | text, image |
| 已发布真值标注层级 | document, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | CC-BY-4.0 for the Hugging Face release; upstream image-source terms may also apply. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

作者发布图像语料与问答。Hugging Face 测试包嵌入查询图像、gt_images、五张 retrieved_images 和四个答案选项，支持金标准上下文与检索上下文评测。

发布规模：1,353 个人工标注问题，语料含 16,130 张图像。
数据划分：测试 benchmark，没有原生训练集。
格式：Hugging Face Parquet with images and an author-hosted corpus archive.。

## 真值与评测

gt_images 指定支持图像，answer_choice 给出正确选项。这些属于图像级支持，不是对象框，也不能保证扩展语料中所有有用图像都已有完整标注。

官方指标：multiple_choice_accuracy, Recall@5。

评测协议：分开报告无 RAG、检索 RAG 和金标准图像 RAG；多数原生比较使用五张图像。ACL 2026 效用选择研究注入金标准图像的固定候选池属于另一种选择协议。

## 适用场景

- 衡量检索视觉知识如何影响回答
- 比较使用金标准图像与不完美检索

## 限制与注意事项

- 正式发表于 ICLR 2025，2024 年 arXiv 日期不是会议年份
- 金标准上下文或注入金标准的候选池须与全语料检索区别报告

## 获取方式与来源

- [官方资源](https://mragbench.github.io/)
- [论文](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ee46288ab2aaf5c6e53aebebe719712c-Abstract-Conference.html)
- [数据](https://huggingface.co/datasets/uclanlp/MRAG-Bench)
- official：[来源](https://mragbench.github.io/) — 支持字段 `summary`、`data.size`、`evaluation.official_metrics`、`evaluation.protocol`
- dataset_card：[来源](https://huggingface.co/datasets/uclanlp/MRAG-Bench) — 支持字段 `data.description`、`data.splits`、`data.format`、`ground_truth.description`、`access.license`
- paper：[来源](https://aclanthology.org/2026.acl-long.1620/) — 支持字段 `evaluation.protocol`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
