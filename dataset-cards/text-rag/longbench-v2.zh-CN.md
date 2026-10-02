<!-- Generated from catalog/datasets/longbench-v2.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# LongBench v2

[English](longbench-v2.md)

人工编写的选择题基准，评测模型对真实长文档、对话、代码仓库和结构化数据的深层推理。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `text_rag` |
| 任务 | long_context_qa |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | MIT |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

每条记录给出长上下文、四个选项与正确选项。原生任务是长上下文理解，发布的代码也支持用检索前 N 个片段进行 RAG 对照。

发布规模：六类任务共 503 个问题，上下文长度为 8k 至 2M 单词。
数据划分：Hugging Face 中名为 train 的划分实际装载评测发布数据，不能将其当作排行榜评测的训练集。
格式：JSON。

## 真值与评测

答案标注为 A/B/C/D。发布格式未提供按问题标注的支持片段、相关性判断或最优切分边界。

官方指标：accuracy。

评测协议：区分直接回答、思维链、无上下文与 RAG 设置。按难度、任务和长度分组报告；RAG 实验需注明 top-N、分块和检索配置。

## 适用场景

- 比较长上下文与检索方案
- 超越抽取式查找的答案质量压力测试

## 限制与注意事项

- 没有支持片段级真值用于分块监督
- 选择题准确率可能体现推理或记忆而非检索成功

## 获取方式与来源

- [官方资源](https://longbench2.github.io/)
- [论文](https://aclanthology.org/2025.acl-long.183/)
- [数据](https://huggingface.co/datasets/zai-org/LongBench-v2)
- paper：[来源](https://aclanthology.org/2025.acl-long.183/) — 支持字段 `summary`、`data.size`、`ground_truth.provenance`
- repository：[来源](https://github.com/THUDM/LongBench) — 支持字段 `data.description`、`data.splits`、`ground_truth.description`、`evaluation.protocol`
- dataset_card：[来源](https://huggingface.co/datasets/zai-org/LongBench-v2) — 支持字段 `access.license`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
