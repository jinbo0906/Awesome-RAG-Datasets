<!-- Generated from catalog/datasets/kqa-pro.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# KQA Pro

[English](kqa-pro.md)

复杂知识库问答，在给定 Wikidata 子集上提供显式 KoPL 程序及 SPARQL 查询。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_convertible` |
| 主分类 | `graph_rag` |
| 任务 | graph_qa, graph_reasoning |
| 模态 | graph, text |
| 已发布真值标注层级 | graph_path, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

官方下载包含 kb.json 与训练、验证、测试文件；问题附有可执行 KoPL 与 SPARQL 监督。

发布规模：117,970 个问题。
格式：JSON。

## 真值与评测

组合程序与 SPARQL 定义知识库运算，问题由众包改写。程序可能包含比较或集合运算，不能一律表示成线性金标准路径。

官方指标：answer_accuracy。

评测协议：在已发布知识库与官方划分上执行或比较答案；报告推理技能类别，并注明是否提供金标准程序或主题实体。

## 适用场景

- 组合图推理与程序执行
- 按推理技能作诊断

## 限制与注意事项

- KoPL 或 SPARQL 监督不自动成为自然语言 GraphRAG 引用路径
- 保留已发布的 Wikidata 子集，不应静默替换成实时图谱

## 获取方式与来源

- [官方资源](https://github.com/shijx12/KQAPro_Baselines)
- [论文](https://aclanthology.org/2022.acl-long.422/)
- repository：[来源](https://github.com/shijx12/KQAPro_Baselines) — 支持字段 `data.description`、`data.format`
- paper：[来源](https://aclanthology.org/2022.acl-long.422.pdf) — 支持字段 `summary`、`classification`、`data.size`、`ground_truth`、`evaluation`、`use`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
