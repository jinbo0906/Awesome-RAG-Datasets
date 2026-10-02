<!-- Generated from catalog/datasets/arxivqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# ArXivQA

[English](arxivqa.md)

由 GPT-4V 生成、用于多模态指令训练与检索改造的科学图表选择题问答。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `multimodal_rag` |
| 任务 | visual_qa, multimodal_retrieval |
| 模态 | text, image, chart, equation |
| 已发布真值标注层级 | answer |
| 证据标注来源 | synthetic |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

Multimodal ArXiv 项目发布图像及生成的问题、选项、标签和解释。VisRAG 根据问题—图像关联另行过滤并构建检索评测。

发布规模：已发布 100,000 个问答样本。
数据划分：原始 Hugging Face 包只有 train 容器；面向检索的评测划分属于衍生协议。
格式：JSON QA and figure-image archive.。

## 真值与评测

生成标签和解释用于图像回答监督。配对图像可构建检索正例，但解释不是人工证据框，也不是原生完整语料相关性真值。

官方指标：multiple_choice_accuracy。

评测协议：原始版本主要用于训练，另行构建留出集时须明确标识。使用 VisRAG 时遵循其转换查询、图像池与检索／生成评分，不能假定原始版本含 RAG 测试集。

## 适用场景

- 科学图像的指令训练
- 明确定义的图像检索改造

## 限制与注意事项

- 合成标签与解释需要独立错误审查
- 项目页面写明 CC-BY-NC-4.0 及研究用途限制，当前数据卡却标 CC-BY-SA-4.0

## 获取方式与来源

- [官方资源](https://mm-arxiv.github.io/)
- [论文](https://aclanthology.org/2024.acl-long.775/)
- [数据](https://huggingface.co/datasets/MMInstruction/ArxivQA)
- official：[来源](https://mm-arxiv.github.io/) — 支持字段 `summary`、`data.description`、`ground_truth.provenance`、`use.caveats`
- dataset_card：[来源](https://huggingface.co/datasets/MMInstruction/ArxivQA) — 支持字段 `data.size`、`data.splits`、`data.format`、`ground_truth.description`、`use.caveats`
- paper：[来源](https://proceedings.iclr.cc/paper_files/paper/2025/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf) — 支持字段 `data.description`、`evaluation.official_metrics`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
