<!-- Generated from catalog/datasets/rgb.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# RGB

[English](rgb.md)

中英双语的固定上下文 RAG 压力测试，覆盖噪声、弃答、信息整合和反事实文档。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `auxiliary` |
| 主分类 | `text_rag` |
| 任务 | rag_robustness, single_hop_qa, multi_hop_qa |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | not_provided / provided / provided |
| 原始数据许可 | CC BY-NC-SA 4.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

仓库提供中英文问题及固定的正负段落，另有信息整合和反事实文件。2024 年 3 月的修订版 更正了部分段落和答案；这些文件不定义一个开放式检索语料。

格式：JSON。

## 真值与评测

参考答案与场景特定的上下文标签可用于受控鲁棒性测试，但不是不可变的来源文档片段，也不是人工核定的最优 chunks。

官方指标：accuracy, rejection_rate, error_detection_rate, error_correction_rate。

评测协议：固定原版或修订版、语言、noise_rate 与 passage_num。负例弃答和反事实检测应分别使用上游脚本，不能把这些指标报告为检索召回。

## 适用场景

- 抵抗干扰段落的鲁棒性
- 证据不足时的弃答
- 跨文档信息整合

## 限制与注意事项

- 固定段落不能评测开放语料检索器
- 修订版改变了部分段落和答案

## 获取方式与来源

- [官方资源](https://github.com/chen700564/RGB)
- [论文](https://arxiv.org/abs/2309.01431)
- repository：[来源](https://github.com/chen700564/RGB) — 支持字段 `summary`、`data.description`、`evaluation.official_metrics`、`evaluation.protocol`、`access.license`
- paper：[来源](https://arxiv.org/abs/2309.01431) — 支持字段 `classification.tasks`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
