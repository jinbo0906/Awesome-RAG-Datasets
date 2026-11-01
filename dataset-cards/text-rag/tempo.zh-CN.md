<!-- Generated from catalog/datasets/tempo.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# TEMPO

[English](tempo.md)

在带时间信息的 Stack Exchange 文档集合上评测跨时段推理与分步检索。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-01 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | time_sensitive_qa, evidence_retrieval, multi_hop_qa |
| 模态 | text |
| 已发布真值标注层级 | document, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

Hugging Face 发布 documents、带 gold_ids/gold_answers 的 examples、分步相关文档及模型推理增强查询。人工选择的问题和模型辅助时间标注支持文档检索，也支持论文另行评测的下游问答。

发布规模：13 个 Stack Exchange 领域，共 1,730 个查询、3,976 个检索步骤和 1,654,055 份文档。
数据划分：按领域命名的评测划分；推理增强查询属于变体，不是独立测试问题。
格式：Hugging Face Parquet。

## 真值与评测

gold_ids 和分步映射标识相关文档，gold_answers 保留参考回答文本。时间意图、锚点与检索规划由模型辅助标注并经人工抽样核验，不代表每个时间判断都经过完整人工确认。

官方指标：nDCG@10, temporal_precision_at_k, temporal_relevance_at_k, temporal_coverage_at_k, ndcg_full_coverage_at_k, answer_correctness_0_100。

评测协议：分开报告领域、原始与推理增强查询，以及查询到文档和分步检索。作者 run.py 将每题 negative_ids 从排名中排除；保留这些文档是更严格的全库改造，不是同一榜单协议。时间指标依赖模型判断。Table 6/Appendix G.3 固定生成器，以 0–100 分参考答案覆盖度评分，并比较无检索和金标准文档条件。

## 适用场景

- 检测找回证据是否覆盖所需时段
- 分开评测分步时间证据覆盖与最终问答

## 限制与注意事项

- HF 元数据写 CC BY 4.0，但数据卡另说明原始 Stack Exchange 内容为 CC BY-SA，适用条款仍需核对
- 排除 negative_ids 会改变候选空间，必须报告
- 模型判断的时间完整性不等于独立且穷尽的证据真值
- 2026 年 1 月作者预印本未被标为未经确认的会议论文

## 获取方式与来源

- [官方资源](https://tempo-bench.github.io/)
- [论文](https://arxiv.org/abs/2601.09523)
- [数据](https://huggingface.co/datasets/tempo26/Tempo)
- paper：[来源](https://arxiv.org/html/2601.09523) — 支持字段 `summary`、`classification`、`data.size`、`ground_truth`、`evaluation.official_metrics`、`evaluation.protocol`、`use`
- dataset_card：[来源](https://huggingface.co/datasets/tempo26/Tempo) — 支持字段 `data.description`、`data.splits`、`data.format`、`data.corpus`、`data.queries`、`data.answers`、`access.data`、`access.license`、`access.gated`
- repository：[来源](https://github.com/tempo-bench/Tempo/blob/main/run.py) — 支持字段 `evaluation.protocol`、`use.caveats`
- repository：[来源](https://github.com/tempo-bench/Tempo/blob/main/temporal_metrics.py) — 支持字段 `evaluation.evaluator`、`evaluation.official_metrics`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
