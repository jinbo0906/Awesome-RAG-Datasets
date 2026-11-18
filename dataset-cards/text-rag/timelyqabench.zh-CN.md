<!-- Generated from catalog/datasets/timelyqabench.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# TimelyQABench

[English](timelyqabench.md)

韩语时效问答与文档相关性标注，测试在保留大量相同文字的修订中选择适用政策。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-18 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | time_sensitive_qa, evidence_retrieval |
| 模态 | text |
| 已发布真值标注层级 | document, answer |
| 证据标注来源 | synthetic |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

TimelyRAG 预印本发布四个合成韩语领域，含高度重叠的文件版本与语义相似但时间无效的负例。查询和文档时间决定适用版本。

发布规模：四个领域各 3,000 个问答和 30,000 个语料文档，合计 12,000 个问答和 120,000 个文档。
数据划分：四个领域评测集，每题在对应领域的聚合语料中检索。
格式：ZIP with domain JSONL files containing QA and documents linked by global IDs。

## 真值与评测

标注文档 ID 指向在查询时间条件下支持答案的文档版本。JSONL 保存插入时间，事件时间通过文字表达，未设独立事件时间字段。

官方指标：nDCG@10, MAP@10, Recall@10, Hit@10, judged_win_tie_loss。

评测协议：在各领域用发布的相关性标注评估排序。论文固定生成器，由 GPT-5 成对判断答案正确性及时间有效性。说明检索时可取得的时间字段，将金标准时间过滤作为上界。

## 适用场景

- 从近重复政策中检索适用版本
- 比较语义检索与时效重排

## 限制与注意事项

- 政策与问答为合成数据
- 固定版本库的排序不测更新传播时延
- 文档 ID 不提供条款级坐标

## 获取方式与来源

- [官方资源](https://github.com/kaist-dmlab/TimelyRAG)
- [论文](https://arxiv.org/abs/2609.11572)
- [数据](https://github.com/kaist-dmlab/TimelyRAG/blob/5213a0c1743f23fd52a258005c3887aaf7e8cd0f/datasets.zip)
- paper：[来源](https://arxiv.org/html/2609.11572) — 支持字段 `summary`、`classification`、`data.description`、`ground_truth`、`evaluation`、`use`
- repository：[来源](https://github.com/kaist-dmlab/TimelyRAG/blob/5213a0c1743f23fd52a258005c3887aaf7e8cd0f/datasets.zip) — 支持字段 `data.size`、`data.splits`、`data.format`、`access.data`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
