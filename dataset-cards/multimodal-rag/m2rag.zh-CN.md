<!-- Generated from catalog/datasets/m2rag.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# M²RAG

[English](m2rag.md)

基于 WebQA 和 Factify 改造并公开的多任务开放域多模态 RAG 数据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_native` |
| 主分类 | `multimodal_rag` |
| 任务 | visual_qa, fact_verification, multimodal_retrieval |
| 模态 | text, image |
| 已发布真值标注层级 | answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | WebQA CC0-1.0 and Factify MIT as stated in paper Appendix A.1; repository code MIT; upstream image terms also apply. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

四项任务包括图像描述、多模态问答、多模态事实核查与图像重排。作者仓库链接任务文件和分卷图像压缩包；问答与描述使用 WebQA，核查使用 Factify。

发布规模：每项任务有 3,000 个测试查询，前三项另有各 3,000 个训练查询，并使用任务各自的语料。
数据划分：作者定义的训练集和测试集；Factify 评测从其验证集抽样。
格式：Task-specific data folders and image TSV/archive assets.。

## 真值与评测

任务目标分别为描述、问答答案、三分类核查标签和参考图像。标注与检索相关性随任务变化，本条目不宣称有通用段落或图像区域证据。

官方指标：BERTScore, ROUGE-L, CIDEr, accuracy, F1, FID。

评测协议：按任务使用语料和指标：描述及问答用文本生成指标，核查用 accuracy/F1，图像重排用 FID。报告 top-k 上下文，不说明聚合方式就不能合并不同任务分数。

## 适用场景

- 跨任务测试多模态检索上下文的利用
- 比较检索增强指令微调和普通 RAG

## 限制与注意事项

- M²RAG 与 M2KR、生成交错回答的 M2RAG 系统不同
- 重排所用 FID 不是标准的查询级相关性指标

## 获取方式与来源

- [官方资源](https://github.com/NEUIR/M2RAG)
- [论文](https://arxiv.org/abs/2502.17297)
- [数据](https://huggingface.co/datasets/whalezzz/M2RAG)
- paper：[来源](https://arxiv.org/html/2502.17297) — 支持字段 `summary`、`data.description`、`data.size`、`data.splits`、`ground_truth.description`、`evaluation.official_metrics`、`evaluation.protocol`、`access.license`
- repository：[来源](https://github.com/NEUIR/M2RAG) — 支持字段 `data.description`、`data.format`、`access.data`、`use.best_for`
- dataset_card：[来源](https://huggingface.co/datasets/whalezzz/M2RAG) — 支持字段 `access.data`、`data.description`、`data.format`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
