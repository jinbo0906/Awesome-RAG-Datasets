<!-- Generated from catalog/suites/m4-rag.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# M4-RAG

[English](m4-rag.md)

基于 CVQA、WorldCuisines 及独立维基百科语料池的多语言、多文化检索增强视觉问答套件。

审查状态：`source_checked`。这是评测套件或协议，不是单一独立数据集。

## 已收录的组成数据集

本目录尚未单独收录该套件的组成数据集卡片。完整清单请查官方资源；这里为空不表示套件没有组成部分。

## 协议与结果解释

CVPR 2026 论文基于 CVQA 和 WorldCuisines 提出 RAG 评测协议，报告超过八万组图像问题、42 种语言、56 种方言或语域及 189 个国家。这些转换组件尚未作为独立变体卡片收录。问答和图像须从两个上游数据集获取，而非只包含语料的 M4-RAG Hugging Face 仓库。当前元数据分别列出 306,794 条 CVQA 领域、223,468 条 WorldCuisines 领域维基百科文章；名为 train 的划分是来源语料，不是有监督问答训练集。使用各自评测脚本及指定的选择题、开放式答案评分，报告语言、提示、检索和金标准描述条件。答案字符串是否出现在检索文本块中只是诊断量，不是独立人工相关性真值。语料数据卡标为 CC-BY-SA-4.0；问答、图像、代码适用各自条款。不能将套件称为新建的原生问答集，也不应声称有完整跨语言相关性判断。

## 官方来源

- [官方资源](https://github.com/davidanugraha/M4-RAG)
- [论文](https://openaccess.thecvf.com/content/CVPR2026/html/Anugraha_M4-RAG_A_Massive-Scale_Multilingual_Multi-Cultural_Multimodal_RAG_CVPR_2026_paper.html)
- paper：[来源](https://openaccess.thecvf.com/content/CVPR2026/html/Anugraha_M4-RAG_A_Massive-Scale_Multilingual_Multi-Cultural_Multimodal_RAG_CVPR_2026_paper.html) — 支持字段 `name`、`summary`、`protocol`
- repository：[来源](https://github.com/davidanugraha/M4-RAG) — 支持字段 `protocol`
- dataset_card：[来源](https://huggingface.co/datasets/davidanugraha/M4-RAG) — 支持字段 `protocol`
- repository：[来源](https://github.com/davidanugraha/M4-RAG/blob/main/src/evaluation/eval_cvqa.py) — 支持字段 `protocol`
