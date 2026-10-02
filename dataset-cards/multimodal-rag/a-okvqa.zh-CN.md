<!-- Generated from catalog/datasets/a-okvqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# A-OKVQA

[English](a-okvqa.md)

包含直接答案、选择题标签和人工解释的知识密集型视觉问答。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `multimodal_rag` |
| 任务 | visual_qa, multimodal_retrieval |
| 模态 | text, image |
| 已发布真值标注层级 | answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | not_provided / provided / provided |
| 原始数据许可 | Apache-2.0 for the official repository; COCO images retain separate upstream terms. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

基于 COCO 2017 图像众包的问题需要世界知识与场景推理。官方 v1.0 数据包含答案选项、直接答案和解释，没有固定外部知识池。

发布规模：约 25,000 个问题。
数据划分：训练集、验证集和测试集；留出测试集预测提交到官方排行榜。
格式：QA JSON; COCO 2017 images downloaded separately.。

## 真值与评测

正确选项、直接答案变体和自由文本解释用于回答与解释监督。解释不代表检索段落标识，也不是经人工核验的外部引用。

官方指标：multiple_choice_accuracy, direct_answer_VQA_accuracy。

评测协议：分别报告选择题和直接回答分数，应用官方直接回答样本资格过滤及匹配规则，并披露知识检索、语料版本和利用解释构建的监督信号。

## 适用场景

- 融合知识检索与场景推理
- 比较直接回答和选择题推理

## 限制与注意事项

- 人工解释不是检索相关性真值
- 该独立后继数据集与 OK-VQA 没有共享的问题—图像对

## 获取方式与来源

- [官方资源](https://github.com/allenai/aokvqa)
- [论文](https://arxiv.org/abs/2206.01718)
- [数据](https://prior-datasets.s3.us-east-2.amazonaws.com/aokvqa/aokvqa_v1p0.tar.gz)
- repository：[来源](https://github.com/allenai/aokvqa) — 支持字段 `summary`、`data.description`、`data.size`、`data.splits`、`ground_truth.description`、`evaluation.protocol`、`access.data`
- repository：[来源](https://github.com/allenai/aokvqa/blob/main/evaluation/eval_predictions.py) — 支持字段 `evaluation.official_metrics`
- repository：[来源](https://github.com/allenai/aokvqa/blob/main/LICENSE) — 支持字段 `access.license`
- official：[来源](https://okvqa.allenai.org/download.html) — 支持字段 `use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
