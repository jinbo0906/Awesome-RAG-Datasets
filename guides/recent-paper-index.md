# RAG paper and benchmark adoption, 2025–2026

[简体中文](recent-paper-index.zh-CN.md)

Updated 2026-11-18. The index covers selected public work from 2025 through November 2026, with recent additions at the top. Older resources also appear when recent experiments use them. Each card records its own source check date.

## Venue and publication scope

The reference is CCF's **seventh-edition formal directory**, published on 2026-03-31: [official PDF](https://www.ccf.org.cn/ccf/contentcore/resource/download?ID=112CF3BF7E1140ACEB271ADAED12A67ADFABB8FF099E40C2759502A85C8A281F). PDF pages 35, 47 and 57 list SIGIR, ACM MM and the AI A venues, including ACL, AAAI, NeurIPS, ICML, CVPR, ICCV and **ICLR**. Page 58 places EMNLP, NAACL and IJCAI in B. Some category webpages still show an older list; the formal PDF takes precedence. Applying this current directory consistently is not a claim that every venue had the same grade in the paper's publication year.

CCF considers formal Full/Regular papers and explicitly excludes Findings, Short/Demo papers and companion Workshops. [Official policy](https://www.ccf.org.cn/Academic_Evaluation/By_category/) Track labels preserve Long, Datasets and Benchmarks (D&B), and Resource distinctions. Venue grade is context, not an inclusion gate in this maintenance pass: Findings, other venues, challenges and public preprints are included with their actual status. Institution-specific recognition is outside this catalog's scope; a public preprint is not relabeled a peer-reviewed conference paper.

The tables distinguish **introduction**, **training use** and **evaluation use**. Dataset cards retain native facts; sampled splits, external corpora and conversion-specific metrics remain properties of the paper's experiment. Machine-readable relationships are in [catalog/papers](../catalog/papers).

## November 18 additions

This pass focuses on 2026 proceedings and releases from September through November. Evidence alternatives, graph triples, acoustic evidence, knowledge changes and agent decisions are the main additions.

| Paper and publication | Resource and relation | Experiment and selection notes |
|---|---|---|
| [RARE](https://aclanthology.org/2026.acl-long.923/) · ACL 2026 Long | Introduces [RedQA](../dataset-cards/text-rag/redqa.md) | §§4–5 and Appendix A.4. Group-level Coverage and PerfRecall distinguish partial support from coverage of every required fact. |
| [One Fact, Many Places](https://arxiv.org/abs/2610.26401) · October 2026 preprint | Re-annotates [MMLongBench-Red / MMDocRAG-Red](../dataset-cards/multimodal-rag/one-fact-many-places.md) | §§2–5 and Appendix I. Two parent benchmark subsets share a release. Separate quote rescoring from set-level masking. |
| [MKG-RAG-Bench](https://doi.org/10.1145/3770855.3817570) · KDD 2026 | Introduces [MKG-RAG-Bench](../dataset-cards/graph-rag/mkg-rag-bench.md) | Table 2 and §§4.2–4.3. Rank graph triples and evaluate answers with the top five triples. Native graph inputs and visual assets have separate access terms. |
| [DualGraph](https://aclanthology.org/2026.findings-emnlp.1319/) · Findings EMNLP 2026 | Introduces [SpecsQA](../dataset-cards/table-rag/specsqa.md) | §§3–4 and Table 2. Exhaustive product lists and factual correctness expose differences between semantic retrieval and symbolic queries. |
| [OAKS](https://aclanthology.org/2026.acl-long.1956/) · ACL 2026 Long | Introduces [OAKS](../dataset-cards/text-rag/oaks.md) | §§3–4 and Appendix B.2. Measure acquisition in stream steps. Public Novel has 435 questions versus 870 reported in the paper. |
| [TimelyRAG](https://arxiv.org/abs/2609.11572) · September 2026 preprint | Introduces [TimelyQABench](../dataset-cards/text-rag/timelyqabench.md) | §§4–5 and Tables 4–6. Four synthetic Korean domains with policy-version qrels and judged temporal validity. |
| [How You Ask Matters](https://aclanthology.org/2026.emnlp-main.2156/) · EMNLP 2026 main | Introduces [Query Robustness](../dataset-cards/text-rag/query-robustness.md) | §§3–4 and §6. Compare equivalent questions on answer quality, decision flips and call counts; 22,183 released forms include 3,000 originals. |
| [HARP](https://arxiv.org/abs/2609.14116) · September 2026 preprint | Introduces recording-local tasks in [HARP Audio QA](../dataset-cards/multimodal-rag/harp-audio.md) | §§III–V. Separate published music and health tracks from the separately licensed emotion track. |
| [CASTELLA](https://arxiv.org/abs/2511.15131) · ICASSP 2026 | Introduces [CASTELLA](../dataset-cards/multimodal-rag/castella.md) | §§4–5 and Table 3. Human timestamps and temporal IoU score within-recording sound localization. |
| [RAGCap-Bench](https://aclanthology.org/2026.aacl-long.245/) · IJCNLP–AACL 2026 Long, November | Introduces [RAGCap-Bench](../dataset-cards/text-rag/ragcap-bench.md) | §3.4, §4.4 and Appendix I. Process MCQs use EM/F1. A separate WebThinker experiment actually evaluates BrowseComp and other web QA tasks under a search-call budget. |
| [Better Together](https://aclanthology.org/2026.emnlp-industry.143/) · EMNLP 2026 Industry | Evaluates [HotpotQA](../dataset-cards/text-rag/hotpotqa.md), [AmbigNQ](../dataset-cards/text-rag/ambigqa.md) and [EnterpriseRAG-Bench](../dataset-cards/text-rag/enterpriserag-bench.md) | §4 and Table 2. Uses the first 5,000 training items, all 2,002 development queries and 470 enterprise queries with relevance labels, respectively. Compares retrieval metrics with fixed reranking and diversification. |

<a name="november-maintenance-new-evaluation-contracts"></a>

## November 1 additions

Each row states **introduces**, **extends**, or **actually evaluates**. A bibliography mention alone does not create an adoption relation. RACE, FACT, agent frameworks and evaluator libraries remain methods, not additional datasets. Dataset descriptions preserve native contracts; a paper-specific transformation is not silently promoted to the original dataset.

### Search agents and research reports

| Source / publication | Resource and relation | Locator and evaluation value |
|---|---|---|
| [BrowseComp](https://arxiv.org/abs/2504.12516) · April 2025 report, foundational supplement | Introduces [BrowseComp](../dataset-cards/text-rag/browsecomp.md) | §§4.1–4.2, Table 3. Live-web search with short answers and calibration, without fixed qrels. |
| [BrowseComp-Plus](https://aclanthology.org/2026.acl-long.1023/) · ACL 2026 Long; August 2025 preprint | Introduces [fixed-corpus conversion](../dataset-cards/text-rag/browsecomp-plus.md) | Benchmark construction and separate retriever/agent experiments. 830 queries, 100,195 documents; evidence_docs and answer-bearing gold_docs have different roles. |
| [DeepSearchQA](https://storage.googleapis.com/deepmind-media/DeepSearchQA/DeepSearchQA_benchmark_paper.pdf) · December 2025 technical report | Introduces [DeepSearchQA](../dataset-cards/text-rag/deepsearchqa.md) | §§3.1–3.2, Table 4. Macro answer-set F1 and strict complete correctness reward exhaustive discovery, not document recall. |
| [DeepResearch Bench](https://proceedings.iclr.cc/paper_files/paper/2026/hash/465f22be10e07b301c6ed58f0472f704-Abstract-Conference.html) · ICLR 2026; June 2025 preprint | Introduces [100-task report benchmark](../dataset-cards/text-rag/deepresearch-bench.md) | Author manuscript §§3.1–3.2/4: RACE report quality versus FACT citation support. May/September 2026 evaluator changes affect historical comparability. |
| [DeepResearch Bench II](https://arxiv.org/abs/2601.08536) · January 2026 preprint, September revision | Introduces [rubric benchmark](../dataset-cards/text-rag/deepresearch-bench-ii.md) | §3.1, §4, Appendix A. 132 released tasks/9,430 criteria; October leaderboard eligibility is 130 tasks. Rubric recall is not retrieval recall. |
| [SGR-Bench](https://arxiv.org/abs/2605.22219) · May 2026 preprint | Introduces [state-dependent web retrieval tasks](../dataset-cards/text-rag/sgr-bench.md) | §§3.2–3.4/4.1–4.2, Table 2, Appendix A. Fifty paired information needs test fields, complete rows and ordering; 100 prompts are not 100 independent needs. |
| [WebWeaver](https://proceedings.iclr.cc/paper_files/paper/2026/file/07fa611a88be1832f4c6a96f044ebede-Paper-Conference.pdf) · ICLR 2026 | Actually evaluates DeepResearch Bench | §§4.1–4.2, Table 1, Appendix B. Three independent runs; the framework is not another benchmark. |
| [DuMate-DeepResearch](https://arxiv.org/html/2606.07299) · June 2026 technical report | Actually evaluates DeepResearch Bench and II | §§3–3.1, Tables 1–2. Its results average three runs; cited baseline leaderboard results were not all rerun in the same environment. |

### Time, uncertainty, preference and enterprise sources

| Source / publication | Resource and relation | Locator and evaluation value |
|---|---|---|
| [TEMPO](https://arxiv.org/abs/2601.09523) · January 2026 preprint | Introduces [TEMPO](../dataset-cards/text-rag/tempo.md) | §§3–5, Table 6/Appendix G.3. Temporal retrieval and downstream QA; official code excludes negative_ids, unlike a stricter unfiltered corpus adaptation. |
| [TempRAGEval](https://aclanthology.org/2025.findings-emnlp.167/) · Findings EMNLP 2025 | Introduces [TempRAGEval](../dataset-cards/text-rag/temprageval.md) | §3, §5, Appendix F. Human time perturbations with unchanged answers; either annotated sentence can satisfy evidence recall. Query files require access approval. |
| [WikiRecentChanges](https://aclanthology.org/2026.findings-acl.103/) · Findings ACL 2026 | Introduces [controlled conflict data](../dataset-cards/text-rag/wikirecentchanges.md) | §3.1, §4/Tables 1–4. Mutable/stable facts and factual/counterfactual supplied contexts; no open retrieval or continuous indexing protocol. |
| [MTRAG-UN](https://aclanthology.org/2026.findings-acl.503/) · Findings ACL 2026 | Introduces [MTRAG-UN](../dataset-cards/text-rag/mtrag-un.md) | §2, §§3.1–3.3. Paper: 666 tasks/six domains; currently released references: 507/four domains. Unanswerable and underspecified targets differ. |
| [MTRAGEval](https://aclanthology.org/2026.semeval-1.447/) · SemEval 2026 Task 8 | Actually evaluates MTRAG-UN; uses [MTRAG](../dataset-cards/text-rag/mtrag.md) as training data | Task setup and evaluation sections. Training and test resources are distinct; neither task name nor framework creates a third dataset. |
| [RAG-RewardBench](https://aclanthology.org/2025.findings-acl.877/) · Findings ACL 2025 | Introduces [preference pairs](../dataset-cards/text-rag/rag-rewardbench.md) | §§3.3/4.1. Chosen/rejected judgments with swapped-order evaluation; citation, refusal and conflict conditions assess judges, not retriever qrels. |
| [Ragability](https://aclanthology.org/2026.lrec-1.182/) · LREC 2026 | Introduces [Ragability Corpus](../dataset-cards/text-rag/ragability.md) | §2, §4.1/Table 2. Fifty-three seed rows produce 1,060 prompt cases per model; the companion library is not a second dataset. |
| [evolveQA](https://aclanthology.org/2026.emnlp-main.2373/) · EMNLP 2026 main, October | Introduces [cutoff-aligned controls](../dataset-cards/text-rag/evolveqa.md) | §§2–3/4.1, Table 4, Appendices C.1/D.3. Closed-book accuracy and outdated-response rate; 4,967 cutoff rows correspond to 937 domain/question-ID keys. Not native update-RAG. |
| [EnterpriseRAG-Bench](https://arxiv.org/abs/2605.05253) · May 2026 preprint | Introduces [synthetic enterprise QA](../dataset-cards/text-rag/enterpriserag-bench.md) | §§4–5 and official answer evaluator. More than 500K documents/500 core questions; completeness and conflicting records expose missing evidence. Gold corrections require version control. |

### Graph, scholarly, document and video evaluation

| Source / publication | Resource and relation | Locator and evaluation value |
|---|---|---|
| [Graph Counselor](https://aclanthology.org/2025.acl-long.1202/) · ACL 2025 Long | Actually evaluates [GRBench](../dataset-cards/graph-rag/grbench.md), introduced in Findings ACL 2024 | Experimental setup and Table 1. Ten text-attributed graphs; ROUGE-L/QwenScore differ from the original Graph-CoT GPT-4 judge. |
| [ARK](https://aclanthology.org/2026.acl-long.714/) · ACL 2026 Long | Actually evaluates [STaRK](../dataset-cards/graph-rag/stark.md), introduced at NeurIPS 2024 D&B | §4.1/Table 1, Appendix Tables 5–6. Entity retrieval under lexical-search/traversal budgets; teacher distillation is separate from training-free evaluation. |
| [WildGraphBench](https://aclanthology.org/2026.findings-acl.679/) · Findings ACL 2026 | Introduces [WildGraphBench](../dataset-cards/graph-rag/wildgraphbench.md) | §§3.5/4.1, Table 2. Current release: 1,197 questions; abstract: 1,100. Index external reference pages, not gold Wikipedia summaries. |
| [CiteRAG](https://doi.org/10.1145/3774904.3792075) · WWW 2026 | Introduces [academic citation prediction](../dataset-cards/text-rag/citerag.md) | §§2/5, Table 2. Bibliographies and local citation placeholders; released Task-2 normalization differs from paper PACA and must be disclosed. |
| [UniDoc-Bench](https://aclanthology.org/2026.findings-emnlp.534/) · Findings EMNLP 2026, October | Introduces [UniDoc-Bench](../dataset-cards/multimodal-rag/unidoc-bench.md) | §§3–4, Tables 3–4. Eight actual domain splits × 200 queries; README's 1,742/single-test claim conflicts with the released configuration. Human-validation claims also differ by version. |
| [ViDoRe v3](https://arxiv.org/abs/2601.08620) · January 2026 preprint | Extends [ViDoRe](../suite-cards/vidore.md), not a duplicate suite record | Dataset construction and retrieval/grounding/generation evaluation. Eight public/two private components; reference answers and boxes extend older retrieval-only contracts. |
| [M4-RAG](https://openaccess.thecvf.com/content/CVPR2026/html/Anugraha_M4-RAG_A_Massive-Scale_Multilingual_Multi-Cultural_Multimodal_RAG_CVPR_2026_paper.html) · CVPR 2026 | Introduces [RAG suite conversions](../suite-cards/m4-rag.md) of CVQA/WorldCuisines | Data construction and evaluation sections. Source VQA, Wikipedia pool and language variants remain distinct; answer-containing chunks are not independent qrels. |
| [CRAG-MM](https://arxiv.org/abs/2510.26160) · October 2025 preprint; KDD Cup 2025 resource | Introduces [CRAG-MM](../dataset-cards/multimodal-rag/crag-mm.md), not the earlier text CRAG | §§2–5. Single/multi-turn wearable-image QA with mock search, refusal and conversation stopping. A competition association is not main-track publication. |
| [CFVBench](https://doi.org/10.1145/3774904.3792726) · WWW 2026 | Introduces [fine-grained video RAG](../dataset-cards/multimodal-rag/cfvbench.md) | §3, §4.1. Visual/transcript keypoints; no verified per-question temporal interval in checked public QA. Paper/repository QA counts differ. |
| [VideoRAG](https://doi.org/10.1145/3770854.3783944) · KDD 2026 | Introduces [LongerVideos](../dataset-cards/multimodal-rag/longervideos.md) | §4.1, Appendices A/C. Public 164-video/602-query file has no reference answers; model-comparison win rate is not answer accuracy. |
| [VimRAG](https://arxiv.org/abs/2602.12735) · February 2026 preprint, April revision | Introduces [XVBench](../dataset-cards/multimodal-rag/xvbench.md) | §4.1/Table 2, Appendices B/J. 497 queries, 138 with multiple reference clips; checked clip sets never cross source-video IDs. |

Version maintenance also preserves [GraphRAG-Bench](../dataset-cards/graph-rag/graphrag-bench.md)'s 2025 release ID while recording author-reported ICLR 2026 acceptance. [ViDoRAG](https://aclanthology.org/2025.emnlp-main.464/) introduces the existing [ViDoSeek](../dataset-cards/multimodal-rag/vidoseek.md); no unsupported VRAGBench alias record is added. The [classification assessment](taxonomy.md#november-2026-classification-assessment) retains source categories and extends capability/annotation facets instead.

## Text, conversation and multilingual use

| Paper / venue | Catalog entry or upstream source | Experimental locator and boundary |
|---|---|---|
| [MAIN-RAG](https://aclanthology.org/2025.acl-long.131/) · ACL 2025 Long | [TriviaQA](../dataset-cards/text-rag/triviaqa.md), [PopQA](../dataset-cards/text-rag/popqa.md), [ALCE](../suite-cards/alce.md) / ASQA | §4.1, Figure 7, Table 1. TriviaQA-unfiltered uses 11,313 queries; long-tail PopQA uses 1,399. ARC-Challenge is an additional unindexed task. |
| [Astute RAG](https://aclanthology.org/2025.acl-long.1476/) · ACL 2025 Long | [NQ](../dataset-cards/text-rag/natural-questions.md), TriviaQA, PopQA, BioASQ | Appendix B, data collection. Its selected BioASQ release is not the catalog's 2026 Task 14b. |
| [UniConv](https://aclanthology.org/2025.acl-long.344/) · ACL 2025 Long | [QReCC](../dataset-cards/text-rag/qrecc.md), [TopiOCQA](../dataset-cards/text-rag/topiocqa.md), [OR-QuAC](../dataset-cards/text-rag/or-quac.md) | §4.1, Appendix A.1. INSCIT and FaithDial are also used; first-stage retrieval, response generation and reliability have different targets. |
| [S2G-RAG](https://aclanthology.org/2026.acl-long.1185/) · ACL 2026 Long | TriviaQA, [HotpotQA](../dataset-cards/text-rag/hotpotqa.md), [2WikiMultiHopQA](../dataset-cards/text-rag/2wikimultihopqa.md) | Iterative-retrieval experiments on the three named QA datasets. Extracting sentences is a system step, not new native evidence gold. |
| [CARL](https://aclanthology.org/2026.acl-long.258/) · ACL 2026 Long | NQ, HotpotQA, TriviaQA, [FEVER](../dataset-cards/text-rag/fever.md), [WoW](../dataset-cards/text-rag/wizard-of-wikipedia.md) | §4, Table 1, Appendix A/Table 5. Also T-REx and zsRE. The paper fixes 2018 Wikipedia and top-3 passages; those settings are not universal native protocols. |
| [All Languages Matter](https://aclanthology.org/2026.acl-long.338/) · ACL 2026 Long | [MKQA](../dataset-cards/text-rag/mkqa.md), [KILT](../suite-cards/kilt.md) / NQ | §2.2, Table 5. A 2.7K overlap subset in 13 languages, externally constructed multilingual Wikipedia and character 3-gram recall; not native MKQA qrels. |
| [RaCoT](https://ojs.aaai.org/index.php/AAAI/article/view/40260) · AAAI 2026 Technical | PopQA, TriviaQA-unfiltered, HotpotQA, 2WikiMultiHopQA | Experimental Settings, Tables 2–3. Also ARC-Challenge/OpenBookQA; the selected corpora and adversarial experiments must be reported separately. |

## Graph-structured retrieval and chunking

| Paper / venue | Catalog entry or source | Experimental locator and boundary |
|---|---|---|
| [HippoRAG 2](https://proceedings.mlr.press/v267/gutierrez25a.html) · ICML 2025 | NQ, PopQA, [MuSiQue](../dataset-cards/text-rag/musique.md), 2WikiMultiHopQA, HotpotQA, [NarrativeQA](../dataset-cards/text-rag/narrativeqa.md) | §4.2, Tables 1–3. Samples and a separate LV-Eval conversion test factual, associative and discourse tasks. Constructed graphs do not change source-dataset gold. |
| [KG-Agent](https://aclanthology.org/2025.acl-long.468/) · ACL 2025 Long | [CWQ](../dataset-cards/graph-rag/complexwebquestions.md), [KQA Pro](../dataset-cards/graph-rag/kqa-pro.md), [WebQSP](../dataset-cards/graph-rag/webqsp.md), [GrailQA](../dataset-cards/graph-rag/grailqa.md), [MetaQA](../dataset-cards/graph-rag/metaqa.md) | §4.1, Tables 2/3/5. Existing-KB reasoning is not source-prose GraphRAG citation completeness. |
| [HiChunk](https://aclanthology.org/2026.acl-long.1372/) · ACL 2026 Long | [HiCBench](../dataset-cards/text-rag/hicbench.md), [QASPER](../dataset-cards/text-rag/qasper.md), [GutenQA](../dataset-cards/text-rag/gutenqa.md), [OHRBench](../dataset-cards/multimodal-rag/ohrbench.md), [LongBench](../suite-cards/longbench.md) | §5.1, Tables 2–3, Appendix Table A1. Cut-point F1, evidence recall and final answering are distinct. Structural GovReport/QASPER settings are also used for training and boundary evaluation. |
| [Beyond Chunking / DISRetrieval](https://aclanthology.org/2026.acl-long.829/) · ACL 2026 Long | QASPER, [QuALITY](../dataset-cards/text-rag/quality.md), NarrativeQA, LongBench MultiFieldQA-zh | §4.1, Appendix B/Table 8. QuALITY uses labeled dev, not hidden test. Discourse-tree nodes are constructed representations, not native evidence annotations. |

## New text/structured benchmarks and long-context controls

| Introducing paper / venue | Dataset | Evaluation boundary |
|---|---|---|
| [SafeRAG](https://aclanthology.org/2025.acl-long.230/) · ACL 2025 Long | [SafeRAG](../dataset-cards/text-rag/saferag.md) | §3 construction, §4 evaluation. Chinese attacks vary by injection stage/intensity; AFR and ASR have opposite directions. |
| [LaRA](https://proceedings.mlr.press/v267/li25dv.html) · ICML 2025 | [LaRA](../dataset-cards/text-rag/lara.md) | §§3–4 and released evaluation scripts. 32k/128k contexts, four QA tasks, human seeds plus model generation and sampled validation; no native chunk-boundary gold. |
| [LongBench v2](https://aclanthology.org/2025.acl-long.183/) · ACL 2025 Long | [LongBench v2](../dataset-cards/text-rag/longbench-v2.md) | Dataset section and model/RAG comparisons; released pred.py supports --rag. Native multiple-choice long-context QA has answer labels, not qrels. |
| [SSRB](https://proceedings.neurips.cc/paper_files/paper/2025/hash/631bbd89466337712564872840a401be-Abstract-Datasets_and_Benchmarks_Track.html) · NeurIPS 2025 D&B | [SSRB](../dataset-cards/table-rag/ssrb.md) | §4.1–4.2, Tables 3–4. Semi-structured object retrieval with R@20/nDCG@10; no answer-generation target. |
| [Worse than Zero-shot?](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ed25c00ff6900989116d3ba5d607d33d-Abstract-Datasets_and_Benchmarks_Track.html) · NeurIPS 2025 D&B | [RAGuard](../dataset-cards/text-rag/raguard.md) | §4, Table 2. Misleading retrieval in fact checking; no-context, retrieved-context and oracle conditions remain separate. |
| [Conflicting Web References](https://aclanthology.org/2026.acl-long.11/) · ACL 2026 Long | [ConfRAG](../dataset-cards/text-rag/confrag.md) | §3.4, §4, Table 2. Answer clustering and answer/reason coverage over contradictory references, not a single unique answer/evidence set. |
| [MINTQA](https://aclanthology.org/2026.acl-long.18/) · ACL 2026 Long | [MINTQA](../dataset-cards/graph-rag/mintqa.md) | §4.2, §§6–7, Table 3, Appendix E.2. New/long-tail knowledge and dynamic retrieval; answer containment is not path correctness. |

## Multimodal use and releases

| Paper / venue | Catalog entry or source | Experimental locator and boundary |
|---|---|---|
| [NoteMR](https://openaccess.thecvf.com/content/CVPR2025/html/Fang_Notes-guided_MLLM_Reasoning_Enhancing_MLLM_with_Knowledge_and_Visual_Notes_CVPR_2025_paper.html) · CVPR 2025 | [OK-VQA](../dataset-cards/multimodal-rag/ok-vqa.md), [A-OKVQA](../dataset-cards/multimodal-rag/a-okvqa.md) | §4.1, Tables 1–2. OK-VQA test uses Google Search Corpus; A-OKVQA validation uses Wikipedia. Visual input is supplied. |
| [VDocRAG](https://openaccess.thecvf.com/content/CVPR2025/papers/Tanaka_VDocRAG_Retrieval-Augmented_Generation_over_Visually-Rich_Documents_CVPR_2025_paper.pdf) · CVPR 2025 | [OpenDocVQA](../dataset-cards/multimodal-rag/opendocvqa.md), [DocVQA](../dataset-cards/multimodal-rag/docvqa.md), [InfographicVQA](../dataset-cards/multimodal-rag/infographicvqa.md), [DUDE](../dataset-cards/multimodal-rag/dude.md) | §5.1/Table 2 sources; Tables 3–4 retrieval/QA. DocVQA is a training source; InfoVQA/DUDE appear in training and evaluation. ChartQA/SlideVQA are also evaluated. Converted pools are not original single-image tasks. |
| [VisRAG](https://proceedings.iclr.cc/paper_files/paper/2025/file/3640a1997a4c9571cea9db2c82e1fc35-Paper-Conference.pdf) · ICLR 2025 | [ArXivQA](../dataset-cards/multimodal-rag/arxivqa.md), [PlotQA](../dataset-cards/multimodal-rag/plotqa.md), InfographicVQA, [MP-DocVQA](../dataset-cards/multimodal-rag/mp-docvqa.md), [ChartQA](../dataset-cards/multimodal-rag/chartqa.md), [SlideVQA](../dataset-cards/multimodal-rag/slidevqa.md) | §3.3/Table 1, Tables 2–3. Explicit filtered retrieval conversions; no invented separate VisRAG-Bench dataset. ICLR membership uses the current 2026 directory, not a retroactive grade claim. |
| [MRAG-Bench](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ee46288ab2aaf5c6e53aebebe719712c-Abstract-Conference.html) · ICLR 2025 | [MRAG-Bench](../dataset-cards/multimodal-rag/mrag-bench.md) | Introducing paper and official release. 1,353 human-annotated multiple-choice questions, 16,130 images and nine scenarios. Distinguish no-retrieval, retrieved-image and gold-image conditions. |
| [CoRe-MMRAG](https://aclanthology.org/2025.acl-long.1583/) · ACL 2025 Long | [InfoSeek](../dataset-cards/multimodal-rag/infoseek.md), [Encyclopedic-VQA](../dataset-cards/multimodal-rag/encyclopedic-vqa.md) | §4.1–4.3, Tables 1–2. Evaluates InfoSeek validation and Encyclopedic-VQA test excluding two-hop questions (4.7K triplets); corpus filtering, URL-based article recall and answer metrics are separate. |
| [REAL-MM-RAG](https://aclanthology.org/2025.acl-long.1528/) · ACL 2025 Long | [REAL-MM-RAG](../dataset-cards/multimodal-rag/real-mm-rag.md) | §5.1, Tables 2–3 and S1. Four document subsets, 4,553 base queries and levels 0–3 of phrasing. Synthetic page relevance scores retrieval, not an official answer-generation task or region/cell localization. |
| [OCR Hinders RAG](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_OCR_Hinders_RAG_Evaluating_the_Cascading_Impact_of_OCR_on_ICCV_2025_paper.html) · ICCV 2025 | [OHRBench](../dataset-cards/multimodal-rag/ohrbench.md) | §§3–4. OCR edit distance, LCS evidence inclusion and answer F1 are different measures. Canonical page evidence must be preserved under corruption. |
| [MMDocRAG](https://proceedings.neurips.cc/paper_files/paper/2025/file/1a93178950e92fd2e7b7448f7d68fd7d-Paper-Datasets_and_Benchmarks_Track.pdf) · NeurIPS 2025 D&B | [MMDocRAG](../dataset-cards/multimodal-rag/mmdocrag.md) | Benchmark construction and retrieval/generation evaluation. Expert-annotated cross-page multimodal evidence is not reducible to answer accuracy. |
| [RAG-IGBench](https://proceedings.neurips.cc/paper_files/paper/2025/hash/b0a4b3e384b4554e65a47ad1f6b0310a-Abstract-Datasets_and_Benchmarks_Track.html) · NeurIPS 2025 D&B | [RAG-IGBench](../dataset-cards/multimodal-rag/rag-igbench.md) | §3.2, Tables 1/3/5. Image-text interleaved output; source queries and expanded bilingual rows are different counting units. |
| [M²RAG](https://doi.org/10.1145/3746027.3755625) · ACM MM 2025 | [M²RAG](../dataset-cards/multimodal-rag/m2rag.md) | Author manuscript §5, Tables 3–4. WebQA/Factify conversions; not the prose/table/KG mmRAG release. |
| [Visual-RAG](https://doi.org/10.1145/3805712.3808615) · SIGIR 2026 Resource | [Visual-RAG](../dataset-cards/multimodal-rag/visual-rag.md) | Author manuscript §5.1, Tables 2–3. Use corrected v2 (374 questions); retained track and manuscript versions matter. |
| [Utility-Oriented Visual Evidence Selection](https://aclanthology.org/2026.acl-long.1620/) · ACL 2026 Long | [MRAG-Bench](../dataset-cards/multimodal-rag/mrag-bench.md), Visual-RAG | §5.1, Tables 1–2. Gold images plus CLIP candidates form a fixed selection pool, not unrestricted full-corpus retrieval. |

## Useful supplementary sources

- [LongBench, ACL 2024 Long](https://aclanthology.org/2024.acl-long.172/): [suite](../suite-cards/longbench.md). A prior-year source for long-context/retrieval compression; converted subsets are distinct from originals.
- [FRAMES, NAACL 2025](https://aclanthology.org/2025.naacl-long.243/): [dataset](../dataset-cards/text-rag/frames.md). Important multi-document reasoning; NAACL is not relabeled ACL main.
- [RAG-QA Arena, EMNLP 2024](https://aclanthology.org/2024.emnlp-main.249/): [LFRQA](../dataset-cards/text-rag/lfrqa.md) is data; Arena is an answer-comparison protocol.
- [MIRAGE, Findings ACL 2024](https://aclanthology.org/2024.findings-acl.372/): [suite](../suite-cards/mirage.md). Medical RAG evaluation with exact context-removed and question-only retrieval settings, retaining Findings publication type.
- [LumberChunker, Findings EMNLP 2024](https://aclanthology.org/2024.findings-emnlp.377/): [GutenQA](../dataset-cards/text-rag/gutenqa.md) was later used by ACL 2026 HiChunk. The original 3,000-question retrieval set and separate 280-question generation experiment differ.
- [mmRAG, author preprint/release](https://arxiv.org/abs/2505.11180): [dataset](../dataset-cards/text-rag/mmrag.md). Fixed 512-token chunk qrels and routing labels; no invented venue grade.
- [FinChain, ACL 2026 Long](https://aclanthology.org/2026.acl-long.662/): [control](../dataset-cards/cross-cutting/finchain.md). Financial reasoning with executable intermediate targets, not native RAG or a retrieval corpus.

## Selection for the two research problems

For chunking, combine HiCBench hierarchy boundaries, QASPER evidence paragraphs, GutenQA substring anchors and OHRBench OCR perturbations, then test transfer on multi-hop data. Separate boundary agreement, complete evidence within a token budget and final answering. LaRA/LongBench v2 supplement answer-level tests; they do not replace chunking gold.

For multimodal fragmentation, combine MMDocIR page/layout retrieval, MMDocRAG cross-page QA, OpenDocVQA's retrieval setting and DUDE/TAT-DQA document evidence. RAG-IGBench adds interleaved-output evaluation; Visual-RAG adds external visual knowledge. Single-image QA, page hits, candidate selection and complete cross-modal evidence chains are distinct targets. Missing relation labels require independent annotation, as described in [evidence ground truth](evidence-ground-truth.md) and [benchmark construction](benchmark-construction.md).

## Maintenance and remaining gaps

Expand from experiment sections, not reference lists. Preserve introduction/training/evaluation roles, split, corpus snapshot, version, sampling, metrics and evaluator. Check original evidence granularity and license before synchronizing both languages. `source_checked` means source-audited, not reproduced.

Exact RAG conversions of ARC-Challenge, OpenBookQA, INSCIT, FaithDial, T-REx, zsRE and LV-Eval remain unindexed in this pass. BEIR, ChatRAG Bench, LongBench and MIRAGE have partial component indexes, explicitly identified in their protocols. Linked native cards are not the full suite's reprocessed evaluation files. Continue through the [coverage policy](coverage-policy.md), without duplicating arbitrary subsets or unsupported paper-only assets.
