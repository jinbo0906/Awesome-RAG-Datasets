<!-- Generated from catalog/datasets/mmdocrag.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# MMDocRAG

[English](mmdocrag.md)

多页多模态文档问答，包含跨模态证据链和摘录选择。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-18 |
| RAG 角色 | `rag_native` |
| 主分类 | `multimodal_rag` |
| 任务 | page_retrieval, layout_retrieval, visual_qa, attribution |
| 模态 | text, image, table, chart, layout |
| 已发布真值标注层级 | page, quote, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | The Hugging Face release is tagged Apache-2.0. The paper Appendix G limits new question, evidence and answer annotations to academic and noncommercial research unless the authors give written permission. Check both terms before reuse. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

官方 Hugging Face 发布 PDF、图像压缩包与问答 JSONL，提供 15 条和 20 条候选摘录设置，包含金标准和困难负例图文摘录。

发布规模：论文报告 222 份文档的 4,055 道问答，其中 2,503 道为跨模态问题。
数据划分：论文划分为 2,055 道开发题与 2,000 道评测题。15 条、20 条摘录评测文件对应评测题的两种候选设置。

## 真值与评测

将题目内的 `gold_quotes` ID 连接到 `text_quotes` 和 `img_quotes`，再按所属文档及 `page_id`、`layout_id` 定位。记录提供短答案和图文交织答案。用 `evidence_modality_type` 筛选涉及多种模态的题目。

官方指标：quote_selection_f1, BLEU, ROUGE-L, answer_quality。

评测协议：给定上下文做摘录选择时，使用对应的 `evaluation_15.jsonl` 或 `evaluation_20.jsonl` 与作者的 `eval_all.py`。评分器比较预测与金标准摘录 ID，单独的 `eval_llm_judge.py` 评分图文交织答案。固定候选设置、输入模式及判分模型，区分从原文检索与给定候选选择的结果。研究证据碎片化时，可结合选型指南，用明确的事实到摘录映射评估完整集合覆盖。

## 适用场景

- 跨页证据选择
- 文本与图像摘录整合
- 困难负例下的鲁棒性

## 限制与注意事项

- 给定 15 或 20 条摘录的选择任务与从原文检索使用不同候选池
- 发布的摘录 ID 表示支持关系；有序依赖边及所有等价证据组合需要额外标注

## 获取方式与来源

- [官方资源](https://mmdocrag.github.io/MMDocRAG/)
- [论文](https://arxiv.org/abs/2505.16470)
- [数据](https://huggingface.co/datasets/MMDocIR/MMDocRAG/tree/04b58dbc5c6c4955291124eed411b09114728061)
- official：[来源](https://mmdocrag.github.io/MMDocRAG/) — 支持字段 `summary`、`data.size`、`ground_truth.description`、`evaluation.protocol`
- paper：[来源](https://proceedings.neurips.cc/paper_files/paper/2025/file/1a93178950e92fd2e7b7448f7d68fd7d-Paper-Datasets_and_Benchmarks_Track.pdf) — 支持字段 `data.description`、`classification.modalities`
- paper：[来源](https://arxiv.org/html/2505.16470) — 支持字段 `data.size`、`data.splits`、`access.license`、`use.caveats`
- dataset_card：[来源](https://huggingface.co/datasets/MMDocIR/MMDocRAG/tree/04b58dbc5c6c4955291124eed411b09114728061) — 支持字段 `access.data`、`access.license`、`data.description`、`data.splits`
- official：[来源](https://datasets-server.huggingface.co/first-rows?dataset=MMDocIR%2FMMDocRAG&config=default&split=test) — 支持字段 `ground_truth.description`
- repository：[来源](https://github.com/MMDocRAG/MMDocRAG/blob/2fd7505c6a576376b4a92aafaff6d87494765bb7/eval_all.py) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`
- repository：[来源](https://github.com/MMDocRAG/MMDocRAG/blob/2fd7505c6a576376b4a92aafaff6d87494765bb7/eval_llm_judge.py) — 支持字段 `evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
