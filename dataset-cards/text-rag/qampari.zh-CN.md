<!-- Generated from catalog/datasets/qampari.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# QAMPARI

[English](qampari.md)

开放域多答案问答，每个问题的多个答案由不同段落支持。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `text_rag` |
| 任务 | multi_hop_qa, long_form_qa, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | paragraph, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

问题根据维基百科知识图谱和表格关系构建，再关联支持段落；ALCE 另行打包检索输出用于引用实验。


## 真值与评测

发布了答案实体及支持段落；段落对齐依赖自动构建和问答验证。

官方指标：answer_f1, citation_quality。

评测协议：将原始答案集合任务与 ALCE 在给定引用条件下的评测区分开。

## 适用场景

- 多答案证据覆盖
- 分散证据下的引用完整性

## 限制与注意事项

- 单一段落未必覆盖全部正确答案
- 必须说明原始语料快照

## 获取方式与来源

- [官方资源](https://arxiv.org/abs/2205.12665)
- paper：[来源](https://arxiv.org/abs/2205.12665) — 支持字段 `summary`、`data.description`、`ground_truth.description`
- repository：[来源](https://github.com/princeton-nlp/ALCE) — 支持字段 `evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
