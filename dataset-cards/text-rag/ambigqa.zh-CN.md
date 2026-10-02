<!-- Generated from catalog/datasets/ambigqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# AmbigQA / AmbigNQ

[English](ambigqa.md)

为有歧义的 Natural Questions 问题标注多种解释、可接受答案和消歧后的问题。

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
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

核心 AmbigNQ 标注提供问题及可接受的单答案或多问答输出。作者另行提供维基百科数据库和后续发布的半预言机证据文章包；使用时应明确标识。

数据划分：训练和开发标注公开；测试评测遵循上游提交流程。

## 真值与评测

多组可接受输出包含答案别名和问题改写。标注者浏览的页面标题与搜索查询是不完整的辅助信息，不是完整检索真值，也不能作为测试输入。

官方指标：F1 answer, F1 edit-f1, F1 bleu1, F1 bleu2, F1 bleu3, F1 bleu4。

评测协议：使用官方评测器分别衡量答案覆盖和问题消歧；标识使用半预言机证据的实验，并保留可替代的标注输出。

## 适用场景

- 覆盖同一问题的多种有效解释
- 区分答案覆盖与消歧质量

## 限制与注意事项

- 半预言机证据会改变检索任务
- 标注过程的辅助信息不能作为系统输入

## 获取方式与来源

- [官方资源](https://github.com/shmsw25/AmbigQA)
- [论文](https://arxiv.org/abs/2004.10645)
- repository：[来源](https://github.com/shmsw25/AmbigQA) — 支持字段 `summary`、`data.description`、`data.splits`、`ground_truth.description`、`evaluation.protocol`
- repository：[来源](https://github.com/shmsw25/AmbigQA/blob/main/ambigqa_evaluate_script.py) — 支持字段 `evaluation.official_metrics`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
