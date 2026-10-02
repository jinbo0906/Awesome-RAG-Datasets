<!-- Generated from catalog/datasets/nomiracl.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# NoMIRACL

[English](nomiracl.md)

多语言 RAG 相关性判断数据，分别提供无相关段落和至少有一个相关段落的上下文集合。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `auxiliary` |
| 主分类 | `text_rag` |
| 任务 | evidence_retrieval, rag_robustness |
| 模态 | text |
| 已发布真值标注层级 | paragraph |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / not_provided |
| 原始数据许可 | Apache-2.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

发布查询、相关性标签和每题最多十个已标注段落，涵盖 18 种语言的相关与非相关子集。评测的是二元相关性判断，而非答案文本正确性。

数据划分：开发集与测试集分别包含相关和非相关子集。

## 真值与评测

人工段落标注决定给定上下文中是否存在相关内容。非相关集合全部由已判为不相关的段落组成；相关集合至少有一个已判为相关的段落。原生标签不是参考答案字符串。

官方指标：hallucination_rate, error_rate。

评测协议：分别报告两个子集。非相关集合的 hallucination rate 为 FP/(FP+TN)，相关集合的 error rate 为 FN/(FN+TP)。两者衡量上下文相关性识别，不是任意生成答案的事实准确率。

## 适用场景

- 检索失败时的多语言弃答
- 平衡错误自信与漏识别相关证据

## 限制与注意事项

- 这里的幻觉率名称对应二元判断协议
- 随题提供的 top-k 上下文不能评测全语料检索召回率

## 获取方式与来源

- [官方资源](https://github.com/project-miracl/nomiracl)
- [论文](https://aclanthology.org/2024.findings-emnlp.730/)
- [数据](https://huggingface.co/datasets/miracl/nomiracl)
- repository：[来源](https://github.com/project-miracl/nomiracl) — 支持字段 `summary`、`ground_truth.description`、`evaluation.official_metrics`、`evaluation.protocol`
- dataset_card：[来源](https://huggingface.co/datasets/miracl/nomiracl) — 支持字段 `data.description`、`data.splits`、`access.license`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
