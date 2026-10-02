# RAG paper and benchmark adoption, 2025–2026

[简体中文](recent-paper-index.zh-CN.md)

Checked on 2026-10-02. This index emphasizes published 2025 and 2026 work, supplements missing 2024 releases, and traces older datasets reused in recent experiments. It is a curated evidence index, not an exhaustive literature census or a quality ranking. Repeated use by several papers does not create several dataset records.

## Venue and publication scope

The reference is CCF's **seventh-edition formal directory**, published on 2026-03-31: [official PDF](https://www.ccf.org.cn/ccf/contentcore/resource/download?ID=112CF3BF7E1140ACEB271ADAED12A67ADFABB8FF099E40C2759502A85C8A281F). PDF pages 35, 47 and 57 list SIGIR, ACM MM and the AI A venues, including ACL, AAAI, NeurIPS, ICML, CVPR, ICCV and **ICLR**. Page 58 places EMNLP, NAACL and IJCAI in B. Some category webpages still show an older list; the formal PDF takes precedence. Applying this current directory consistently is not a claim that every venue had the same grade in the paper's publication year.

CCF considers formal Full/Regular papers and explicitly excludes Findings, Short/Demo papers and companion Workshops. [Official policy](https://www.ccf.org.cn/Academic_Evaluation/By_category/) Track labels below preserve Long, Datasets and Benchmarks (D&B), and Resource distinctions rather than silently treating all conference-associated material as main-track long papers. Institution-specific recognition is outside this catalog's scope. For 2026, only already published, verifiable materials as of the checking date are recorded.

The tables distinguish **introduction**, **training use** and **evaluation use**. Dataset cards retain native facts; sampled splits, external corpora and conversion-specific metrics remain properties of the paper's experiment. Machine-readable relationships are in [catalog/papers](../catalog/papers).

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
