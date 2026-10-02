<!-- Generated from catalog/datasets/wizard-of-wikipedia.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# Wizard of Wikipedia

[English](wizard-of-wikipedia.md)

人工写出的知识对话，附检索得到的维基百科候选内容与选定支持句。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | conversational_qa, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | sentence, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

原始对话提供话题、用户和向导发言、检索段落及已选知识。随题提供的候选内容支持原生任务；替换为完整维基百科索引时需另行明确设置。

数据划分：训练、验证和测试资源区分已见话题与未见话题评测。

## 真值与评测

向导轮次通过 checked_sentence 和 checked_passage 标识标注者选定的知识，并提供实际回复。选中的知识不一定枚举所有能支持可接受回复的句子。

官方指标：knowledge_accuracy, response_f1, perplexity, human_rating。

评测协议：分别报告已见与未见话题，区分知识选择与回复生成；复现原生知识选择设置时保留其候选池。

## 适用场景

- 有知识依据的对话回复
- 向未见对话话题泛化

## 限制与注意事项

- 选定句子不是完整的可替代证据集合
- 原生检索候选内容与不受限的维基百科检索不同

## 获取方式与来源

- [官方资源](https://parl.ai/projects/wizard_of_wikipedia/)
- [论文](https://arxiv.org/abs/1811.01241)
- official：[来源](https://parl.ai/projects/wizard_of_wikipedia/) — 支持字段 `summary`、`data.description`、`data.splits`、`ground_truth.description`、`evaluation.official_metrics`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
