<!-- Generated from catalog/suites/longbench.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# LongBench (v1)

[English](longbench.md)

包含 21 项任务的双语长上下文套件，覆盖问答、摘要、少样本学习、合成检索与代码补全。

审查状态：`source_checked`。这是评测套件或协议，不是单一独立数据集。

## 已收录的组成数据集

- [narrativeqa](../dataset-cards/text-rag/narrativeqa.zh-CN.md)
- [qasper](../dataset-cards/text-rag/qasper.zh-CN.md)
- [hotpotqa](../dataset-cards/text-rag/hotpotqa.zh-CN.md)
- [2wikimultihopqa](../dataset-cards/text-rag/2wikimultihopqa.zh-CN.md)
- [musique](../dataset-cards/text-rag/musique.zh-CN.md)
- [triviaqa](../dataset-cards/text-rag/triviaqa.zh-CN.md)

## 协议与结果解释

本目录链接原始来源数据集，而非 LongBench 实际重处理的子集，仅构成部分组成项索引。须同时使用 THUDM/LongBench 测试文件与分任务指标，并区分按长度均衡的 LongBench-E 变体。基于检索的上下文压缩是已记录的对照设置，但套件没有通用的金标准分块边界。LongBench v2 是独立发布数据，单独收录为数据集。

## 官方来源

- [官方资源](https://github.com/THUDM/LongBench/tree/main/LongBench)
- [论文](https://aclanthology.org/2024.acl-long.172/)
- repository：[来源](https://github.com/THUDM/LongBench/tree/main/LongBench) — 支持字段 `summary`、`components`、`protocol`
