<!-- Generated from catalog/datasets/beir-scifact.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# SciFact (BEIR variant)

[English](beir-scifact.md)

BEIR 零样本信息检索套件中的科学主张到论文摘要检索变体。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `auxiliary` |
| 主分类 | `text_rag` |
| 任务 | fact_verification, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | document |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / not_provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

BEIR 版本提供语料、查询和文档级相关性标注；本条目不是原始 SciFact 主张核查数据包。


## 真值与评测

BEIR 的 qrels 标识相关论文摘要，而不是生成回答的金标准。

官方指标：ndcg_at_10, map_at_k, recall_at_k。

评测协议：使用 BEIR 测试集相关性标注和固定语料；若声称评测端到端 RAG，必须另外定义回答任务。

## 适用场景

- 比较科学领域检索器
- 展示语料—查询—相关性标注的数据结构

## 限制与注意事项

- 仅用于检索的辅助数据；没有原生的生成回答评测

## 获取方式与来源

- [官方资源](https://github.com/beir-cellar/beir)
- repository：[来源](https://github.com/beir-cellar/beir) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.official_metrics`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
