<!-- Generated from catalog/datasets/asqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# ASQA

[English](asqa.md)

针对有歧义的事实性问题，提供长篇回答及用于消歧的短问答对。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `text_rag` |
| 任务 | long_form_qa, attribution |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

问题和长篇回答附有抽取式问答对；ALCE 另行发布使用检索结果的改造版本。


## 真值与评测

参考答案覆盖同一问题的多种解释；原生来源引用与 ALCE 改造版中的引用并不等价。

官方指标：rouge, qa_accuracy。

评测协议：使用 ALCE 提供的检索段落时，应单独报告其检索快照与引用评分设置。

## 适用场景

- 评测长篇回答对歧义解释的覆盖
- 通过 ALCE 评测引用

## 限制与注意事项

- 原始 ASQA 与 ALCE-ASQA 是不同评测设置

## 获取方式与来源

- [官方资源](https://github.com/google-research/language/tree/master/language/asqa)
- dataset_card：[来源](https://github.com/tensorflow/datasets/blob/master/docs/catalog/asqa.md) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.official_metrics`
- repository：[来源](https://github.com/princeton-nlp/ALCE) — 支持字段 `data.description`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
