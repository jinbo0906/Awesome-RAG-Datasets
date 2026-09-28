# Text RAG：从来源检索到有依据的回答

[English](text-rag.md)

Text RAG 涉及文档、段落和句子检索、回答生成、多跳证据、引用、鲁棒性，以及时效性或对话场景。这些场景采用不同评测协议，分数不能直接互换。先查看[数据集目录](../../README.zh-CN.md#text-rag)，建立索引前再核对每张卡片的原生检索范围。

| 子方向 | 建议先看 | 实际发布的标注 |
|---|---|---|
| 多跳推理与分块 | [HotpotQA](../../dataset-cards/text-rag/hotpotqa.zh-CN.md)、[2WikiMultiHopQA](../../dataset-cards/text-rag/2wikimultihopqa.zh-CN.md)、[StrategyQA](../../dataset-cards/text-rag/strategyqa.zh-CN.md)、[HiCBench](../../dataset-cards/text-rag/hicbench.zh-CN.md) | 句子、段落或层级标注，但构建方法不同 |
| 长来源证据 | [QASPER](../../dataset-cards/text-rag/qasper.zh-CN.md)、[CLAP NQ](../../dataset-cards/text-rag/clapnq.zh-CN.md)、[NarrativeQA](../../dataset-cards/text-rag/narrativeqa.zh-CN.md) | 论文、段落或来源文档；NarrativeQA 不提供最小证据片段 |
| 对话 | [MTRAG](../../dataset-cards/text-rag/mtrag.zh-CN.md) | 分轮回答和相关性标注；参考证据与完整 RAG 是不同设置 |
| 鲁棒性与依据 | [RGB](../../dataset-cards/text-rag/rgb.zh-CN.md)、[RAGTruth](../../dataset-cards/text-rag/ragtruth.zh-CN.md)、[RAGBench](../../dataset-cards/text-rag/ragbench.zh-CN.md) | 固定上下文回答、生成回答中的错误片段或支持关系元数据；并非共同的检索相关性真值 |
| 时效性回答 | [FreshQA](../../dataset-cards/text-rag/freshqa.zh-CN.md)、[RealTime QA](../../dataset-cards/text-rag/realtimeqa.zh-CN.md) | 带日期的答案；来源快照需要单独控制 |
| 仅检索的对照 | [BEIR](../../suite-cards/beir.zh-CN.md)、[MS MARCO Passage Ranking](../../dataset-cards/text-rag/msmarco-passage.zh-CN.md)、[BRIGHT](../../dataset-cards/text-rag/bright.zh-CN.md) | 语料—查询相关性，而不是回答忠实度 |
| 专业领域 | [BioASQ Task 14b](../../dataset-cards/text-rag/bioasq-14b.zh-CN.md)、[PUBHEALTH](../../dataset-cards/text-rag/pubhealth.zh-CN.md) | 生物医学来源片段，与公共卫生主张的标签和解释，标注范围不同 |

研究分块时，应使用不随分块策略改变的文档、段落或句子坐标，并固定 token 预算。一句支持性证据不是唯一正确的分块边界。宜成对分析完整证据检索、额外上下文开销和回答质量；研究回答时，应分别报告提供金标准证据的 oracle 设置与实际检索设置。RGB 和 RAGTruth 可用于**诊断**，但不能当作完整开放语料检索测试。动态更新答案的数据集必须固定版本日期，并记录来源获取时间。

完整的[证据真值指南](../evidence-ground-truth.zh-CN.md)规定了来源坐标和可替代证据集合的处理方式。领域是独立筛选维度：生物医学和公共卫生条目放在这里，是因为它们发布的证据是文本，而不是因为“医疗 RAG”是另一种来源表示形式。
