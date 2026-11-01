<!-- Generated from catalog/datasets/browsecomp-plus.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# BrowseComp-Plus

[English](browsecomp-plus.md)

通过固定语料分别评测检索质量、证据收集、答案正确性和搜索开销的深度搜索基准。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-01 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | agentic_search, multi_hop_qa, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | document, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | MIT for the official Hugging Face release; original web-source terms may also apply. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

这一独立发布的 BrowseComp 改造提供冻结网页语料、人工核验的推理证据文档、包含最终答案的 gold 文档及挖掘的困难负例。查询与标注字段经过混淆，官方仓库提供还原、检索和代理评测工具。

发布规模：官方 Hugging Face 发布含 830 个测试查询和 100,195 篇语料文档。
数据划分：查询与相关性标注使用 test 划分；独立语料库中名为 train 的划分是检索候选池，不是代理训练监督。
格式：Hugging Face Parquet and author-provided JSONL/TSV conversion.。

## 真值与评测

evidence_docs 支持推理链，gold_docs 在语义上包含最终答案。模型辅助收集后由人工核验；两种标注不能互换，文档相关性也不能确定最优分块边界。

官方指标：accuracy, evidence_recall, search_calls, calibration_error, Recall@5, Recall@100, Recall@1000, nDCG@10。

评测协议：固定语料及指定 evidence/gold 相关性标注，分别报告代理答案正确率、跨调用证据覆盖、调用次数和校准误差，以及独立检索器指标。项目使用 GPT-4.1 判答案；须固定判分模型、搜索接口和预算，不混用实时网页 BrowseComp 分数。

## 适用场景

- 区分检索器与代理各自的贡献
- 比较迭代获取证据与单次检索

## 限制与注意事项

- 只改造了部分 BrowseComp 问题，分数不是原生 BrowseComp 分数
- 混淆用于降低泄漏而非访问控制，不能向被测代理暴露标签
- 相关文档比最小完整证据片段或唯一推理路径更粗

## 获取方式与来源

- [官方资源](https://texttron.github.io/BrowseComp-Plus/)
- [论文](https://aclanthology.org/2026.acl-long.1023/)
- [数据](https://huggingface.co/datasets/Tevatron/browsecomp-plus)
- paper：[来源](https://aclanthology.org/2026.acl-long.1023/) — 支持字段 `name`、`summary`、`classification.rag_role`、`use.caveats`
- dataset_card：[来源](https://huggingface.co/datasets/Tevatron/browsecomp-plus) — 支持字段 `data.description`、`data.size`、`data.splits`、`data.format`、`ground_truth.description`、`ground_truth.provenance`、`access.license`
- official：[来源](https://texttron.github.io/BrowseComp-Plus/) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`、`ground_truth.description`
- repository：[来源](https://github.com/texttron/BrowseComp-Plus) — 支持字段 `data.description`、`data.splits`、`evaluation.protocol`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
