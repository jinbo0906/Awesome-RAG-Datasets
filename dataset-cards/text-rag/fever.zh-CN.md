<!-- Generated from catalog/datasets/fever.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# FEVER

[English](fever.md)

基于维基百科的主张核查数据，附支持句集合标注。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | fact_verification, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | sentence, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

对照固定的维基百科快照，将主张标为支持、反驳或信息不足。


## 真值与评测

维基百科句子组成的证据集合用于支持或反驳可核查主张。

官方指标：label_accuracy, fever_score。

评测协议：FEVER 分数要求标签正确，且支持或反驳类主张的完整证据也被找回。

## 适用场景

- 句子级证据检索
- 测试完整证据集合覆盖

## 限制与注意事项

- 信息不足（NEI）样本没有正向的金标准证据集合

## 获取方式与来源

- [官方资源](https://fever.ai/dataset/fever.html)
- [论文](https://aclanthology.org/N18-1074/)
- paper：[来源](https://aclanthology.org/N18-1074/) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
