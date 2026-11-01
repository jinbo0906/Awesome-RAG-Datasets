<!-- Generated from catalog/datasets/wikirecentchanges.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# WikiRecentChanges

[English](wikirecentchanges.md)

提供稳定与已更新事实、真实与反事实段落，诊断时间条件下的上下文与参数记忆冲突。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-01 |
| RAG 角色 | `auxiliary` |
| 主分类 | `text_rag` |
| 任务 | time_sensitive_qa, rag_robustness |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

作者仓库发布 mutable 与 stable 最终 CSV，包含问题、答案、反事实答案及真实/反事实上下文段落。事实种子来自 Wikidata，但原生实验直接提供段落，不搜索开放知识图谱。

发布规模：发布的 mutable_final.csv 有 2,330 行，stable_final.csv 有 2,381 行，共 4,711 个最终样本；这与过滤前种子事实数量不同。
数据划分：事实在 2025 年发生变化的 mutable 与稳定事实 stable 是诊断分层，不是训练/测试划分。
格式：CSV plus dataset-reconstruction and evaluation scripts。

## 真值与评测

Wikidata 事实答案配有模型生成的反事实内容与段落。真实/反事实输入和稳定/更新事实支持受控冲突实验；本任务没有发布原生开放语料相关性标注或图证据路径真值。

官方指标：OpenEval, answer_match, context_acceptance_rate, temporal_reasoning_detection。

评测协议：将事实类型与无上下文、真实上下文、反事实上下文交叉，保留模型知识截止点和日期提示。分别比较事实答案、反事实答案及闭卷答案。OpenEval 使用模型评判，Match 是宽松答案匹配；论文的上下文接受率是相对指定基线的边际变化，不是原始答案准确率。

## 适用场景

- 分开考察时间冲突识别与最终正确决策
- 测试模型对生成证据和参数记忆的依赖

## 限制与注意事项

- 对知识截止日期更新的模型，应重新评估 2025 年变化目标是否适用
- 给定合成段落不评测检索或持续索引更新
- README 的 sample.csv 示例不对应实际发布的最终 CSV 文件名
- 作者仓库中尚未确认明确的数据集许可

## 获取方式与来源

- [官方资源](https://github.com/jwallat/knowledge-conflicts-mutability)
- [论文](https://aclanthology.org/2026.findings-acl.103/)
- [数据](https://github.com/jwallat/knowledge-conflicts-mutability/tree/main/data/recent_changes)
- paper：[来源](https://aclanthology.org/2026.findings-acl.103.pdf) — 支持字段 `summary`、`classification`、`ground_truth`、`evaluation.official_metrics`、`evaluation.protocol`、`use`
- repository：[来源](https://github.com/jwallat/knowledge-conflicts-mutability) — 支持字段 `data.description`、`data.splits`、`data.format`、`data.corpus`、`access.license`、`access.gated`、`evaluation.evaluator`、`use.caveats`
- repository：[来源](https://raw.githubusercontent.com/jwallat/knowledge-conflicts-mutability/main/data/recent_changes/mutable_final.csv) — 支持字段 `data.size`、`data.queries`、`data.answers`
- repository：[来源](https://raw.githubusercontent.com/jwallat/knowledge-conflicts-mutability/main/data/recent_changes/stable_final.csv) — 支持字段 `data.size`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
