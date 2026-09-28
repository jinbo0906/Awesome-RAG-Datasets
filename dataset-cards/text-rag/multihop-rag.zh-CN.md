<!-- Generated from catalog/datasets/multihop-rag.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# MultiHop-RAG

[English](multihop-rag.md)

开放式多文档 RAG 问答，附问题类型及支持证据标签。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | multi_hop_qa, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | document, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

发布的知识库和问题集包含推断、比较、时间推理以及无答案案例。


## 真值与评测

每个问题与多个来源文档中的支持证据关联。

官方指标：retrieval_recall, answer_accuracy。

评测协议：将无答案案例与可回答的多跳案例分开报告。

## 适用场景

- 多文档检索
- 时间或比较推理

## 限制与注意事项

- 支持文档不一定对应最小充分证据片段

## 获取方式与来源

- [官方资源](https://github.com/yixuantt/MultiHop-RAG)
- [论文](https://arxiv.org/abs/2401.15391)
- repository：[来源](https://github.com/yixuantt/MultiHop-RAG) — 支持字段 `summary`、`data.description`、`ground_truth.description`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
