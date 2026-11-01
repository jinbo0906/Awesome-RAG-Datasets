<!-- Generated from catalog/datasets/citerag.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# CiteRAG (academic citation prediction)

[English](citerag.md)

在分层学术语料上，分别预测论文参考文献列表及局部引用占位符。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-01 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | citation_prediction, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | document, answer |
| 证据标注来源 | distant |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

WWW 2026 引入，预印本首次发布于 2026-01-21。Task 1 从标题与摘要预测参考列表，Task 2 在局部占位符预测文献。作者发布 trainQA、test、多卷压缩语料，以及检索与生成的独立脚本。

发布规模：论文报告 Task 1 有 7,267 个实例、Task 2 有 8,541 个实例，语料含 554,719 篇论文；任务实例不是独立来源论文数或纯测试数量。
数据划分：作者提供 trainQA 和 test 目录；按论文要求从检索语料移除测试实例，并从相应输入视图去掉参考文献及引用标记。
格式：Per-example JSON and a multi-volume compressed hierarchical corpus.。

## 真值与评测

已发表论文的实际引用提供目标文献及列表监督，不是所有合适文献的穷尽相关性标注，也不证明生成陈述得到引用材料蕴含。

官方指标：Recall@k, MRR@k, NDCG@k, Hit@k, PACA@k, Citation_Diversity_Entropy, Hallucination_Rate。

评测协议：分开评测检索、Task 1 列表生成和 Task 2 占位符预测。论文 §5 的 PACA 以全部占位符为分母，而发布的 task2_metrics.py 仅对匹配成功的排名归一化后再按文章平均。Task 1 代码允许 0.90 标题相似度匹配，Task 2 使用规范化后精确标题。应固定评分器并披露差异，不把代码与论文得分视为相同。

## 适用场景

- 比较文档级与局部上下文学术检索
- 诊断生成参考列表中的遗漏和虚构文献

## 限制与注意事项

- 引用预测不同于普通回答的引用忠实性评测
- 未确认专门的数据再分发许可
- 官方论文与发布代码的指标聚合存在实质差异

## 获取方式与来源

- [官方资源](https://github.com/LQgdwind/CiteRAG)
- [论文](https://doi.org/10.1145/3774904.3792075)
- [数据](https://github.com/LQgdwind/CiteRAG/tree/main/data)
- paper：[来源](https://arxiv.org/abs/2601.14949) — 支持字段 `summary`、`data.description`、`data.size`、`access.paper`
- paper：[来源](https://arxiv.org/html/2601.14949) — 支持字段 `data.splits`、`ground_truth.description`、`evaluation.official_metrics`、`evaluation.protocol`
- repository：[来源](https://github.com/LQgdwind/CiteRAG) — 支持字段 `data.format`、`data.description`、`access.license`
- repository：[来源](https://github.com/LQgdwind/CiteRAG/blob/main/eval/task1_metrics.py) — 支持字段 `evaluation.protocol`
- repository：[来源](https://github.com/LQgdwind/CiteRAG/blob/main/eval/task2_metrics.py) — 支持字段 `evaluation.protocol`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
