<!-- Generated from catalog/datasets/opendialkg.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# OpenDialKG

[English](opendialkg.md)

人类对话与参与者标注的知识图谱路径配对，并发布底层图谱。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `graph_rag` |
| 任务 | conversational_qa, graph_reasoning |
| 模态 | graph, text |
| 已发布真值标注层级 | graph_path, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | CC BY-NC 4.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

发布包包含对话 CSV 及实体、关系、三元组文件；对话上下文可作查询，后续发言可作回复。

发布规模：13,802 段对话、91,209 轮；底层知识图谱有 100,813 个实体及 1,190,658 条双向三元组。
格式：CSV with JSON actions and tab-separated KG triples。

## 真值与评测

参与者选择连接相邻轮次概念的路径；中间实体不必出现在正文中，路径也不是唯一的事实答案证据集合。

官方指标：entity_recall_at_k, human_response_preference。

评测协议：原论文按 k=1、3、5、10、25 评测回复实体预测，并让人工判断自然程度。保留同领域与跨领域设置的区别。

## 适用场景

- 具有显式监督的对话图谱路径
- 跨对话领域的图推理

## 限制与注意事项

- 实体预测指标不是完整答案的事实性或引用指标
- 官方仓库已归档，没有提供统一的现代 GraphRAG 评测器

## 获取方式与来源

- [官方资源](https://github.com/facebookresearch/opendialkg)
- [论文](https://aclanthology.org/P19-1081/)
- [数据](https://github.com/facebookresearch/opendialkg/tree/main/data)
- repository：[来源](https://github.com/facebookresearch/opendialkg) — 支持字段 `summary`、`classification`、`data`、`ground_truth`、`access.license`、`use`
- paper：[来源](https://aclanthology.org/P19-1081.pdf) — 支持字段 `evaluation`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
