<!-- Generated from catalog/datasets/natural-questions.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# Natural Questions

[English](natural-questions.md)

搜索式问题与维基百科页面配对，含长答案和短答案标注。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `text_rag` |
| 任务 | single_hop_qa, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | span, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

每个样本包含问题及候选维基百科页面；检索实验须另行定义开放语料索引。


## 真值与评测

长答案定位 HTML 区域，短答案定位一个或多个文本片段；部分样本没有答案。

官方指标：long_answer_f1, short_answer_f1。

评测协议：转换为纯文本或 chunks 时，保留字节和 HTML 坐标。

## 适用场景

- 基于来源坐标的证据覆盖
- 可回答与不可回答问答

## 限制与注意事项

- 原生任务直接给出候选页面，而不是开放语料检索协议

## 获取方式与来源

- [官方资源](https://github.com/google-research-datasets/natural-questions)
- repository：[来源](https://github.com/google-research-datasets/natural-questions) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.official_metrics`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
