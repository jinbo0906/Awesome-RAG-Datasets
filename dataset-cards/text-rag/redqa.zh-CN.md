<!-- Generated from catalog/datasets/redqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# RedQA (RARE)

[English](redqa.md)

面向高相似度语料的多跳问答，为每条必需事实标出一组可替代的文本块。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-18 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | evidence_retrieval, multi_hop_qa |
| 模态 | text |
| 已发布真值标注层级 | chunk, answer |
| 证据标注来源 | synthetic |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

RARE 是构建框架，RedQA 发布问题、答案、固定文本块语料及证据分组。作者用金融报告、法律材料和专利构建三个高重叠领域，并对 HotpotQA 做重处理形成 General-Wiki 对照。

发布规模：金融 645 题、法律 605 题、专利 480 题，合计 1,730 题，另有 General-Wiki 对照 688 题。四份语料分别有 3,281、4,090、3,339 和 3,218 块。
数据划分：按领域和对照条件发布四个评测文件，使用发布的证据分组，并按跳数分层报告。
格式：JSON with corpus, queries, gold_chunk_ids and gold_chunk_groups。

## 真值与评测

每组是构建流程判定能支持同一必需事实的文本块。完整检索结果需命中每组至少一项。块 ID 对应发布时的固定切分。

官方指标：Coverage@10, PerfRecall@10, group_nDCG@10, group_MRR, judged_answer_accuracy。

评测协议：Coverage 统计命中的事实组比例，PerfRecall 要求每组均命中，对应代码中的 perfect_match@k。分组 nDCG 和 MRR 遵循发布实现。论文还比较有无检索时的答案正确率，由模型评分。

## 适用场景

- 区分部分命中与完整事实覆盖
- 评估重复证据对互补证据的挤占

## 限制与注意事项

- 更换分块方法后需重新映射来源证据
- 模型辅助等价判断可能漏掉有效替代项
- 仓库 MIT 许可不能确定来源语料的权利

## 获取方式与来源

- [官方资源](https://github.com/gkswns0531/RARE)
- [论文](https://aclanthology.org/2026.acl-long.923/)
- [数据](https://github.com/gkswns0531/RARE/tree/7d5e6749d8a2dc38e1c0c8ba21bc1cc43e4d76cd/dataset)
- paper：[来源](https://aclanthology.org/2026.acl-long.923/) — 支持字段 `summary`、`classification`
- paper：[来源](https://arxiv.org/html/2604.19047) — 支持字段 `data.description`、`ground_truth`、`evaluation.official_metrics`、`evaluation.protocol`、`use`
- repository：[来源](https://github.com/gkswns0531/RARE/tree/7d5e6749d8a2dc38e1c0c8ba21bc1cc43e4d76cd/dataset) — 支持字段 `data.size`、`data.splits`、`data.format`、`access.data`
- repository：[来源](https://raw.githubusercontent.com/gkswns0531/RARE/master/evaluation/metrics.py) — 支持字段 `evaluation.evaluator`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
