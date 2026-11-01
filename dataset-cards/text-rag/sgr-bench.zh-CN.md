<!-- Generated from catalog/datasets/sgr-bench.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# SGR-Bench (paper-linked release)

[English](sgr-bench.md)

通过来源发现、筛选与范围控制及完整结构化答案，评测依赖站内状态的网页检索。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-01 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | agentic_search, multi_hop_qa |
| 模态 | text, table |
| 已发布真值标注层级 | answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | external / provided / provided |
| 原始数据许可 | CC-BY-4.0 for released task data; external source websites retain their own terms. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

论文链接的 PKUAIWeb 发布将相同信息需求改写为目标式与约束引导式提示。记录包含输出格式、参考答案、状态与依赖元数据和复核量规；实际来源仍是实时专业网站。

发布规模：论文中共 100 个任务表述，即 50 对 goal/constraint，覆盖六类来源和 12 个公共数据生态。
数据划分：50 条 goal 与 50 条 constraint 英文记录，另有对齐中文逐任务文件。这些是成对评测表述，不是独立训练与测试划分。
格式：Hugging Face JSONL splits and per-task JSON files.。

## 真值与评测

LLM 辅助起草并经专家核验，形成有序表格参考答案、有限规范化规则和检索状态标注。发布不提供所有动作的完整金标准轨迹；表格形式的答案也不是来源单元格坐标。

官方指标：exact_match, Item-F1, Row-F1, P.O.A.。

评测协议：固定论文链接的 100 条发布版。向代理提供声明的任务提示与输出格式，说明是否暴露参考入口 URL。规范化不得补写缺失事实；按键对齐行，分别计算字段、完整行和共有行顺序。论文主表使用 Item-F1、Row-F1、P.O.A.，发布说明另含 exact match。轨迹根因审查与确定性答案指标分开。

## 适用场景

- 测试检索状态保持而非仅发现相关网站
- 诊断字段局部正确但结构化答案不完整的问题

## 限制与注意事项

- 成对提示共享答案，不能视为独立信息需求
- 公共网站变化与系统工具差异会影响复现
- 本条目固定原始论文链接版本，更大规模同名发布须另外核实来源承继和版本

## 获取方式与来源

- [官方资源](https://huggingface.co/datasets/PKUAIWeb/SGR-BENCH)
- [论文](https://arxiv.org/abs/2605.22219)
- [数据](https://huggingface.co/datasets/PKUAIWeb/SGR-BENCH)
- paper：[来源](https://arxiv.org/html/2605.22219) — 支持字段 `summary`、`classification.rag_role`、`data.size`、`ground_truth.description`、`ground_truth.provenance`、`evaluation.official_metrics`、`evaluation.protocol`
- dataset_card：[来源](https://huggingface.co/datasets/PKUAIWeb/SGR-BENCH) — 支持字段 `data.description`、`data.splits`、`data.format`、`evaluation.protocol`、`access.license`、`access.gated`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
