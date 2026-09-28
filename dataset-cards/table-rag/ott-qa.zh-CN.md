<!-- Generated from catalog/datasets/ott-qa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# OTT-QA

[English](ott-qa.md)

要求从大型表格与段落池检索证据的开放域表格—文本问答。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `table_rag` |
| 任务 | table_qa, text_table_reasoning, evidence_retrieval |
| 模态 | text, table |
| 已发布真值标注层级 | table, paragraph, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | MIT |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

去上下文化的问题对应超过 40 万张表格和 500 万个段落的候选池；在开放式设置中， 金标准表格和段落不会直接提供给模型。


## 真值与评测

问题记录及关联来源数据支持表格和段落检索评测；本目录不宣称存在通用的单元格引用真值。

官方指标：table_hits_at_k, answer_em, answer_f1。

评测协议：使用开放检索设置，不要换成直接提供表格的 HybridQA；测试集评分使用官方挑战赛流程。

## 适用场景

- 联合检索表格与文本
- 开放域证据组合

## 限制与注意事项

- 原始关联段落和表格快照须版本化
- 金标准表格或段落比最小单元格—片段证据链更粗

## 获取方式与来源

- [官方资源](https://github.com/wenhuchen/OTT-QA)
- repository：[来源](https://github.com/wenhuchen/OTT-QA) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.protocol`、`access.license`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
