<!-- Generated from catalog/datasets/harp-audio.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# HARP Audio QA (SongEval / MedMosaic)

[English](harp-audio.md)

在指定录音内检索音频证据并回答问题，覆盖歌曲对比及口头报告与声学症状的区分。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-18 |
| RAG 角色 | `rag_native` |
| 主分类 | `multimodal_rag` |
| 任务 | audio_qa, evidence_retrieval, multimodal_retrieval |
| 模态 | audio, text |
| 已发布真值标注层级 | time_interval, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | MIT for queries and checkpoints per release notice. Source audio terms differ (SongEval CC-BY-NC-SA-4.0 and MedMosaic CC-BY-4.0). |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

2026 年 9 月的 HARP 论文评测给定长录音的片段检索。公开问题和元数据覆盖音乐比较与模拟问诊，源音频由上游获取并根据作者脚本准备。

发布规模：公布 712 题。SongEval 在 50 段串烧上有 500 题，音频提示 200、时间提示 150、顺序提示 150。MedMosaic 在 106 次模拟问诊中有 212 题，报告症状和表现症状各 106。
数据划分：公开两条评测轨，问题文件无独立训练集。第三条情绪轨需另行取得 MSP 许可并本地重建。
格式：JSONL questions and song metadata with external audio。

## 真值与评测

音乐题的两个曲目通过文件名与录音 ID 关联到完整歌曲的起止时间和专家审美评分。MedMosaic 提供是非答案及评分背景，未发布逐题支持时间区间。

官方指标：retrieval_hit_rate, judged_answer_accuracy, judged_rationale_accuracy。

评测协议：在能解析证据的设置下计算必需证据命中比例，由模型评估回答与理由。发布评分器在纯音频理由上回退到事实正确性。分开报告评测轨、检索模态、oracle 条件及评委。

## 适用场景

- 测试同一录音内多片段检索
- 比较转录检索与声学证据检索

## 限制与注意事项

- 曲目区间覆盖整首歌而非最短理由位置
- 公开问题数不含 MSP 情绪轨且论文计 426 条与仓库文档 466 条不同
- 检索范围是题目指定的录音

## 获取方式与来源

- [官方资源](https://github.com/chinjouli/harp)
- [论文](https://arxiv.org/abs/2609.14116)
- [数据](https://huggingface.co/cjli/harp/tree/68f6baf120e7b0fa4627e6f6a15789498e676d97)
- paper：[来源](https://arxiv.org/html/2609.14116) — 支持字段 `summary`、`classification`、`data.description`、`data.splits`、`ground_truth`、`evaluation.official_metrics`、`evaluation.protocol`、`use`
- official：[来源](https://huggingface.co/cjli/harp/tree/68f6baf120e7b0fa4627e6f6a15789498e676d97) — 支持字段 `data.size`、`data.format`、`access.data`、`access.license`、`ground_truth.description`
- repository：[来源](https://github.com/chinjouli/harp/blob/fea0bf987c92caff0be755d22ab27fa2423f3571/dataset/process_gt_music.py) — 支持字段 `ground_truth.description`、`evaluation.protocol`
- repository：[来源](https://github.com/chinjouli/harp/blob/fea0bf987c92caff0be755d22ab27fa2423f3571/evaluate/README.md) — 支持字段 `evaluation.evaluator`、`evaluation.protocol`
- repository：[来源](https://github.com/chinjouli/harp/blob/main/dataprep/emotion/README.md) — 支持字段 `data.splits`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
