<!-- Generated from catalog/datasets/unidoc-bench.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# UniDoc-Bench

[English](unidoc-bench.md)

关联文本、表格与图形证据，并在统一条件下比较检索范式的文档型多模态 RAG 数据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-01 |
| RAG 角色 | `rag_native` |
| 主分类 | `multimodal_rag` |
| 任务 | page_retrieval, visual_qa, multi_hop_qa, attribution |
| 模态 | text, image, table, chart, layout |
| 已发布真值标注层级 | page, figure, fact_citation, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | CC-BY-NC-4.0 with an additional author notice against developing competing models; consult LICENSE.txt and source-document rights. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

八个领域的 PDF 压缩包配有问答、来源元数据及选定的文本和图像证据。GitHub 过滤后 JSON 与 Hugging Face Parquet 的字段结构不同，需要明确映射。

发布规模：论文在约 70,000 个 PDF 页面上评测 1,600 道问答；当前 Hugging Face 配置与规模 API 给出八个领域划分，每个 200 行。其 README 正文却写 1,742 道问答，属于尚未解决的文档矛盾。
数据划分：当前 Hugging Face 默认配置提供八个按领域命名的评测划分，并非 README 正文所称单一 test 划分。
格式：Domain PDF archives, QA JSON and domain-split Hugging Face Parquet.。

## 真值与评测

问答通过 chunk_used 元数据关联用到的文本块和图形，并列出支持事实。引用可映射到来源页面，但不是通用的逐题边界框。问答由模型合成并经人工核验，不同论文与发布说明的核验范围存在差异。

官方指标：Precision@10, Recall@10, answer_completeness, faithfulness。

评测协议：文本、图像、融合与联合检索应使用相同候选语料、提示和预算。将检索文本块或图像页映射回原文件与页码评分；页面部分重叠可能抬高召回。事实完整性和忠实性应使用指定模型评判，记录版本和评分器，不以通用 Ragas 默认值替代。

## 适用场景

- 在共享候选池中比较多模态检索
- 研究跨文本与图形的证据完整性

## 限制与注意事项

- Hugging Face 正文声称单一测试集有 1742 题但其领域划分配置合计为 1600；应检查实际文件而非推断新版本
- 正式发表摘要及 Hugging Face 数据卡写明百分之二十人工核验而修订预印本声称全量核验；须固定版本
- 页面重叠命中不代表细粒度证据完整
- 许可除所标 Creative Commons 名称外还有额外模型使用说明

## 获取方式与来源

- [官方资源](https://github.com/SalesforceAIResearch/UniDoc-Bench)
- [论文](https://aclanthology.org/2026.findings-emnlp.534/)
- [数据](https://huggingface.co/datasets/Salesforce/UniDoc-Bench)
- paper：[来源](https://aclanthology.org/2026.findings-emnlp.534/) — 支持字段 `name`、`summary`、`data.size`、`ground_truth.provenance`、`use.caveats`
- paper：[来源](https://arxiv.org/html/2510.03663) — 支持字段 `ground_truth.description`、`evaluation.official_metrics`、`evaluation.protocol`、`use.caveats`
- dataset_card：[来源](https://huggingface.co/datasets/Salesforce/UniDoc-Bench) — 支持字段 `data.size`、`data.splits`、`data.format`、`access.data`、`access.gated`、`use.caveats`
- official：[来源](https://datasets-server.huggingface.co/size?dataset=Salesforce%2FUniDoc-Bench) — 支持字段 `data.size`、`data.splits`、`use.caveats`
- repository：[来源](https://github.com/SalesforceAIResearch/UniDoc-Bench/blob/main/data/QA/filtered/finance.json) — 支持字段 `data.description`、`ground_truth.levels`、`ground_truth.description`
- official：[来源](https://github.com/SalesforceAIResearch/UniDoc-Bench/blob/main/LICENSE.txt) — 支持字段 `access.license`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
