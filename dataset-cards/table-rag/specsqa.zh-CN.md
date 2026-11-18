<!-- Generated from catalog/datasets/specsqa.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# SpecsQA

[English](specsqa.md)

半结构化商品问答，测量完整枚举、多约束过滤与跨产品比较。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-18 |
| RAG 角色 | `rag_native` |
| 主分类 | `table_rag` |
| 任务 | table_qa, text_table_reasoning |
| 模态 | text, table |
| 已发布真值标注层级 | answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | CC-BY-ND-4.0 (data) |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

以 2025 年 11 月 Samsung 英国站快照为来源，包含商品规格表与说明文字。SpecsQA 提供问题类别、参考文本以及可用的产品列表，DualGraph 方法从快照构建文本和符号图。

发布规模：questions.json 实数 117 题。作者发布记录 2,162 个商品页面，覆盖 26 类商品。
数据划分：一份评测集，包含反向查询、多条件过滤和推理比较，单列仅含客观答案的列表子集成绩。
格式：Question JSON and split tar.xz raw HTML archive with parsing code。

## 真值与评测

问题经人工策划，参考材料含产品列表、来源提示与优选检索方式，部分自然语言答案由列表生成。缺少逐题穷尽的来源段落、单元格和图路径标注。

官方指标：factual_correctness_F1, list_match_precision_recall_F1, pairwise_judge_win_rate, input_output_tokens。

评测协议：在完整快照上运行检索或符号查询。List Match 通过模型从回答提取列表，对参考列表计算集合精确率、召回率和 F1。分别报告事实正确性、成对判分与索引和查询 token 开销。

## 适用场景

- 比较语义检索与精确结构化过滤
- 测试跨文档完整列举产品

## 限制与注意事项

- 结论适用于单一厂商快照
- 列表提取和判分依赖模型
- 已核对的版本提供系统代码和数据但独立评分器尚未确认

## 获取方式与来源

- [官方资源](https://github.com/corneliocristina/DualGraphRAG)
- [论文](https://aclanthology.org/2026.findings-emnlp.1319/)
- [数据](https://github.com/corneliocristina/DualGraphRAG/tree/main/SpecsQA)
- paper：[来源](https://aclanthology.org/2026.findings-emnlp.1319/) — 支持字段 `summary`、`classification`
- paper：[来源](https://arxiv.org/html/2605.27164) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`、`use`
- repository：[来源](https://raw.githubusercontent.com/corneliocristina/DualGraphRAG/main/SpecsQA/README.md) — 支持字段 `data`、`ground_truth.description`、`access.data`、`access.license`
- repository：[来源](https://github.com/corneliocristina/DualGraphRAG/blob/main/SpecsQA/questions.json) — 支持字段 `data.size`、`ground_truth`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
