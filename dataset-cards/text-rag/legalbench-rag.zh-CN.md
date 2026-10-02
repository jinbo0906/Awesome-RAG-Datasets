<!-- Generated from catalog/datasets/legalbench-rag.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# LegalBench-RAG

[English](legalbench-rag.md)

法律检索基准，按字符范围标注评测精确文本片段。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `auxiliary` |
| 主分类 | `text_rag` |
| 任务 | evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | document, span |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / not_provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

可下载的文本语料和查询以 ContractNLI、CUAD、MAUD 与 PrivacyQA 为来源；片段检索目标不是自由生成答案的参考文本。

发布规模：论文报告 6,858 个查询与片段样本，语料超过 7,900 万字符。
格式：Text files and JSON benchmark files。

## 真值与评测

每个目标指定语料文件及字符范围；上游专家标注经过 LLM 辅助处理，转换为检索样本。

官方指标：character_precision_at_k, character_recall_at_k。

评测协议：分块时保留文件路径与原始字符偏移。报告 k 值及完整或 mini 版本；官方基准评测检索。

## 适用场景

- 法律文本分块与精确证据检索
- 字符级检索覆盖

## 限制与注意事项

- 该检索发布包没有建立原生答案生成评分协议
- 重新生成数据前需要检查四个上游法律数据集的使用条款

## 获取方式与来源

- [官方资源](https://github.com/zeroentropy-ai/legalbenchrag)
- [论文](https://arxiv.org/abs/2408.10343)
- repository：[来源](https://github.com/zeroentropy-ai/legalbenchrag) — 支持字段 `summary`、`classification`、`data.description`、`data.format`、`ground_truth`、`evaluation`、`use`
- paper：[来源](https://arxiv.org/html/2408.10343v1) — 支持字段 `data.size`、`evaluation.official_metrics`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
