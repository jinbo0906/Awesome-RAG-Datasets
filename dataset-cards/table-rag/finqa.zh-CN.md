<!-- Generated from catalog/datasets/finqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# FinQA

[English](finqa.md)

财务数值问答，提供文本与表格支持事实及可执行推理程序。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `table_rag` |
| 任务 | table_qa, text_table_reasoning, evidence_retrieval |
| 模态 | text, table |
| 已发布真值标注层级 | sentence, table, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | MIT |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

JSON 样本包含表格前后的文本、财报表格、问题、支持事实索引、推理程序及执行答案。

数据划分：训练、开发及公开测试集提供参考标注；私有测试集问题没有金标准参考。
格式：JSON。

## 真值与评测

gold_inds 选择支持文本句子及序列化表格行；程序监督数值运算。这些行目标不是原始 PDF 单元格坐标。

官方指标：execution_accuracy, program_accuracy。

评测协议：挑战赛提交应运行检索与程序生成全流程。金标准检索输入仅用于诊断；区分公开与私有测试集，并使用修正后的表格行序列化方式。

## 适用场景

- 财务计算前的证据检索
- 可执行答案与程序监督

## 限制与注意事项

- 原生候选上下文已给定，完整财报检索属于额外改造
- 仓库记录了过去会泄露检索标签的序列化缺陷

## 获取方式与来源

- [官方资源](https://github.com/czyssrs/FinQA)
- [论文](https://aclanthology.org/2021.emnlp-main.300/)
- [数据](https://github.com/czyssrs/FinQA/tree/main/dataset)
- repository：[来源](https://github.com/czyssrs/FinQA) — 支持字段 `summary`、`classification`、`data`、`ground_truth`、`evaluation`、`access.license`、`use`
- paper：[来源](https://aclanthology.org/2021.emnlp-main.300/) — 支持字段 `ground_truth.provenance`、`access.paper`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
