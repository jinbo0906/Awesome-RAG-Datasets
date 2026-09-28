<!-- Generated from catalog/datasets/narrativeqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# NarrativeQA

[English](narrativeqa.md)

围绕书籍和剧本的问题，附人工答案及文档级链接。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `text_rag` |
| 任务 | long_context_qa, summarization |
| 模态 | text |
| 已发布真值标注层级 | document, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | Apache-2.0 repository; source stories have separate terms |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

发布数据包含问答对、文档元数据、维基百科摘要，以及获取完整故事的链接或下载脚本。


## 真值与评测

问题有参考答案，但原生数据没有句子级支持事实映射。

官方指标：rouge_l, bleu, meteor。

评测协议：披露使用摘要还是完整故事，并说明所用故事的准确快照。

## 适用场景

- 长文档检索压力测试
- 故事级回答生成

## 限制与注意事项

- 不是原生的分块边界真值
- 完整故事能否获取取决于来源 URL 与权利

## 获取方式与来源

- [官方资源](https://github.com/google-deepmind/narrativeqa)
- [论文](https://arxiv.org/abs/1712.07040)
- repository：[来源](https://github.com/google-deepmind/narrativeqa) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`access.license`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
