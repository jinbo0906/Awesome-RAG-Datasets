<!-- Generated from catalog/datasets/stark.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# STaRK (textual and relational retrieval)

[English](stark.md)

在半结构化知识库上检索实体，同时满足文本和关系条件。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-01 |
| RAG 角色 | `auxiliary` |
| 主分类 | `graph_rag` |
| 任务 | reasoning_retrieval, evidence_retrieval |
| 模态 | text, graph |
| 已发布真值标注层级 | document |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / not_provided |
| 原始数据许可 | CC-BY-4.0 for the HF query release; underlying knowledge-base sources retain their terms. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

NeurIPS 2024 数据与基准轨道发布，包含 Amazon、MAG、Prime 三个知识库。相关节点 ID 是检索目标，而非自然语言参考答案。ACL 2026 ARK 用它评测自适应词面搜索与图邻居探索。

发布规模：当前 HF synthesized-all 配置中 Amazon、MAG、Prime 分别有 9,100、13,323、11,204 行；人工查询集分别为 81、84、98 题，均不能当作纯测试集数量。
数据划分：使用加载器提供的 train/val/test 索引；test-0.1 与 human_generated_eval 是另行评测设置。HF synthesized_all_split 合并了原生划分。
格式：QA CSV, split indices and processed semi-structured knowledge bases through the stark-qa loader.。

## 真值与评测

正例实体或节点 ID 标识相关检索对象，此处 document 表示可寻址节点记录。合成查询与另行人工查询的来源不同；没有自由生成答案或最小支持图路径真值。

官方指标：Hit@1, Hit@5, Recall@20, MRR。

评测协议：对符合候选类型的节点排序，而非任意文本块，并保留全部正例节点。固定知识库、划分索引及候选类型。ARK 的免训练比较和教师轨迹蒸馏是不同实验，蒸馏轨迹不是 STaRK 原生真值。

## 适用场景

- 分开评测实体检索与答案生成
- 测试文本和关系约束下的预算化图遍历

## 限制与注意事项

- 不要与同名对话数据或代理方法混淆
- 全划分行数不能写成测试规模
- 来源节点相关性不是自然语言引用链真值

## 获取方式与来源

- [官方资源](https://github.com/snap-stanford/stark)
- [论文](https://papers.nips.cc/paper_files/paper/2024/hash/e607b1419e9ae7cd5cb5b5bb60c2ad5c-Abstract-Datasets_and_Benchmarks_Track.html)
- [数据](https://huggingface.co/datasets/snap-stanford/stark)
- paper：[来源](https://papers.nips.cc/paper_files/paper/2024/hash/e607b1419e9ae7cd5cb5b5bb60c2ad5c-Abstract-Datasets_and_Benchmarks_Track.html) — 支持字段 `summary`、`data.description`、`ground_truth.provenance`
- dataset_card：[来源](https://huggingface.co/datasets/snap-stanford/stark) — 支持字段 `data.format`、`access.license`、`ground_truth.description`
- dataset_card：[来源](https://datasets-server.huggingface.co/size?dataset=snap-stanford/stark) — 支持字段 `data.size`
- repository：[来源](https://github.com/snap-stanford/stark) — 支持字段 `data.splits`、`evaluation.protocol`
- paper：[来源](https://aclanthology.org/2026.acl-long.714.pdf) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`、`data.description`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
