<!-- Generated from catalog/datasets/raguard.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# RAGuard

[English](raguard.md)

政治主张核查基准，测试 RAG 面对 Reddit 真实误导检索内容的表现。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | fact_verification, rag_robustness |
| 模态 | text |
| 已发布真值标注层级 | document, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | MIT |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

主张与文档存于两个 CSV，包含二元结论、文档 ID、Reddit 正文及支持、误导或无关标签。

发布规模：2,648 条主张和 16,331 篇文档。
格式：CSV。

## 真值与评测

结论来自 PolitiFact；文档标签描述其对标注 LLM 的影响，并不代表普遍适用的真假片段判断或最小证据。

官方指标：accuracy。

评测协议：比较无上下文、完整语料检索及直接提供关联文档的设置；区分 RAG-1、RAG-5、oracle-all 与 oracle-misleading。无效类别输出按错误计。

## 适用场景

- 真实误导检索内容下的鲁棒性
- 检索与无上下文主张核查的比较

## 限制与注意事项

- 误导性相对于模型行为定义，且任务集中在政治领域
- 两个 CSV 应分别读取，Hugging Face 默认查看器会报告字段不兼容

## 获取方式与来源

- [官方资源](https://huggingface.co/datasets/UCSC-IRKM/RAGuard)
- [论文](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ed25c00ff6900989116d3ba5d607d33d-Abstract-Datasets_and_Benchmarks_Track.html)
- [数据](https://huggingface.co/datasets/UCSC-IRKM/RAGuard/tree/main)
- dataset_card：[来源](https://huggingface.co/datasets/UCSC-IRKM/RAGuard) — 支持字段 `data.description`、`data.format`、`access.license`、`use.caveats`
- paper：[来源](https://arxiv.org/html/2502.16101v5) — 支持字段 `summary`、`classification`、`data.size`、`ground_truth`、`evaluation`、`use.best_for`
- paper：[来源](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ed25c00ff6900989116d3ba5d607d33d-Abstract-Datasets_and_Benchmarks_Track.html) — 支持字段 `access.paper`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
