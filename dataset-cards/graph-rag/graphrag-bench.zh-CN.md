<!-- Generated from catalog/datasets/graphrag-bench.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# GraphRAG-Bench

[English](graphrag-bench.md)

在事实性与上下文生成任务上比较图式 RAG 的领域 benchmark。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `graph_rag` |
| 任务 | graph_reasoning, single_hop_qa, summarization |
| 模态 | text, graph |
| 已发布真值标注层级 | answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

发布的小说和医疗任务覆盖事实检索、复杂推理、上下文摘要及创意生成。


## 真值与评测

数据提供参考答案与任务级评测；本目录不宣称其有通用的金标准图路径。

官方指标：accuracy, rouge_l, coverage, factual_score。

评测协议：将建图成本和检索效果与生成质量分开报告。

## 适用场景

- 比较 GraphRAG 与文本 RAG
- 研究哪些任务类型从图结构受益

## 限制与注意事项

- 被评测方法可能自行建图；其生成的图边不是金标准证据路径

## 获取方式与来源

- [官方资源](https://github.com/GraphRAG-Bench/GraphRAG-Benchmark)
- [论文](https://arxiv.org/abs/2506.05690)
- repository：[来源](https://github.com/GraphRAG-Bench/GraphRAG-Benchmark) — 支持字段 `summary`、`data.description`、`evaluation.official_metrics`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
