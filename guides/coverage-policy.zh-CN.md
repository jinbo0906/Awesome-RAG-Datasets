# 收录决策与待核查候选

[English](coverage-policy.md)

本目录追求有用、可审计的覆盖，而非最大化条目数量。RAG 论文提到的名称，可能指原始数据集、重处理变体、套件、语料、评测框架，或仅是论文中的一次实验。只有当对象类型、原生任务、获取方式和关键字段来源都能说清楚时才建立记录；不能假装上游发布了实际不存在的标注。

## 已收录，但需守住边界

- [RGB](../dataset-cards/text-rag/rgb.md)测试固定上下文鲁棒性，不测试开放语料检索。[RAGTruth](../dataset-cards/text-rag/ragtruth.md)标注生成回答中的幻觉，而不是来源证据片段。[MTRAG](../dataset-cards/text-rag/mtrag.md)的参考证据设置与完整 RAG 设置不同。
- [BioASQ Task 14b](../dataset-cards/text-rag/bioasq-14b.md)固定到具体挑战年份；[PUBHEALTH](../dataset-cards/text-rag/pubhealth.md)的论文与仓库统计数量不同，且若做检索需另外构建语料。
- [MS MARCO Passage Ranking](../dataset-cards/text-rag/msmarco-passage.md)是明确的检索变体，不能作为原始生成式 MS MARCO 或 TREC-DL 的同义词。
- [MetaQA](../dataset-cards/graph-rag/metaqa.md)提供电影知识库与按跳数划分的问答；Microsoft GraphRAG 的[播客资产](../catalog/corpora/ms-graphrag-podcasts.yaml)只按语料收录，不能宣称有金标准图路径。
- [SQA](../dataset-cards/table-rag/sqa.md)直接提供表格；[ToTTo](../dataset-cards/table-rag/totto.md)直接提供高亮单元格。如果没有记录清楚改造步骤，它们的原生结果不能与开放表格检索结果比较。

## 不自动收录为 RAG 数据集的对象

| 候选类型 | 判断规则 |
|---|---|
| [Ragas](https://docs.ragas.io/en/stable/concepts/metrics/overview/)、DeepEval、TruLens 等评测工具库 | 评分工具不是固定数据集。若另有具体发布的评测集，应作为独立对象记录。 |
| MMLU、TruthfulQA、MedQA、HLE 等通识测验与考试 | 它们可测知识或推理，但没有明确来源池和证据/检索协议时，不是原生 RAG。衍生的 RAG 版本必须另取名称。 |
| MITRE ATT&CK、医学图像档案、教材、新闻或播客转录等来源集合 | 若能确定快照和访问方式，可按语料记录；不能推断它们有金标准问答或引用标注。 |
| [BEIR](../suite-cards/beir.md)、[ViDoRe](../suite-cards/vidore.md)、[M-BEIR](../suite-cards/m-beir.md)、[M2KR](../suite-cards/m2kr.md) 等套件的子集 | 转换后的子集可能改变语料、划分、相关性标注和指标。须核查具体版本后作为变体关联，不能悄悄复用原始数据集卡片。 |
| 只有论文描述或发布不稳定的资产 | 在能够确认权威下载、版本与评测器前，不标记为 `source_checked`。HTTP 403、429 或超时并不能证明资源已移除。 |

## 后续优先核查

以下只是**候选调查**，不是已完成复核的结论：检查 TableRAG 的 ArcadeQA/BirdQA 大型表格变体是否有可公开复现的资产与许可（[论文](https://arxiv.org/abs/2410.04739)、[上游下载问题](https://github.com/google-research/google-research/issues/3190)）；分开核对 ViDoRe 和 M2KR 的版本化子集转换；审查视频 RAG 数据是否发布了时间坐标、问题及评测器。法律、金融、医疗和代码等领域也应按同一套来源与证据条件筛选，而非仅凭领域名称升为顶层分类。

新候选应遵循[条目判断规则](benchmark-vs-dataset.zh-CN.md#新条目的判断规则)与[贡献清单](../CONTRIBUTING.zh-CN.md)。关键事实未知时，应标为未知或保留在候选区，不要用二手摘要补齐。
