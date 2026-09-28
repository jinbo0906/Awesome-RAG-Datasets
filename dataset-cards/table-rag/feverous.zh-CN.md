<!-- Generated from catalog/datasets/feverous.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# FEVEROUS

[English](feverous.md)

面向维基百科句子与表格单元格的开放域事实核查数据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `table_rag` |
| 任务 | fact_verification, evidence_retrieval, text_table_reasoning |
| 模态 | text, table |
| 已发布真值标注层级 | sentence, table_cell, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

发布的主张对照含正文和表格的维基百科页面，标为支持、反驳或信息不足。

发布规模：完整数据集有 87,026 条已核查主张；较小研究子集需另行标识。

## 真值与评测

最多三组证据集合可包含句子、单元格、表头、图注或列表项 ID，并保留结构上下文。

官方指标：label_accuracy, feverous_score。

评测协议：结论标签与完整证据集合应联合评测。

## 适用场景

- 融合文本与表格证据
- 保留单元格与表头关系
- 按替代证据集合评分

## 限制与注意事项

- 只看结论会掩盖单元格检索失败；应保留单元格 ID 的结构上下文

## 获取方式与来源

- [官方资源](https://fever.ai/dataset/feverous.html)
- [论文](https://arxiv.org/abs/2106.05707)
- [数据](https://huggingface.co/datasets/fever/feverous)
- repository：[来源](https://github.com/Raldir/FEVEROUS) — 支持字段 `summary`、`data.size`、`ground_truth.description`、`evaluation.protocol`
- dataset_card：[来源](https://huggingface.co/datasets/fever/feverous) — 支持字段 `ground_truth.alternatives`、`classification.modalities`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
