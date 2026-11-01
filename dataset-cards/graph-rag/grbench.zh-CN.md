<!-- Generated from catalog/datasets/grbench.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# GRBench (Graph-CoT)

[English](grbench.md)

在十个带文本属性的图上提供人工问题，分别测试图查询、多跳和归纳推理。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-01 |
| RAG 角色 | `rag_native` |
| 主分类 | `graph_rag` |
| 任务 | graph_qa, graph_reasoning, multi_hop_qa |
| 模态 | text, graph |
| 已发布真值标注层级 | answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | Apache-2.0 for the HF QA release; original graph sources retain their own terms. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

Graph-CoT 于 Findings ACL 2024 引入，后被 ACL 2025 Graph Counselor 采用。问答位于 Hugging Face，作者另行链接图环境文件。它不是后来的小说与医疗版 GraphRAG-Bench。

发布规模：引入论文报告五个应用领域的十个图，共 1,740 道问题。
数据划分：十个领域配置均以 test 发布；easy、medium、hard 是推理难度分层，不是训练、开发、测试划分。
格式：JSON questions and answers plus separately downloaded graph environments.。

## 真值与评测

问题与参考答案由人工设计；提供图环境和难度标签不代表另有独立标注的最小证据路径或代理动作轨迹。

官方指标：exact_match, BLEU, ROUGE, GPT4score。

评测协议：固定图环境及对应问答配置。原始脚本报告字符串指标和 GPT-4 答案评判；Graph Counselor 的 ROUGE-L/QwenScore 使用不同评分模型，不能与原始 GPT4score 混合。

## 适用场景

- 比较迭代图探索与平面文本检索
- 测试从查询到关系与归纳问题的迁移

## 限制与注意事项

- GRBench 与 GraphRAG-Bench 是不同资源而非别名
- 答案评判器不测来源路径完整性
- 问答必须与图环境一起获取

## 获取方式与来源

- [官方资源](https://github.com/PeterGriffinJin/Graph-CoT)
- [论文](https://aclanthology.org/2024.findings-acl.11/)
- [数据](https://huggingface.co/datasets/PeterJinGo/GRBench)
- paper：[来源](https://aclanthology.org/2024.findings-acl.11/) — 支持字段 `summary`、`data.description`、`data.size`、`ground_truth.provenance`
- dataset_card：[来源](https://huggingface.co/datasets/PeterJinGo/GRBench) — 支持字段 `data.splits`、`data.format`、`access.license`、`ground_truth.description`
- repository：[来源](https://github.com/PeterGriffinJin/Graph-CoT/blob/main/eval.py) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`
- paper：[来源](https://aclanthology.org/2025.acl-long.1202/) — 支持字段 `data.description`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
