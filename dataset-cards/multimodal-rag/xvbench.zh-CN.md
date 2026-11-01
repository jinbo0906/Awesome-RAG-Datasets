<!-- Generated from catalog/datasets/xvbench.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# XVBench

[English](xvbench.md)

提供明确支持片段文件名的视频语料 RAG 问题，用于评测迭代检索与推理中的视觉细节保留。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-01 |
| RAG 角色 | `rag_native` |
| 主分类 | `multimodal_rag` |
| 任务 | video_qa, multimodal_retrieval, long_context_qa |
| 模态 | text, video |
| 已发布真值标注层级 | document, answer |
| 证据标注来源 | synthetic |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | CC-BY-4.0 for annotations; obtain source videos under HowTo100M and upstream video terms. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

VimRAG 引入由 HowTo100M 衍生的评测集。官方版本提供 query、gt、video_name 与 reference 片段文件名；需另行获取视频，并使用随附固定时长预处理脚本切分。

发布规模：已发布 test JSONL 共 497 题，其中 138 题引用多个片段；所检查版本中没有任何一题的引用集合跨越不同来源视频 ID。
数据划分：单一公开 test 划分；VimRAG 训练数据及约二十万条项目组成的混合评测语料是独立实验资产。
格式：JSONL plus a video splitting shell script; external HowTo100M videos.。

## 真值与评测

gt 是目标答案，reference 列出可寻址支持片段。这里 document 表示视频片段，而非完整原视频。片段命名及默认六十秒切分可用于重建，但不提供最小时间区间或完整的替代证据集合。

官方指标：model_judged_answer_accuracy。

评测协议：VimRAG §4.1 和 Table 2 报告模型判定的二元答案正确率，Appendix B 指定 Qwen3-Max，Appendix J 给出评分提示。记录语料组成，检索前精确重建片段命名。可基于片段引用进行分析，但本目录不将额外排序指标写成官方已报告分数。

## 适用场景

- 测试迭代 RAG 对支持视频片段的保留
- 比较视觉记忆压缩与回答正确性

## 限制与注意事项

- 跨视频 benchmark 的名称不保证每题都需多个不同来源视频
- 论文完整混合语料不等于这份 497 行标注
- 需要获取来源视频并精确重建预处理
- 支持片段名称比分块最优时间边界粗

## 获取方式与来源

- [官方资源](https://huggingface.co/datasets/Alibaba-NLP/xvbench)
- [论文](https://arxiv.org/abs/2602.12735)
- [数据](https://huggingface.co/datasets/Alibaba-NLP/xvbench/tree/main)
- paper：[来源](https://arxiv.org/html/2602.12735) — 支持字段 `summary`、`ground_truth.provenance`、`evaluation.official_metrics`、`evaluation.protocol`、`data.splits`
- dataset_card：[来源](https://huggingface.co/datasets/Alibaba-NLP/xvbench) — 支持字段 `data.description`、`data.size`、`data.splits`、`data.format`、`access.license`、`access.gated`、`ground_truth.description`、`use.caveats`
- official：[来源](https://huggingface.co/datasets/Alibaba-NLP/xvbench/blob/main/xvbench.jsonl) — 支持字段 `data.size`、`ground_truth.levels`、`use.caveats`
- official：[来源](https://huggingface.co/datasets/Alibaba-NLP/xvbench/blob/main/split_video.sh) — 支持字段 `ground_truth.description`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
