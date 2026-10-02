<!-- Generated from catalog/datasets/medmcqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# MedMCQA

[English](medmcqa.md)

印度医学入学考试选择题数据，附解释、学科和主题信息，是 MIRAGE 的组成部分。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `text_rag` |
| 任务 | single_hop_qa |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | not_provided / provided / provided |
| 原始数据许可 | MIT in author repository; consult source-question terms |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

问题记录包含四个选项、正确选项、解释及学科和主题字段。RAG 需另设固定的医学检索语料，解释文本不等于来源文档。

格式：JSON。

## 真值与评测

正确选项和解释未提供来源文档相关性或支持片段坐标。

官方指标：accuracy。

评测协议：遵循上游划分标签；MIRAGE 使用 4,183 个开发集问题而非原生隐藏测试集。报告 RAG 语料与仅问题检索配置。

## 适用场景

- 使用外部检索生成医学选择题答案
- 比较 MIRAGE 子任务

## 限制与注意事项

- 需另行指定检索语料和证据映射
- MIRAGE 开发集评测不能称为原生测试集结果

## 获取方式与来源

- [官方资源](https://medmcqa.github.io/)
- [论文](https://proceedings.mlr.press/v174/pal22a.html)
- [数据](https://github.com/medmcqa/medmcqa)
- repository：[来源](https://github.com/medmcqa/medmcqa) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`access.data`
- repository：[来源](https://github.com/medmcqa/medmcqa/blob/main/LICENSE.md) — 支持字段 `access.license`
- repository：[来源](https://github.com/gzxiong/MIRAGE) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
