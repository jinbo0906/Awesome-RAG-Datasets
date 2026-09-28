<!-- Generated from catalog/datasets/mmlongbench-doc.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# MMLongBench-Doc

[English](mmlongbench-doc.md)

长 PDF 文档问答，提供证据页面及证据来源模态标注。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `multimodal_rag` |
| 任务 | long_context_qa, page_retrieval, visual_qa |
| 模态 | text, image, table, chart, layout |
| 已发布真值标注层级 | page, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

仓库发布 PDF 和包含 doc_id、问题、答案、证据页与证据来源的问答记录；2025 年版本修订了部分问答。


## 真值与评测

证据页面和来源模态标签可定位支持信息，但没有普遍提供针对问题的区域或单元格坐标。

官方指标：answer_f1。

评测协议：说明数据修订版本，并明确页面是由系统检索还是全部直接提供给模型。

## 适用场景

- 长视觉文档上下文
- 跨页证据收集

## 限制与注意事项

- 原始评测是长上下文 VQA；页面检索协议属于改造
- 问答修订要求固定版本

## 获取方式与来源

- [官方资源](https://github.com/mayubo2333/MMLongBench-Doc)
- repository：[来源](https://github.com/mayubo2333/MMLongBench-Doc) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
