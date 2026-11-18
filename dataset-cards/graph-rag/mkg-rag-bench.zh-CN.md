<!-- Generated from catalog/datasets/mkg-rag-bench.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# MKG-RAG-Bench

[English](mkg-rag-bench.md)

检索文本或带图像的知识图谱三元组，并评测基于同一三元组构建的问答。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-18 |
| RAG 角色 | `rag_native` |
| 主分类 | `graph_rag` |
| 任务 | evidence_retrieval, multimodal_retrieval, graph_qa |
| 模态 | graph, text, image |
| 已发布真值标注层级 | graph_triplet, answer |
| 证据标注来源 | synthetic |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

通用 G 基于 MarKG，医疗 M 基于 MedMKG。发布包提供三元组、文本／多模态问题及 TSV 相关性标签。完整视觉条件需获取上游图像，部分医疗图像路径来自 MIMIC-CXR-JPG。

发布规模：G 训练／验证／测试分别有 48,908／6,113／6,115 问与 25,517 个三元组。M 对应 4,781／597／599 问与 18,468 个三元组。测试问题数已从发布文件核对。
数据划分：每个领域设训练、验证和测试，各划分共享本领域语料。记录允许的查询与候选三元组模态。
格式：JSONL for queries and triple records, TSV for qrels, external image files。

## 真值与评测

问题从选定三元组遮蔽元素后构建。相关性标签定位支持三元组，答案来自被遮蔽元素。逐三元组标签不覆盖多跳路径完整性。

官方指标：nDCG_at_k, precision_at_k, recall_at_k, EM, token_F1, Contains_at_1, BLEU_1。

评测协议：固定查询和候选模态组合，用相关性标注评估三元组排序。论文在生成阶段向 GPT-5 提供前五个检索三元组，用词面答案指标与无检索对照比较。

## 适用场景

- 比较图像对三元组检索的贡献
- 在受控模态条件下拆开检索与回答评估

## 限制与注意事项

- 图像需从上游取得且部分可能要求凭资质访问
- 论文许可不确定数据与图像条款
- 从三元组构造问答不测从原始文档建图

## 获取方式与来源

- [官方资源](https://github.com/XiaochenWang-PSU/MKG-RAG-Bench)
- [论文](https://doi.org/10.1145/3770855.3817570)
- [数据](https://github.com/XiaochenWang-PSU/MKG-RAG-Bench/tree/34a1b5d96fbcaf92eac0c478f41ca6ce972b437e)
- paper：[来源](https://arxiv.org/html/2606.26458) — 支持字段 `summary`、`classification`、`data.description`、`data.size`、`ground_truth`、`evaluation.official_metrics`、`evaluation.protocol`、`use`
- repository：[来源](https://github.com/XiaochenWang-PSU/MKG-RAG-Bench/tree/34a1b5d96fbcaf92eac0c478f41ca6ce972b437e) — 支持字段 `data`、`access.data`、`evaluation.evaluator`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
