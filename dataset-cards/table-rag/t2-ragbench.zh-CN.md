<!-- Generated from catalog/datasets/t2-ragbench.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# T²-RAGBench

[English](t2-ragbench.md)

结合正文、表格与数值推理的金融文档 RAG benchmark。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `rag_native` |
| 主分类 | `table_rag` |
| 任务 | text_table_reasoning, table_qa |
| 模态 | text, table |
| 已发布真值标注层级 | answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

基于 FinQA、ConvFinQA 和 TAT-DQA 风格的金融文档问答构建；PDF 与结构化上下文需要明确所选版本。

发布规模：项目网站报告 23,088 个三元组，原论文摘要报告 32,908 个；核清前应视为不同发布版或计数范围。

## 真值与评测

发布了问题—上下文—答案三元组；精确的表格单元格证据覆盖须按具体发布版核查。

官方指标：answer_accuracy。

评测协议：比较系统时说明下载版本及来源文档转换方法。

## 适用场景

- 跨正文与表格的数值推理
- 金融文档检索测试

## 限制与注意事项

- 论文与实时项目页面的三元组总数不一致；未经核查不能跨版本合并结果

## 获取方式与来源

- [官方资源](https://t2ragbench.demo.hcds.uni-hamburg.de/)
- [论文](https://arxiv.org/abs/2506.12071)
- [数据](https://huggingface.co/datasets/G4KMU/t2-ragbench)
- official：[来源](https://t2ragbench.demo.hcds.uni-hamburg.de/) — 支持字段 `summary`、`data.description`、`data.size`
- paper：[来源](https://arxiv.org/abs/2506.12071) — 支持字段 `data.size`、`classification.tasks`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
