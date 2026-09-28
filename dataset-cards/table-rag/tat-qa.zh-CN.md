<!-- Generated from catalog/datasets/tat-qa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# TAT-QA

[English](tat-qa.md)

在已提供的财报表格与周边文本混合上下文上进行的金融问答。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `table_rag` |
| 任务 | table_qa, text_table_reasoning |
| 模态 | text, table |
| 已发布真值标注层级 | table_cell, span, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | CC BY 4.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

官方版本从 2,757 个金融报告表格—文本上下文构建了 16,552 个问题。


## 真值与评测

问题包含推导过程和 answer-from 元数据；模型专用的启发式事实与映射属于另行衍生的表示。

官方指标：em, f1。

评测协议：若未另行构建来源文档语料与划分，不能把给定上下文直接当作开放检索测试。

## 适用场景

- 融合文本与单元格证据
- 检索后的数值推理

## 限制与注意事项

- 原生上下文已直接提供
- 启发式 TagOp 映射不是原始人工证据标签

## 获取方式与来源

- [官方资源](https://github.com/NExTplusplus/TAT-QA)
- [论文](https://aclanthology.org/2021.acl-long.254/)
- repository：[来源](https://github.com/NExTplusplus/TAT-QA) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.protocol`、`access.license`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
