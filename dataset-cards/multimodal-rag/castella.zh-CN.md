<!-- Generated from catalog/datasets/castella.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# CASTELLA

[English](castella.md)

人工标注的长音频事件定位，声音描述可对应同一录音中的多个区间。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-18 |
| RAG 角色 | `auxiliary` |
| 主分类 | `multimodal_rag` |
| 任务 | evidence_retrieval, multimodal_retrieval |
| 模态 | audio, text |
| 已发布真值标注层级 | time_interval |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | external / provided / not_provided |
| 原始数据许可 | CC-BY-4.0 for the annotation release. Source audio availability and terms vary. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

给定录音与局部声音描述，在 1 至 5 分钟音频内寻找对应时段。仓库提供英日标注、来源 ID、下载工具及抽取特征链接。

发布规模：1,862 段录音，训练／验证／测试为 1,009／213／640 段。固定版本英日各含 2,182／352／1,347 条实际局部描述及 6,157／973／4,175 对区间。num_moments 汇总 2,208／357／1,361 与实际描述行不同。
数据划分：原生训练、验证和测试拆分。原论文定位实验排除 242 段无局部描述的录音，挑战赛改造需注明对应协议。
格式：JSON with YouTube IDs, local captions and timestamp pairs, plus separately hosted features。

## 真值与评测

人工以秒为分辨率标注描述对应的起止时间，同一描述可有多个匹配区间，也允许带少量邻近内容。

官方指标：Recall1_at_tIoU_0.5, Recall1_at_tIoU_0.7, mAP_at_tIoU_0.5, mAP_at_tIoU_0.75, mean_mAP_over_tIoU_thresholds。

评测协议：使用论文的时间交并比阈值评估录音内定位，报告划分、特征版本与波形获取情况。生成问答需另建协议。

## 适用场景

- 在语音转录之外独立测试声学定位
- 检索同一长录音中的多次事件

## 限制与注意事项

- 波形实验需另行获取音频语料
- 定位标注用于组件评测且无参考答案
- 一秒分辨率限制很短事件的边界精度

## 获取方式与来源

- [官方资源](https://github.com/line/CASTELLA)
- [论文](https://arxiv.org/abs/2511.15131)
- [数据](https://github.com/line/CASTELLA/tree/9b592efe898e6452631dcea001033009762fe36a/json)
- official：[来源](https://research.lycorp.co.jp/en/publications/2663) — 支持字段 `summary`、`classification`、`data.size`
- paper：[来源](https://arxiv.org/html/2511.15131v2) — 支持字段 `data.description`、`data.splits`、`ground_truth`、`evaluation.official_metrics`、`evaluation.protocol`、`use`
- repository：[来源](https://github.com/line/CASTELLA/tree/9b592efe898e6452631dcea001033009762fe36a/json) — 支持字段 `data.size`、`data.format`、`access.data`、`ground_truth.description`
- repository：[来源](https://github.com/line/CASTELLA) — 支持字段 `access.license`、`evaluation.evaluator`
- official：[来源](https://zenodo.org/records/17412176) — 支持字段 `data.description`、`data.format`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
