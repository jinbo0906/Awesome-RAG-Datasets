<!-- Generated from catalog/datasets/temprageval.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# TempRAGEval

[English](temprageval.md)

对时间条件进行保持答案不变的扰动，并人工定位维基百科证据的时效 RAG 评测数据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-01 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | time_sensitive_qa, evidence_retrieval, rag_robustness |
| 模态 | text |
| 已发布真值标注层级 | sentence, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | Apache-2.0 in query-release metadata; external Wikipedia/ATLAS corpus retains upstream terms. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

人工为 SituatedQA 和 TimeQA 问题改写更复杂的时间条件，同时保留原始答案。查询发布数据与论文采用的 ATLAS 2021 年 12 月英文维基百科语料分开获取，后者含 3,310 万个文本块。

发布规模：论文报告 1,000 个证据标注测试样本；作者协议排除 time_relation 为空的行。
数据划分：测试 benchmark 包含 SituatedQA 和 TimeQA 两种来源分层，原始问题与扰动问题需分开报告。
格式：CSV test file on Hugging Face plus external ATLAS text corpus。

## 真值与评测

每题最多提供两个支持句。检索块包含任一支持句即记为命中，因此证据指标测量至少一个支持句是否出现，不是多句完整证据覆盖。答案及来源问题具有不同的原始构建方式。

官方指标：answer_recall_at_k, gold_evidence_recall_at_k, exact_match, token_f1。

评测协议：固定维基百科/ATLAS 语料，排除 time_relation 为空的行，评分对象是检索块而非系统抽取句。答案包含召回与标注证据召回是不同指标：偶然出现答案可能抬高前者，未被标注的有效段落可能降低后者。MRAG 是引入该数据的方法，不是另一个数据集。

## 适用场景

- 诊断语义相似但时间不适用的检索
- 测试检索与问答对保持答案不变的日期变化是否敏感

## 限制与注意事项

- HF API 标明自动授权门槛，本次未下载查询文件
- 句子锚点不是最优分块边界或穷尽的相关性标注
- 历史时间推理本身不评测知识库持续更新
- 正式论文为 Findings EMNLP 2025，2024 年 12 月预印本属于不同发表节点

## 获取方式与来源

- [官方资源](https://github.com/siyue-zhang/MRAG)
- [论文](https://aclanthology.org/2025.findings-emnlp.167/)
- [数据](https://huggingface.co/datasets/siyue/TempRAGEval)
- paper：[来源](https://aclanthology.org/2025.findings-emnlp.167.pdf) — 支持字段 `summary`、`classification`、`data.description`、`data.size`、`ground_truth`、`evaluation.official_metrics`、`use`
- repository：[来源](https://github.com/siyue-zhang/MRAG) — 支持字段 `data.corpus`、`data.splits`、`ground_truth.description`、`evaluation.protocol`、`evaluation.evaluator`、`access.data`
- dataset_card：[来源](https://huggingface.co/api/datasets/siyue/TempRAGEval) — 支持字段 `data.format`、`access.license`、`access.gated`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
