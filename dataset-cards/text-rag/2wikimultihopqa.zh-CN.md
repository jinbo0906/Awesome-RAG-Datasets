<!-- Generated from catalog/datasets/2wikimultihopqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# 2WikiMultiHopQA

[English](2wikimultihopqa.md)

基于维基百科的多跳问答，提供支持事实与结构化推理证据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | multi_hop_qa, evidence_retrieval |
| 模态 | text, graph |
| 已发布真值标注层级 | sentence, graph_path, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

问题由维基百科文本和 Wikidata 关系构建；使用时应遵循官方数据划分与证据格式。


## 真值与评测

发布的标注包含支持句和证据路径；具体如何使用图证据取决于所选评测设置。

官方指标：answer_em, answer_f1, supporting_fact_em, supporting_fact_f1。


## 适用场景

- 多跳证据链检索
- 比较文本证据与图衍生证据

## 限制与注意事项

- 不能把生成的推理路径等同于人工核验且唯一的最小证据集合

## 获取方式与来源

- [官方资源](https://github.com/Alab-NII/2wikimultihop)
- [论文](https://aclanthology.org/2020.coling-main.580/)
- repository：[来源](https://github.com/Alab-NII/2wikimultihop) — 支持字段 `summary`、`data.description`、`ground_truth.levels`、`evaluation.official_metrics`
- paper：[来源](https://aclanthology.org/2020.coling-main.580/) — 支持字段 `summary`、`classification.tasks`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
