<!-- Generated from catalog/datasets/confrag.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# ConfRAG

[English](confrag.md)

面向矛盾信息的问答基准，要求覆盖所提供网页参考中的不同观点。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | long_form_qa, rag_robustness, attribution |
| 模态 | text |
| 已发布真值标注层级 | document, fact_citation, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | HF card: CC BY 4.0; repository says dataset research use only and original web licenses apply |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

样本包含网页正文与 URL、矛盾标记、答案观点簇，以及附网页索引的支持理由；推荐版本改进了标注。

发布规模：1,814 个问题；论文报告其中 57.2% 存在矛盾。
格式：JSONL。

## 真值与评测

LLM 抽取及人工复核生成观点簇、理由与网页索引。这些引用不是精确句子偏移，也不保证观点客观真实。

官方指标：normalized_mutual_information, answer_coverage, reason_coverage, valid_partition_rate。

评测协议：固定已发布网页上下文与标注版本。结构化输出按聚类及基于关键词的答案与理由匹配评分；单独报告格式有效率。

## 适用场景

- 互相矛盾的多来源答案整合
- 观点与理由覆盖

## 限制与注意事项

- 给定网页参考主要测试检索后的推理，开放语料检索需要另行定义协议
- 数据卡与仓库的许可证表述不同，使用前应核实适用条款

## 获取方式与来源

- [官方资源](https://github.com/XaiverYuan/ConfRAG)
- [论文](https://aclanthology.org/2026.acl-long.11/)
- [数据](https://huggingface.co/datasets/OracleY/ConfRAG)
- dataset_card：[来源](https://huggingface.co/datasets/OracleY/ConfRAG) — 支持字段 `summary`、`classification`、`data`、`ground_truth`、`evaluation.official_metrics`、`evaluation.protocol`、`access.license`、`use`
- repository：[来源](https://github.com/XaiverYuan/ConfRAG) — 支持字段 `evaluation.evaluator`、`access.license`、`use.caveats`
- paper：[来源](https://aclanthology.org/2026.acl-long.11.pdf) — 支持字段 `data.size`、`evaluation.official_metrics`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
