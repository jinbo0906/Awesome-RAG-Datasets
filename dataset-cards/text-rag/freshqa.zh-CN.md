<!-- Generated from catalog/datasets/freshqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# FreshQA

[English](freshqa.md)

面向模型训练后才出现或随时间变化的事实、按版本维护的问答数据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `text_rag` |
| 任务 | time_sensitive_qa, single_hop_qa |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | not_provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

作者维护带日期的电子表格快照和评测器；问题及可接受答案会随时间更新，并非固定不变的检索语料。


## 真值与评测

答案判断与问题表格一起版本化，但未锚定到稳定的段落坐标；来源文档快照和时间相关性标签需在改造时另建。

官方指标：accuracy。

评测协议：比较系统前固定 FreshQA 表格版本与评测模式，并记录搜索日期、检索网页及其获取日期，避免用未来答案评价过去的系统。

## 适用场景

- 评测回答的新鲜度
- 设计时间敏感的检索协议

## 限制与注意事项

- 答案键变化使跨日期分数不可直接比较
- 原生数据没有固定来源池或证据片段坐标

## 获取方式与来源

- [官方资源](https://github.com/freshllms/freshqa)
- [论文](https://arxiv.org/abs/2310.03214)
- repository：[来源](https://github.com/freshllms/freshqa) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
