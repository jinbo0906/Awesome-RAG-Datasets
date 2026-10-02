<!-- Generated from catalog/datasets/ssrb.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# SSRB

[English](ssrb.md)

半结构化检索基准，将精确字段条件与语义要求结合起来。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `auxiliary` |
| 主分类 | `table_rag` |
| 任务 | evidence_retrieval, reasoning_retrieval |
| 模态 | text, table |
| 已发布真值标注层级 | document |
| 证据标注来源 | synthetic |
| 语料 / 查询 / 答案 | provided / provided / not_provided |
| 原始数据许可 | Apache-2.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

发布包区分结构化对象语料、测试查询和正向查询对象相关性标注；嵌套字段及缺失字段也是任务的一部分。

发布规模：六个领域、99 种 schema 中约 1,400 万个对象，另有 8,485 个测试查询。
格式：JSONL。

## 真值与评测

LLM 生成对象和查询，并判断候选检索结果；qrels 标记完整对象的相关性，不是单元格证据或生成答案。

官方指标：recall_at_20, ndcg_at_10。

评测协议：分别报告同 schema 与同领域跨 schema 检索，并对领域作宏平均。固定候选池与序列化方式。

## 适用场景

- 异构结构化记录检索
- 数值筛选与语义约束的联合处理

## 限制与注意事项

- 合成候选池上的 qrels 不是穷尽的人工相关性判断
- 本基准评测检索，答案生成需要独立协议

## 获取方式与来源

- [官方资源](https://github.com/vec-ai/struct-ir)
- [论文](https://proceedings.neurips.cc/paper_files/paper/2025/hash/631bbd89466337712564872840a401be-Abstract-Datasets_and_Benchmarks_Track.html)
- [数据](https://huggingface.co/datasets/vec-ai/struct-ir)
- dataset_card：[来源](https://huggingface.co/datasets/vec-ai/struct-ir) — 支持字段 `data`、`ground_truth.levels`、`access.license`
- repository：[来源](https://github.com/vec-ai/struct-ir) — 支持字段 `summary`、`classification`、`ground_truth`、`evaluation.evaluator`、`use`
- paper：[来源](https://proceedings.neurips.cc/paper_files/paper/2025/file/631bbd89466337712564872840a401be-Paper-Datasets_and_Benchmarks_Track.pdf) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`、`data.size`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
