<!-- Generated from catalog/datasets/popqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# PopQA

[English](popqa.md)

以实体为中心的事实问答，附答案别名、Wikidata 标识与维基百科流行度信息。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `text_rag` |
| 任务 | single_hop_qa, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | distant |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

问题由实体关系构造；发布数据包括别名和流行度信息，检索实验所需的段落或检索结果另行获取。

发布规模：约 1.4 万个问答对。
数据划分：作者在 Hugging Face 上发布的是 test 划分；后续训练集或长尾子集属于单独的实验选择。

## 真值与评测

Wikidata 关系与客体别名定义可接受答案；实体标识和页面浏览量不提供正文支持段落标注。

官方指标：answer_accuracy。

评测协议：原始代码在生成文本包含可接受答案别名及其支持的大小写形式时判为正确，并非严格的归一化精确匹配。报告流行度筛选规则及外部语料快照。

## 适用场景

- 长尾事实知识
- 比较自适应检索与参数记忆回答

## 限制与注意事项

- 按流行度筛选的子集不等同于完整数据集
- 本条目不宣称原生数据具有段落相关性或支持片段标注

## 获取方式与来源

- [官方资源](https://github.com/AlexTMallen/adaptive-retrieval)
- [论文](https://aclanthology.org/2023.acl-long.546/)
- [数据](https://huggingface.co/datasets/akariasai/PopQA)
- repository：[来源](https://github.com/AlexTMallen/adaptive-retrieval) — 支持字段 `summary`、`data.description`、`data.size`、`ground_truth.description`
- dataset_card：[来源](https://huggingface.co/datasets/akariasai/PopQA) — 支持字段 `data.splits`、`ground_truth.alternatives`
- repository：[来源](https://github.com/AlexTMallen/adaptive-retrieval/blob/main/run_model.py) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
