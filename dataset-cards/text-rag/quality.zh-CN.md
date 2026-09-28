<!-- Generated from catalog/datasets/quality.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# QuALITY

[English](quality.md)

围绕文章和故事的长文档理解选择题数据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `text_rag` |
| 任务 | long_context_qa |
| 模态 | text |
| 已发布真值标注层级 | document, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | article-specific terms |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

样本包含文章、四个答案选项、金标准标签和标注元数据；较难子集依据限时人工表现划定。


## 真值与评测

答案标签经人工验证，但原生版本并未为每题提供最小支持片段。

官方指标：accuracy, hard_subset_accuracy。

评测协议：完整集与困难子集应分开报告；构建可检索 chunks 属于后续改造。

## 适用场景

- 改造为检索任务后的长上下文推理

## 限制与注意事项

- QuALITY 是长输入问答数据，而非产品质量数据集
- 没有原生证据片段真值

## 获取方式与来源

- [官方资源](https://github.com/nyu-mll/quality)
- [论文](https://aclanthology.org/2022.naacl-main.391/)
- repository：[来源](https://github.com/nyu-mll/quality) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.official_metrics`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
