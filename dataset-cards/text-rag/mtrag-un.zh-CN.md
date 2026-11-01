<!-- Generated from catalog/datasets/mtrag-un.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# MTRAG-UN

[English](mtrag-un.md)

多轮 RAG 评测，覆盖不可回答、信息不足、非独立问题与需要澄清的回答。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-01 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | conversational_qa, evidence_retrieval, rag_robustness, query_rewriting |
| 模态 | text |
| 已发布真值标注层级 | paragraph, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

人工会话被转换成每个会话一个高难度评测轮次，部分信息不足的结尾由拼接已有会话构造。核查时 reference.jsonl 公开 ClapNQ、Cloud、FiQA、Govt 四域的 507 个任务；README 仍标 Banking/Telco 语料及关联任务即将发布，因此论文六域 benchmark 尚未完整公开。

发布规模：论文报告六域、666 个会话对应 666 个任务和超过 2,800 个会话轮次；核查的公开参考文件含四域 507 行。
数据划分：评测 benchmark；SemEval-2026 MTRAGEval 将 MTRAG 作为独立训练资源，二者不是同一个数据集。
格式：JSONL generation tasks and BEIR-format passage-retrieval qrels。

## 真值与评测

参考段落、目标回答、可回答性和会话类型标签支持生成与澄清评分。相关性标注只覆盖可回答或部分可回答轮次，论文完整 benchmark 中共 468 个，不包含全部不可回答或信息不足样本。

官方指标：Recall@5, Recall@10, nDCG@5, nDCG@10, RB_llm, RB_alg, IDK_judge, RAGAS_faithfulness, underspecified_response_judge。

评测协议：保留历史，比较最后一轮直接查询与查询改写。仅在适用轮次评测检索，生成指标按可回答性调整；信息不足的回复单独用专门评判器。Reference 与完整 RAG 条件分开报告。论文评判模型和当前四域发布数据不能被悄悄替换成完整六域分数。

## 适用场景

- 区分适当拒答与需要追问澄清的情况
- 评测检索查询改写及高难度后续会话轮次

## 限制与注意事项

- 作者 README 显示两个企业领域尚未发布
- 评测轮次、会话数量与完整会话轮次必须分开统计
- 评判模型及按可回答性调整的评分会影响与原始 MTRAG 的可比性
- 仓库软件许可不代表每个来源语料具有统一许可

## 获取方式与来源

- [官方资源](https://github.com/IBM/mt-rag-benchmark/tree/main/mtragun-human)
- [论文](https://aclanthology.org/2026.findings-acl.503/)
- [数据](https://github.com/IBM/mt-rag-benchmark/blob/main/mtragun-human/generation_tasks/reference.jsonl)
- paper：[来源](https://aclanthology.org/2026.findings-acl.503.pdf) — 支持字段 `summary`、`classification`、`data.size`、`ground_truth`、`evaluation.official_metrics`、`evaluation.protocol`
- repository：[来源](https://github.com/IBM/mt-rag-benchmark/blob/main/mtragun-human/README.md) — 支持字段 `data.description`、`data.corpus`、`data.format`、`access.license`、`access.gated`、`use`
- repository：[来源](https://raw.githubusercontent.com/IBM/mt-rag-benchmark/main/mtragun-human/generation_tasks/reference.jsonl) — 支持字段 `data.size`、`data.queries`、`data.answers`、`data.description`
- repository：[来源](https://github.com/IBM/mt-rag-benchmark) — 支持字段 `data.splits`
- repository：[来源](https://github.com/IBM/mt-rag-benchmark/tree/main/scripts/evaluation) — 支持字段 `evaluation.evaluator`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
