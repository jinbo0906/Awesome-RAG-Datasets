<!-- Generated from catalog/suites/mirage.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# MIRAGE (medical RAG)

[English](mirage.md)

汇集五个医学问答数据集的 7,663 个问题，以零样本和仅问题检索设置评测医学 RAG。

审查状态：`source_checked`。这是评测套件或协议，不是单一独立数据集。

## 已收录的组成数据集

- [medqa](../dataset-cards/text-rag/medqa.zh-CN.md)
- [medmcqa](../dataset-cards/text-rag/medmcqa.zh-CN.md)
- [pubmedqa](../dataset-cards/text-rag/pubmedqa.zh-CN.md)

## 协议与结果解释

使用发布的 benchmark.json：MMLU-Med（1,089 题）、MedQA-US 四选项测试集（1,273 题）、MedMCQA 开发集（4,183 题）、去掉上下文的 PubMedQA* 测试集（500 题），以及 2019–2023 年 BioASQ 是非测试题（618 题）。链接卡片介绍其中三个原始数据集，另两个精确子集未单独索引。BioASQ-Y/N 不等于 BioASQ14b。仅用不含选项的问题检索，固定 MedRAG 语料与检索器快照，报告各任务和平均答案准确率。检索片段 ID 是系统输出而非证据真值。论文发表于 Findings ACL 2024，不能称为 ACL 主会论文。

## 官方来源

- [官方资源](https://github.com/gzxiong/MIRAGE)
- [论文](https://aclanthology.org/2024.findings-acl.372/)
- repository：[来源](https://github.com/gzxiong/MIRAGE) — 支持字段 `summary`、`components`、`protocol`
- paper：[来源](https://aclanthology.org/2024.findings-acl.372/) — 支持字段 `protocol`
