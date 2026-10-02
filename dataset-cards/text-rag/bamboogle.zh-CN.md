<!-- Generated from catalog/datasets/bamboogle.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# Bamboogle

[English](bamboogle.md)

人工编写的两跳问题，要求组合维基百科中的事实，并使直接搜索摘要难以正确回答。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `text_rag` |
| 任务 | multi_hop_qa |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | MIT |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

作者发布问题和答案；维基百科与实时搜索属于外部资源。发布包没有固定检索集合或逐跳证据标注。

发布规模：125 个人工编写的两跳问题。

## 真值与评测

作者提供组合式问题的最终答案。两跳事实可在维基百科找到，并不意味着已提供段落标识、支持句或参考推理轨迹。

官方指标：exact_match。

评测协议：抽取最终答案并评分，记录搜索或语料快照。原始实验使用完整的小规模 benchmark，且未在其上调优提示；后续子集应单独报告。

## 适用场景

- 迭代搜索与问题分解
- 形式多样的两跳事实问答

## 限制与注意事项

- 样本较少限制了统计精度
- 原始搜索摘要失败条件会随时间变化

## 获取方式与来源

- [官方资源](https://github.com/ofirpress/self-ask)
- [论文](https://aclanthology.org/2023.findings-emnlp.378/)
- repository：[来源](https://github.com/ofirpress/self-ask) — 支持字段 `data.description`
- repository：[来源](https://github.com/ofirpress/self-ask/blob/main/datasets/bamboogle.md) — 支持字段 `access.license`
- paper：[来源](https://aclanthology.org/2023.findings-emnlp.378.pdf) — 支持字段 `summary`、`data.size`、`ground_truth.description`、`evaluation.official_metrics`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
