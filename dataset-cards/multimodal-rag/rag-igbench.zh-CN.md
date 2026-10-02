<!-- Generated from catalog/datasets/rag-igbench.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# RAG-IGBench

[English](rag-igbench.md)

根据检索到的社交平台内容，生成文字与图像交错回答的开放域 RAG benchmark。

| 字段 | 内容 |
|---|---|
| 目录审查状态 | `source_checked` |
| 来源核对日期 | 2026-10-02 |
| RAG 角色 | `rag_native` |
| 主分类 | `multimodal_rag` |
| 任务 | long_form_qa, attribution, multimodal_retrieval |
| 模态 | text, image |
| 已发布真值标注层级 | answer |
| 证据标注来源 | mixed |
| 语料 / 查询 / 答案 | provided / provided / provided |
| 原始数据许可 | unknown |

`source_checked` 表示所引用字段已与上游来源核对，不代表数据已下载或评测器已复现。

## 数据与构建方式

样本包含查询、已检索文档、图像 URL、类别、划分，以及带文档引用和图像索引的参考答案。发布版本主要固定每题检索上下文，没有开放完整的社交平台搜索语料。

发布规模：论文报告 6,057 个来源查询；双语 Hugging Face 数据包显示约 12,100 行。
数据划分：按每行 split 字段读取划分；Hugging Face 查看器将双语数据包放在名为 train 的容器中。
格式：Chinese JSONL and English JSON with retrieved text and external image URLs.。

## 真值与评测

模型辅助构建的参考答案经人工检查，保留选用的图像索引与文档引用。检索上下文属于候选输入，不是完整相关性真值或最小人工证据集合。

官方指标：ROUGE-1, modified_edit_distance, Kendall_score, CLIP_score, alignment_score。

评测协议：保留图像 ID 与顺序，使用作者的指标定义，并报告语言及行级划分。缓存获准使用的来源图像并记录失效 URL；翻译对不能算作独立来源问题。

## 适用场景

- 评测生成回答中的图像选择与位置
- 比较文本质量和图文一致性

## 限制与注意事项

- 论文附录 C 写明数据为 CC-BY-4.0，但当前 Hugging Face 卡标为 Apache-2.0
- 外部社交平台图像可能失效，且保留上游权利条款

## 获取方式与来源

- [官方资源](https://github.com/USTC-StarTeam/RAG-IGBench)
- [论文](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b0a4b3e384b4554e65a47ad1f6b0310a-Abstract-Datasets_and_Benchmarks_Track.html)
- [数据](https://huggingface.co/datasets/Muyi13/RAG-IGBench)
- paper：[来源](https://proceedings.neurips.cc/paper_files/paper/2025/file/b0a4b3e384b4554e65a47ad1f6b0310a-Paper-Datasets_and_Benchmarks_Track.pdf) — 支持字段 `summary`、`data.size`、`ground_truth.description`、`evaluation.official_metrics`、`use.caveats`
- repository：[来源](https://github.com/USTC-StarTeam/RAG-IGBench) — 支持字段 `data.description`、`data.format`、`evaluation.protocol`
- dataset_card：[来源](https://huggingface.co/datasets/Muyi13/RAG-IGBench) — 支持字段 `data.description`、`data.size`、`data.splits`、`use.caveats`

原始数据集的许可与访问条款由发布者确定；本目录条目不授予再分发权利。
