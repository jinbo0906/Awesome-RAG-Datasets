<!-- Generated from catalog/datasets/mmrag.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# mmRAG (text, tables and knowledge graphs)

[English](mmrag.md)

将文本、表格和知识图谱统一表示为可检索文档，发布问题与相关性标注的集成 RAG 数据。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_native` |
| 主分类 | `text_rag` |
| 任务 | evidence_retrieval, single_hop_qa, graph_qa, table_qa |
| 模态 | text, table, graph |
| 已发布真值标注层级 | document, answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown; source datasets retain their own terms |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

从 NQ、TriviaQA、OTT-QA、TAT-QA、ComplexWebQuestions 和 WebQSP 派生问题与检索记录。表格和图谱事实转成文档后切为不重叠的 512-token 块，不是 M2RAG 一类的图像与文本基准。

格式：JSON。

## 真值与评测

对候选池中的 512-token 块由模型标注 0/1/2 级相关性，再派生数据集路由标签。目录的 document 层级在此指可寻址的检索记录，不是原始整文档相关性。标签不监督图路径或替代分块边界。

官方指标：ndcg_at_k, map_at_k, hits_at_k。

评测协议：同时使用发布的 512-token 块、相关性判断和划分。重新分块后必须重映射证据或重新标注，不能沿用旧块 ID。检索脚本报告 1/3/5 截断处的 NDCG、MAP 和 Hits，路由与回答生成单独报告。重建时固定模型标注和评分配置。

## 适用场景

- 在文本、表格和图谱来源间进行查询路由
- 比较异构表示的组件级相关性

## 限制与注意事项

- 模型判断与不完整候选池不是穷尽的人工证据真值
- 图谱和表格被序列化，原生协议不评测图像布局推理

## 获取方式与来源

- [官方资源](https://github.com/nju-websoft/mmRAG)
- [论文](https://arxiv.org/abs/2505.11180)
- [数据](https://huggingface.co/datasets/Askio/mmrag_benchmark)
- paper：[来源](https://arxiv.org/html/2505.11180v1) — 支持字段 `data.description`、`ground_truth.description`、`evaluation.protocol`
- repository：[来源](https://github.com/nju-websoft/mmRAG) — 支持字段 `summary`、`data.description`、`ground_truth.description`、`evaluation.protocol`、`access.data`
- repository：[来源](https://github.com/nju-websoft/mmRAG/blob/main/mmrag_experiments/eval.py) — 支持字段 `evaluation.official_metrics`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
