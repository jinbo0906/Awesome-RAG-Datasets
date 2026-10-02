<!-- Generated from catalog/datasets/opendocvqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# OpenDocVQA

[English](opendocvqa.md)

VDocRAG 公开的开放域文档图像问答集合，提供汇集页面和相关图像标识。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_native` |
| 主分类 | `multimodal_rag` |
| 任务 | page_retrieval, visual_qa, multi_hop_qa |
| 模态 | text, image, table, chart, layout |
| 已发布真值标注层级 | page, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | Per-source licenses; MHDocVQA/VisualMRC/SlideVQA QA use the NTT evaluation license. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

九个经过过滤的集合融合 DocVQA、InfographicVQA、VisualMRC、ChartQA、OpenWikiTable、DUDE、MPMQA、SlideVQA 和新建 MHDocVQA。官方问答与图像语料分别发布。

发布规模：约 43,000 组问答、200,000 张文档图像，包含干扰页面。
数据划分：按来源划分训练／开发和测试配置；ChartQA 与 SlideVQA 是零样本测试来源。
格式：Hugging Face QA records with query, answers and relevant_doc_ids; separate image corpus.。

## 真值与评测

relevant_doc_ids 标识相关文档图像，MHDocVQA 可对应多张图像。人工来源问答与新建多跳问题共存；不宣称有统一的区域、表格单元格或最小跨度真值。

官方指标：nDCG@5, ANLS, relaxed_accuracy, F1。

评测协议：区分按来源的 single-pool 和统一的 all-pool 检索。检索使用 nDCG@5，问答使用原始来源指标；VDocRAG 报告的生成结果使用前三张检索图像。

## 适用场景

- 开放域页面检索后进行视觉回答
- 比较独立来源池和统一图像语料

## 限制与注意事项

- 获取语料需要接受条款并共享联系信息
- 过滤后的来源问答与新建 MHDocVQA 应保留各自的数据集身份

## 获取方式与来源

- [官方资源](https://vdocrag.github.io/)
- [论文](https://arxiv.org/abs/2504.09795)
- [数据](https://huggingface.co/datasets/NTT-hil-insight/OpenDocVQA)
- official：[来源](https://vdocrag.github.io/) — 支持字段 `summary`、`data.size`、`use.best_for`
- dataset_card：[来源](https://huggingface.co/datasets/NTT-hil-insight/OpenDocVQA) — 支持字段 `data.description`、`data.splits`、`data.format`、`ground_truth.description`、`access.license`
- dataset_card：[来源](https://huggingface.co/datasets/NTT-hil-insight/OpenDocVQA-Corpus) — 支持字段 `access.gated`、`access.license`、`use.caveats`
- paper：[来源](https://arxiv.org/html/2504.09795) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`、`ground_truth.provenance`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
