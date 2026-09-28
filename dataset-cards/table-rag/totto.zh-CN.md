<!-- Generated from catalog/datasets/totto.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# ToTTo

[English](totto.md)

根据给定的维基百科表格与高亮单元格进行受控表格到文本生成。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-09-28 |
| RAG 角色 | `auxiliary` |
| 主分类 | `table_rag` |
| 任务 | table_to_text |
| 模态 | text, table |
| 已发布真值标注层级 | table_cell, answer |
| 证据标注来源 | human |
| 语料 / 查询 / 答案 | provided / not_provided / provided |
| 原始数据许可 | CC BY-SA 3.0 |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

官方训练版超过 12 万个样本。每个输入包含表格元数据、表格及高亮单元格坐标，目标是经编辑的 单句描述。开发集、私有测试参考答案和表头重叠子集分别采用不同协议。


## 真值与评测

高亮单元格标识直接给定的条件证据，经编辑句子是参考输出；原生任务并不要求从开放表格集合检索这些单元格。

官方指标：尚未确认。

评测协议：这属于给定证据的生成任务，不是检索 benchmark。若要评测 TableRAG，应在不暴露高亮单元格的前提下补充查询、表格语料、qrels 和留出集划分。

## 适用场景

- 依据选定单元格忠实生成
- 测试证据打包时是否保留表头上下文

## 限制与注意事项

- 没有原生检索查询或候选池
- 高亮单元格是输入而非系统找回的证据

## 获取方式与来源

- [官方资源](https://github.com/google-research-datasets/totto)
- repository：[来源](https://github.com/google-research-datasets/totto) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.protocol`、`access.license`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
