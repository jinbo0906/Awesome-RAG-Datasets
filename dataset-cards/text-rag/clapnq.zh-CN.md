<!-- Generated from catalog/datasets/clapnq.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# CLAP NQ

[English](clapnq.md)

基于 Natural Questions 段落中非连续句子、生成有来源依据的长篇回答。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | long_form_qa, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | sentence, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | Apache-2.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

官方版本包括已标注问答、原始维基百科文档和检索格式数据，覆盖可回答与不可回答样本。


## 真值与评测

从段落中选出的句子为简洁连贯的答案提供依据；许多回答需要组合不相邻的句子。

官方指标：retrieval_recall, answer_quality。

评测协议：重建段落时保留原始句子标识；官方测试集答案未公开。

## 适用场景

- 跨非连续证据的分块研究
- 有依据的长篇回答

## 限制与注意事项

- 官方测试标签需要通过上游评测流程获取

## 获取方式与来源

- [官方资源](https://github.com/primeqa/clapnq)
- [论文](https://arxiv.org/abs/2404.02103)
- repository：[来源](https://github.com/primeqa/clapnq) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.protocol`、`access.license`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
