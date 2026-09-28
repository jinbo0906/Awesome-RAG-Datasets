<!-- Generated from catalog/datasets/crag.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# CRAG

[English](crag.md)

面向 RAG 的时效性事实问答，附网页结果和模拟知识接口。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | single_hop_qa, multi_hop_qa |
| 模态 | text, graph |
| 已发布真值标注层级 | answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | CC BY-NC 4.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

问题跨五个领域和八种类别；发布的检索内容包括网页搜索结果和模拟 API。


## 真值与评测

提供金标准答案和可接受的替代答案；检索到的网页是候选上下文，并非金标准支持片段。

官方指标：correctness_with_abstention。

评测协议：官方评分区分正确答案、未回答和错误答案。

## 适用场景

- 有时间变化的事实检索
- 弃答策略与错误成本分析

## 限制与注意事项

- 搜索结果不是相关性真值；不能把每个返回网页都当成支持证据

## 获取方式与来源

- [官方资源](https://github.com/facebookresearch/CRAG)
- [论文](https://arxiv.org/abs/2406.04744)
- repository：[来源](https://github.com/facebookresearch/CRAG) — 支持字段 `summary`、`data.description`、`evaluation.protocol`、`access.license`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
