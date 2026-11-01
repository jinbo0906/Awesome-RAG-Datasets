<!-- Generated from catalog/datasets/ragability.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# Ragability Corpus

[English](ragability.md)

用人工构造的虚构实体上下文，分开考察来源间矛盾识别与适当拒答。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-01 |
| RAG 角色 | `auxiliary` |
| 主分类 | `text_rag` |
| 任务 | rag_robustness, time_sensitive_qa |
| 模态 | text |
| 已发布真值标注层级 | answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | CC-BY-SA-4.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

小规模种子语料提供四种上下文变体、内容问题、依赖各上下文的长短答案及推理类型标签。作者为选定 WikiContradict 案例人工替换虚构实体、日期与数值。配套 Ragability 库构造受控提示组合，它是独立工具，不应再统计为一个数据集。

发布规模：由 43 组来源上下文对构造 53 行公开 CSV 种子；论文实验为每个被测模型生成 1,060 个测试提示。
数据划分：一个在 Hugging Face 上命名为 train 的种子表；生成提示组合不是独立的训练/测试划分。
格式：CSV seed data plus a Python prompt-generation and checking library。

## 真值与评测

人工构造的上下文与答案定义可回答、矛盾和信息不足条件；矛盾或信息不足组合可能要求拒答。上下文片段是给定输入，不是更大语料库的相关性标注或最优切分标签。

官方指标：contradiction_identification, correct_answer_all, refusal_not_answerable, correct_answer_answerable。

评测协议：生成指定上下文组合并保留提示线索、可回答性、推理类型和上下文顺序。论文每个种子使用 20 个提示，对双上下文情况交换顺序，更多上下文时不枚举全部排列。语义正确性和拒答评分依赖 checker 模型，需固定其身份，不能将模型一致性当人工真值。

## 适用场景

- 分开考察冲突识别、内容回答与拒答
- 在不依赖真实世界实体记忆的条件下进行受控测试

## 限制与注意事项

- 少量构造种子不代表真实检索分布
- 生成提示数不能作为独立问题或文档数报告
- 矛盾警告可能改善有矛盾场景而损害无矛盾场景
- 给定上下文不测检索效果

## 获取方式与来源

- [官方资源](https://huggingface.co/datasets/ofai/RagabilityCorpus)
- [论文](https://aclanthology.org/2026.lrec-1.182/)
- [数据](https://huggingface.co/datasets/ofai/RagabilityCorpus)
- paper：[来源](https://aclanthology.org/2026.lrec-1.182.pdf) — 支持字段 `summary`、`classification`、`data.description`、`data.size`、`ground_truth`、`evaluation.official_metrics`、`evaluation.protocol`、`use`
- dataset_card：[来源](https://huggingface.co/datasets/ofai/RagabilityCorpus) — 支持字段 `data.corpus`、`data.queries`、`data.answers`、`data.splits`、`data.format`、`data.size`、`access.license`、`access.gated`
- repository：[来源](https://github.com/OFAI/python-ragability) — 支持字段 `evaluation.evaluator`、`data.description`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
