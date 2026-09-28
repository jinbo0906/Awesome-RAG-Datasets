<!-- Generated from catalog/datasets/bright.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# BRIGHT

[English](bright.md)

文本相关性判断需要较强推理能力的检索 benchmark。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `auxiliary` |
| 主分类 | `text_rag` |
| 任务 | reasoning_retrieval, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | document |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / not_provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

查询和候选文档支持推理密集型的检索评测。


## 真值与评测

文档级相关性标注评测的是检索，而不是回答生成。

官方指标：ndcg_at_10。

评测协议：将其用作检索组件测试；如需称为端到端 RAG benchmark，还必须补充回答协议。

## 适用场景

- 选择擅长推理的检索器
- 跨领域检索压力测试

## 限制与注意事项

- 本目录条目未确认原生的回答生成金标准

## 获取方式与来源

- [官方资源](https://brightbenchmark.github.io/)
- [论文](https://arxiv.org/abs/2407.12883)
- official：[来源](https://brightbenchmark.github.io/) — 支持字段 `summary`、`classification.tasks`、`data.description`、`ground_truth.levels`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
