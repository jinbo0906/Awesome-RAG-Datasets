<!-- Generated from catalog/datasets/lfrqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# LFRQA / RAG-QA Arena

[English](lfrqa.md)

人工编写的长篇答案及文档引用，用于跨领域检索增强问答。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | long_form_qa, attribution |
| 模态 | text |
| 已发布真值标注层级 | document, fact_citation, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | Apache-2.0 for the project; underlying corpus terms apply separately |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

LFRQA 在 RobustQA 基础上增加长篇答案；底层原始文档与段落需要按 RobustQA 流程下载。包含引用标注的文件是独立修订版本。

发布规模：EMNLP 2024 论文报告七个领域约 2.6 万个查询；后续引用版本的数量有所不同。
格式：JSONL。

## 真值与评测

引用版本通过 faithful_answer_w_citation 和 citation_numbers 映射到金标准 doc_id；它们是文档引用，不是字符片段。

官方指标：win_rate, win_plus_tie_rate, elo_rating。

评测协议：RAG-QA Arena 用固定 LLM 评判器比较模型答案与 LFRQA 或其他系统答案。记录标注版本、检索段落数与评判模型。

## 适用场景

- 跨领域长篇答案比较
- 文档引用与回答质量评测

## 限制与注意事项

- Arena 是评测协议，LFRQA 是数据集
- 官方仓库提供新标注，其许可证不替代底层语料条款

## 获取方式与来源

- [官方资源](https://github.com/awslabs/rag-qa-arena)
- [论文](https://aclanthology.org/2024.emnlp-main.249/)
- [数据](https://github.com/awslabs/rag-qa-arena/tree/main/data)
- paper：[来源](https://aclanthology.org/2024.emnlp-main.249/) — 支持字段 `summary`、`classification`、`data.size`
- repository：[来源](https://github.com/awslabs/rag-qa-arena) — 支持字段 `data.description`、`data.format`、`ground_truth`、`evaluation`、`access.license`、`use`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
