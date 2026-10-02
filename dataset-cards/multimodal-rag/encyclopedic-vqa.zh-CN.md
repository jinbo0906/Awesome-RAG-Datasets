<!-- Generated from catalog/datasets/encyclopedic-vqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# Encyclopedic-VQA (E-VQA)

[English](encyclopedic-vqa.md)

提供受控维基百科知识库和证据章节标识的细粒度视觉知识问答。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_native` |
| 主分类 | `multimodal_rag` |
| 任务 | visual_qa, multimodal_retrieval, multi_hop_qa |
| 模态 | text, image |
| 已发布真值标注层级 | document, section, quote, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

CSV 问答记录将 iNaturalist 和 Google Landmarks 图像关联到公开的 WikiWeb2M 衍生知识库 JSON。图像像素须另行获取；作者也发布了 Google Lens 测试检索结果。

发布规模：约 221,000 组独立问答、一百万个图像—问题—答案样本。
数据划分：训练集、验证集和测试集，提供问题类型和维基百科实体是否在训练中出现的标识。
格式：QA CSV, knowledge-base JSON and separately sourced images.。

## 真值与评测

维基百科 URL 与 evidence_section_id 定位支持信息；两跳问题含两个连续来源。只有模板问题提供证据字符串，不能声称每题都有原文引用或视觉区域标注。

官方指标：BEM_answer_accuracy。

评测协议：使用公开 BEM 评测器及问题类型处理，包含多答案情形。保留维基百科 URL 键和知识库章节，后续 M2KR 检索转换不能视为原始协议。

## 适用场景

- 由图像驱动的百科证据检索
- 评测章节依据与多跳视觉知识

## 限制与注意事项

- 知识库图像和查询图像像素需要分别从上游下载
- 原文引用支持仅覆盖模板问题

## 获取方式与来源

- [官方资源](https://github.com/google-research/google-research/tree/master/encyclopedic_vqa)
- [论文](https://arxiv.org/abs/2306.09224)
- [数据](https://github.com/google-research/google-research/blob/master/encyclopedic_vqa/README.md)
- repository：[来源](https://github.com/google-research/google-research/blob/master/encyclopedic_vqa/README.md) — 支持字段 `summary`、`data.description`、`data.size`、`data.splits`、`ground_truth.description`、`evaluation.official_metrics`、`evaluation.protocol`
- paper：[来源](https://arxiv.org/abs/2306.09224) — 支持字段 `classification.rag_role`、`ground_truth.provenance`、`use.best_for`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
