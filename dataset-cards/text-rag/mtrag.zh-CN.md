<!-- Generated from catalog/datasets/mtrag.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# MTRAG (human)

[English](mtrag.md)

人工编写的多轮 RAG 对话，覆盖四种语料的检索与生成任务。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | conversational_qa, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | paragraph, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

人工版本有 110 组经过审查的对话，平均每组 7.7 轮，共 842 个轮次级评测任务。 ClapNQ、Cloud、FiQA 和 Govt 是不同语料；合成版 MTRAG 与 MTRAG-UN 是其他发布版本， 不包含在本条目中。


## 真值与评测

对话包含参考段落、段落相关性与回答。可回答和部分可回答轮次的检索任务以 BEIR 格式提供； 不可回答轮次需要单独的评测处理。

官方指标：尚未确认。

评测协议：保留对话历史、领域和轮次顺序。分别比较 reference、reference+RAG 和 full-RAG 设置；只有最后一种会让检索遗漏影响生成。

## 适用场景

- 追问与欠明确查询
- 分析跨对话轮次的检索错误
- 多领域 RAG

## 限制与注意事项

- 不能把 842 个轮次级任务当作 842 组独立对话
- 合成版和 UN 变体的来源及协议不同

## 获取方式与来源

- [官方资源](https://github.com/IBM/mt-rag-benchmark)
- [论文](https://arxiv.org/abs/2501.03468)
- repository：[来源](https://github.com/IBM/mt-rag-benchmark) — 支持字段 `summary`、`data.description`、`ground_truth.description`
- repository：[来源](https://github.com/IBM/mt-rag-benchmark/blob/main/mtrag-human/README.md) — 支持字段 `data.description`、`evaluation.protocol`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
