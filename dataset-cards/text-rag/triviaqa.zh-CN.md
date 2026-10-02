<!-- Generated from catalog/datasets/triviaqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# TriviaQA

[English](triviaqa.md)

来自趣味问答的问题，附答案别名以及独立收集的维基百科与网页证据文档。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `text_rag` |
| 任务 | single_hop_qa, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | document, answer |
| 证据标注来源 | distant |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | Apache-2.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

阅读理解版本提供与问题关联的证据文档；未过滤版本保留检索文档可能不含答案的问题。若进行开放域检索，还需另行定义共享索引。

发布规模：超过 65 万个问题—答案—证据三元组；阅读理解版本约有 9.5 万个问答对，未过滤版本有 11 万个。

## 真值与评测

答案别名用于回答评分。证据文档独立收集，主要通过远程监督建立关联；文档被纳入并不意味着具有人工支持片段或完整相关性标注。

官方指标：exact_match, token_f1。

评测协议：区分维基百科与网页、过滤与未过滤、人工核验子集等设置；使用官方答案别名评分。

## 适用场景

- 开放域事实问答
- 对照答案别名评分与检索覆盖率

## 限制与注意事项

- 随题提供的证据文档不是现成的共享检索索引
- 远程监督证据标签不是金标准分块边界

## 获取方式与来源

- [官方资源](https://nlp.cs.washington.edu/triviaqa/)
- [论文](https://aclanthology.org/P17-1147/)
- official：[来源](https://nlp.cs.washington.edu/triviaqa/) — 支持字段 `summary`、`data.description`、`data.size`、`ground_truth.description`
- repository：[来源](https://github.com/mandarjoshi90/triviaqa) — 支持字段 `access.license`、`evaluation.protocol`
- repository：[来源](https://github.com/mandarjoshi90/triviaqa/blob/master/evaluation/triviaqa_evaluation.py) — 支持字段 `evaluation.official_metrics`、`ground_truth.alternatives`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
