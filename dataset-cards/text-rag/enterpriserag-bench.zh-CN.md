<!-- Generated from catalog/datasets/enterpriserag-bench.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# EnterpriseRAG-Bench

[English](enterpriserag-bench.md)

在密集干扰、冲突记录、穷尽式问题与缺失信息条件下评测合成企业内部检索及问答。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-01 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | multi_hop_qa, evidence_retrieval, rag_robustness |
| 模态 | text |
| 已发布真值标注层级 | document, answer |
| 证据标注来源 | synthetic |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | MIT (HF dataset card); record the corpus release separately from the code version. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

2026-05-05 公开预印本，模拟一家公司的九种来源，包括 Slack、邮件、工单和 Wiki。作者数据卡提供问题、expected_doc_ids、gold_answer 和 answer_facts，文档另行发布。这是合成企业数据，不是真实内部通信披露。

发布规模：超过五十万份文档、十类共 500 个核心问题；另有 100 个依赖元数据的问题，不计入核心榜单。
数据划分：HF questions/test 与 documents/test 是两个配置，不是互斥的训练与测试语料；须固定具体发布版本及真值集合。
格式：HF Parquet configurations, JSONL questions and released document archives.。

## 真值与评测

在人工参与的语料框架上，模型生成问题、答案、原子事实与汇集文档 ID。High-Level 和 Info-Not-Found 类没有金标准文档 ID；其他集合也被作者视为可修订，不是人工穷尽相关性或逐事实来源引用映射。

官方指标：Overall_Score, Answer_Correctness, Answer_Completeness, Document_Recall, Invalid_Extra_Docs。

评测协议：提交 question_id、answer 和 document_ids。Overall Score 是逐题二元正确性乘完整性的平均；Invalid Extra Docs 越低越好。保留缺失答案、高层问题的处理方式，固定评分模型和是否启用真值修正。修正后的标签与初始榜单标签应分版本报告，不能当同一固定测试集。

## 适用场景

- 测试噪声企业来源中的一致跨文档检索
- 研究大语料下的信息缺失与真值不完整

## 限制与注意事项

- 合成数据的逼真性不等于私有生产数据验证
- 原子答案事实不是最小来源片段
- 真值修正及评分模型变更影响得分可比性

## 获取方式与来源

- [官方资源](https://github.com/onyx-dot-app/EnterpriseRAG-Bench)
- [论文](https://arxiv.org/abs/2605.05253)
- [数据](https://huggingface.co/datasets/onyx-dot-app/EnterpriseRAG-Bench)
- paper：[来源](https://arxiv.org/abs/2605.05253) — 支持字段 `summary`、`data.description`、`data.size`
- dataset_card：[来源](https://huggingface.co/datasets/onyx-dot-app/EnterpriseRAG-Bench) — 支持字段 `data.splits`、`data.format`、`access.license`、`evaluation.official_metrics`、`evaluation.protocol`
- repository：[来源](https://github.com/onyx-dot-app/EnterpriseRAG-Bench) — 支持字段 `data.size`、`ground_truth.description`
- paper：[来源](https://arxiv.org/html/2605.05253) — 支持字段 `ground_truth.provenance`、`ground_truth.description`、`evaluation.protocol`
- repository：[来源](https://github.com/onyx-dot-app/EnterpriseRAG-Bench/blob/main/answer_evaluation/README.md) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
