<!-- Generated from catalog/datasets/deepresearch-bench-ii.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# DeepResearch Bench II

[English](deepresearch-bench-ii.md)

基于专家报告的细粒度量规，分别测量深度研究报告的信息召回、分析与呈现。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-01 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | agentic_search, long_form_qa, attribution |
| 模态 | text |
| 已发布真值标注层级 | rubric |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | Per-task data terms follow DATA_LICENSE and each record's source license; 129 tasks CC-BY-4.0, two CC-BY-NC-4.0 and one CC0, not the Apache-2.0 code license. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

tasks_and_rubrics.jsonl 提供问题及含实质内容的评分量规，经 LLM 抽取、修订和人工专家复核从专家文章构建。代理自行研究网页并写报告；参考文章和禁止引用规则用于评测，不能作为金标准上下文提供给代理。

发布规模：发布 132 个任务、22 个领域，包含 66 个英文和 66 个中文任务、9,430 条量规；2026 年 10 月榜单排除任务 112 和 114，剩余 130 个可评分任务。
数据划分：公开评测集；保留全部 132 条记录用于版本核算，同时报告实际评分任务 ID、有效结果数量和排除项。
格式：JSONL tasks/rubrics; evaluated Markdown or DOCX reports are parsed to text by the current pipeline.。

## 真值与评测

公开二元内容量规编码输出应满足的事实或推断要求，不是来源坐标相关性标注，也不是唯一参考报告。当前判分中 1 表示有依据地满足、0 表示未提及、-1 表示依赖禁用参考；evidence 字符串定位生成报告中的文字，不是原始来源证据真值。

官方指标：total, inforecall, analysis, presentation, blocked_rate。

评测协议：聚合器计算评分为 1 的量规比例，另报禁用参考比例，再平均可用任务结果。固定任务 ID、分母和评分分支；官方评分器于 2026 年 8 月迁移，10 月评分排除两题。不能混用历史 132 题和当前 130 题分数，也不能把量规满足率当作文档召回率。

## 适用场景

- 区分信息遗漏与分析或呈现不足
- 设计可独立核验的细粒度报告量规

## 限制与注意事项

- 来源文章泄漏与禁用参考使用须与写作质量分别分析
- 当前仓库解析会忽略报告内嵌图像，支持文件格式不等于具有多模态检索真值
- 各任务许可与评分资格不同，须保留逐任务元数据，不能统一指定许可或分母

## 获取方式与来源

- [官方资源](https://github.com/imlrz/DeepResearch-Bench-II)
- [论文](https://arxiv.org/abs/2601.08536)
- [数据](https://github.com/imlrz/DeepResearch-Bench-II/blob/main/tasks_and_rubrics.jsonl)
- paper：[来源](https://arxiv.org/html/2601.08536) — 支持字段 `name`、`summary`、`data.description`、`data.size`、`ground_truth.provenance`、`use.best_for`
- repository：[来源](https://github.com/imlrz/DeepResearch-Bench-II) — 支持字段 `data.splits`、`data.format`、`ground_truth.description`、`evaluation.protocol`、`use.caveats`
- repository：[来源](https://github.com/imlrz/DeepResearch-Bench-II/blob/main/aggregate_scores.py) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`
- repository：[来源](https://github.com/imlrz/DeepResearch-Bench-II/blob/main/DATA_LICENSE) — 支持字段 `access.license`
- repository：[来源](https://github.com/imlrz/DeepResearch-Bench-II/blob/main/tasks_and_rubrics.jsonl) — 支持字段 `data.size`、`ground_truth.levels`、`ground_truth.description`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
