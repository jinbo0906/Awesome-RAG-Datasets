<!-- Generated from catalog/datasets/visual-rag.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# Visual-RAG

[English](visual-rag.md)

提供人工核验线索图像相关性、面向文本到图像 RAG 的细粒度自然物种问答。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_native` |
| 主分类 | `multimodal_rag` |
| 任务 | visual_qa, multimodal_retrieval |
| 模态 | text, image |
| 已发布真值标注层级 | document, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | CC-BY-NC-4.0 for annotations; iNaturalist images retain individual upstream licenses. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

官方 v2 JSONL 提供文本问题、答案变体、科学名称和逐图像二值线索标签。图像来自 iNaturalist 2021，原生评测检索同一物种的子集。

发布规模：修订后的 v2 标注有 374 个问题；每题原生候选池约含 200–300 张同物种图像。
数据划分：用于评测的标注，没有原生训练集。
格式：v2_anno.jsonl and upstream iNaturalist image files.。

## 真值与评测

模型提出的问题与图像标签经人工核验。公开二值标签指定线索图像和可接受答案，没有统一的图像内部证据框。

官方指标：Recall@k, nDCG@k, Hit@k, Hit_Count@k, LLM_judged_answer_accuracy, ROUGE, gCUE。

评测协议：使用修订后的 v2 标签及规定的同物种语料。区分无图像、金标准线索、非线索、top-k RAG 与 one-in-k 设置；固定裁判模型，并区别报告 ACL 2026 注入金标准的选择候选池。

## 适用场景

- 检索细粒度视觉线索的文本到图像任务
- 区分线索利用失败和检索失败

## 限制与注意事项

- v1 存在无效问题和图像标签错误，已在 v2 修订
- 作者不重新分发图像，原生候选池小于整个 iNaturalist 语料

## 获取方式与来源

- [官方资源](https://github.com/visual-rag/visual-rag)
- [论文](https://arxiv.org/abs/2502.16636)
- [数据](https://github.com/visual-rag/visual-rag/blob/main/v2_anno.jsonl)
- repository：[来源](https://github.com/visual-rag/visual-rag) — 支持字段 `summary`、`data.description`、`data.size`、`data.format`、`ground_truth.description`、`use.caveats`
- paper：[来源](https://arxiv.org/html/2502.16636) — 支持字段 `ground_truth.provenance`、`evaluation.official_metrics`、`evaluation.protocol`、`data.splits`、`access.license`
- paper：[来源](https://aclanthology.org/2026.acl-long.1620/) — 支持字段 `evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
