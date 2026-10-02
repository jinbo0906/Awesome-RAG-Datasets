<!-- Generated from catalog/datasets/pubmedqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# PubMedQA

[English](pubmedqa.md)

基于 PubMed 摘要预测是、否或不确定的生物医学研究问答，含已标注、未标注和人工合成子集。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `text_rag` |
| 任务 | single_hop_qa, fact_verification |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown; PubMed abstract rights depend on upstream content |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

原生样本提供问题、摘要上下文及从结论得到的长答案。MIRAGE 的 PubMedQA* 从 500 个人工专家标注测试问题中去掉给定上下文，改用外部检索。

发布规模：1,000 个人工专家标注样本、61.2k 个未标注样本和 211.3k 个人工合成样本；未标注子集没有金标准决策。
格式：JSON。

## 真值与评测

评分目标是最终是、否或不确定的判断，PQA-L 使用专家标签，PQA-A 使用合成标签。给定摘要是任务上下文，不是穷尽的开放语料相关性判断。

官方指标：accuracy, macro_f1。

评测协议：报告所选子集与监督设置。原生摘要条件问答与去掉上下文的 MIRAGE PubMedQA* 是不同任务，准确率或 F1 不能当作检索召回率。

## 适用场景

- 以生物医学摘要为条件的问答
- 通过 MIRAGE 比较去掉上下文的医学 RAG

## 限制与注意事项

- 去掉上下文的评测不能泄漏来源摘要或参考结论
- 不同标注来源需分别报告

## 获取方式与来源

- [官方资源](https://pubmedqa.github.io/)
- [论文](https://aclanthology.org/D19-1259/)
- [数据](https://github.com/pubmedqa/pubmedqa)
- official：[来源](https://pubmedqa.github.io/) — 支持字段 `summary`、`data.size`
- repository：[来源](https://github.com/pubmedqa/pubmedqa) — 支持字段 `data.description`、`ground_truth.description`、`ground_truth.provenance`
- repository：[来源](https://github.com/pubmedqa/pubmedqa/blob/master/evaluation.py) — 支持字段 `evaluation.official_metrics`
- repository：[来源](https://github.com/gzxiong/MIRAGE) — 支持字段 `evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
