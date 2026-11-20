<!-- Generated from catalog/datasets/cofaithfulqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# CoFaithfulQA

[English](cofaithfulqa.md)

给定证据的问答基准，衡量模型能否在闭卷答案与正确段落冲突时依据段落作答。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-20 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | single_hop_qa, multi_hop_qa, rag_robustness |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | Hub dataset card: MIT. Paper Appendix A.2 states academic research distribution. Source dataset terms are listed in Appendix A.1. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

六个公开 JSONL 文件来自 HotpotQA、NewsQA、Natural Questions、SearchQA、SQuAD 和 TriviaQA。 每行包含问题、给定上下文、参考答案、构建模型的闭卷答案及出现次数。公开版提供逐题段落。

数据划分：Hugging Face 将公开文件标成 train。作者将这些文件用于评测，论文另行报告去重统计。
格式：JSONL。

## 真值与评测

参考答案与支持段落来自原始问答数据。构建时用重复采样找出稳定的闭卷答案，再用多个模型核验冲突。 公开版没有独立的开放语料检索标注。

官方指标：context_recall, memory_recall, memorization_ratio。

评测协议：给每个模型相同的问题和上下文，使用论文第五节的答案归一化方法，并记录数据版本、子集、提示与评分设置。 上下文召回和记忆召回匹配不同参考答案，记忆比例为 MemR / (MemR + ConR)。

## 适用场景

- 评估正确证据与模型记忆冲突时的回答忠实度
- 在固定证据下比较上下文召回与记忆召回

## 限制与注意事项

- 冲突样本取决于构建模型及其闭卷答案
- 开放语料检索需要单独评估
- 数据卡与论文描述的分发条款不同

## 获取方式与来源

- [官方资源](https://huggingface.co/datasets/chengpingan/CoFaithfulQA)
- [论文](https://doi.org/10.52202/085713-3356)
- [数据](https://huggingface.co/datasets/chengpingan/CoFaithfulQA/tree/main)
- paper：[来源](https://arxiv.org/html/2502.15543v4#S4) — 支持字段 `summary`、`classification.tasks`、`ground_truth`
- paper：[来源](https://arxiv.org/html/2502.15543v4#S5) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`
- paper：[来源](https://arxiv.org/html/2502.15543v4#A1.SS2) — 支持字段 `access.license`、`use.caveats`
- dataset_card：[来源](https://huggingface.co/datasets/chengpingan/CoFaithfulQA) — 支持字段 `classification.languages`、`data`、`ground_truth.alternatives`、`access.official`、`access.data`、`access.license`
- paper：[来源](https://doi.org/10.52202/085713-3356) — 支持字段 `access.paper`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
