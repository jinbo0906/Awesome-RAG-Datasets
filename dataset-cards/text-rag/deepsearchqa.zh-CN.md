<!-- Generated from catalog/datasets/deepsearchqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# DeepSearchQA

[English](deepsearchqa.md)

通过单一答案与穷尽式答案集合评测多步网页研究，惩罚过早停止和额外猜测。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-01 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | agentic_search, multi_hop_qa |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | Apache-2.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

Google 于 2025 年 12 月发布人工编写的因果链式信息搜索问题，覆盖 17 个领域。发布字段为 problem、problem_category、answer 和 answer_type，证据环境仍是外部网页。

发布规模：共 900 个问题；官方数据卡说明其中 65% 要求集合答案。
数据划分：单一 eval 划分；answer_type 属于评测元数据，推理时不能提供给代理。
格式：CSV, loadable through Hugging Face Datasets.。

## 真值与评测

参考答案枚举目标条目，而不是相关页面或浏览动作。LLM 评分器先匹配语义等价答案，再计算集合指标；答案成员正确不代表引用有依据或来源链完整。

官方指标：answer_set_F1, answer_precision, answer_recall, fully_correct_rate, fully_incorrect_rate, correct_with_extraneous_answers_rate。

评测协议：以逐题答案集合 F1 的宏平均作为主要排序指标，另报严格完全正确率。去重答案条目并进行语义匹配；论文使用 Gemini 2.5 Flash 判分。记录网页、搜索、判分模型版本和预算，漏项与多余猜测都须影响得分。

## 适用场景

- 评测网页研究中的穷尽收集与停止决策
- 区分高答案召回率与完全正确的答案集合

## 限制与注意事项

- 答案层面的精确率和召回率不是文档检索相关性标注
- 实时来源可用性与判分模型行为可能随运行时间变化
- 多数集合答案任务要求完整成员，而非一个貌似合理的支持事实

## 获取方式与来源

- [官方资源](https://huggingface.co/datasets/google/deepsearchqa)
- [论文](https://storage.googleapis.com/deepmind-media/DeepSearchQA/DeepSearchQA_benchmark_paper.pdf)
- [数据](https://huggingface.co/datasets/google/deepsearchqa)
- dataset_card：[来源](https://huggingface.co/datasets/google/deepsearchqa) — 支持字段 `summary`、`classification`、`data`、`ground_truth.description`、`access.license`、`access.gated`、`evaluation.evaluator`
- paper：[来源](https://storage.googleapis.com/deepmind-media/DeepSearchQA/DeepSearchQA_benchmark_paper.pdf) — 支持字段 `data.description`、`ground_truth.provenance`、`evaluation.official_metrics`、`evaluation.protocol`、`use.caveats`
- official：[来源](https://blog.google/innovation-and-ai/technology/developers-tools/deep-research-agent-gemini-api/) — 支持字段 `data.description`、`use.best_for`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
