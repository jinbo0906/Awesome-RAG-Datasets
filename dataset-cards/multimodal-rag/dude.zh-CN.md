<!-- Generated from catalog/datasets/dude.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# DUDE

[English](dude.md)

覆盖多种答案形式、领域和可选答案区域标注的多页文档问答。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `multimodal_rag` |
| 任务 | visual_qa, page_retrieval, long_context_qa |
| 模态 | text, image, layout, table |
| 已发布真值标注层级 | page, bbox, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | CC-BY-4.0 for the author-linked dataset loader; source documents retain their upstream terms. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

官方版本包含 PDF、问答标注和多种 OCR 结果。作者链接的数据加载器支持公开真值；OpenDocVQA 另行过滤并构建开放域版本。

数据划分：训练集、验证集和测试集；应使用明确命名的公开真值版本，不要假定所有竞赛数据包都公开标签。
格式：PDF documents, JSON annotations and OCR in provider-specific or DUE format.。

## 真值与评测

加载器提供答案、可接受变体以及带页坐标的 answers_page_bounding_boxes。部分样本没有框；抽象答案和不可回答问题也不一定有可定位的支持区域。

官方指标：ANLS。

评测协议：保留答案类型、空答案、页码和 OCR 配置，使用官方阈值计算 ANLS。开放域检索改造需披露候选池和过滤后的查询。

## 适用场景

- 页面选择与长文档回答
- 测试多样答案形式及已有答案区域

## 限制与注意事项

- 并非每个问题都有答案框
- 不同 OCR 结果及过滤后的 OpenDocVQA 协议属于独立版本

## 获取方式与来源

- [官方资源](https://github.com/duchallenge-team/dude)
- [论文](https://openaccess.thecvf.com/content/ICCV2023/html/Van_Landeghem_Document_Understanding_Dataset_and_Evaluation_DUDE_ICCV_2023_paper.html)
- [数据](https://huggingface.co/datasets/jordyvl/DUDE_loader)
- repository：[来源](https://github.com/duchallenge-team/dude) — 支持字段 `summary`、`data.description`、`data.format`、`use.caveats`
- dataset_card：[来源](https://huggingface.co/datasets/jordyvl/DUDE_loader/blob/main/DUDE_loader.py) — 支持字段 `data.splits`、`ground_truth.levels`、`ground_truth.description`、`access.license`
- repository：[来源](https://github.com/Jordy-VL/DUDEeval) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`
- paper：[来源](https://arxiv.org/html/2504.09795) — 支持字段 `data.description`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
