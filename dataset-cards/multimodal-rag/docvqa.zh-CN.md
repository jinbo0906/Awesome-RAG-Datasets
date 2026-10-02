<!-- Generated from catalog/datasets/docvqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# DocVQA (single-page)

[English](docvqa.md)

基于单页工业文档扫描图像的人工抽取式问答。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `multimodal_rag` |
| 任务 | visual_qa, page_retrieval |
| 模态 | text, image, layout |
| 已发布真值标注层级 | answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

原始任务为每个问题提供一张文档图像、OCR 和人工答案。VDocRAG 将过滤后的子集用于开放域训练；其 OpenDocVQA 协议是另行构建的改造版本。

发布规模：约 50,000 个问题，对应 12,767 张文档图像。
数据划分：原始训练集、验证集和留出测试集；测试集通过官方挑战平台评测。
格式：Document images, question/answer JSON and OCR.。

## 真值与评测

答案是所给图像中的文本跨度，但答案字符串不代表通用的 OCR 跨度坐标或全语料检索相关性标注。图像配对关系可用于明确定义的页面检索改造。

官方指标：ANLS。

评测协议：保留原始划分与答案别名，单独报告图像池、问题过滤和新增相关性标注。单页 DocVQA、MP-DocVQA 与 OpenDocVQA 属于不同设置。

## 适用场景

- 视觉文档阅读基线
- 明确定义页面候选池的检索改造

## 限制与注意事项

- 原始问题假定相关图像已经给出
- 挑战平台访问和测试标签公开程度与衍生镜像可能不同

## 获取方式与来源

- [官方资源](https://site.docvqa.org/datasets/docvqa)
- [论文](https://openaccess.thecvf.com/content/WACV2021/papers/Mathew_DocVQA_A_Dataset_for_VQA_on_Document_Images_WACV_2021_paper.pdf)
- [数据](https://rrc.cvc.uab.es/?ch=17&com=downloads)
- official：[来源](https://site.docvqa.org/datasets/docvqa) — 支持字段 `summary`、`data.description`、`data.size`、`access.data`、`access.gated`
- paper：[来源](https://openaccess.thecvf.com/content/WACV2021/papers/Mathew_DocVQA_A_Dataset_for_VQA_on_Document_Images_WACV_2021_paper.pdf) — 支持字段 `ground_truth.description`、`evaluation.official_metrics`、`data.splits`
- paper：[来源](https://arxiv.org/html/2504.09795) — 支持字段 `data.description`、`evaluation.protocol`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
