<!-- Generated from catalog/datasets/mmdocir.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# MMDocIR

[English](mmdocir.md)

长文档多模态检索 benchmark，含人工标注的页面与版面证据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `auxiliary` |
| 主分类 | `multimodal_rag` |
| 任务 | page_retrieval, layout_retrieval |
| 模态 | text, image, table, equation, layout |
| 已发布真值标注层级 | page, layout, bbox |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

评测数据覆盖 313 份长文档；专家问题附页面和版面证据，另有较大的引导构建集合用于训练。

发布规模：评测部分有 1,658 个专家问题、2,107 个页面标签和 2,638 个版面标签。

## 真值与评测

标注者选择证据页面和 MinerU 衍生的版面元素，并手工补充遗漏区域。

官方指标：recall_at_k。

评测协议：页面检索与版面检索是不同任务，应分别评测。

## 适用场景

- 测量跨页面和区域的证据碎片化
- 比较视觉与 OCR 检索

## 限制与注意事项

- 版面标签部分依赖解析器；应保留原始页面坐标和解析器版本
- 项目页面与论文的问题数量不同；须固定所用发布版本

## 获取方式与来源

- [官方资源](https://mmdocrag.github.io/MMDocIR/)
- [论文](https://arxiv.org/abs/2501.08828)
- [数据](https://huggingface.co/MMDocIR)
- official：[来源](https://mmdocrag.github.io/MMDocIR/) — 支持字段 `summary`、`data.description`、`data.size`、`ground_truth.description`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
