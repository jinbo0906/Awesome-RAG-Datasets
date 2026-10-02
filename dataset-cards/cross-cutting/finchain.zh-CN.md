<!-- Generated from catalog/datasets/finchain.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# FinChain

[English](finchain.md)

辅助财务推理基准，提供可执行符号模板与可核验的中间计算。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `auxiliary` |
| 主分类 | `cross_cutting` |
| 任务 | single_hop_qa |
| 模态 | text, equation |
| 已发布真值标注层级 | answer |
| 证据标注来源 | synthetic |
| 语料 / 查询 / 答案 | not_provided / provided / provided |
| 原始数据许可 | Apache-2.0 for original code and executable templates |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

已发布 Python 模板生成财务问题、中间金标准数值与可执行轨迹；不提供文档检索语料或相关性标注。

发布规模：12 个领域、58 个主题；每主题五个模板、每模板十个种子，构成论文中的 2,900 个评测样本。
格式：Executable Python templates and generated problem/trace records。

## 真值与评测

可执行符号模板定义最终数值与中间计算；它们是推理目标，不是来源文档引用。

官方指标：chaineval, final_answer_correctness, rouge_2, rouge_l, bertscore。

评测协议：固定模板、种子与步骤提取方式；论文采用结合最终答案正确性的 DTWNormGate，数值容差为 0.05。本条目用于推理组件测试。

## 适用场景

- 验证检索后的数值推理
- 区分最终答案正确性与中间计算质量

## 限制与注意事项

- 没有原生 RAG 检索任务发布
- 新模板种子本身不能消除模型对问题模式的训练接触

## 获取方式与来源

- [官方资源](https://github.com/mbzuai-nlp/finchain)
- [论文](https://aclanthology.org/2026.acl-long.662/)
- [数据](https://github.com/mbzuai-nlp/finchain/tree/main/data/templates)
- repository：[来源](https://github.com/mbzuai-nlp/finchain) — 支持字段 `summary`、`classification`、`data`、`ground_truth`、`access.license`、`evaluation.evaluator`、`use`
- paper：[来源](https://aclanthology.org/2026.acl-long.662.pdf) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`、`data.size`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
