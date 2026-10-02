<!-- Generated from catalog/datasets/convfinqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# ConvFinQA

[English](convfinqa.md)

对话式财务问答，逐轮提供相互关联的数值程序和答案。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `table_rag` |
| 任务 | conversational_qa, text_table_reasoning |
| 模态 | text, table |
| 已发布真值标注层级 | sentence, table, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | MIT |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

发布包有对话级和轮次级格式，包含表格、周边文本、dialogue_break、turn_program 与 exe_ans_list。

发布规模：3,892 段对话，包含 14,115 个问题。
数据划分：对话级训练、开发与测试集分别有 3,037、421、434 个样本；已发布测试集提供财报和对话，评分参考标注未公开。
格式：JSON in data.zip。

## 真值与评测

逐轮程序与执行答案指定数值依赖；有标注的划分通过 gold_ind 指定支持事实。这些标注不是来源 PDF 的单元格坐标。

官方指标：execution_accuracy, program_accuracy。

评测协议：保留轮次顺序与对话边界。用官方执行与程序评测器评分，并说明前轮程序或答案采用金标准还是模型预测。

## 适用场景

- 检索后的对话式数值推理
- 前轮计算结果依赖

## 限制与注意事项

- 对话合成及标注基于 FinQA，自定义划分时应避免原始财报泄漏
- 已发布表格与文本上下文不能证明开放语料检索性能

## 获取方式与来源

- [官方资源](https://github.com/czyssrs/ConvFinQA)
- [论文](https://aclanthology.org/2022.emnlp-main.421/)
- [数据](https://github.com/czyssrs/ConvFinQA/blob/main/data.zip)
- repository：[来源](https://github.com/czyssrs/ConvFinQA) — 支持字段 `summary`、`classification`、`data.description`、`data.splits`、`data.format`、`ground_truth`、`evaluation`、`access.license`、`use`
- paper：[来源](https://aclanthology.org/2022.emnlp-main.421/) — 支持字段 `data.size`、`ground_truth.provenance`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
