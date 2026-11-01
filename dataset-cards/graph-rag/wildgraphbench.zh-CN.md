<!-- Generated from catalog/datasets/wildgraphbench.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# WildGraphBench

[English](wildgraphbench.md)

在长外部引用文档上，分开评测 GraphRAG 的单事实问答、多事实聚合与逐陈述摘要。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-01 |
| RAG 角色 | `rag_native` |
| 主分类 | `graph_rag` |
| 任务 | single_hop_qa, multi_hop_qa, summarization |
| 模态 | text, graph |
| 已发布真值标注层级 | document, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | Apache-2.0 for the released benchmark; third-party reference documents retain their original rights. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

Findings ACL 2026 基准，使用维基百科文章及异构外部引用构建。应索引 reference_pages，而不是用于构建真值的维基百科文章。按主题发布问题、参考 URL、来源文本及摘要陈述。

发布规模：当前仓库与 HF 发布为十二主题、1,197 题，含 667 个单事实、191 个多事实和 339 个摘要问题；论文摘要写 1,100，不能悄悄视为同一版本。
数据划分：HF 的十二个主题划分用于评测分区，不是十二个独立训练与测试任务。
格式：Question JSONL, source text files and reference metadata; optional statement files.。

## 真值与评测

维基百科带引用陈述用于模型辅助问答与摘要构造。ref_urls 是问题级来源引用，gold_statements 是摘要目标；都不保证逐事实最小片段或金标准图边。

官方指标：single_fact_accuracy, multi_fact_accuracy, statement_precision, statement_recall, statement_f1。

评测协议：论文 §3.5/§4.1 区分模型评判的问答正确率与摘要陈述匹配，默认评判模型为 gpt-5-mini。固定建图、回答模型及检索预算；1,200-token 分块与 100-token 重叠只是基线设置，不是分块边界真值。不得把金标准维基百科摘要文章索引为检索证据。

## 适用场景

- 在短精选段落之外测试证据聚合
- 比较 GraphRAG 的细节保留与全局摘要

## 限制与注意事项

- 当前发布与论文摘要的问题数量不同
- 构建得到的图边不是独立真值路径
- 参考 URL 与模型陈述匹配不能证明来源坐标级证据完整

## 获取方式与来源

- [官方资源](https://github.com/BstWPY/WildGraphBench)
- [论文](https://aclanthology.org/2026.findings-acl.679/)
- [数据](https://huggingface.co/datasets/Bstwpy/WildGraphBench)
- paper：[来源](https://aclanthology.org/2026.findings-acl.679/) — 支持字段 `summary`、`data.description`、`data.size`
- dataset_card：[来源](https://huggingface.co/datasets/Bstwpy/WildGraphBench) — 支持字段 `data.size`、`data.splits`、`data.format`、`access.license`、`ground_truth.description`
- repository：[来源](https://github.com/BstWPY/WildGraphBench) — 支持字段 `data.description`、`evaluation.protocol`、`data.size`
- paper：[来源](https://arxiv.org/html/2602.02053) — 支持字段 `ground_truth.provenance`、`evaluation.official_metrics`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
