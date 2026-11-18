<!-- Generated from catalog/datasets/query-robustness.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# Query Robustness (How You Ask Matters)

[English](query-robustness.md)

将原问和等义变体配对，评估自适应 RAG 的答案、检索决策与成本变化。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-18 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | rag_robustness, retrieval_routing |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | CC-BY-SA-4.0 (released variation data) |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

EMNLP 2026 评测从六个已有问答集抽样，每条原问搭配六种机器改写及至多两条人工改写。基线检索使用另行获取的 DPR Wikipedia 段落。

发布规模：固定版本有 3,000 条原问、18,000 个机器变体，597 条原问另含 1,183 条非空人工改写，共 22,183 种问法。
数据划分：六个评测配置各 500 条原问。HF 查看器自动标为 train，发布文件名为 test.jsonl，实际用于评测。
格式：JSONL with original_question, answers, human rewrite and surface-variation columns。

## 真值与评测

变体共享原问答案，改变正式程度、可读性、句式或错误形式，保留问题意图。数据没有为每道题标注唯一正确的检索决策。

官方指标：answer_accuracy, InAccuracy, semantic_answer_consistency, retrieval_calls, LLM_calls, normalized_cost_deviation, retrieval_decision_robustness。

评测协议：在相同语料和模型环境下比较同一问题的问法。InAccuracy 检查生成内容是否包含参考答案字符串。分别报告正确性变化、语义一致性、检索路由与调用量，衍生划分保留同题各问法在一起。

## 适用场景

- 发现同义问法导致的检索路由变化
- 评估适应式检索的鲁棒性与调用成本

## 限制与注意事项

- 同一原问的不同问法是重复测量
- 基线覆盖代码 MIT 与改写数据和 Wikipedia 条款分别适用
- 路由变化可以提示不稳定但是否有益需借助对照验证

## 获取方式与来源

- [官方资源](https://huggingface.co/datasets/YunahJang/query-robustness)
- [论文](https://aclanthology.org/2026.emnlp-main.2156/)
- [数据](https://huggingface.co/datasets/YunahJang/query-robustness/tree/48bbc43c76a4581ab2f62331e455a1f37d9e1482)
- paper：[来源](https://aclanthology.org/2026.emnlp-main.2156.pdf) — 支持字段 `summary`、`classification`、`data.description`、`ground_truth`、`evaluation.official_metrics`、`evaluation.protocol`、`use`
- dataset_card：[来源](https://huggingface.co/datasets/YunahJang/query-robustness/tree/48bbc43c76a4581ab2f62331e455a1f37d9e1482) — 支持字段 `data.size`、`data.splits`、`data.format`、`access.data`、`access.license`
- repository：[来源](https://github.com/YunahJang/AdaptiveRAG-Robustness/tree/c9a5bfc8d10957baa006bbe24dc05b8e8f842b10) — 支持字段 `evaluation.evaluator`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
