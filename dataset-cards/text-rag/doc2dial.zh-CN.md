<!-- Generated from catalog/datasets/doc2dial.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# Doc2Dial

[English](doc2dial.md)

以目标为导向的信息寻求对话，提供文档片段依据与助手回复标注。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `text_rag` |
| 任务 | conversational_qa, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | document, span, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

文档文件提供正文、HTML、片段偏移与章节结构。对话文件将用户和助手轮次链接到文档及证据引用；后续版本与原论文版本不同。


## 真值与评测

人工写出的对话通过片段标识关联到文档。依据片段、条件或解决方案标注以及上下文标题的作用不同；来源结构片段不是通用的最佳分块边界。

官方指标：span_exact_match, span_token_f1, mapped_span_exact_match, BLEU-1, BLEU-2, BLEU-3, BLEU-4。

评测协议：分别报告文档检索、依据预测和回复生成。保留片段偏移、对话历史、数据版本和是否包含无关轮次等设置；原始回复任务直接提供文档上下文。

## 适用场景

- 有文档依据的服务对话
- 跟踪上下文追问中的片段证据

## 限制与注意事项

- 版本和无关轮次设置会改变评测
- 在给定文档上生成回复不能衡量开放语料检索

## 获取方式与来源

- [官方资源](https://doc2dial.github.io/data.html)
- [论文](https://aclanthology.org/2020.emnlp-main.652/)
- official：[来源](https://doc2dial.github.io/data.html) — 支持字段 `summary`、`data.description`、`ground_truth.description`
- official：[来源](https://doc2dial.github.io/README.html) — 支持字段 `ground_truth.levels`、`evaluation.protocol`
- paper：[来源](https://aclanthology.org/2020.emnlp-main.652.pdf) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
