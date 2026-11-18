<!-- Generated from catalog/suites/ragperf.yaml and catalog/i18n/zh-CN.yaml. Edit the sources, not this file. -->
# RAGPerf

[English](ragperf.md)

面向 RAG 吞吐、延迟、资源开销和回答质量的系统评测套件。公开静态文本协议已核查，并发更新实验以论文为准。

审查状态：`source_checked`。这是评测套件或协议，不是单一独立数据集。

## 已收录的组成数据集

本目录尚未单独收录该套件的组成数据集卡片。完整清单请查官方资源；这里为空不表示套件没有组成部分。

## 协议与结果解释

**公开静态文本负载。** 固定下方作者代码提交，按上游说明构建 Linux C++20 监控扩展，并安装 Python、向量库和模型依赖。先用 `python3 src/run_new.py --config config/lance_insert.yaml --msys-config config/monitor/example_config.yaml` 入库并建索引，再把 `--config` 换成 `config/lance_query.yaml` 执行检索与生成。两份配置均需设置本地库路径。入库配置默认从作者本机路径读取预计算向量 pickle。自行构建输入时，启用向量计算、关闭载入既有向量，并让入库与查询使用相同的编码器。

文本加载器使用 Wikimedia Wikipedia `20231101.en`，查询加载器默认取 `sentence-transformers/natural-questions` 的 `train` 前 512 条问答。外部资产沿用各自条款。这里记录的是公开负载预设，没有独立收录的组件变体或统一的固定问答下载包。固定数据提交、采样规模、模型、索引、硬件、批量大小和查询并发，报告吞吐、端到端与各阶段延迟、CPU/GPU 与内存开销。文本质量评分默认关闭，公开的 vLLM 评估器启用后使用 Ragas 的 `LLMContextRecall`、`FactualCorrectness` 和 `AnswerAccuracy`。记录评估器配置与版本，区分它们与论文的质量指标及基于相关性标注的检索召回。作者代码采用 Apache-2.0。本目录已核查入口、配置和数据来源，GPU 流水线尚未实跑。

**论文中的并发更新。** §5.5 与图 9 使用 LanceDB IVF-HNSW 和 Qwen-7B，在 60 分钟内各发出 50% 的查询与文档更新请求。实验比较均匀访问、Zipfian 访问和临时平面索引设置，报告随时间变化的查询延迟、上下文召回和准确率。已查公开版本只提供分开的入库和查询配置，混合负载精确配置、版本化更新问答、可回放轨迹或等效生成器仍未确认。自建更新回放需另行发布轨迹、标签和结果，见[选型指南](../guides/selecting-a-benchmark.zh-CN.md#evidence-and-update-protocols)。

## 官方来源

- [官方资源](https://github.com/platformxlab/RAGPerf/tree/49c9794895666d029a3c98a48afd872197d83b23)
- [论文](https://www.vldb.org/pvldb/vol19/p3689-li.pdf)
- paper：[来源](https://www.vldb.org/pvldb/vol19/p3689-li.pdf) — 支持字段 `name`、`summary`、`protocol`
- repository：[来源](https://github.com/platformxlab/RAGPerf/blob/49c9794895666d029a3c98a48afd872197d83b23/src/run_new.py) — 支持字段 `protocol`
- repository：[来源](https://github.com/platformxlab/RAGPerf/blob/49c9794895666d029a3c98a48afd872197d83b23/config/lance_insert.yaml) — 支持字段 `protocol`
- repository：[来源](https://github.com/platformxlab/RAGPerf/blob/49c9794895666d029a3c98a48afd872197d83b23/config/lance_query.yaml) — 支持字段 `protocol`
- repository：[来源](https://github.com/platformxlab/RAGPerf/blob/49c9794895666d029a3c98a48afd872197d83b23/src/datasetLoader/TextDatasetLoader.py) — 支持字段 `protocol`
- repository：[来源](https://github.com/platformxlab/RAGPerf/blob/49c9794895666d029a3c98a48afd872197d83b23/src/RAGRequest/TextsRAGRequest.py) — 支持字段 `protocol`
- repository：[来源](https://github.com/platformxlab/RAGPerf/blob/49c9794895666d029a3c98a48afd872197d83b23/src/evaluator/Ragasvllm.py) — 支持字段 `protocol`
- dataset_card：[来源](https://huggingface.co/datasets/wikimedia/wikipedia) — 支持字段 `protocol`
- dataset_card：[来源](https://huggingface.co/datasets/sentence-transformers/natural-questions) — 支持字段 `protocol`
- repository：[来源](https://github.com/platformxlab/RAGPerf/blob/49c9794895666d029a3c98a48afd872197d83b23/LICENSE) — 支持字段 `protocol`
