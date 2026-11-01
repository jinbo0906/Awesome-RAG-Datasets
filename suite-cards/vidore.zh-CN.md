<!-- Generated from catalog/suites/vidore.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# ViDoRe

[English](vidore.md)

版本化视觉文档评测套件系列；v3 在相关性检索外增加证据定位与参考答案评测。

审查状态：`source_checked`。这是评测套件或协议，不是单一独立数据集。

## 已收录的组成数据集

本目录尚未单独收录该套件的组成数据集卡片。完整清单请查官方资源；这里为空不表示套件没有组成部分。

## 协议与结果解释

v1/v2 检索设置应与 v3 分开。2026 年一月 v3 论文报告十个数据集、约 26,000 页和 3,099 个经人工核验的基础查询，每题有六种语言，附相关性、边界框定位和参考答案标注。其中八个数据集公开、两个保留为私有，不能称十个组件全部可下载。当前单检索器的 v1–v3 评测使用 MTEB；作者仓库现维护 v3 复杂检索流水线评测，包括 OCR、分块和重排、nDCG@10、召回及可选索引和查询成本。该检索分数不同于论文的模型判定答案正确率或证据定位评分。记录语言、版本、公开或私有子集及评分器。各组件尚未逐一建立独立变体卡片；须查看各数据集条款，不把代码的 MIT 许可套用到来源文档。

## 官方来源

- [官方资源](https://github.com/illuin-tech/vidore-benchmark)
- [论文](https://arxiv.org/abs/2601.08620)
- repository：[来源](https://github.com/illuin-tech/vidore-benchmark) — 支持字段 `summary`、`protocol`
- paper：[来源](https://arxiv.org/html/2601.08620) — 支持字段 `summary`、`protocol`
- official：[来源](https://huggingface.co/collections/vidore/vidore-benchmark-v3) — 支持字段 `protocol`
