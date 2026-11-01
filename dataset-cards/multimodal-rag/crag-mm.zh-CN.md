<!-- Generated from catalog/datasets/crag-mm.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# CRAG-MM

[English](crag-mm.md)

面向可穿戴场景的图像单轮与多轮 RAG，提供模拟图像知识库、网页检索，以及拒答和会话层面评分。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-11-01 |
| RAG 角色 | `rag_native` |
| 主分类 | `multimodal_rag` |
| 任务 | visual_qa, conversational_qa, multimodal_retrieval, rag_robustness |
| 模态 | text, image, graph |
| 已发布真值标注层级 | answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | CC-BY-NC-4.0 stated by the author project; source images and retrieved material can retain separate rights. |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

KDD Cup 2025 挑战赛发布单轮与多轮问题、图像或来源 URL、参考答案及版本化图像和网页搜索索引。它不同于早期纯文本 CRAG，并非改名后的重复条目。

发布规模：论文 Table 3 报告 6,462 道单轮问题和 1,956 段多轮会话；这些总数不代表每个公开划分的大小。
数据划分：当前 Hugging Face 包提供 validation 与 public_test。单轮分别为 1,938、1,936 行，多轮分别为 586、587 段会话，核验日期为 2026-11-01。挑战赛私有数据另行保留。
格式：Hugging Face Parquet with session-level turns and answers, image fields and separately versioned search indices.。

## 真值与评测

标注者创建和检查答案，多轮种子还使用模型生成会话。发布金标准答案与问题、图像元数据，但模拟检索输出不是完整相关性标注，也不是最小跨来源证明链。

官方指标：accuracy, missing_rate, hallucination_rate, truthfulness_score, mean_multi_turn_conversation_score。

评测协议：固定各任务允许的图像知识库、网页来源及索引和 API 版本。正确、拒答、错误分别计为 +1、0、-1。多轮按会话平均，并在连续两轮失败后提前停止；README、论文与实现对拒答是否触发停止可能不同，须固定评分器版本。冻结图像及来源快照，不把 dynamism 标签视为实时知识更新。

## 适用场景

- 带拒答的图像与外部知识对话
- 在真实视觉退化下比较单来源与图像加网页 RAG

## 限制与注意事项

- 承办 KDD Cup 不等于引入该数据的预印本是 KDD 主会论文
- 部分图像仅提供 URL 而非内嵌文件
- 数据卡叙述可能落后于 public_test 发布和评分器行为；须固定版本
- 回答正确不能证明完整检索了跨来源证据

## 获取方式与来源

- [官方资源](https://github.com/facebookresearch/CRAG-MM)
- [论文](https://arxiv.org/abs/2510.26160)
- [数据](https://huggingface.co/crag-mm-2025)
- paper：[来源](https://arxiv.org/html/2510.26160) — 支持字段 `summary`、`data.size`、`ground_truth.provenance`、`evaluation.protocol`、`use.caveats`
- repository：[来源](https://github.com/facebookresearch/CRAG-MM) — 支持字段 `data.description`、`data.format`、`access.license`、`ground_truth.description`
- dataset_card：[来源](https://huggingface.co/datasets/crag-mm-2025/crag-mm-single-turn-public) — 支持字段 `data.splits`、`access.gated`、`use.caveats`
- dataset_card：[来源](https://huggingface.co/datasets/crag-mm-2025/crag-mm-multi-turn-public) — 支持字段 `data.splits`、`access.gated`
- repository：[来源](https://github.com/facebookresearch/CRAG-MM/blob/main/evaluation/README.md) — 支持字段 `evaluation.official_metrics`、`evaluation.protocol`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
