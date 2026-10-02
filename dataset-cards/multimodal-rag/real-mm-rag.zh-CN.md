<!-- Generated from catalog/datasets/real-mm-rag.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# REAL-MM-RAG

[English](real-mm-rag.md)

面向内容相似的 IBM 金融与技术材料、包含三级查询改写的文档页面检索数据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `auxiliary` |
| 主分类 | `multimodal_rag` |
| 任务 | page_retrieval, multimodal_retrieval, rag_robustness |
| 模态 | text, image, table, chart, layout |
| 已发布真值标注层级 | page, answer |
| 证据标注来源 | synthetic |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | CDLA-Permissive-2.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

作者发布 FinReport、FinSlides、TechReport、TechSlides 四个子集。Parquet 行包含页面图像、image_filename、query、三级改写和生成答案；查询为空的行保留干扰页面。官方 benchmark 评测检索，不评测答案生成。

发布规模：论文 Table S1 报告 163 份文档、8,604 页和 4,553 个基础查询，每题有四种措辞版本。
数据划分：四个测试子集；论文提出的 FinTab 和改写后的 ColPali 训练数据是独立资源。
格式：Hugging Face Parquet with embedded page images and nullable query/answer fields.。

## 真值与评测

生成查询关联 image_filename。VLM 检查其他页面，仅保留被判断为只有原始页面能够回答的查询。生成答案辅助数据构建；相关性标签不是人工完整真值，也没有针对问题的区域或单元格坐标。

官方指标：nDCG@5, Recall@1, Recall@5。

评测协议：按 image_filename 去重页面语料，保留空查询的干扰页面，分别评测各子集和措辞等级。Table 2 使用三级改写，Table 3 比较 0–3 级。分块改造须保留页面身份；生成答案不代表已有官方问答评分。

## 适用场景

- 语义查询改写下的检索鲁棒性
- 在内容相似且表格密集的文档上比较文本分块与页面图像

## 限制与注意事项

- 模型生成与核验的相关性仍可能存在假负例
- Hugging Face 行数不等于独立页面数或非空查询数
- 页面级真值不能直接评分细粒度分块或单元格定位

## 获取方式与来源

- [官方资源](https://navvewas.github.io/REAL-MM-RAG/)
- [论文](https://aclanthology.org/2025.acl-long.1528/)
- [数据](https://huggingface.co/collections/ibm-research/real-mm-rag-bench)
- official：[来源](https://navvewas.github.io/REAL-MM-RAG/) — 支持字段 `summary`、`classification.rag_role`、`data.description`、`evaluation.protocol`
- paper：[来源](https://aclanthology.org/2025.acl-long.1528.pdf) — 支持字段 `data.size`、`data.splits`、`ground_truth.description`、`ground_truth.provenance`、`evaluation.official_metrics`、`use.caveats`
- dataset_card：[来源](https://huggingface.co/datasets/ibm-research/REAL-MM-RAG_FinReport) — 支持字段 `data.description`、`data.format`、`access.license`、`access.gated`、`evaluation.protocol`
- dataset_card：[来源](https://huggingface.co/datasets/ibm-research/REAL-MM-RAG_FinSlides) — 支持字段 `data.description`、`access.license`
- dataset_card：[来源](https://huggingface.co/datasets/ibm-research/REAL-MM-RAG_TechReport) — 支持字段 `data.description`、`access.license`
- dataset_card：[来源](https://huggingface.co/datasets/ibm-research/REAL-MM-RAG_TechSlides) — 支持字段 `data.description`、`access.license`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
