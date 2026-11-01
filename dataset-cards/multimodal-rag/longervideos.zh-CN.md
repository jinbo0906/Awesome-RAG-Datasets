<!-- Generated from catalog/datasets/longervideos.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# LongerVideos

[English](longervideos.md)

在长视频集合上进行开放式问答和生成质量比较的数据，未发布参考答案或时间相关性标注。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-01 |
| RAG 角色 | `auxiliary` |
| 主分类 | `multimodal_rag` |
| 任务 | video_qa, long_form_qa, summarization |
| 模态 | text, video, audio |
| 已发布真值标注层级 | 未说明 |
| 证据标注来源 | unknown |
| 语料 / 查询 / 答案 | external / provided / not_provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

VideoRAG 作者按集合组织 YouTube URL、主题描述和开放问题。使用者需获取原视频，构建采帧、ASR 及检索表示；已发布问题没有 reference_answer 或证据区间。

发布规模：作者概览报告 22 个集合、164 个视频、602 个查询，合计约 134.6 小时。
数据划分：评测集合；未确认原生训练划分或带逐题答案真值的划分。
格式：Collection-indexed JSON with video_url, description, questions and type; external videos.。

## 真值与评测

已检查的 dataset.json 提供问题 ID 和文本，但没有参考答案、时间相关性标注或独立标注的跨视频证明链。集合成员定义可用上下文，不是逐题相关性标签。

官方指标：pairwise_win_rate, Comprehensiveness, Empowerment, Trustworthiness, Depth, Density, Overall_Score。

评测协议：沿用 VideoRAG 的模型比较提示和聚合脚本。成对评测交换答案顺序，并聚合多次判定；量表评分使用指定标准。固定对照系统、评分模型、视频可用性、处理成本和检索预算。偏好胜率不是参考答案准确率，也不是检索召回。

## 适用场景

- 在按主题分组的数小时视频上压力测试生成
- 研究相对回答质量和索引成本

## 限制与注意事项

- 已检查的问题文件没有公开金标准答案或时间相关性标注
- YouTube 可用性和上游权利可能变化
- 框架许可不能确定单独的数据集或视频许可
- 模型比较分数不能证明事实证据完整

## 获取方式与来源

- [官方资源](https://github.com/HKUDS/VideoRAG)
- [论文](https://doi.org/10.1145/3770854.3783944)
- [数据](https://github.com/HKUDS/VideoRAG/blob/main/VideoRAG-algorithm/longervideos/dataset.json)
- repository：[来源](https://github.com/HKUDS/VideoRAG) — 支持字段 `summary`、`data.size`、`use.caveats`
- repository：[来源](https://github.com/HKUDS/VideoRAG/blob/main/VideoRAG-algorithm/longervideos/dataset.json) — 支持字段 `data.description`、`data.format`、`data.answers`、`ground_truth.levels`、`ground_truth.description`
- paper：[来源](https://arxiv.org/html/2502.01549) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`、`use.best_for`
- repository：[来源](https://github.com/HKUDS/VideoRAG/tree/main/VideoRAG-algorithm/reproduce) — 支持字段 `evaluation.protocol`、`evaluation.evaluator`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
