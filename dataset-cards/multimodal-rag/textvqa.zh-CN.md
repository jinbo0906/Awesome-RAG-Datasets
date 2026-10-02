<!-- Generated from catalog/datasets/textvqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# TextVQA

[English](textvqa.md)

需要识别并推理自然场景图像中文字的视觉问答。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `multimodal_rag` |
| 任务 | visual_qa |
| 模态 | text, image |
| 已发布真值标注层级 | answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | CC-BY-4.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

问题及十份参考答案关联 OpenImages 照片。v0.5.1 更新 Rosetta OCR 文本，但没有更改 v0.5 的问题或图像。

发布规模：共 45,336 个问题，训练集 34,602 题、验证集 5,000 题、测试集 5,734 题。
数据划分：官方 v0.5.1 训练集、验证集和 test-std 测试集。
格式：Image files, QA JSON and separate OCR JSON.。

## 真值与评测

人工答案变体用于 VQA 评分。Rosetta 文字框属于机器生成的 OCR 输入，不是针对问题的证据区域真值或原生检索相关性标签。

官方指标：VQA_accuracy。

评测协议：固定 OCR 版本，并处理 OpenImages 的旋转元数据。原生评测已提供查询图像；检索实验须另行定义语料、相关性标签和回答协议。

## 适用场景

- 场景文字阅读与 OCR 鲁棒性
- 视觉回答生成组件评测

## 限制与注意事项

- 原生任务没有外部知识检索池或相关性标注
- OCR 框不能证明哪一区域支持答案

## 获取方式与来源

- [官方资源](https://textvqa.org/)
- [论文](https://arxiv.org/abs/1904.08920)
- [数据](https://textvqa.org/dataset/)
- official：[来源](https://textvqa.org/dataset/) — 支持字段 `summary`、`data.description`、`data.size`、`data.splits`、`ground_truth.description`、`access.license`
- official：[来源](https://textvqa.org/challenge/) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
