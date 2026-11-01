<!-- Generated from catalog/datasets/evolveqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# evolveQA

[English](evolveqa.md)

按知识截止日期对齐，区分当前有效、已经过时与完全错误答案的动态事实探测数据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-01 |
| RAG 角色 | `auxiliary` |
| 主分类 | `text_rag` |
| 任务 | time_sensitive_qa |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | synthetic |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | CC-BY-NC-ND-4.0; the author README limits the release to academic/scientific reproducibility and prohibits model training. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

作者于 2026 年 10 月公开带时间戳的 AWS 更新、Azure 变化和 WHO 疾病暴发新闻来源，以及生成的问答。问题包括开放回答、选择题和成对可验证形式，具有实体/概念/属性元数据及答案日期。原生实验不检索，而是探测参数知识；公开原始来源不代表已经发布开放 RAG 的相关性或引用评测协议。

发布规模：发布修订 2deea4042935b44b06c19c6dfed19ce25d928887 的 18 个截止日期 JSON 文件共含 4,967 条记录，按领域和 question_id 去重为 937 个键。最新截止日期单独含 922 条（AWS 550、Azure 203、WHO 169）。
数据划分：2023 年 8 月至 2024 年 8 月的六个知识截止日期条件，不是独立的训练/测试划分；问题 ID 在不同截止日期文件中重复出现。
格式：JSON question arrays plus domain-organized raw source data。

## 真值与评测

模型生成的参考答案及选项/是非标签与选定截止日期对齐。人工抽样审查构建质量，不代表每个公开标签都经过人工确认。实体/概念/属性和 recent_answer_date 字段不提供逐题文档相关性标注或证据片段。

官方指标：accuracy, verifiable_qa_hard_accuracy, outdated_response_rate。

评测协议：将模型知识截止点与所选条件匹配，并分开报告各类探测形式。Hard accuracy 要求同一事实的真与假诱导问题均答对。开放回答使用论文规定的评判模型，结合当前与历史答案分成当前正确、过时或错误；ORR 越低越好。任何检索改造都须另外定义来源快照、相关性标注及证据/引用指标。

## 适用场景

- 为 RAG 实验提供按知识截止点对齐的参数知识对照
- 区分已经过时的回答与完全错误的回答

## 限制与注意事项

- 原生分数不评测检索或知识库持续更新
- 六个历史截止日期不测量截至 2026 年 11 月的最新知识
- 重复问题 ID 和多种探测形式不能作为独立问题计数
- 公开可获取不代表取消禁止训练和限定用途条款

## 获取方式与来源

- [官方资源](https://github.com/amazon-science/evolveQA)
- [论文](https://aclanthology.org/2026.emnlp-main.2373/)
- [数据](https://github.com/amazon-science/evolveQA/tree/main/evolveQA-benchmark)
- paper：[来源](https://aclanthology.org/2026.emnlp-main.2373.pdf) — 支持字段 `summary`、`classification`、`ground_truth`、`evaluation.official_metrics`、`evaluation.protocol`、`use.best_for`
- repository：[来源](https://github.com/amazon-science/evolveQA) — 支持字段 `data.description`、`data.corpus`、`data.queries`、`data.answers`、`data.splits`、`data.format`、`access.data`、`access.license`、`access.gated`、`use.caveats`
- repository：[来源](https://github.com/amazon-science/evolveQA/tree/2deea4042935b44b06c19c6dfed19ce25d928887/evolveQA-benchmark) — 支持字段 `data.size`
- repository：[来源](https://github.com/amazon-science/evolveQA/blob/main/LICENSE) — 支持字段 `access.license`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
