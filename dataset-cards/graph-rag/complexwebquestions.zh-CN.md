<!-- Generated from catalog/datasets/complexwebquestions.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# ComplexWebQuestions 1.1

[English](complexwebquestions.md)

基于 Freebase 或检索网页片段的复杂组合问答，附问题分解监督。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `graph_rag` |
| 任务 | graph_qa, multi_hop_qa |
| 模态 | graph, text |
| 已发布真值标注层级 | graph_path, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

1.1 版本发布复杂问题、SPARQL、答案及分解问题监督；知识库实验使用 Freebase，网页实验检索片段。

数据划分：使用修正后的 1.1 版本划分；1.0 版本存在已公布的数据划分问题。
格式：JSON。

## 真值与评测

自动构造的组合查询与人工改写的问题提供逻辑形式监督；检索网页片段是候选证据，不是金标准句子引用。

官方指标：precision_at_1。

评测协议：使用官方答案评分器与 1.1 划分。说明回答采用网页检索还是指定 Freebase 快照；后续 KBQA 论文可能报告额外指标。

## 适用场景

- 问题分解与组合知识库问答
- 图谱与网页检索路线比较

## 限制与注意事项

- 原始知识库重建使用 freebase-rdf-2015-08-02-00-00 快照
- 逻辑形式不能证明被检索子图唯一且最小

## 获取方式与来源

- [官方资源](https://www.tau-nlp.sites.tau.ac.il/compwebq)
- [论文](https://aclanthology.org/N18-1059/)
- official：[来源](https://www.tau-nlp.sites.tau.ac.il/compwebq) — 支持字段 `summary`、`classification`、`data`、`evaluation.protocol`、`use.caveats`
- paper：[来源](https://aclanthology.org/N18-1059/) — 支持字段 `ground_truth`、`evaluation.official_metrics`、`use.best_for`
- paper：[来源](https://arxiv.org/abs/1807.09623) — 支持字段 `data.splits`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
