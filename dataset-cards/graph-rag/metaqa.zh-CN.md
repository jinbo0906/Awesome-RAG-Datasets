<!-- Generated from catalog/datasets/metaqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# MetaQA

[English](metaqa.md)

电影领域知识库问答，包含一跳、两跳和三跳问题变体。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `graph_rag` |
| 任务 | graph_qa, graph_reasoning |
| 模态 | text, graph, audio |
| 已发布真值标注层级 | answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

官方版本以主语—关系—宾语三元组提供电影知识库，按跳数划分问答，还包含问题改写变体 与可选的音频问题。图问答任务应与音频变体分开报告。


## 真值与评测

发布了答案实体；知识库与问题模板体现设计上的跳数复杂度，但不能假设每题都有唯一标注图路径或被引用的文本段落。

官方指标：answer_accuracy。

评测协议：固定知识库版本、跳数及原始/改写/音频变体。若要测试 GraphRAG 路径，应增加独立核查的路径 或子图标签，而不是用被测检索器的输出反推真值。

## 适用场景

- 可控的图多跳推理
- 知识库检索器的消融实验

## 限制与注意事项

- 模板衍生问题不同于开放式 GraphRAG 任务
- 原生版本不保证有金标准引用路径

## 获取方式与来源

- [官方资源](https://github.com/yuyuz/MetaQA)
- repository：[来源](https://github.com/yuyuz/MetaQA) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
