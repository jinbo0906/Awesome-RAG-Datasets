<!-- Generated from catalog/datasets/mintqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# MINTQA

[English](mintqa.md)

基于 Wikidata 的多跳 RAG 问答，区分新旧知识及热门长尾知识。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_native` |
| 主分类 | `graph_rag` |
| 任务 | multi_hop_qa, graph_reasoning, time_sensitive_qa |
| 模态 | graph, text |
| 已发布真值标注层级 | graph_path, answer |
| 证据标注来源 | synthetic |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | MIT |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

POP 与 TI 发布包包含主问题及子问题、答案、逐跳知识标签、事实链和事实；作者链接的 MintQA-KG 提供检索知识库。

发布规模：MINTQA-POP 有 17,887 个问题，MINTQA-TI 有 10,479 个问题。
数据划分：两个测试子集，应按知识类型和跳数报告结果。
格式：JSONL。

## 真值与评测

显式发布用于生成问题的事实链与子答案；这些链基于 Wikidata 构造，并不证明它们在完整知识库中唯一。

官方指标：answer_containment_accuracy。

评测协议：论文检查转为小写的模型输出是否包含金标准答案。区分参数知识、直接检索和分解后检索设置，并固定知识库版本与线性化方式。

## 适用场景

- 按知识熟悉程度研究问题分解与检索决策
- 多跳事实链检索

## 限制与注意事项

- 新旧知识由指定 Wikidata 快照定义，不代表今天的实时新鲜度
- 数据文件已发布，但仓库说明完整项目代码仍在整理中

## 获取方式与来源

- [官方资源](https://github.com/probe2/multi-hop)
- [论文](https://aclanthology.org/2026.acl-long.18/)
- [数据](https://huggingface.co/datasets/probejie/MINTQA)
- repository：[来源](https://github.com/probe2/multi-hop) — 支持字段 `data`、`ground_truth.levels`、`use.caveats`
- dataset_card：[来源](https://huggingface.co/Sp1der/MintQA-KG/tree/main) — 支持字段 `data.corpus`、`data.description`
- paper：[来源](https://arxiv.org/html/2412.17032v3) — 支持字段 `summary`、`classification`、`ground_truth`、`evaluation`、`access.license`、`use`
- paper：[来源](https://aclanthology.org/2026.acl-long.18.pdf) — 支持字段 `evaluation`、`access.license`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
