<!-- Generated from catalog/datasets/medqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# MedQA

[English](medqa.md)

医师资格考试选择题问答数据，含多语言子集和用于医学 RAG 实验的参考资料。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `text_rag` |
| 任务 | single_hop_qa |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown for source exam/textbook content; repository code is MIT |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

作者仓库提供问答划分与参考教材下载。MIRAGE 选用美国英语四选项测试子集；原生 MedQA 还有其他语言与选项数量设置。

格式：JSONL。

## 真值与评测

正确选项监督考试问答。参考教材是候选知识来源，不是按问题标注的支持文档或引用真值。

官方指标：accuracy。

评测协议：注明语言、选项数量和划分。在 MIRAGE 中使用 1,273 题的美国四选项子集，仅用问题检索并固定语料快照。

## 适用场景

- 医学领域的检索增强考试问答
- 通过 MIRAGE 比较语料与检索器组合

## 限制与注意事项

- 答案标签不指出哪个检索来源支持答案
- 原始语言或选项变体与 MIRAGE-US 不能互换

## 获取方式与来源

- [官方资源](https://github.com/jind11/MedQA)
- [论文](https://arxiv.org/abs/2009.13081)
- [数据](https://github.com/jind11/MedQA)
- repository：[来源](https://github.com/jind11/MedQA) — 支持字段 `summary`、`data.description`、`data.corpus`、`ground_truth.description`、`access.data`、`access.license`
- repository：[来源](https://github.com/gzxiong/MIRAGE) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
