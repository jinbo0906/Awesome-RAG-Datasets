# 收录决策与待核查候选

[English](coverage-policy.md)

本目录追求有用、可审计的覆盖，而非最大化条目数量。RAG 论文提到的名称，可能指原始数据集、重处理变体、套件、语料、评测框架，或仅是论文中的一次实验。只有当对象类型、原生任务、获取方式和关键字段来源都能说清楚时才建立记录；不能假装上游发布了实际不存在的标注。

## 已收录，但需守住边界

- [RGB](../dataset-cards/text-rag/rgb.zh-CN.md)测试固定上下文鲁棒性，不测试开放语料检索。[RAGTruth](../dataset-cards/text-rag/ragtruth.zh-CN.md)标注生成回答中的幻觉，而不是来源证据片段。[MTRAG](../dataset-cards/text-rag/mtrag.zh-CN.md)的参考证据设置与完整 RAG 设置不同。
- [BioASQ Task 14b](../dataset-cards/text-rag/bioasq-14b.zh-CN.md)固定到具体挑战年份；[PUBHEALTH](../dataset-cards/text-rag/pubhealth.zh-CN.md)的论文与仓库统计数量不同，且若做检索需另外构建语料。
- [MS MARCO Passage Ranking](../dataset-cards/text-rag/msmarco-passage.zh-CN.md)是明确的检索变体，不能作为原始生成式 MS MARCO 或 TREC-DL 的同义词。
- [MetaQA](../dataset-cards/graph-rag/metaqa.zh-CN.md)提供电影知识库与按跳数划分的问答；Microsoft GraphRAG 的[播客资产](../catalog/corpora/ms-graphrag-podcasts.yaml)只按语料收录，不能宣称有金标准图路径。
- [SQA](../dataset-cards/table-rag/sqa.zh-CN.md)直接提供表格；[ToTTo](../dataset-cards/table-rag/totto.zh-CN.md)直接提供高亮单元格。如果没有记录清楚改造步骤，它们的原生结果不能与开放表格检索结果比较。

## 不自动收录为 RAG 数据集的对象

| 候选类型 | 判断规则 |
|---|---|
| [Ragas](https://docs.ragas.io/en/stable/concepts/metrics/overview/)、DeepEval、TruLens 等评测工具库 | 评分工具不是固定数据集。若另有具体发布的评测集，应作为独立对象记录。 |
| MMLU、TruthfulQA、MedQA、HLE 等通识测验与考试 | 它们可测知识或推理，但没有明确来源池和证据/检索协议时，不是原生 RAG。衍生的 RAG 版本必须另取名称。 |
| MITRE ATT&CK、医学图像档案、教材、新闻或播客转录等来源集合 | 若能确定快照和访问方式，可按语料记录；不能推断它们有金标准问答或引用标注。 |
| [BEIR](../suite-cards/beir.zh-CN.md)、[ViDoRe](../suite-cards/vidore.zh-CN.md)、[M-BEIR](../suite-cards/m-beir.zh-CN.md)、[M2KR](../suite-cards/m2kr.zh-CN.md) 等套件的子集 | 转换后的子集可能改变语料、划分、相关性标注和指标。须核查具体版本后作为变体关联，不能悄悄复用原始数据集卡片。 |
| 只有论文描述或发布不稳定的资产 | 在能够确认权威下载、版本与评测器前，不标记为 `source_checked`。HTTP 403、429 或超时并不能证明资源已移除。 |

## 近期论文覆盖

[2025–2026 年论文采用索引](recent-paper-index.zh-CN.md)追溯近期论文的实际实验数据，保留正式轨道、Findings、挑战赛和预印本状态。CCF 等级只是背景，不是收录门槛。近期复用的早期数据与新引入 benchmark 均纳入，但不会将转换子集再次统计为新数据集。[MedQA](../dataset-cards/text-rag/medqa.zh-CN.md)、[MedMCQA](../dataset-cards/text-rag/medmcqa.zh-CN.md)、[PubMedQA](../dataset-cards/text-rag/pubmedqa.zh-CN.md)已有原生卡片，并通过 [MIRAGE](../suite-cards/mirage.zh-CN.md)关联；这些原生任务仍不提供开放检索的证据真值。

## 证据与更新评测的发布核查

核查日期为 2026-11-18。[选型指南](selecting-a-benchmark.zh-CN.md#evidence-and-update-protocols)说明如何用当前发布资源搭建实验，以及哪些改造需要额外标注或负载轨迹。

| 资源 | 论文协议 | 公开发布与收录状态 |
|---|---|---|
| FRESCO | 每个查询重排给定的 51 个段落，含 1 个正例和 50 个负例。论文报告 7,316 条显式或隐式时效查询，用排序指标及 Obsolete Ratio 诊断相关但已过时的事实。 | **候选。** 数据生成依赖 Wikidata、维基百科修订记录和 Rankify 负例。`generate_data.sh` 调用 `collect_neg_pssgs.py`，已查提交中提供的文件是 `collect_neg_pssgs_rankify.py`。冻结候选池、标签和精确复建仍未确认。指令优化评分器实现了 MAP、MRR 和 nDCG。[论文 §§3–5](https://aclanthology.org/2026.findings-emnlp.54.pdf) · [固定提交](https://github.com/facebookresearch/fresco/tree/51eadebff0e8ec625d66ace44d44e12020c550a2) |
| LongAudioQA | 论文报告基于 AliMeeting、AMI 和 DailyTalk 的 190 段录音构建 16,456 道问答。附录 L 示例含时间区间、说话人和转录。论文用模型评判语义回答准确率，并按 ±2 秒容差报告时间引用的精确率和召回率。 | **候选。** 作者 README 仍将基准标为待发布。已查分支、发布页和论文补充材料未能确认冻结划分、逐题证据、录音映射或批量评分器。原始录音不足以重建这些标签。[论文 §4 与附录 B、L](https://aclanthology.org/2026.findings-acl.1038.pdf) · [固定提交](https://github.com/tangquanwei/GRGA/tree/12a0f0d77abd1ab89bb3989b521ac9aa46c2204d) |
| CrossModalQA | 论文报告 1,863 道问答、4,987 篇维基百科文章、4,431 张图像和五种路径类型。§3.5 定义按证据项计算的 Recall、Precision 和 Hit，截断值为 1/5/10，回答按原子事实算 EM 和微平均 F1。Hit 统计是否命中任意证据项。 | **候选。** 图 1 展示路径示例。已查预印本及源码包未指向逐题发布包或评分器，精确图文候选池、证据 ID 和原子答案仍未确认。[预印本 §§3.2–3.5 与附录 B](https://arxiv.org/html/2609.05518v1) |
| RAGPerf | §5.5 与图 9 比较 60 分钟各半查询与更新的混合负载，涉及均匀／Zipfian 访问及索引缓冲。 | **按公开静态负载收录为套件。** [卡片](../suite-cards/ragperf.zh-CN.md)提供文本入库、查询预设及外部数据入口。已查代码将入库和查询分为两阶段，精确混合配置、更新问答、轨迹或生成器仍未确认。[论文](https://www.vldb.org/pvldb/vol19/p3689-li.pdf) · [固定提交](https://github.com/platformxlab/RAGPerf/tree/49c9794895666d029a3c98a48afd872197d83b23) |

其他待核查项包括 TableRAG 的 ArcadeQA/BirdQA 大型表格变体的发布资产与许可，以及 ViDoRe 和 M2KR 的版本化子集转换。[TableRAG 论文](https://arxiv.org/abs/2410.04739) · [上游下载问题](https://github.com/google-research/google-research/issues/3190)

十一月维护已增加经核查的视频条目，但 [CFVBench](../dataset-cards/multimodal-rag/cfvbench.zh-CN.md) 的要点与 [XVBench](../dataset-cards/multimodal-rag/xvbench.zh-CN.md) 的片段 ID 仍没有经核实的最小时间区间；[LongerVideos](../dataset-cards/multimodal-rag/longervideos.zh-CN.md)缺少公开参考答案。[MTRAG-UN](../dataset-cards/text-rag/mtrag-un.zh-CN.md)的两个未发布领域、ViDoRe v3 私有组件、CiteRAG 未解决的数据条款，以及未确认作者承继的更大同名 SGR 发布，都是明确边界，不是假定已完成的覆盖。[ComplexWebQuestions](../dataset-cards/graph-rag/complexwebquestions.zh-CN.md)旧主页返回 404，现关联作者代码，但修正版数据获取仍需单独核对。

新候选应遵循[条目判断规则](benchmark-vs-dataset.zh-CN.md#新条目的判断规则)与[贡献清单](../CONTRIBUTING.zh-CN.md)。关键事实未知时，应标为未知或保留在候选区，不要用二手摘要补齐。
