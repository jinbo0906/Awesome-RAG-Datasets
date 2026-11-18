<!-- Generated from catalog/datasets/ragcap-bench.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# RAGCap-Bench

[English](ragcap-bench.md)

通过选项任务诊断搜索代理的规划、证据提取、有依据推理和抗噪能力。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-18 |
| RAG 角色 | `auxiliary` |
| 主分类 | `text_rag` |
| 任务 | agentic_search, rag_robustness |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | not_provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

AACL 2026 长文用深度研究代理的中间执行输出构建可控选择题。发布包含带上下文或选项的问题以及六项子能力的提示。

发布规模：六份 CSV 共 255 题。发散／收敛规划 25／51，证据提取 69，基于证据推理 53，噪声拒答／可信度 37／20。
数据划分：一个按子能力划分的评测集合，分别报告不同提示设置。
格式：CSV with multiple-choice items and Python prompt definitions。

## 真值与评测

基于中间轨迹策划正确项，用错误引导和模板构造候选项。给定上下文下的选择题针对代理某一步的局部能力。

官方指标：exact_match, option_F1。

评测协议：在裸提示或带说明提示下提取选项，按任务计算选项集合完全匹配及宏平均 F1。WebThinker 的独立实验在 BrowseComp 等网页问答上报告下游 pass@1。

## 适用场景

- 在端到端运行前诊断具体中间任务
- 在匹配的给定上下文下比较模型能力

## 限制与注意事项

- 选项分数不能直接评估自由规划或工具执行
- 轨迹用于构造数据且未发布可索引的搜索库
- 仓库发布提示定义但没有单独评分器

## 获取方式与来源

- [官方资源](https://github.com/jingru-lin/RAGCap-Bench)
- [论文](https://aclanthology.org/2026.aacl-long.245/)
- [数据](https://github.com/jingru-lin/RAGCap-Bench/tree/99ed0d915cb2816a1182ef1a2a85a45d6fb6afde/data)
- paper：[来源](https://aclanthology.org/2026.aacl-long.245.pdf) — 支持字段 `summary`、`classification`、`data.description`、`ground_truth`、`evaluation.official_metrics`、`evaluation.protocol`、`use`
- repository：[来源](https://github.com/jingru-lin/RAGCap-Bench/tree/99ed0d915cb2816a1182ef1a2a85a45d6fb6afde/data) — 支持字段 `data.size`、`data.splits`、`data.format`、`access.data`
- repository：[来源](https://github.com/jingru-lin/RAGCap-Bench/tree/main/prompts) — 支持字段 `evaluation.protocol`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
