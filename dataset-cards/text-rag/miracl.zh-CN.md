<!-- Generated from catalog/datasets/miracl.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# MIRACL

[English](miracl.md)

覆盖 18 种语言的同语言维基百科检索，由母语标注者提供段落相关性判断。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `auxiliary` |
| 主分类 | `text_rag` |
| 任务 | evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | paragraph |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / not_provided |
| 原始数据许可 | Apache-2.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

作者资源提供各语言的维基百科段落语料、查询和正负相关性标注。原生查询与语料使用同一种语言，不自动构成跨语言检索或生成回答评测。

发布规模：论文报告了约 7.8 万个查询和超过 72.6 万条相关性判断，覆盖 18 种语言。
数据划分：各语言划分不同；作为额外评测语言加入的德语与约鲁巴语没有训练数据。

## 真值与评测

母语标注者判断检索段落的相关性。段落保留文章标题及文章、段落标识；qrels 不提供参考答案，也不标注重新分块后的最佳边界。

官方指标：nDCG@10, Recall@100。

评测协议：保留各语言的语料版本、划分和段落标识，按官方 qrels 评分。在称为端到端 RAG 实验之前，另行定义回答评测协议。

## 适用场景

- 多语言检索组件评测
- 比较高资源与低资源语言的检索

## 限制与注意事项

- 原生任务没有生成回答参考答案
- 查询与 qrels 的许可不替代维基百科语料的上游条款

## 获取方式与来源

- [官方资源](https://github.com/project-miracl/miracl)
- [论文](https://aclanthology.org/2023.tacl-1.63/)
- [数据](https://huggingface.co/datasets/miracl/miracl)
- repository：[来源](https://github.com/project-miracl/miracl) — 支持字段 `summary`、`data.description`、`ground_truth.description`
- paper：[来源](https://aclanthology.org/2023.tacl-1.63/) — 支持字段 `data.size`
- paper：[来源](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00595/117438/MIRACL-A-Multilingual-Retrieval-Dataset-Covering) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`
- dataset_card：[来源](https://huggingface.co/datasets/miracl/miracl) — 支持字段 `access.license`、`ground_truth.alternatives`
- dataset_card：[来源](https://huggingface.co/datasets/miracl/miracl/discussions/1) — 支持字段 `data.splits`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
