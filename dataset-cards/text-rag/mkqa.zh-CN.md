<!-- Generated from catalog/datasets/mkqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# MKQA

[English](mkqa.md)

将同一批 Natural Questions 查询对齐到 26 种语言的事实问答，答案标注不依赖特定段落。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `text_rag` |
| 任务 | single_hop_qa, rag_robustness |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | not_provided / provided / provided |
| 原始数据许可 | CC-BY-SA-3.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

对抽样的 Natural Questions 查询重新收集不依赖段落的答案，再由人工翻译问题与答案。提供文本、实体、二元答案及不可回答标签，没有原生检索语料。

发布规模：1 万个对齐查询覆盖 26 种语言，共形成 26 万个语言特定问答对。

## 真值与评测

类型化答案包含可接受别名，部分答案附 Wikidata QID。这些标识用于跨语言答案对齐，不是金标准支持文档或片段。

官方指标：exact_match, token_f1。

评测协议：使用官方的语言特定归一化与无答案阈值。官方宏平均需要全部 26 种语言；披露可回答性筛选条件和另选的 RAG 语料。

## 适用场景

- 比较对齐的多语言答案质量
- 改造成跨语言检索任务

## 限制与注意事项

- 不提供原生段落相关性真值
- 仅保留可回答问题或只对部分语言求平均会改变协议

## 获取方式与来源

- [官方资源](https://github.com/apple-aiml-research/ml-mkqa)
- [论文](https://aclanthology.org/2021.tacl-1.82/)
- repository：[来源](https://github.com/apple-aiml-research/ml-mkqa) — 支持字段 `summary`、`data.description`、`data.size`、`ground_truth.description`、`evaluation.official_metrics`、`evaluation.protocol`、`access.license`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
