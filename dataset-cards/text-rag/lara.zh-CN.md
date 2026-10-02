<!-- Generated from catalog/datasets/lara.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# LaRA

[English](lara.md)

面向书籍、论文和财务报告的长上下文问答基准，用于比较检索增强与完整上下文推理。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | long_context_qa, rag_robustness |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown; repository code is MIT, source texts retain upstream rights |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

发布 32k/128k 上下文文件及定位、比较、推理和幻觉任务的问题。问题针对给定来源上下文构建，不是无约束的开放网页检索。

发布规模：共 2,326 个测试样本，覆盖三种上下文类型和四种问答任务。
格式：JSON/JSONL。

## 真值与评测

人工编写的种子问答引导 GPT-4o 生成，随后抽样人工验证并迭代提示词，不代表每个问答都独立由人工编写。参考答案不意味着穷尽的支持片段或最优分块边界。

官方指标：llm_judged_accuracy。

评测协议：分别报告上下文长度、来源类型与任务。在相同来源文本上使用发布的 RAG 和完整上下文脚本，固定 compute_score_llm.py 使用的评分模型与提示词。

## 适用场景

- 比较 RAG 与长上下文的路由选择
- 分析检索效果如何随上下文长度与任务改变

## 限制与注意事项

- 模型评分结果依赖评分模型与提示词
- 仅凭答案正确不能验证分块边界

## 获取方式与来源

- [官方资源](https://github.com/Alibaba-NLP/LaRA)
- [论文](https://proceedings.mlr.press/v267/li25dv.html)
- [数据](https://github.com/Alibaba-NLP/LaRA/tree/main/datasets)
- paper：[来源](https://arxiv.org/html/2502.09977#S3.SS3) — 支持字段 `ground_truth.provenance`、`ground_truth.description`
- paper：[来源](https://proceedings.mlr.press/v267/li25dv.html) — 支持字段 `summary`、`data.size`
- repository：[来源](https://github.com/Alibaba-NLP/LaRA) — 支持字段 `data.description`、`ground_truth.description`、`evaluation.protocol`、`access.data`、`access.license`
- repository：[来源](https://github.com/Alibaba-NLP/LaRA/blob/main/evaluation/compute_score_llm.py) — 支持字段 `evaluation.official_metrics`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
