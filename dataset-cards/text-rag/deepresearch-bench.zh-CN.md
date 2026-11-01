<!-- Generated from catalog/datasets/deepresearch-bench.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# DeepResearch Bench (Du et al.)

[English](deepresearch-bench.md)

专家设计的开放网页研究任务，结合自适应报告质量标准与引用支持度核查。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-01 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | agentic_search, long_form_qa, attribution |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | Apache-2.0 for the official Hugging Face report/annotation release; retrieved web sources retain their own terms. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

官方仓库提供研究问题、参考与评测材料和生成报告；Hugging Face 配套发布模型报告及人工评分标注。RACE 根据参考报告评测质量，FACT 抽取陈述—URL 对并核查网页支持；这两个框架本身不是另外两个数据集。

发布规模：共 100 个任务、22 个领域，包含 50 个英文和 50 个中文问题；用于构建分析的 96,147 条用户查询不是评测规模。
数据划分：公开评测任务集；参考协议未指定训练划分。
格式：JSONL prompts, reference/model reports and evaluation annotations.。

## 真值与评测

专家任务结合参考报告和 LLM 衍生评分标准，公开人工标注用于分析评分器一致性。参考中含模型生成报告，并非唯一人工金标准答案。FACT 在评分时验证输出引用，不提供完整检索相关性标签。

官方指标：RACE_overall, RACE_comprehensiveness, RACE_depth, RACE_instruction_following, RACE_readability, FACT_citation_accuracy, FACT_effective_citations。

评测协议：分别报告 RACE 与 FACT，固定参考、清洗器、评分器和抓取流程。2026 年 5 月官方更换 RACE 判分模型，9 月更换清洗模型，因此历史 Gemini 评分与新 GPT 评分不能合并。记录代理检索预算和评测日期；引用页面无法抓取会影响 FACT。

## 适用场景

- 分别评测长报告综合与引用支持
- 审查深度研究代理的质量和搜索成本

## 限制与注意事项

- 这是 Du 等人的 100 任务基准，不是 FutureSearch 同名的 91 任务 DeepResearchBench
- RACE 依赖参考和判分模型，FACT 引用准确率不是穷尽式证据召回率
- Hugging Face 配套集包含报告和标注，实际任务问题应读取仓库的 query.jsonl

## 获取方式与来源

- [官方资源](https://github.com/Ayanami0730/deep_research_bench)
- [论文](https://proceedings.iclr.cc/paper_files/paper/2026/hash/465f22be10e07b301c6ed58f0472f704-Abstract-Conference.html)
- [数据](https://huggingface.co/datasets/muset-ai/DeepResearch-Bench-Dataset)
- paper：[来源](https://proceedings.iclr.cc/paper_files/paper/2026/hash/465f22be10e07b301c6ed58f0472f704-Abstract-Conference.html) — 支持字段 `name`、`summary`、`data.size`、`classification.rag_role`
- paper：[来源](https://arxiv.org/html/2506.11763) — 支持字段 `data.description`、`ground_truth.description`、`ground_truth.provenance`、`ground_truth.alternatives`、`evaluation.official_metrics`
- repository：[来源](https://github.com/Ayanami0730/deep_research_bench) — 支持字段 `data.size`、`data.splits`、`data.format`、`evaluation.protocol`、`evaluation.evaluator`、`use.caveats`
- dataset_card：[来源](https://huggingface.co/datasets/muset-ai/DeepResearch-Bench-Dataset) — 支持字段 `access.license`、`data.description`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
