# Selecting a benchmark

[简体中文](selecting-a-benchmark.zh-CN.md)

Start with the failure mode, then ask which upstream labels can actually score it. The cards linked from the [catalog](../README.md#datasets) document access, labels, protocol and limitations. The entries below are **shortlists**, not a leaderboard or an assertion that all datasets have equivalent licenses, splits or annotations.

| Research question | First inspect | What to score | Main limitation |
|---|---|---|---|
| Chunk boundary vs complete multi-hop evidence | [HiCBench](../dataset-cards/text-rag/hicbench.md), [HotpotQA](../dataset-cards/text-rag/hotpotqa.md), [2WikiMultiHopQA](../dataset-cards/text-rag/2wikimultihopqa.md), [MuSiQue](../dataset-cards/text-rag/musique.md) | Source-coordinate evidence coverage and answer quality | Supporting sentences are not unique optimal chunks |
| Long-document evidence retention | [QASPER](../dataset-cards/text-rag/qasper.md), [CLAP NQ](../dataset-cards/text-rag/clapnq.md), [QuALITY](../dataset-cards/text-rag/quality.md) | Evidence recall under a fixed token budget | QuALITY has no native minimal evidence span |
| Grounded answer and citation | [ALCE](../suite-cards/alce.md), [RAGBench](../dataset-cards/text-rag/ragbench.md), [MAVIS](../dataset-cards/multimodal-rag/mavis.md) | Answer correctness, claim/citation support, coverage | Retrieved context and source-collection variants differ |
| Visual page and layout retrieval | [MMDocIR](../dataset-cards/multimodal-rag/mmdocir.md), [SlideVQA](../dataset-cards/multimodal-rag/slidevqa.md), [ViDoRe](../suite-cards/vidore.md) | Page Recall@K, region coverage where labeled | Layout boxes need not be question-specific evidence |
| Cross-page/cross-modal evidence | [MMDocRAG](../dataset-cards/multimodal-rag/mmdocrag.md), [XL-DocBench](../dataset-cards/multimodal-rag/xl-docbench.md), [MAVIS](../dataset-cards/multimodal-rag/mavis.md), [MultiModalQA](../dataset-cards/multimodal-rag/multimodalqa.md) | Complete evidence set/chain plus answer/citation | Annotation granularity differs by release |
| Open table plus text | [OTT-QA](../dataset-cards/table-rag/ott-qa.md), [HybridQA](../dataset-cards/table-rag/hybridqa.md), [TAT-QA](../dataset-cards/table-rag/tat-qa.md) | Table/passage retrieval and downstream QA | HybridQA and TAT-QA provide a context; OTT-QA is open retrieval |
| Graph-grounded retrieval/reasoning | [GraphRAG-Bench](../dataset-cards/graph-rag/graphrag-bench.md), [GrailQA](../dataset-cards/graph-rag/grailqa.md), [WebQuestionsSP](../dataset-cards/graph-rag/webqsp.md) | Graph evidence, path/logical-form correctness and answer | A KBQA logical form is not a GraphRAG citation graph |
| Retriever only or robustness control | [BEIR](../suite-cards/beir.md), [BRIGHT](../dataset-cards/text-rag/bright.md), [M-BEIR](../suite-cards/m-beir.md) | Official qrels/ranking metrics | No intrinsic answer-generation ground truth |

<a name="capability-routes"></a>

## Capability routes beyond source categories

These routes cross the existing category folders. They index different evaluation contracts, not comparable leaderboard columns. Publication and experiment locators are in the [recent-paper index](recent-paper-index.md).

| Evaluation need | Start with | Contract to preserve |
|---|---|---|
| Adaptive search and stopping | [BrowseComp-Plus](../dataset-cards/text-rag/browsecomp-plus.md), [BrowseComp](../dataset-cards/text-rag/browsecomp.md), [DeepSearchQA](../dataset-cards/text-rag/deepsearchqa.md), [SGR-Bench](../dataset-cards/text-rag/sgr-bench.md) | Fixed corpus versus live web; evidence/gold documents, complete answer sets, structured rows and tool budgets are different targets |
| Research-report quality | [DeepResearch Bench](../dataset-cards/text-rag/deepresearch-bench.md), [DeepResearch Bench II](../dataset-cards/text-rag/deepresearch-bench-ii.md) | RACE/FACT versus content rubrics; pin current task eligibility and judge version; no gold action trajectory is implied |
| Temporal evidence versus parametric knowledge | [TEMPO](../dataset-cards/text-rag/tempo.md), [TempRAGEval](../dataset-cards/text-rag/temprageval.md), [WikiRecentChanges](../dataset-cards/text-rag/wikirecentchanges.md), [evolveQA](../dataset-cards/text-rag/evolveqa.md) | Retrieved-period coverage, date perturbation, supplied-context conflict and closed-book cutoff probes are separate tests; none alone measures continuous index updates |
| Clarification, abstention and conflict | [MTRAG-UN](../dataset-cards/text-rag/mtrag-un.md), [Ragability](../dataset-cards/text-rag/ragability.md), [ConfRAG](../dataset-cards/text-rag/confrag.md) | Unanswerable versus underspecified queries, consistent versus conflicting context, and reference versus full-RAG conditions |
| Response judges and preference alignment | [RAG-RewardBench](../dataset-cards/text-rag/rag-rewardbench.md), [RAGTruth](../dataset-cards/text-rag/ragtruth.md) | Pairwise ranking versus response error-span detection; neither score establishes open-corpus retrieval quality |
| Dense enterprise distractors | [EnterpriseRAG-Bench](../dataset-cards/text-rag/enterpriserag-bench.md) | Synthetic cross-source coherence, no-answer cases and revisable gold sets; separate release-specific corrections from fixed leaderboard labels |
| Graph traversal versus global synthesis | [STaRK](../dataset-cards/graph-rag/stark.md), [GRBench](../dataset-cards/graph-rag/grbench.md), [WildGraphBench](../dataset-cards/graph-rag/wildgraphbench.md) | Entity ranking versus answer judges versus statement coverage; forbid indexing Wikipedia gold summaries in WildGraphBench |
| Academic reference recommendation | [CiteRAG](../dataset-cards/text-rag/citerag.md) | Bibliography/placeholder prediction, not claim entailment; released PACA aggregation differs from the paper definition |
| Video evidence retention | [CFVBench](../dataset-cards/multimodal-rag/cfvbench.md), [XVBench](../dataset-cards/multimodal-rag/xvbench.md), [LongerVideos](../dataset-cards/multimodal-rag/longervideos.md) | Video IDs, addressable clips and answer keypoints are not minimal temporal spans; LongerVideos has no released reference answers |
| Document/multilingual end-to-end controls | [UniDoc-Bench](../dataset-cards/multimodal-rag/unidoc-bench.md), [ViDoRe](../suite-cards/vidore.md), [M4-RAG](../suite-cards/m4-rag.md), [CRAG-MM](../dataset-cards/multimodal-rag/crag-mm.md) | Versioned retrieval/grounding/QA, language variants and multi-turn stopping; hold source visibility and budgets constant |

For the original chunking problem, BrowseComp-Plus adds document-level acquisition labels and TEMPO adds period coverage, but neither supplies optimal chunk boundaries. For multimodal fragmentation, UniDoc-Bench adds linked source facts and ViDoRe v3 adds grounding/answers; CFV/XVBench still need independent temporal or cross-element chain annotation where missing. Report oracle evidence, actual retrieval, complete-set coverage, answer/citation quality and cost separately.

### Recent additions

| Evaluation need | Start with | Evaluation contract |
|---|---|---|
| Alternative evidence and complete fact coverage | [RedQA](../dataset-cards/text-rag/redqa.md), [One Fact, Many Places](../dataset-cards/multimodal-rag/one-fact-many-places.md) | Group interchangeable sources for each fact. Require sufficient support for every required fact and distinguish complementary combinations from contextual mentions. |
| Acoustic evidence and localization | [HARP Audio QA](../dataset-cards/multimodal-rag/harp-audio.md), [CASTELLA](../dataset-cards/multimodal-rag/castella.md) | HARP music identifies whole-song intervals and answers. CASTELLA supplies human-marked event intervals. HARP health supports answer scoring. |
| Applicable versions and sequential adaptation | [TimelyQABench](../dataset-cards/text-rag/timelyqabench.md), [OAKS](../dataset-cards/text-rag/oaks.md) | Use version-level ranking for the former and answer-state recovery per stream step for the latter. Index visibility needs a timestamped write-and-query workload. |
| Retrieval decisions and agent step diagnosis | [Query Robustness](../dataset-cards/text-rag/query-robustness.md), [RAGCap-Bench](../dataset-cards/text-rag/ragcap-bench.md) | Pair equivalent question forms for routing and cost. Use controlled choices to diagnose intermediate capabilities. |
| Structured retrieval and exact filters | [MKG-RAG-Bench](../dataset-cards/graph-rag/mkg-rag-bench.md), [SpecsQA](../dataset-cards/table-rag/specsqa.md) | Score triple rankings with MKG-RAG-Bench qrels and evaluate product-list completeness with SpecsQA. |

## Selection checklist

1. Identify the target unit: source document, page, sentence, cell, region, graph path, atomic fact or final answer.
2. Check whether the **released** fields identify that unit. Do not upgrade a page label to a cell label by interpretation.
3. Choose a retrieval scope: fixed supplied context, document-local, multi-document, open corpus or time-varying web. Keep the official scope separate from an adapted one.
4. Fix split and source snapshot before chunking/indexing. Split by source document or source family, never random chunks.
5. Match denominators and budgets: Top-K documents and Top-K chunks are not comparable if token counts differ.
6. Report retrieval, complete evidence, answer and citation results separately. Include an oracle-evidence condition to localize failure.
7. Check license, gating, unavailable pages and official evaluator before committing to a large experiment.

For a new RAG method, use at least one in-domain benchmark and one transfer benchmark, then an error-analysis subset with independently checked source coordinates. Do not optimize against a test leaderboard repeatedly. Full recipes for the two motivating research problems are in [evidence ground truth](evidence-ground-truth.md).
