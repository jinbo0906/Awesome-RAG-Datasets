<!-- Generated from catalog/datasets/cfvbench.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# CFVBench

[English](cfvbench.md)

面向图表密集报告、新闻与教程的视频细粒度 RAG 数据，分别标注视觉和转录文本中的答案要点。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-01 |
| RAG 角色 | `rag_native` |
| 主分类 | `multimodal_rag` |
| 任务 | video_qa, multimodal_retrieval, multi_hop_qa |
| 模态 | text, video, audio, chart, table |
| 已发布真值标注层级 | document, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | CC-BY-4.0 for author annotations; raw videos have separate academic/non-commercial/no-redistribution terms and upstream copyrights. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

作者仓库发布逐视频问答 JSON，并链接视频压缩包。问题区分视觉、仅转录文本及多模态要点；来源视频目录标识关联视频。

发布规模：599 个视频；论文报告 5,360 道问答，当前仓库 README 报告 5,363 道。
数据划分：已发布的评测集合；未确认单独的官方训练划分。
格式：MP4 archive and per-video multiQA, tsingleQA and vsingleQA JSON.。

## 真值与评测

模型生成并经人工检查的问题配有答案和 keypoints，多模态问答将 keypoints.video 与 keypoints.text 分开。这里 document 表示关联视频 ID。虽然构建流程有时间戳抽取，但所检查的公开问答样本未提供逐题起止区间。

官方指标：Recall@1, Recall@3, Recall@5, Recall@10, video_keypoint_recall, text_keypoint_recall, keypoint_precision, keypoint_f1, ROUGE-L, semantic_similarity, LLM_Likert_score。

评测协议：视频检索命中与生成回答的要点覆盖应分别报告。固定论文及代码版本、评分模型、采帧、ASR/OCR 和检索预算。论文除词面与要点指标外还用语义相似度及模型评分；当前代码可配置相似度后端且使用启发式要点匹配，须记录设置。

## 适用场景

- 测试检索视频是否保留短暂出现的图表或界面细节
- 分开衡量视觉与转录文本的证据覆盖

## 限制与注意事项

- 论文与仓库问答总数相差三道
- 视频关联与答案要点不等于已发布的细粒度时间相关性真值
- 视频访问和再分发条款不同于标注许可
- 评分模型及相似度后端变化可能在系统不变时改变分数

## 获取方式与来源

- [官方资源](https://github.com/CQU-MM-Intelligent-Lab/CFVBENCH)
- [论文](https://doi.org/10.1145/3774904.3792726)
- [数据](https://github.com/CQU-MM-Intelligent-Lab/CFVBENCH/tree/main/Bench)
- paper：[来源](https://arxiv.org/html/2510.09266) — 支持字段 `summary`、`data.size`、`ground_truth.provenance`、`evaluation.official_metrics`、`evaluation.protocol`
- repository：[来源](https://github.com/CQU-MM-Intelligent-Lab/CFVBENCH) — 支持字段 `data.description`、`data.size`、`data.format`、`access.license`、`use.caveats`
- repository：[来源](https://github.com/CQU-MM-Intelligent-Lab/CFVBENCH/blob/main/Bench/-3h4Xt9No9o/multiQA.json) — 支持字段 `ground_truth.levels`、`ground_truth.description`
- repository：[来源](https://github.com/CQU-MM-Intelligent-Lab/CFVBENCH/blob/main/videorag/evaluate/evaluate.py) — 支持字段 `evaluation.protocol`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
