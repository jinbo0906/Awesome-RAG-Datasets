<!-- Generated from catalog/datasets/musique.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# MuSiQue

[English](musique.md)

由单跳来源组合成的问题，要求连贯的多跳推理。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | multi_hop_qa, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | paragraph, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | CC BY 4.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

MuSiQue-Ans 与 MuSiQue-Full 的可回答性设置不同；训练、开发和测试数据按官方格式发布。


## 真值与评测

问题分解与支持段落可用于测试完整证据链检索。

官方指标：answer_em, answer_f1, support_f1。

评测协议：Ans 与 Full 应分开比较。

## 适用场景

- 连贯的多跳推理
- 固定上下文预算下的证据完整性

## 限制与注意事项

- 作为种子的单跳问题可能与其他训练数据重叠；应查阅发布的泄漏 ID

## 获取方式与来源

- [官方资源](https://github.com/StonyBrookNLP/musique)
- [论文](https://aclanthology.org/2022.tacl-1.31/)
- repository：[来源](https://github.com/StonyBrookNLP/musique) — 支持字段 `summary`、`data.description`、`access.license`、`use.caveats`、`evaluation.evaluator`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
