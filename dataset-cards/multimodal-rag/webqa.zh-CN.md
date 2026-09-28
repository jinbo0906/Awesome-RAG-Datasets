<!-- Generated from catalog/datasets/webqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# WebQA

[English](webqa.md)

回答生成前需要检索相关网页片段与图像的多模态网页问答。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `multimodal_rag` |
| 任务 | multimodal_retrieval, multi_hop_qa, visual_qa |
| 模态 | text, image |
| 已发布真值标注层级 | document, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

Benchmark 提供受限检索和完整检索两种设置，候选包括网页片段与图像；问题类别区分文本和图像证据。


## 真值与评测

相关来源片段与图像支持来源检索和自然语言回答评测；本目录不宣称有通用的图像内部边界框真值。

官方指标：source_retrieval_f1, answer_quality。

评测协议：不要混用受限和完整检索设置的分数；说明大型预提取图像特征是否可用。

## 适用场景

- 网页图文联合检索
- 多模态多跳回答

## 限制与注意事项

- 部分托管特征文件需申请或可能不可用
- 来源 ID 比图像区域证据更粗

## 获取方式与来源

- [官方资源](https://webqna.github.io/)
- [论文](https://arxiv.org/abs/2109.00590)
- [数据](https://github.com/WebQnA/WebQA_Baseline)
- official：[来源](https://webqna.github.io/) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.official_metrics`
- repository：[来源](https://github.com/WebQnA/WebQA_Baseline) — 支持字段 `use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
