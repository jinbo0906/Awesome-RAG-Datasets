<!-- Generated from catalog/datasets/saferag.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# SafeRAG

[English](saferag.md)

中文 RAG 安全评测基准，包含银噪声、上下文间冲突、软广告和拒绝服务上下文。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | rag_robustness, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | sentence, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

仓库发布干净与攻击增强的知识库，以及分任务的问题和上下文文件。新闻问题与金标准上下文由模型辅助生成，经人工核验和修改。

格式：Text/JSON。

## 真值与评测

金标准上下文和正确或错误命题支持分任务评分。这些是选定的证据句，不是原始新闻所有有效切分方式的标注。

官方指标：f1_correct, f1_incorrect, f1_avg, attack_success_rate, retrieval_accuracy。

评测协议：固定攻击类型、注入阶段、攻击比例与检索窗口。区分索引、检索结果和过滤后上下文遭受的攻击，不将其混成干净检索分数。攻击失败率 AFR 等于 1-ASR，因此 AFR 越高、攻击成功率越低表示防御越好。

## 适用场景

- 评测注入上下文下的中文 RAG 鲁棒性
- 比较不同阶段的检索与过滤防御

## 限制与注意事项

- 按任务构造的攻击不代表无约束的真实攻击分布
- 金标准证据句不等于唯一的分块边界真值

## 获取方式与来源

- [官方资源](https://github.com/IAAR-Shanghai/SafeRAG)
- [论文](https://aclanthology.org/2025.acl-long.230/)
- [数据](https://github.com/IAAR-Shanghai/SafeRAG/tree/main/nctd_datasets)
- paper：[来源](https://aclanthology.org/2025.acl-long.230.pdf) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.official_metrics`
- repository：[来源](https://github.com/IAAR-Shanghai/SafeRAG) — 支持字段 `data.corpus`、`access.data`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
