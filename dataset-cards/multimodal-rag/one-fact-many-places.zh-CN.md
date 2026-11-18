<!-- Generated from catalog/datasets/one-fact-many-places.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# One Fact, Many Places (MMLongBench-Red / MMDocRAG-Red)

[English](one-fact-many-places.md)

为文档检索、引用和遮挡归因提供按事实组织的可替代证据标注。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-18 |
| RAG 角色 | `auxiliary` |
| 主分类 | `multimodal_rag` |
| 任务 | page_retrieval, evidence_retrieval, attribution |
| 模态 | text, image, table, chart, layout |
| 已发布真值标注层级 | page, bbox, quote, fact_citation |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | external / provided / external |
| 原始数据许可 | CC-BY-NC-4.0 (released data annotations) |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

2026 年 10 月预印本为 MMLongBench-Doc 与 MMDocRAG 的样本补充标注。arXiv 附件含两份标注、复核版本、评分库与冻结输出。MMLongBench-Red 含原始答案，完整原始材料及答案请取上游发布，包括 PDF 和候选图像。

发布规模：两份文件共 420 题。MMLongBench-Red 220 题，开发 60、测试 160；MMDocRAG-Red 的两个抽样批次分别是 80 和 120 题。
数据划分：MMLongBench-Red 有 208 题适合此协议，开发 54、测试 154；MMDocRAG-Red 有 196 题适用。对齐论文分数时用冻结原始标注，敏感性实验注明复核版本。
格式：JSONL annotations and Python scoring library in the arXiv ancillary 7z archive。

## 真值与评测

按事实分组记录页面和摘录。MMDocRAG-Red 区分严格支持、宽松支持、组合支持与只提供上下文的摘录。MMLongBench-Red 通过关键字符串和 OCR 定位部分 PDF 坐标框。模型执行标注流程，两位人工复核者各自重新标注抽样的 60 题。

官方指标：evidence_aware_recall_at_k, redundancy_aware_quote_F1, set_level_masking_answer_survival。

评测协议：比较原数据页、核实页和考虑替代证据的页面召回。注明 Quote F1 版本，区别严格支持、需联合使用的摘录和上下文提示。遮挡对照应在相当粒度下覆盖所有已标注实例，并报告适用样本数。

## 适用场景

- 度量单位置标签造成的检索漏判与引用误判
- 检查遮挡一处证据后是否仍存在有效副本

## 限制与注意事项

- 图像和 PDF 需从上游获取
- OCR 和文本层搜索可能漏掉仅存在于像素中的事实
- 坐标框和替代位置标注覆盖有限

## 获取方式与来源

- [官方资源](https://arxiv.org/abs/2610.26401)
- [论文](https://arxiv.org/pdf/2610.26401)
- [数据](https://arxiv.org/src/2610.26401v1/anc/code-and-data.7z)
- paper：[来源](https://arxiv.org/pdf/2610.26401) — 支持字段 `summary`、`classification`、`data.description`、`ground_truth`、`evaluation.official_metrics`、`evaluation.protocol`、`access.license`、`use`
- official：[来源](https://arxiv.org/src/2610.26401v1/anc/code-and-data.7z) — 支持字段 `data.size`、`data.splits`、`data.format`、`ground_truth.provenance`、`access.data`、`access.license`、`evaluation.evaluator`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
