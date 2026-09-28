<!-- Generated from catalog/datasets/eli5.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# ELI5

[English](eli5.md)

来自 Reddit 问答、配有网页支持文档的解释性长篇问答数据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `text_rag` |
| 任务 | long_form_qa, attribution |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | source content rights vary |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

官方脚本重建 Reddit 问答和 CommonCrawl 支持文档；作者没有托管处理后的数据。


## 真值与评测

网页支持文档通过启发式方法选择，不是人工标注的最小引用集合。

官方指标：rouge_l。

评测协议：记录 Reddit 和 CommonCrawl 快照；ALCE-ELI5 使用独立的 BM25 检索包和引用评测器。

## 适用场景

- 长篇解释生成
- 通过 ALCE 评测引用

## 限制与注意事项

- 重建需要大量计算及上游内容访问
- 支持段落来自启发式选择而非人工真值

## 获取方式与来源

- [官方资源](https://github.com/facebookresearch/ELI5)
- [论文](https://arxiv.org/abs/1907.09190)
- repository：[来源](https://github.com/facebookresearch/ELI5) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`use.caveats`
- repository：[来源](https://github.com/princeton-nlp/ALCE) — 支持字段 `evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
