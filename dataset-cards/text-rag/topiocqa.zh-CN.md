<!-- Generated from catalog/datasets/topiocqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# TopiOCQA

[English](topiocqa.md)

包含话题切换的开放域多轮问答，提供自由形式答案与金标准维基百科段落。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | conversational_qa, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | paragraph, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | CC-BY-NC-SA-4.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

作者资源提供对话、金标准问题—段落对、维基百科语料及其分段检索版本。答案可以是生成式表达，不一定作为原样子串出现在支持段落中。

发布规模：发布的检索设置使用约 2,570 万个维基百科段落。

## 真值与评测

金标准段落为答案提供依据；阅读器评测还使用额外的人工答案。段落标识支持检索评分，无需假定答案字符串匹配就能识别证据。

官方指标：Hits@k, exact_match, token_f1。

评测协议：按提供的金标准段落评测检索，使用官方 CoQA 风格的多参考答案评测器评测生成。保留对话历史和话题切换；明确标识外部生成的问题改写。

## 适用场景

- 多轮检索中的话题切换
- 基于检索段落生成非抽取式答案

## 限制与注意事项

- 答案字符串包含关系不足以用于检索评分
- 模型资源中的问题改写不能直接视为原始人工标注

## 获取方式与来源

- [官方资源](https://mcgill-nlp.github.io/topiocqa/)
- [论文](https://arxiv.org/abs/2110.00768)
- [数据](https://github.com/McGill-NLP/topiocqa)
- repository：[来源](https://github.com/McGill-NLP/topiocqa) — 支持字段 `summary`、`data.description`、`data.size`、`ground_truth.description`、`evaluation.protocol`、`access.license`
- repository：[来源](https://github.com/McGill-NLP/topiocqa/blob/main/evaluate_retriever.py) — 支持字段 `evaluation.official_metrics`
- repository：[来源](https://github.com/McGill-NLP/topiocqa/blob/main/evaluate_reader.py) — 支持字段 `evaluation.official_metrics`、`ground_truth.alternatives`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
