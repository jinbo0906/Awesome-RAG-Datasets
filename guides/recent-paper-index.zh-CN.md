# 2025–2026 年 RAG 论文与 benchmark 采用索引

[English](recent-paper-index.md)

核查日期：2026-10-02。本索引重点整理已发表的 2025、2026 年工作，补查缺失的 2024 年发布数据，以及近期实验重复使用的早期数据。它是精选的采用证据索引，不是完整文献普查或质量排行榜。同一数据被多篇论文采用，不会重复统计为多个数据集。

## 会议与发表类型口径

统一参照 CCF 于 2026-03-31 发布的**第七版正式目录**：[官方 PDF](https://www.ccf.org.cn/ccf/contentcore/resource/download?ID=112CF3BF7E1140ACEB271ADAED12A67ADFABB8FF099E40C2759502A85C8A281F)。PDF 第 35、47、57 页分别列出 SIGIR、ACM MM 和人工智能 A 类会议，其中包括 ACL、AAAI、NeurIPS、ICML、CVPR、ICCV、**ICLR**。第 58 页将 EMNLP、NAACL、IJCAI 列为 B 类。部分分类网页仍显示旧目录，以正式 PDF 为准。采用当前目录统一筛选，不表示这些会议在论文发表当年已经具有同样等级。

CCF 将正式 Full/Regular 长文纳入考虑，并明确排除 Findings、Short/Demo 和伴随 Workshop。[官方说明](https://www.ccf.org.cn/Academic_Evaluation/By_category/) 下表保留 Long、Datasets and Benchmarks（D&B）和 Resource 轨道差异，不将一切会议关联材料直接当作主轨道长文。具体机构认定规则不由本目录判断。2026 年只记录截至核查日已发表且可验证的材料。

表格区分**数据引入**、**训练采用**和**评测采用**。数据集卡片保留原生事实；抽样划分、外部语料和改造版指标属于论文实验设置。机器可读关系位于 [catalog/papers](../catalog/papers)。

## 文本、会话与多语言采用

| 论文／会议 | 目录入口或原始来源 | 实验位置与边界 |
|---|---|---|
| [MAIN-RAG](https://aclanthology.org/2025.acl-long.131/) · ACL 2025 Long | [TriviaQA](../dataset-cards/text-rag/triviaqa.zh-CN.md)、[PopQA](../dataset-cards/text-rag/popqa.zh-CN.md)、[ALCE](../suite-cards/alce.zh-CN.md) / ASQA | §4.1、Figure 7、Table 1。TriviaQA-unfiltered 使用 11,313 题，PopQA 长尾子集使用 1,399 题；另用尚未索引的 ARC-Challenge。 |
| [Astute RAG](https://aclanthology.org/2025.acl-long.1476/) · ACL 2025 Long | [NQ](../dataset-cards/text-rag/natural-questions.zh-CN.md)、TriviaQA、PopQA、BioASQ | Appendix B 数据收集。论文选用的 BioASQ 版本不是目录中的 2026 Task 14b。 |
| [UniConv](https://aclanthology.org/2025.acl-long.344/) · ACL 2025 Long | [QReCC](../dataset-cards/text-rag/qrecc.zh-CN.md)、[TopiOCQA](../dataset-cards/text-rag/topiocqa.zh-CN.md)、[OR-QuAC](../dataset-cards/text-rag/or-quac.zh-CN.md) | §4.1、Appendix A.1。还使用 INSCIT 和 FaithDial；第一阶段检索、回复生成与可靠性的评测目标不同。 |
| [S2G-RAG](https://aclanthology.org/2026.acl-long.1185/) · ACL 2026 Long | TriviaQA、[HotpotQA](../dataset-cards/text-rag/hotpotqa.zh-CN.md)、[2WikiMultiHopQA](../dataset-cards/text-rag/2wikimultihopqa.zh-CN.md) | 在这三个问答数据集上进行迭代检索实验；系统的句子抽取不是新增的原生证据真值。 |
| [CARL](https://aclanthology.org/2026.acl-long.258/) · ACL 2026 Long | NQ、HotpotQA、TriviaQA、[FEVER](../dataset-cards/text-rag/fever.zh-CN.md)、[WoW](../dataset-cards/text-rag/wizard-of-wikipedia.zh-CN.md) | §4、Table 1、Appendix A/Table 5；另用 T-REx 和 zsRE。论文固定 2018 维基百科和 top-3 段落，这不是所有原始数据共用的协议。 |
| [All Languages Matter](https://aclanthology.org/2026.acl-long.338/) · ACL 2026 Long | [MKQA](../dataset-cards/text-rag/mkqa.zh-CN.md)、[KILT](../suite-cards/kilt.zh-CN.md) / NQ | §2.2、Table 5。采用 2.7K 重叠问题和 13 种语言，外建多语言维基百科语料，用字符 3-gram recall，不是原生 MKQA 相关性真值。 |
| [RaCoT](https://ojs.aaai.org/index.php/AAAI/article/view/40260) · AAAI 2026 Technical | PopQA、TriviaQA-unfiltered、HotpotQA、2WikiMultiHopQA | Experimental Settings、Tables 2–3；另用 ARC-Challenge/OpenBookQA，所选语料与对抗实验需单独报告。 |

## 图结构检索与分块研究

| 论文／会议 | 目录入口或来源 | 实验位置与边界 |
|---|---|---|
| [HippoRAG 2](https://proceedings.mlr.press/v267/gutierrez25a.html) · ICML 2025 | NQ、PopQA、[MuSiQue](../dataset-cards/text-rag/musique.zh-CN.md)、2WikiMultiHopQA、HotpotQA、[NarrativeQA](../dataset-cards/text-rag/narrativeqa.zh-CN.md) | §4.2、Tables 1–3。抽样及另行改造的 LV-Eval 分别评测事实、关联与篇章任务；构建图谱不改变原始数据真值。 |
| [KG-Agent](https://aclanthology.org/2025.acl-long.468/) · ACL 2025 Long | [CWQ](../dataset-cards/graph-rag/complexwebquestions.zh-CN.md)、[KQA Pro](../dataset-cards/graph-rag/kqa-pro.zh-CN.md)、[WebQSP](../dataset-cards/graph-rag/webqsp.zh-CN.md)、[GrailQA](../dataset-cards/graph-rag/grailqa.zh-CN.md)、[MetaQA](../dataset-cards/graph-rag/metaqa.zh-CN.md) | §4.1、Tables 2/3/5。已有知识库上的推理，不等于来源文本 GraphRAG 的引用完整性。 |
| [HiChunk](https://aclanthology.org/2026.acl-long.1372/) · ACL 2026 Long | [HiCBench](../dataset-cards/text-rag/hicbench.zh-CN.md)、[QASPER](../dataset-cards/text-rag/qasper.zh-CN.md)、[GutenQA](../dataset-cards/text-rag/gutenqa.zh-CN.md)、[OHRBench](../dataset-cards/multimodal-rag/ohrbench.zh-CN.md)、[LongBench](../suite-cards/longbench.zh-CN.md) | §5.1、Tables 2–3、Appendix Table A1。切分点 F1、证据召回和最终回答分别评测；结构化 GovReport/QASPER 设置还用于训练与边界评测。 |
| [Beyond Chunking / DISRetrieval](https://aclanthology.org/2026.acl-long.829/) · ACL 2026 Long | QASPER、[QuALITY](../dataset-cards/text-rag/quality.zh-CN.md)、NarrativeQA、LongBench MultiFieldQA-zh | §4.1、Appendix B/Table 8。QuALITY 使用有标签开发集，不是隐藏测试集；篇章树节点是系统构建的表示，不是原生证据标注。 |

## 新文本或结构化基准与长上下文对照

| 引入论文／会议 | 数据集 | 评测边界 |
|---|---|---|
| [SafeRAG](https://aclanthology.org/2025.acl-long.230/) · ACL 2025 Long | [SafeRAG](../dataset-cards/text-rag/saferag.zh-CN.md) | §3 数据构建、§4 评测。中文攻击随注入阶段与强度变化，AFR 与 ASR 的分数方向相反。 |
| [LaRA](https://proceedings.mlr.press/v267/li25dv.html) · ICML 2025 | [LaRA](../dataset-cards/text-rag/lara.zh-CN.md) | §§3–4 与发布的评分脚本。32k/128k 上下文、四类问答，人工种子结合模型生成与抽样核验，没有原生分块边界真值。 |
| [LongBench v2](https://aclanthology.org/2025.acl-long.183/) · ACL 2025 Long | [LongBench v2](../dataset-cards/text-rag/longbench-v2.zh-CN.md) | 数据集章节和模型/RAG 对照；pred.py 支持 --rag。原生长上下文选择题有答案标签，没有检索相关性真值。 |
| [SSRB](https://proceedings.neurips.cc/paper_files/paper/2025/hash/631bbd89466337712564872840a401be-Abstract-Datasets_and_Benchmarks_Track.html) · NeurIPS 2025 D&B | [SSRB](../dataset-cards/table-rag/ssrb.zh-CN.md) | §4.1–4.2、Tables 3–4。半结构化对象检索使用 R@20/nDCG@10，不提供回答生成目标。 |
| [Worse than Zero-shot?](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ed25c00ff6900989116d3ba5d607d33d-Abstract-Datasets_and_Benchmarks_Track.html) · NeurIPS 2025 D&B | [RAGuard](../dataset-cards/text-rag/raguard.zh-CN.md) | §4、Table 2。面向主张核查的误导检索，区分无上下文、检索上下文与金标准证据条件。 |
| [Conflicting Web References](https://aclanthology.org/2026.acl-long.11/) · ACL 2026 Long | [ConfRAG](../dataset-cards/text-rag/confrag.zh-CN.md) | §3.4、§4、Table 2。在矛盾参考资料上评测答案聚类与答案/理由覆盖，不假定唯一答案或证据集合。 |
| [MINTQA](https://aclanthology.org/2026.acl-long.18/) · ACL 2026 Long | [MINTQA](../dataset-cards/graph-rag/mintqa.zh-CN.md) | §4.2、§§6–7、Table 3、Appendix E.2。评测新知识、长尾知识和动态检索，答案包含评分不等于路径正确性。 |

## 多模态采用与数据发布

| 论文／会议 | 目录入口或来源 | 实验位置与边界 |
|---|---|---|
| [NoteMR](https://openaccess.thecvf.com/content/CVPR2025/html/Fang_Notes-guided_MLLM_Reasoning_Enhancing_MLLM_with_Knowledge_and_Visual_Notes_CVPR_2025_paper.html) · CVPR 2025 | [OK-VQA](../dataset-cards/multimodal-rag/ok-vqa.zh-CN.md)、[A-OKVQA](../dataset-cards/multimodal-rag/a-okvqa.zh-CN.md) | §4.1、Tables 1–2。OK-VQA 测试集使用 Google Search Corpus；A-OKVQA 验证集使用维基百科，视觉输入已给定。 |
| [VDocRAG](https://openaccess.thecvf.com/content/CVPR2025/papers/Tanaka_VDocRAG_Retrieval-Augmented_Generation_over_Visually-Rich_Documents_CVPR_2025_paper.pdf) · CVPR 2025 | [OpenDocVQA](../dataset-cards/multimodal-rag/opendocvqa.zh-CN.md)、[DocVQA](../dataset-cards/multimodal-rag/docvqa.zh-CN.md)、[InfographicVQA](../dataset-cards/multimodal-rag/infographicvqa.zh-CN.md)、[DUDE](../dataset-cards/multimodal-rag/dude.zh-CN.md) | §5.1/Table 2 来源，Tables 3–4 检索/问答。DocVQA 是训练来源，InfoVQA/DUDE 参与训练与评测；还评测 ChartQA/SlideVQA。改造候选池不是原始单图任务。 |
| [VisRAG](https://proceedings.iclr.cc/paper_files/paper/2025/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf) · ICLR 2025 | [ArXivQA](../dataset-cards/multimodal-rag/arxivqa.zh-CN.md)、[PlotQA](../dataset-cards/multimodal-rag/plotqa.zh-CN.md)、InfographicVQA、[MP-DocVQA](../dataset-cards/multimodal-rag/mp-docvqa.zh-CN.md)、[ChartQA](../dataset-cards/multimodal-rag/chartqa.zh-CN.md)、[SlideVQA](../dataset-cards/multimodal-rag/slidevqa.zh-CN.md) | §3.3/Table 1、Tables 2–3。明确过滤后的检索改造，不另造 VisRAG-Bench 数据名称。ICLR 按当前 2026 目录分类，不作追溯认定。 |
| [MRAG-Bench](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ee46288ab2aaf5c6e53aebebe719712c-Abstract-Conference.html) · ICLR 2025 | [MRAG-Bench](../dataset-cards/multimodal-rag/mrag-bench.zh-CN.md) | 引入论文及官方发布数据：1,353 道人工标注选择题、16,130 张图像、九类场景。区分无检索、检索图像与金标准图像条件。 |
| [CoRe-MMRAG](https://aclanthology.org/2025.acl-long.1583/) · ACL 2025 Long | [InfoSeek](../dataset-cards/multimodal-rag/infoseek.zh-CN.md)、[Encyclopedic-VQA](../dataset-cards/multimodal-rag/encyclopedic-vqa.zh-CN.md) | §4.1–4.3、Tables 1–2。使用 InfoSeek 验证集，以及排除二跳问题后的 Encyclopedic-VQA 测试集（4.7K 图像问答三元组）；语料过滤、按 URL 匹配的文章召回与答案指标分别报告。 |
| [REAL-MM-RAG](https://aclanthology.org/2025.acl-long.1528/) · ACL 2025 Long | [REAL-MM-RAG](../dataset-cards/multimodal-rag/real-mm-rag.zh-CN.md) | §5.1、Tables 2–3 与 S1。四个文档子集、4,553 个基础查询及 0–3 级措辞；合成页面相关性用于检索评分，不代表官方生成任务，也不是区域或单元格定位真值。 |
| [OCR Hinders RAG](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_OCR_Hinders_RAG_Evaluating_the_Cascading_Impact_of_OCR_on_ICCV_2025_paper.html) · ICCV 2025 | [OHRBench](../dataset-cards/multimodal-rag/ohrbench.zh-CN.md) | §§3–4。OCR 编辑距离、LCS 证据包含度与答案 F1 是不同指标，来源损坏后仍需保留标准页面证据。 |
| [MMDocRAG](https://proceedings.neurips.cc/paper_files/paper/2025/file/1a93178950e92fd2e7b7448f7d68fd7d-Paper-Datasets_and_Benchmarks_Track.pdf) · NeurIPS 2025 D&B | [MMDocRAG](../dataset-cards/multimodal-rag/mmdocrag.zh-CN.md) | 基准构建及检索/生成评测。专家标注的跨页多模态证据不能简化为答案正确率。 |
| [RAG-IGBench](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b0a4b3e384b4554e65a47ad1f6b0310a-Abstract-Datasets_and_Benchmarks_Track.html) · NeurIPS 2025 D&B | [RAG-IGBench](../dataset-cards/multimodal-rag/rag-igbench.zh-CN.md) | §3.2、Tables 1/3/5。评测图文交错输出，原始问题与双语扩展行是不同计数单位。 |
| [M²RAG](https://doi.org/10.1145/3746027.3755625) · ACM MM 2025 | [M²RAG](../dataset-cards/multimodal-rag/m2rag.zh-CN.md) | 作者原文 §5、Tables 3–4。WebQA/Factify 改造，不是文本、表格、图谱 mmRAG。 |
| [Visual-RAG](https://doi.org/10.1145/3805712.3808615) · SIGIR 2026 Resource | [Visual-RAG](../dataset-cards/multimodal-rag/visual-rag.zh-CN.md) | 作者原文 §5.1、Tables 2–3。使用修订 v2（374 题），保留会议轨道与原文版本差异。 |
| [Utility-Oriented Visual Evidence Selection](https://aclanthology.org/2026.acl-long.1620/) · ACL 2026 Long | [MRAG-Bench](../dataset-cards/multimodal-rag/mrag-bench.zh-CN.md)、Visual-RAG | §5.1、Tables 1–2。金标准图像加 CLIP 候选构成固定选择池，不是无约束全库检索。 |

## 有价值的补充来源

- [LongBench，ACL 2024 Long](https://aclanthology.org/2024.acl-long.172/)：[套件](../suite-cards/longbench.zh-CN.md)。长上下文与检索压缩的早一年来源，改造子集不同于原始数据。
- [FRAMES，NAACL 2025](https://aclanthology.org/2025.naacl-long.243/)：[数据集](../dataset-cards/text-rag/frames.zh-CN.md)。重要的多文档推理评测，不将 NAACL 写成 ACL 主会。
- [RAG-QA Arena，EMNLP 2024](https://aclanthology.org/2024.emnlp-main.249/)：[LFRQA](../dataset-cards/text-rag/lfrqa.zh-CN.md) 是数据，Arena 是答案比较协议。
- [MIRAGE，Findings ACL 2024](https://aclanthology.org/2024.findings-acl.372/)：[套件](../suite-cards/mirage.zh-CN.md)。医学 RAG 需严格保留去上下文与仅问题检索设置，并保留 Findings 发表类型。
- [LumberChunker，Findings EMNLP 2024](https://aclanthology.org/2024.findings-emnlp.377/)：[GutenQA](../dataset-cards/text-rag/gutenqa.zh-CN.md) 后被 ACL 2026 HiChunk 采用。原始 3,000 题检索集与另行使用的 280 题生成实验不同。
- [mmRAG，作者预印本及发布数据](https://arxiv.org/abs/2505.11180)：[数据集](../dataset-cards/text-rag/mmrag.zh-CN.md)。固定 512-token 分块相关性与路由标签，不添加未经确认的会议等级。
- [FinChain，ACL 2026 Long](https://aclanthology.org/2026.acl-long.662/)：[组件对照](../dataset-cards/cross-cutting/finchain.zh-CN.md)。提供可执行中间目标的财务推理，不是原生 RAG，也没有检索语料。

## 对两个研究问题的选型建议

分块研究组合 HiCBench 的层级边界、QASPER 的证据段落、GutenQA 的子串锚点和 OHRBench 的 OCR 扰动，再在多跳数据上测试迁移。分别回答边界是否匹配标注、完整证据是否在 token 预算内、最终回答是否改善。LaRA/LongBench v2 补充回答层面评测，不替代分块真值。

多模态碎片化研究组合 MMDocIR 的页面/布局检索、MMDocRAG 的跨页问答、OpenDocVQA 的检索设置及 DUDE/TAT-DQA 的文档证据。RAG-IGBench 补充图文交错输出，Visual-RAG 补充外部视觉知识。单图问答、页面命中、候选选择与完整跨模态证据链是不同目标。缺失关系标签需独立标注，详见[证据真值](evidence-ground-truth.zh-CN.md)与[基准构建](benchmark-construction.zh-CN.md)。

## 维护方式与剩余缺口

扩充从实验章节出发，而非参考文献名单。保留引入、训练与评测角色，核对划分、语料快照、版本、抽样、指标和评测器。检查原始证据粒度与许可后同步双语；`source_checked` 表示核对来源，不等于已经复现。

本轮未单独索引 ARC-Challenge、OpenBookQA、INSCIT、FaithDial、T-REx、zsRE、LV-Eval 的确切 RAG 改造。BEIR、ChatRAG Bench、LongBench、MIRAGE 是部分组成项索引，协议已明确说明。链接的原生卡片不等于整套重处理评测文件。后续遵循[收录边界](coverage-policy.zh-CN.md)继续补查，不重复收录随意子集或无发布依据的论文资产。
