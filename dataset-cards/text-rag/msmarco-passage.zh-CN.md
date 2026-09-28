<!-- Generated from catalog/datasets/msmarco-passage.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# MS MARCO Passage Ranking (v1)

[English](msmarco-passage.md)

具有查询—段落相关性标注的大规模网页段落检索数据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `auxiliary` |
| 主分类 | `text_rag` |
| 任务 | evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | document |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / not_provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

本条目特指 v1 段落排序变体，而不是原始 MS MARCO 生成式问答、文档排序或 TREC Deep Learning 赛道。v1 集合约有 880 万个段落，另含查询和稀疏 qrels。


## 真值与评测

Qrels 标识排序用的相关段落，但没有穷尽所有相关段落；这个排序变体也没有生成回答的参考答案。

官方指标：mrr_at_10。

评测协议：指明 v1/v2、训练/开发/测试划分及全库检索或重排设置。标注稀疏时，不宜直接把未判断段落当成负例。

## 适用场景

- 训练检索器及排序对照
- 大规模段落索引

## 限制与注意事项

- 仅检索的变体不是端到端回答 benchmark
- 稀疏 qrels 可能低估相关证据

## 获取方式与来源

- [官方资源](https://microsoft.github.io/msmarco/)
- repository：[来源](https://github.com/microsoft/msmarco/blob/master/Datasets.md) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.protocol`
- repository：[来源](https://github.com/microsoft/MSMARCO-Passage-Ranking) — 支持字段 `evaluation.official_metrics`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
