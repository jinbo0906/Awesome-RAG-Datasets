<!-- Generated from catalog/datasets/pubhealth.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# PUBHEALTH

[English](pubhealth.md)

公共卫生主张核查数据，附记者撰写的解释与来源元数据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `text_rag` |
| 任务 | fact_verification, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | not_provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

官方 v1.0 TSV 版本的训练、开发和测试集共 12,279 行；论文描述的是更早的约 1.18 万条主张版本。 记录含主张、日期、主要证据文本、证据来源 URL 和标签，但不提供固定的可检索来源语料。

发布规模：仓库 v1.0 发布版有 12,279 条主张；论文数量对应较早版本。

## 真值与评测

提供事实核查标签和解释。来源 URL 与主要证据文本可作为依据线索，但开放检索所需的稳定文档或字符偏移并无保证。

官方指标：label_accuracy。

评测协议：固定 TSV 发布版及获取日期。RAG 实验应构建有许可、带日期的文档集合，并在不泄露事实核查解释的前提下定义来源匹配。

## 适用场景

- 特定领域的主张核查
- 分析有时间属性的证据来源

## 限制与注意事项

- 发布的 TSV 不是完整的固定检索语料
- 仓库与论文报告的是不同版本的计数

## 获取方式与来源

- [官方资源](https://github.com/neemakot/Health-Fact-Checking/tree/master/data)
- [论文](https://arxiv.org/abs/2010.09926)
- repository：[来源](https://github.com/neemakot/Health-Fact-Checking/blob/master/data/README.md) — 支持字段 `summary`、`data.description`、`data.size`、`ground_truth.description`
- paper：[来源](https://arxiv.org/abs/2010.09926) — 支持字段 `data.description`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
