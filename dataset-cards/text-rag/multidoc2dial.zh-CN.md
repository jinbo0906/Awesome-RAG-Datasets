<!-- Generated from catalog/datasets/multidoc2dial.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# MultiDoc2Dial

[English](multidoc2dial.md)

随对话推进而切换依据文档的目标导向对话，包含检索与助手回复生成任务。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | conversational_qa, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | document, span, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

发布四个领域的文档和对话。每轮引用包含文档和片段标识，允许相关文档随对话的子目标变化。

数据划分：v1.0 数据说明列出训练、验证文件和占位测试文件；共享任务版本需要另行标识。

## 真值与评测

人工助手回复关联到包含 doc_id 和 id_sp 的证据引用。特定的不可回答或无关轮次具有空引用；precondition/solution 被说明为模糊标注。

官方指标：document_Recall@k, passage_Recall@k, exact_match, token_f1, BLEU。

评测协议：分别评测文档级与段落级检索，以及回复生成；改变分段方式时保留对话历史和文档、片段映射。

## 适用场景

- 相关文档变化的多轮检索
- 比较文档与段落证据覆盖率

## 限制与注意事项

- 占位测试文件不是有标签的评测集
- 发布者数据卡的许可元数据与许可正文不一致；使用前需确认适用许可

## 获取方式与来源

- [官方资源](https://doc2dial.github.io/multidoc2dial/)
- [论文](https://aclanthology.org/2021.emnlp-main.498/)
- [数据](https://github.com/IBM/multidoc2dial)
- official：[来源](https://doc2dial.github.io/multidoc2dial/) — 支持字段 `summary`、`data.description`
- official：[来源](https://doc2dial.github.io/multidoc2dial/data_readme.html) — 支持字段 `data.splits`、`ground_truth.description`、`ground_truth.levels`
- repository：[来源](https://github.com/IBM/multidoc2dial) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`
- dataset_card：[来源](https://huggingface.co/datasets/IBM/multidoc2dial) — 支持字段 `use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
