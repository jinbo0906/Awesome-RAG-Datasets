# 如何选择 benchmark

[English](selecting-a-benchmark.md)

先明确要解决的失败方式，再判断上游**实际发布的标注**能否为它打分。从[目录](../README.zh-CN.md#数据集)进入的卡片记录了访问方式、标注、协议和限制。下表是**候选短名单**，不是排行榜，也不意味着这些数据集的许可、划分或标注等价。

| 研究问题 | 优先查看 | 需要评测什么 | 主要限制 |
|---|---|---|---|
| 分块边界与多跳证据完整性 | [HiCBench](../dataset-cards/text-rag/hicbench.zh-CN.md)、[HotpotQA](../dataset-cards/text-rag/hotpotqa.zh-CN.md)、[2WikiMultiHopQA](../dataset-cards/text-rag/2wikimultihopqa.zh-CN.md)、[MuSiQue](../dataset-cards/text-rag/musique.zh-CN.md) | 基于来源坐标的证据覆盖与回答质量 | 支持句不是唯一最优的分块 |
| 长文档证据保留 | [QASPER](../dataset-cards/text-rag/qasper.zh-CN.md)、[CLAP NQ](../dataset-cards/text-rag/clapnq.zh-CN.md)、[QuALITY](../dataset-cards/text-rag/quality.zh-CN.md) | 固定 token 预算下的证据召回 | QuALITY 没有原生的最小证据片段标注 |
| 有依据的回答与引用 | [ALCE](../suite-cards/alce.zh-CN.md)、[RAGBench](../dataset-cards/text-rag/ragbench.zh-CN.md)、[MAVIS](../dataset-cards/multimodal-rag/mavis.zh-CN.md) | 回答正确性、主张与引用的支持程度、证据覆盖 | 已检索上下文及来源语料的变体不同 |
| 视觉页面和版面检索 | [MMDocIR](../dataset-cards/multimodal-rag/mmdocir.zh-CN.md)、[SlideVQA](../dataset-cards/multimodal-rag/slidevqa.zh-CN.md)、[ViDoRe](../suite-cards/vidore.zh-CN.md) | 页面 Recall@K；有标注时的区域覆盖 | 版面框不一定是针对问题的证据 |
| 跨页、跨模态证据 | [MMDocRAG](../dataset-cards/multimodal-rag/mmdocrag.zh-CN.md)、[XL-DocBench](../dataset-cards/multimodal-rag/xl-docbench.zh-CN.md)、[MAVIS](../dataset-cards/multimodal-rag/mavis.zh-CN.md)、[MultiModalQA](../dataset-cards/multimodal-rag/multimodalqa.zh-CN.md) | 完整证据集合或证据链，以及回答和引用 | 各发布版本的标注粒度不同 |
| 开放表格加文本 | [OTT-QA](../dataset-cards/table-rag/ott-qa.zh-CN.md)、[HybridQA](../dataset-cards/table-rag/hybridqa.zh-CN.md)、[TAT-QA](../dataset-cards/table-rag/tat-qa.zh-CN.md) | 表格/段落检索及后续问答 | HybridQA 和 TAT-QA 提供上下文；OTT-QA 要求开放检索 |
| 图证据检索与推理 | [GraphRAG-Bench](../dataset-cards/graph-rag/graphrag-bench.zh-CN.md)、[GrailQA](../dataset-cards/graph-rag/grailqa.zh-CN.md)、[WebQuestionsSP](../dataset-cards/graph-rag/webqsp.zh-CN.md) | 图证据、路径或逻辑形式的正确性，以及答案 | 知识库问答逻辑形式不等于 GraphRAG 引用图 |
| 仅检索或鲁棒性对照 | [BEIR](../suite-cards/beir.zh-CN.md)、[BRIGHT](../dataset-cards/text-rag/bright.zh-CN.md)、[M-BEIR](../suite-cards/m-beir.zh-CN.md) | 官方相关性标注与排序指标 | 没有内置的回答生成真值 |

## 选型检查清单

1. 确定目标单位：来源文档、页面、句子、单元格、区域、图路径、原子事实，还是最终答案。
2. 核查**已发布字段**能否识别该单位。不能仅凭解释把页面标签提升为单元格标签。
3. 选择检索范围：固定给定上下文、单文档、多文档、开放语料或随时间变化的网页。原生设置与自行改造的设置要分开。
4. 分块和建索引前固定划分与来源快照。按来源文档或文档家族划分，不要随机切分 chunks。
5. 对齐分母和预算：若 token 数不同，Top-K 文档与 Top-K chunks 不可直接比较。
6. 分别报告检索、完整证据、答案和引用结果；加入金标准证据 oracle 条件以定位失败来源。
7. 投入大实验前确认许可、访问门槛、不可用页面和官方评测器。

评估新的 RAG 方法时，至少使用一个领域内 benchmark 和一个迁移 benchmark，再建立一个来源坐标经独立核对的错误分析子集。不要反复对测试集排行榜调参。针对“分块真值”与“多模态证据碎片化”的完整设计见[证据真值指南](evidence-ground-truth.zh-CN.md)。
