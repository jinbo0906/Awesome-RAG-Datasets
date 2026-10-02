<!-- Generated from catalog/datasets/or-quac.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# OR-QuAC

[English](or-quac.md)

将 QuAC 对话改造成开放检索任务，结合 CANARD 问题改写与维基百科段落集合。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | conversational_qa, query_rewriting, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | paragraph, span, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | CC-BY-SA-4.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

作者提供段落集合、衍生 qrels、训练与开发及测试样本，以及 QuAC 格式的开发和测试参考答案。数据整合 QuAC 对话、CANARD 独立问题改写和维基百科段落。


## 真值与评测

答案片段来自人工 QuAC 标注；段落 qrels 由这些金标准上下文衍生，作者明确说明它们是不完整的，因为其他段落也可能回答同一问题。

官方指标：answer_f1, HEQ-Q, HEQ-D, MRR, retrieval_recall。

评测协议：保留原始对话历史和 QuAC 参考答案，将检索与阅读器质量分开评测。不能假定预处理的开发和测试 evidence 字段始终包含金标准段落。

## 适用场景

- 多轮检索与阅读器流水线
- 比较独立问题改写与感知历史的检索

## 限制与注意事项

- 衍生段落相关性判断不完整
- 使用金标准上下文的问答不能衡量端到端表现

## 获取方式与来源

- [官方资源](https://github.com/prdwb/orconvqa-release)
- [论文](https://ciir-publications.cs.umass.edu/getpdf.php?id=1386)
- repository：[来源](https://github.com/prdwb/orconvqa-release) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.protocol`、`access.license`
- paper：[来源](https://ciir-publications.cs.umass.edu/getpdf.php?id=1386) — 支持字段 `evaluation.official_metrics`
- repository：[来源](https://github.com/prdwb/orconvqa-release/blob/master/scorer.py) — 支持字段 `evaluation.official_metrics`
- repository：[来源](https://github.com/prdwb/orconvqa-release/blob/master/train_pipeline.py) — 支持字段 `evaluation.official_metrics`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
