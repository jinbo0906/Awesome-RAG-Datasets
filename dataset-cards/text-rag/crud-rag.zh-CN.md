<!-- Generated from catalog/datasets/crud-rag.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# CRUD-RAG

[English](crud-rag.md)

中文 RAG 基准，覆盖续写、问答、摘要与文本纠错。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | single_hop_qa, multi_hop_qa, summarization, rag_robustness |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

发布包包含完整任务数据、论文选用的实验子集，以及用于构建检索库的八万余篇新闻文档。

格式：JSON and text documents。

## 真值与评测

任务参考文本用于生成与纠错评分；本条目不声称所有样本都提供统一的句子级支持证据集合。

官方指标：bleu, rouge, bertscore, ragquesteval。

评测协议：选择已发布的实验子集，报告任务、分块方式、top-k 与模型提示词。RAGQuestEval 需要问题生成与回答模型。

## 适用场景

- 中文新闻中超出短问答的 RAG 任务
- 在同一检索语料上比较多种生成任务

## 限制与注意事项

- 参考文本风格及提示词会影响词面匹配指标
- 仓库引用注明 ACM TOIS，不能把 arXiv 版本改写成会议论文

## 获取方式与来源

- [官方资源](https://github.com/IAAR-Shanghai/CRUD_RAG)
- [论文](https://doi.org/10.1145/3701228)
- [数据](https://github.com/IAAR-Shanghai/CRUD_RAG/tree/main/data)
- repository：[来源](https://github.com/IAAR-Shanghai/CRUD_RAG) — 支持字段 `summary`、`classification`、`data`、`ground_truth`、`evaluation`、`access.paper`、`use`
- paper：[来源](https://arxiv.org/html/2401.17043v3) — 支持字段 `ground_truth.provenance`、`evaluation.official_metrics`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
