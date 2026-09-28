<!-- Generated from catalog/datasets/strategyqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# StrategyQA

[English](strategyqa.md)

隐含多步推理的是/否问答，包含问题分解和每一步的段落证据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | multi_hop_qa, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | paragraph, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

论文描述了 2,780 个问题。作者发布维基百科段落语料及单独的索引方法；代码仓库中的 90/10 训练/开发划分是官方训练数据的非官方再划分。


## 真值与评测

问题包含是/否答案、分解子问题和各推理步骤的证据段落；这些段落标签并非唯一最优分块边界。

官方指标：answer_accuracy, paragraph_recall_at_10。

评测协议：明确区分官方划分与作者代码的 90/10 划分；使用段落证据时保留问题级和步骤级检索分母。

## 适用场景

- 隐含多步检索
- 段落证据完整性

## 限制与注意事项

- 只有答案标签无法评测检索
- 重建索引和非官方划分会影响可比性

## 获取方式与来源

- [官方资源](https://github.com/eladsegal/strategyqa)
- [论文](https://aclanthology.org/2021.tacl-1.21/)
- paper：[来源](https://aclanthology.org/2021.tacl-1.21/) — 支持字段 `summary`、`data.description`、`ground_truth.description`
- repository：[来源](https://github.com/eladsegal/strategyqa) — 支持字段 `data.description`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
