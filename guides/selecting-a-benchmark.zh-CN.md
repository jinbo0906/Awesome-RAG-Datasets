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

<a name="capability-routes"></a>

## 跨来源分类的能力选型入口

这些入口横跨现有分类目录，索引不同评测契约，不是可以直接比较的排行榜列。发表信息及实验位置见[近期论文索引](recent-paper-index.zh-CN.md)。

| 评测需求 | 优先查看 | 必须保留的契约 |
|---|---|---|
| 自适应搜索与停止决策 | [BrowseComp-Plus](../dataset-cards/text-rag/browsecomp-plus.zh-CN.md)、[BrowseComp](../dataset-cards/text-rag/browsecomp.zh-CN.md)、[DeepSearchQA](../dataset-cards/text-rag/deepsearchqa.zh-CN.md)、[SGR-Bench](../dataset-cards/text-rag/sgr-bench.zh-CN.md) | 固定语料与实时网页不同；推理/答案文档、完整答案集合、结构化行与工具预算是不同目标 |
| 研究报告质量 | [DeepResearch Bench](../dataset-cards/text-rag/deepresearch-bench.zh-CN.md)、[DeepResearch Bench II](../dataset-cards/text-rag/deepresearch-bench-ii.zh-CN.md) | RACE/FACT 与内容量规不同；固定当前有资格评分的任务及判分版本，不推断有金标准动作轨迹 |
| 时间证据与参数知识 | [TEMPO](../dataset-cards/text-rag/tempo.zh-CN.md)、[TempRAGEval](../dataset-cards/text-rag/temprageval.zh-CN.md)、[WikiRecentChanges](../dataset-cards/text-rag/wikirecentchanges.zh-CN.md)、[evolveQA](../dataset-cards/text-rag/evolveqa.zh-CN.md) | 检索时间覆盖、日期扰动、给定上下文冲突、闭卷知识截止点是不同测试；均不能单独证明持续索引更新能力 |
| 澄清、拒答与冲突 | [MTRAG-UN](../dataset-cards/text-rag/mtrag-un.zh-CN.md)、[Ragability](../dataset-cards/text-rag/ragability.zh-CN.md)、[ConfRAG](../dataset-cards/text-rag/confrag.zh-CN.md) | 区分不可回答与信息不足、上下文一致与冲突、参考证据与完整 RAG |
| 回答评判器与偏好对齐 | [RAG-RewardBench](../dataset-cards/text-rag/rag-rewardbench.zh-CN.md)、[RAGTruth](../dataset-cards/text-rag/ragtruth.zh-CN.md) | 偏好对排序不同于回答错误片段检测，二者都不能证明开放语料检索质量 |
| 企业密集干扰项 | [EnterpriseRAG-Bench](../dataset-cards/text-rag/enterpriserag-bench.zh-CN.md) | 合成跨来源一致性、无答案情况、可修订真值；分开记录版本修正与固定榜单标签 |
| 图遍历与全局综合 | [STaRK](../dataset-cards/graph-rag/stark.zh-CN.md)、[GRBench](../dataset-cards/graph-rag/grbench.zh-CN.md)、[WildGraphBench](../dataset-cards/graph-rag/wildgraphbench.zh-CN.md) | 节点排序、答案评判和陈述覆盖不同；WildGraphBench 不得索引金标准维基百科摘要 |
| 学术参考文献推荐 | [CiteRAG](../dataset-cards/text-rag/citerag.zh-CN.md) | 参考列表或占位符预测不是主张蕴含评测，发布代码 PACA 聚合不同于论文定义 |
| 视频证据保留 | [CFVBench](../dataset-cards/multimodal-rag/cfvbench.zh-CN.md)、[XVBench](../dataset-cards/multimodal-rag/xvbench.zh-CN.md)、[LongerVideos](../dataset-cards/multimodal-rag/longervideos.zh-CN.md) | 视频 ID、可寻址片段和答案要点不等于最小时间区间；LongerVideos 未发布参考答案 |
| 文档与多语言全流程对照 | [UniDoc-Bench](../dataset-cards/multimodal-rag/unidoc-bench.zh-CN.md)、[ViDoRe](../suite-cards/vidore.zh-CN.md)、[M4-RAG](../suite-cards/m4-rag.zh-CN.md)、[CRAG-MM](../dataset-cards/multimodal-rag/crag-mm.zh-CN.md) | 区分版本化检索、定位、问答、语言变体和多轮停止规则，固定来源可见性及预算 |

对于最初的分块问题，BrowseComp-Plus 补充文档级证据获取标签，TEMPO 补充时段覆盖，但都不提供最优切分边界。对于多模态碎片化，UniDoc-Bench 补充关联来源事实，ViDoRe v3 补充定位和答案；CFV/XVBench 缺失的时间或跨元素证据链仍需独立标注。分别报告金标准证据 oracle、实际检索、完整集合覆盖、答案/引用质量及成本。

## 选型检查清单

1. 确定目标单位：来源文档、页面、句子、单元格、区域、图路径、原子事实，还是最终答案。
2. 核查**已发布字段**能否识别该单位。不能仅凭解释把页面标签提升为单元格标签。
3. 选择检索范围：固定给定上下文、单文档、多文档、开放语料或随时间变化的网页。原生设置与自行改造的设置要分开。
4. 分块和建索引前固定划分与来源快照。按来源文档或文档家族划分，不要随机切分 chunks。
5. 对齐分母和预算：若 token 数不同，Top-K 文档与 Top-K chunks 不可直接比较。
6. 分别报告检索、完整证据、答案和引用结果；加入金标准证据 oracle 条件以定位失败来源。
7. 投入大实验前确认许可、访问门槛、不可用页面和官方评测器。

评估新的 RAG 方法时，至少使用一个领域内 benchmark 和一个迁移 benchmark，再建立一个来源坐标经独立核对的错误分析子集。不要反复对测试集排行榜调参。针对“分块真值”与“多模态证据碎片化”的完整设计见[证据真值指南](evidence-ground-truth.zh-CN.md)。
