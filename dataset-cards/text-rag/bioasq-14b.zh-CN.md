<!-- Generated from catalog/datasets/bioasq-14b.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# BioASQ Task 14b (2026)

[English](bioasq-14b.md)

具有论文、片段和答案监督信号的生物医学问答挑战赛。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | evidence_retrieval, single_hop_qa, long_form_qa |
| 模态 | text |
| 已发布真值标注层级 | document, span, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

BioASQ 是按届举办的挑战赛，并非一份永不变化的文件。官方参与者页面列出 2026 年 Task 14b 的 5,729 个训练问题，以及金标准概念、论文、片段、精确答案和理想答案。来源论文位于外部， 官方下载需要注册。

发布规模：BioASQ14 Task b 有 5,729 个训练问题；测试集按阶段另行发布。

## 真值与评测

金标准论文和片段可用于检索监督；精确答案和理想答案分别支持简短与段落式生成。 实际构建语料时必须保留证据标识及来源版本。

官方指标：尚未确认。

评测协议：指明挑战年份与阶段。A 阶段评测检索，B 阶段评测答案；不能把 2026 年训练集规模与其他届测试集或指标混用。

## 适用场景

- 生物医学检索与回答联合评测
- 来源片段证据及精确答案与理想答案的比较

## 限制与注意事项

- 下载官方数据需要注册
- 必须固定外部论文语料及每届挑战规则

## 获取方式与来源

- [官方资源](https://participants-area.bioasq.org/datasets/)
- official：[来源](https://participants-area.bioasq.org/datasets/) — 支持字段 `summary`、`data.description`、`data.size`、`ground_truth.description`、`access.gated`
- official：[来源](https://www.bioasq.org/node/2) — 支持字段 `evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
