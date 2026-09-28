<!-- Generated from catalog/datasets/hotpotqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# HotpotQA

[English](hotpotqa.md)

具有句子级支持事实和答案标签的维基百科多跳问答数据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | multi_hop_qa, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | sentence, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | CC BY-SA 4.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

干扰文档设置与完整维基百科设置使用不同检索池；比较结果时必须保留所选设置。

格式：JSON。

## 真值与评测

支持事实由维基百科页面标题和从零开始的句子索引标识；答案另行评测。

官方指标：answer_em, answer_f1, supporting_fact_em, supporting_fact_f1, joint_em, joint_f1。

评测协议：分别报告干扰文档和完整维基百科设置的结果。

## 适用场景

- 跨文档证据组合
- 对照句子来源坐标评测与问题无关的分块

## 限制与注意事项

- 支持句不是唯一最优分块边界
- 干扰文档上下文不等同于开放语料检索

## 获取方式与来源

- [官方资源](https://hotpotqa.github.io/)
- [论文](https://arxiv.org/abs/1809.09600)
- [数据](https://hotpotqa.github.io/)
- repository：[来源](https://github.com/hotpotqa/hotpot) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.official_metrics`、`access.license`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
