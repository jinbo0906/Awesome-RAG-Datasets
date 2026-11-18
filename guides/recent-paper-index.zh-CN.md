# 2025–2026 年 RAG 论文与 benchmark 采用索引

[English](recent-paper-index.md)

更新于 2026-11-18。索引选录 2025 年至 2026 年 11 月公开的研究，近期增补放在前面。较早资源也会在近期实验实际使用时收录。各卡片记录各自的来源核查日期。

## 会议与发表类型口径

统一参照 CCF 于 2026-03-31 发布的**第七版正式目录**：[官方 PDF](https://www.ccf.org.cn/ccf/contentcore/resource/download?ID=112CF3BF7E1140ACEB271ADAED12A67ADFABB8FF099E40C2759502A85C8A281F)。PDF 第 35、47、57 页分别列出 SIGIR、ACM MM 和人工智能 A 类会议，其中包括 ACL、AAAI、NeurIPS、ICML、CVPR、ICCV、**ICLR**。第 58 页将 EMNLP、NAACL、IJCAI 列为 B 类。部分分类网页仍显示旧目录，以正式 PDF 为准。采用当前目录统一筛选，不表示这些会议在论文发表当年已经具有同样等级。

CCF 将正式 Full/Regular 长文纳入考虑，并明确排除 Findings、Short/Demo 和伴随 Workshop。[官方说明](https://www.ccf.org.cn/Academic_Evaluation/By_category/) 表中保留 Long、Datasets and Benchmarks（D&B）和 Resource 差异。本轮维护将会议等级作为背景而非收录门槛：Findings、其他会议、挑战赛和公开预印本均按真实状态记录。具体机构认定规则不由本目录判断，公开预印本不会被改称已同行评审的会议论文。

表格区分**数据引入**、**训练采用**和**评测采用**。数据集卡片保留原生事实；抽样划分、外部语料和改造版指标属于论文实验设置。机器可读关系位于 [catalog/papers](../catalog/papers)。

## 11 月 18 日补充

本次核查以 2026 年正式会议和秋季公开发布为主，重点是证据等价、图三元组、声学证据、知识变化与代理决策。标注改版按发布包记录，方法沿用论文采用关系。

| 论文与发表状态 | 资源和关系 | 实验位置与选型要点 |
|---|---|---|
| [RAGPerf](https://www.vldb.org/pvldb/vol19/p3689-li.pdf) · PVLDB 19(11)，2026 | 引入 [RAGPerf 系统评测套件](../suite-cards/ragperf.zh-CN.md) | §§3–5 与图 9。公开静态文本入库和查询配置，精确混合更新预设及版本化评测轨迹仍未确认。 |
| [RARE](https://aclanthology.org/2026.acl-long.923/) · ACL 2026 长文 | 引入 [RedQA](../dataset-cards/text-rag/redqa.zh-CN.md) | §§4–5 与附录 A.4。分组 Coverage 与 PerfRecall 区分部分命中和全部必需事实覆盖。 |
| [One Fact, Many Places](https://arxiv.org/abs/2610.26401) · 2026 年 10 月预印本 | 重标 [MMLongBench-Red / MMDocRAG-Red](../dataset-cards/multimodal-rag/one-fact-many-places.zh-CN.md) | §§2–5 与附录 I。两套原有资源的子集共同发布，分别评估摘录重评分与集合遮挡。 |
| [MKG-RAG-Bench](https://doi.org/10.1145/3770855.3817570) · KDD 2026 | 引入 [MKG-RAG-Bench](../dataset-cards/graph-rag/mkg-rag-bench.zh-CN.md) | 表 2 与 §§4.2–4.3。先评三元组排序，再用前五个三元组评测问答。原生图数据与图像获取条件分别记录。 |
| [DualGraph](https://aclanthology.org/2026.findings-emnlp.1319/) · Findings EMNLP 2026 | 引入 [SpecsQA](../dataset-cards/table-rag/specsqa.zh-CN.md) | §§3–4 与表 2。完整产品列表和事实正确性揭示语义检索与符号查询的差异。 |
| [OAKS](https://aclanthology.org/2026.acl-long.1956/) · ACL 2026 长文 | 引入 [OAKS](../dataset-cards/text-rag/oaks.zh-CN.md) | §§3–4 与附录 B.2。用流片段步数测量知识获取迟滞。公开小说轨有 435 题，论文报告 870 题。 |
| [TimelyRAG](https://arxiv.org/abs/2609.11572) · 2026 年 9 月预印本 | 引入 [TimelyQABench](../dataset-cards/text-rag/timelyqabench.zh-CN.md) | §§4–5 与表 4–6。四个合成韩语领域提供政策版本相关性和答案时间有效性评判。 |
| [How You Ask Matters](https://aclanthology.org/2026.emnlp-main.2156/) · EMNLP 2026 主会 | 引入 [Query Robustness](../dataset-cards/text-rag/query-robustness.zh-CN.md) | §§3–4 与 §6。比较等义问法下的答案质量、检索决策翻转和调用量。22,183 种发布问法包含 3,000 条原问。 |
| [HARP](https://arxiv.org/abs/2609.14116) · 2026 年 9 月预印本 | 引入录音内检索任务 [HARP Audio QA](../dataset-cards/multimodal-rag/harp-audio.zh-CN.md) | §§III–V。公开音乐和健康轨与需另行授权的情绪轨分别统计。 |
| [CASTELLA](https://arxiv.org/abs/2511.15131) · ICASSP 2026 | 引入 [CASTELLA](../dataset-cards/multimodal-rag/castella.zh-CN.md) | §§4–5 与表 3。使用人工时间标注和时间交并比评估录音内声音定位。 |
| [RAGCap-Bench](https://aclanthology.org/2026.aacl-long.245/) · 2026 年 11 月 IJCNLP–AACL 长文 | 引入 [RAGCap-Bench](../dataset-cards/text-rag/ragcap-bench.zh-CN.md) | §3.4、§4.4 与附录 I。过程选择题用 EM/F1。独立 WebThinker 实验在搜索调用预算下实际评测 BrowseComp 等网页问答。 |
| [Better Together](https://aclanthology.org/2026.emnlp-industry.143/) · EMNLP 2026 Industry | 实际评测 [HotpotQA](../dataset-cards/text-rag/hotpotqa.zh-CN.md)、[AmbigNQ](../dataset-cards/text-rag/ambigqa.zh-CN.md) 和 [EnterpriseRAG-Bench](../dataset-cards/text-rag/enterpriserag-bench.zh-CN.md) | §4 与表 2。分别用训练集前 5,000 条、完整开发集 2,002 条和 470 条有相关性标注的企业题。固定重排与多样化设置下比较检索指标，原始数据集划分以卡片为准。 |

<a name="十一月维护新的评测契约"></a>

## 11 月 1 日补充

每行明确**引入**、**扩展**或**实际评测采用**。仅在参考文献中出现不构成采用关系。RACE、FACT、代理框架和评分工具库仍是方法，不额外计为数据集。卡片保留原生协议，论文特有转换不会悄悄升级为原始数据的属性。

### 搜索代理与研究报告

| 来源／发表状态 | 资源及关系 | 定位与评测价值 |
|---|---|---|
| [BrowseComp](https://arxiv.org/abs/2504.12516) · 2025 年四月报告，基础资源补充 | 引入 [BrowseComp](../dataset-cards/text-rag/browsecomp.zh-CN.md) | §§4.1–4.2、Table 3。实时网页搜索、短答案及校准，无固定检索相关性标注。 |
| [BrowseComp-Plus](https://aclanthology.org/2026.acl-long.1023/) · ACL 2026 Long，2025 年八月预印本 | 引入[固定语料改造](../dataset-cards/text-rag/browsecomp-plus.zh-CN.md) | 数据构建及分开的检索器/代理实验。830 查询、100,195 文档，evidence_docs 与包含答案的 gold_docs 角色不同。 |
| [DeepSearchQA](https://storage.googleapis.com/deepmind-media/DeepSearchQA/DeepSearchQA_benchmark_paper.pdf) · 2025 年十二月技术报告 | 引入 [DeepSearchQA](../dataset-cards/text-rag/deepsearchqa.zh-CN.md) | §§3.1–3.2、Table 4。宏平均答案集合 F1 与严格完整正确率奖励穷尽发现，不是文档召回。 |
| [DeepResearch Bench](https://proceedings.iclr.cc/paper_files/paper/2026/hash/465f22be10e07b301c6ed58f0472f704-Abstract-Conference.html) · ICLR 2026，2025 年六月预印本 | 引入[百任务报告基准](../dataset-cards/text-rag/deepresearch-bench.zh-CN.md) | 作者原文 §§3.1–3.2/4：RACE 报告质量与 FACT 引用支持。2026 年五月、九月评分流程变更影响历史可比性。 |
| [DeepResearch Bench II](https://arxiv.org/abs/2601.08536) · 2026 年一月预印本，九月修订 | 引入[量规基准](../dataset-cards/text-rag/deepresearch-bench-ii.zh-CN.md) | §3.1、§4、Appendix A。发布 132 任务、9,430 条量规；十月榜单只有 130 个有资格任务。量规召回不是检索召回。 |
| [SGR-Bench](https://arxiv.org/abs/2605.22219) · 2026 年五月预印本 | 引入[依赖网页状态的检索任务](../dataset-cards/text-rag/sgr-bench.zh-CN.md) | §§3.2–3.4/4.1–4.2、Table 2、Appendix A。五十对信息需求测字段、完整行及顺序；一百提示不是一百个独立需求。 |
| [WebWeaver](https://proceedings.iclr.cc/paper_files/paper/2026/file/07fa611a88be1832f4c6a96f044ebede-Paper-Conference.pdf) · ICLR 2026 | 实际评测 DeepResearch Bench | §§4.1–4.2、Table 1、Appendix B。三次独立运行，框架不另算 benchmark。 |
| [DuMate-DeepResearch](https://arxiv.org/html/2606.07299) · 2026 年六月技术报告 | 实际评测 DeepResearch Bench 及 II | §§3–3.1、Tables 1–2。自身结果平均三次运行，引用的榜单 baseline 不是全部同环境重跑。 |

### 时间、不确定性、偏好与企业来源

| 来源／发表状态 | 资源及关系 | 定位与评测价值 |
|---|---|---|
| [TEMPO](https://arxiv.org/abs/2601.09523) · 2026 年一月预印本 | 引入 [TEMPO](../dataset-cards/text-rag/tempo.zh-CN.md) | §§3–5、Table 6/Appendix G.3。时间检索与下游问答；官方代码排除 negative_ids，不同于更严格的未过滤全库改造。 |
| [TempRAGEval](https://aclanthology.org/2025.findings-emnlp.167/) · Findings EMNLP 2025 | 引入 [TempRAGEval](../dataset-cards/text-rag/temprageval.zh-CN.md) | §3、§5、Appendix F。人工扰动时间但保持答案不变，任一标注句即可满足证据召回；查询文件需访问批准。 |
| [WikiRecentChanges](https://aclanthology.org/2026.findings-acl.103/) · Findings ACL 2026 | 引入[受控冲突数据](../dataset-cards/text-rag/wikirecentchanges.zh-CN.md) | §3.1、§4/Tables 1–4。变化/稳定事实与真实/反事实给定上下文，没有开放检索或持续索引协议。 |
| [MTRAG-UN](https://aclanthology.org/2026.findings-acl.503/) · Findings ACL 2026 | 引入 [MTRAG-UN](../dataset-cards/text-rag/mtrag-un.zh-CN.md) | §2、§§3.1–3.3。论文六域 666 任务，当前公开参考文件四域 507 任务。不可回答与信息不足目标不同。 |
| [MTRAGEval](https://aclanthology.org/2026.semeval-1.447/) · SemEval 2026 Task 8 | 实际评测 MTRAG-UN，以 [MTRAG](../dataset-cards/text-rag/mtrag.zh-CN.md) 为训练数据 | 任务设置与评测章节。训练与测试资源不同，任务名和框架不产生第三份数据。 |
| [RAG-RewardBench](https://aclanthology.org/2025.findings-acl.877/) · Findings ACL 2025 | 引入[偏好对](../dataset-cards/text-rag/rag-rewardbench.zh-CN.md) | §§3.3/4.1。交换优选/拒选位置评分；引用、拒答与冲突条件测评判器，不是检索相关性。 |
| [Ragability](https://aclanthology.org/2026.lrec-1.182/) · LREC 2026 | 引入 [Ragability Corpus](../dataset-cards/text-rag/ragability.zh-CN.md) | §2、§4.1/Table 2。53 种子行生成每模型 1,060 个提示，配套库不是第二个数据集。 |
| [evolveQA](https://aclanthology.org/2026.emnlp-main.2373/) · EMNLP 2026 main，十月 | 引入[截止日期对齐对照](../dataset-cards/text-rag/evolveqa.zh-CN.md) | §§2–3/4.1、Table 4、Appendices C.1/D.3。闭卷正确率与过时回答率；4,967 截止日期记录对应 937 个领域/问题 ID 键，不是原生更新 RAG。 |
| [EnterpriseRAG-Bench](https://arxiv.org/abs/2605.05253) · 2026 年五月预印本 | 引入[合成企业问答](../dataset-cards/text-rag/enterpriserag-bench.zh-CN.md) | §§4–5 及官方答案评分器。超过五十万文档、500 核心问题，穷尽性与冲突记录暴露证据缺失；真值修正需固定版本。 |

### 图、学术、文档与视频评测

| 来源／发表状态 | 资源及关系 | 定位与评测价值 |
|---|---|---|
| [Graph Counselor](https://aclanthology.org/2025.acl-long.1202/) · ACL 2025 Long | 实际评测 Findings ACL 2024 引入的 [GRBench](../dataset-cards/graph-rag/grbench.zh-CN.md) | 实验设置与 Table 1。十个带文本属性的图；ROUGE-L/QwenScore 不同于原始 Graph-CoT 的 GPT-4 评判。 |
| [ARK](https://aclanthology.org/2026.acl-long.714/) · ACL 2026 Long | 实际评测 NeurIPS 2024 D&B 引入的 [STaRK](../dataset-cards/graph-rag/stark.zh-CN.md) | §4.1/Table 1、Appendix Tables 5–6。词面搜索/遍历预算下的实体检索；教师蒸馏不同于免训练比较。 |
| [WildGraphBench](https://aclanthology.org/2026.findings-acl.679/) · Findings ACL 2026 | 引入 [WildGraphBench](../dataset-cards/graph-rag/wildgraphbench.zh-CN.md) | §§3.5/4.1、Table 2。当前发布 1,197 题，摘要 1,100；索引外部引用页，不索引金标准维基百科摘要。 |
| [CiteRAG](https://doi.org/10.1145/3774904.3792075) · WWW 2026 | 引入[学术引用预测](../dataset-cards/text-rag/citerag.zh-CN.md) | §§2/5、Table 2。参考列表与局部占位符；发布的 Task 2 归一化不同于论文 PACA，必须披露。 |
| [UniDoc-Bench](https://aclanthology.org/2026.findings-emnlp.534/) · Findings EMNLP 2026，十月 | 引入 [UniDoc-Bench](../dataset-cards/multimodal-rag/unidoc-bench.zh-CN.md) | §§3–4、Tables 3–4。实际八个领域划分各 200 题，README 的 1,742/单一 test 说法与配置冲突，人工核验程度也随版本不同。 |
| [ViDoRe v3](https://arxiv.org/abs/2601.08620) · 2026 年一月预印本 | 扩展 [ViDoRe](../suite-cards/vidore.zh-CN.md)，不重复建套件记录 | 数据构建及检索、定位、生成评测。八个公开、两个私有组件；参考答案与框标注扩展了早期纯检索契约。 |
| [M4-RAG](https://openaccess.thecvf.com/content/CVPR2026/html/Anugraha_M4-RAG_A_Massive-Scale_Multilingual_Multi-Cultural_Multimodal_RAG_CVPR_2026_paper.html) · CVPR 2026 | 引入 CVQA/WorldCuisines 的 [RAG 套件改造](../suite-cards/m4-rag.zh-CN.md) | 数据构建与评测章节。原始 VQA、维基百科池和语言变体分开，包含答案的块不是独立相关性真值。 |
| [CRAG-MM](https://arxiv.org/abs/2510.26160) · 2025 年十月预印本，KDD Cup 2025 资源 | 引入 [CRAG-MM](../dataset-cards/multimodal-rag/crag-mm.zh-CN.md)，不同于早期文本 CRAG | §§2–5。可穿戴图像单/多轮问答、模拟搜索、拒答和会话停止；挑战赛关联不是主会发表。 |
| [CFVBench](https://doi.org/10.1145/3774904.3792726) · WWW 2026 | 引入[细粒度视频 RAG](../dataset-cards/multimodal-rag/cfvbench.zh-CN.md) | §3、§4.1。视觉/转录文本要点；检查的公开问答中未见逐题时间区间，论文与仓库问答数不同。 |
| [VideoRAG](https://doi.org/10.1145/3770854.3783944) · KDD 2026 | 引入 [LongerVideos](../dataset-cards/multimodal-rag/longervideos.zh-CN.md) | §4.1、Appendices A/C。公开 164 视频、602 查询没有参考答案；模型比较胜率不是答案准确率。 |
| [VimRAG](https://arxiv.org/abs/2602.12735) · 2026 年二月预印本，四月修订 | 引入 [XVBench](../dataset-cards/multimodal-rag/xvbench.zh-CN.md) | §4.1/Table 2、Appendices B/J。497 查询，其中 138 含多个参考片段；检查版本的引用集合没有跨来源视频 ID。 |

版本维护还保留 [GraphRAG-Bench](../dataset-cards/graph-rag/graphrag-bench.zh-CN.md) 的 2025 发布 ID，并记录作者所报 ICLR 2026 接收。[ViDoRAG](https://aclanthology.org/2025.emnlp-main.464/)引入已有 [ViDoSeek](../dataset-cards/multimodal-rag/vidoseek.zh-CN.md)，不新增缺乏依据的 VRAGBench 别名条目。[分类评估](taxonomy.zh-CN.md#2026-年十一月分类评估)保留来源主分类，仅扩展能力和标注维度。

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
