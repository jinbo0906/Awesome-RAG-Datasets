<!-- Generated from catalog/datasets/ohrbench.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# OHRBench

[English](ohrbench.md)

文档 RAG 基准，用于追踪 OCR 语义和格式错误如何影响证据检索与回答生成。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_native` |
| 主分类 | `multimodal_rag` |
| 任务 | rag_robustness, evidence_retrieval, visual_qa |
| 模态 | text, image, table, chart, equation, layout |
| 已发布真值标注层级 | page, quote, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown; HF metadata says CC BY 4.0, but author copyright statement restricts research use and prohibits commercial use |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

发布 PDF、人工核验的页面结构化数据、qas_v2.json、OCR 输出及语义或格式扰动。原生流程从文档图像抽取文本知识库，不要求生成器只能使用视觉输入。

发布规模：ICCV 2025 论文版本包含七个领域的 8,561 张文档页面图像和 8,498 个问答对。
格式：PDF/JSON/text。

## 真值与评测

问题保留来源页面及支持内容映射；人工核验的页面转录提供 OCR 参考。转录正确性与问答支持内容是不同标签，均不等于最优切分边界。

官方指标：ocr_edit_distance, evidence_lcs, answer_f1。

评测协议：分别报告 OCR 编辑距离、通过最长公共子序列（LCS）度量的检索证据包含度、金标准上下文生成和完整 RAG。固定 OCR 版本、扰动强度和问答版本，按文本、表格、公式、图表和阅读顺序任务分组。LCS 证据包含度不是文档 Recall@K。

## 适用场景

- 追踪 OCR 错误在 RAG 流程中的传递
- 在结构化文档损坏条件下评测分块

## 限制与注意事项

- 来源文本被破坏后需将证据重新映射到标准页面内容
- OCR 或答案 F1 高分不代表跨模态证据完整
- 许可元数据与仅限研究的版权声明不同，须核对作者条款及来源文档权利

## 获取方式与来源

- [官方资源](https://github.com/opendatalab/OHR-Bench)
- [论文](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_OCR_Hinders_RAG_Evaluating_the_Cascading_Impact_of_OCR_on_ICCV_2025_paper.html)
- [数据](https://huggingface.co/datasets/opendatalab/OHR-Bench)
- repository：[来源](https://github.com/opendatalab/OHR-Bench#copyright-statement) — 支持字段 `access.license`、`use.caveats`
- dataset_card：[来源](https://huggingface.co/datasets/opendatalab/OHR-Bench) — 支持字段 `access.license`
- paper：[来源](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_OCR_Hinders_RAG_Evaluating_the_Cascading_Impact_of_OCR_on_ICCV_2025_paper.html) — 支持字段 `summary`、`data.size`
- repository：[来源](https://github.com/opendatalab/OHR-Bench) — 支持字段 `data.description`、`ground_truth.description`、`evaluation.protocol`、`access.data`
- paper：[来源](https://openaccess.thecvf.com/content/ICCV2025/papers/Zhang_OCR_Hinders_RAG_Evaluating_the_Cascading_Impact_of_OCR_on_ICCV_2025_paper.pdf) — 支持字段 `evaluation.official_metrics`
- paper：[来源](https://arxiv.org/html/2412.02592v4) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
