<!-- Generated from catalog/datasets/squad.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# SQuAD 2.0

[English](squad.md)

基于维基百科段落的阅读理解，结合抽取式问题和对抗构造的不可回答问题。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `text_rag` |
| 任务 | single_hop_qa, rag_robustness |
| 模态 | text |
| 已发布真值标注层级 | span, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | CC-BY-SA-4.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

每个样本提供阅读段落和问题；可回答问题有答案片段，不可回答问题要求弃答。本条目使用 2.0 版本，不为 1.1 版本另建条目。

发布规模：2.0 版本将约 10 万个 1.1 版本问题与超过 5 万个对抗构造的不可回答问题结合。
数据划分：训练集和开发集公开；官方测试数据不公开。

## 真值与评测

众包标注者提供答案文本及其在给定段落中的字符位置；空答案表示在该段落中不可回答，并非在所有外部文档中都不可回答。

官方指标：exact_match, token_f1。

评测协议：使用 2.0 版本评测器及其无答案处理规则。改造成 RAG 时需定义检索池并保留来源偏移；随题提供的段落不等同于开放语料检索结果。

## 适用场景

- 从检索上下文中抽取答案
- 按上下文判断是否应当弃答

## 限制与注意事项

- 原生评测直接提供段落
- SQuAD 1.1 与 2.0 的可回答性设置不同

## 获取方式与来源

- [官方资源](https://rajpurkar.github.io/SQuAD-explorer/)
- [论文](https://arxiv.org/abs/1806.03822)
- official：[来源](https://rajpurkar.github.io/SQuAD-explorer/) — 支持字段 `summary`、`data.description`、`data.size`、`data.splits`、`ground_truth.description`、`evaluation.official_metrics`、`evaluation.protocol`、`access.license`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
