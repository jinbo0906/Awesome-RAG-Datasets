# Coverage choices and candidate queue

[简体中文](coverage-policy.zh-CN.md)

The catalog aims for useful, auditable coverage rather than a maximum row count. A name mentioned in a RAG paper can denote a primary dataset, a reprocessed variant, a suite, a corpus, an evaluation framework or only the paper's experiment. We add a record only when its entity, native task, access and source of key claims can be described without pretending it has annotations it does not release.

## Included now, with boundaries

- [RGB](../dataset-cards/text-rag/rgb.md) tests fixed-context robustness, not open-corpus retrieval. [RAGTruth](../dataset-cards/text-rag/ragtruth.md) labels generated-response hallucinations, not source evidence spans. [MTRAG](../dataset-cards/text-rag/mtrag.md) has separate reference and full-RAG settings.
- [BioASQ Task 14b](../dataset-cards/text-rag/bioasq-14b.md) is pinned to a challenge edition; [PUBHEALTH](../dataset-cards/text-rag/pubhealth.md) has a different paper/repository count and needs a newly constructed retrieval corpus.
- [MS MARCO Passage Ranking](../dataset-cards/text-rag/msmarco-passage.md) is a specific retrieval variant, not a synonym for original generative MS MARCO or TREC-DL.
- [MetaQA](../dataset-cards/graph-rag/metaqa.md) supplies a movie KB and hop-labeled QA, while Microsoft GraphRAG [podcast assets](../catalog/corpora/ms-graphrag-podcasts.yaml) are cataloged as a corpus rather than claimed to provide gold graph paths.
- [SQA](../dataset-cards/table-rag/sqa.md) supplies the table; [ToTTo](../dataset-cards/table-rag/totto.md) supplies highlighted cells. Their native results cannot be compared with open table retrieval without a documented conversion.

## Not automatically added as RAG datasets

| Candidate kind | Decision rule |
|---|---|
| Evaluator libraries such as [Ragas](https://docs.ragas.io/en/stable/concepts/metrics/overview/), DeepEval or TruLens | A scoring tool is not a fixed dataset. Document a specific released evaluation set, if any, as a separate object. |
| General quizzes and exams such as MMLU, TruthfulQA, MedQA or HLE | They test knowledge/reasoning but do not become native RAG without a specified source pool and evidence/retrieval protocol. A derived RAG version must be named separately. |
| Source collections such as MITRE ATT&CK, medical image archives, textbooks, news or podcast transcripts | Record as corpora when an identifiable snapshot/access can be given; do not infer gold query-answer or citation labels. |
| Suite subsets from [BEIR](../suite-cards/beir.md), [ViDoRe](../suite-cards/vidore.md), [M-BEIR](../suite-cards/m-beir.md) or [M2KR](../suite-cards/m2kr.md) | A converted subset may change corpus, split, qrels and metrics. Link it as a variant only after checking the exact release; do not silently copy the original dataset card. |
| Paper-only or unstable-release assets | Keep out of the source-checked catalog until canonical download, version and evaluator can be stated. A 403/429/timeout is inconclusive, not proof of removal. |

## Recent-paper coverage

The [2025–2026 paper adoption index](recent-paper-index.md) traces recent papers to their actual experimental datasets, preserving formal tracks, Findings, challenges and preprint status. CCF grades provide context rather than an inclusion gate. Older reused datasets and newly introduced benchmarks are both included, but a converted subset is not counted again as a new dataset. [MedQA](../dataset-cards/text-rag/medqa.md), [MedMCQA](../dataset-cards/text-rag/medmcqa.md) and [PubMedQA](../dataset-cards/text-rag/pubmedqa.md) have native cards and links through [MIRAGE](../suite-cards/mirage.md); their native tasks still do not supply open-retrieval evidence gold.

## High-value follow-up checks

[HARP Audio QA](../dataset-cards/multimodal-rag/harp-audio.md) and [CASTELLA](../dataset-cards/multimodal-rag/castella.md) now cover recording-local audio QA and acoustic event localization. [TimelyQABench](../dataset-cards/text-rag/timelyqabench.md) and [OAKS](../dataset-cards/text-rag/oaks.md) support version ranking and chronological replay. The following candidates still have specific access or protocol gaps.

- LongAudioQA describes a larger meeting QA release with timing evidence. The checked author repository still defers the evaluation files. [Paper](https://aclanthology.org/2026.findings-acl.1038/) · [Code](https://github.com/tangquanwei/GRGA)
- CrossModalQA describes complementary image/text chains and complete retrieval metrics. The benchmark download and evaluator are still unconfirmed. [Preprint](https://arxiv.org/abs/2609.05518)
- FRESCO studies recency-aware reranking over supplied candidate pools. A frozen evaluation bundle and exact rebuild are unconfirmed. [Paper](https://aclanthology.org/2026.findings-emnlp.54/) · [Generation code](https://github.com/facebookresearch/fresco)
- RAGPerf reports concurrent updates and queries in §5.5. The exact mixed workload could not be located in the checked public revision. [Paper](https://www.vldb.org/pvldb/vol19/p3689-li.pdf) · [Code](https://github.com/platformxlab/RAGPerf/tree/49c9794895666d029a3c98a48afd872197d83b23)

Other follow-up checks include release artifacts and licenses for TableRAG's ArcadeQA/BirdQA large-table variants and the versioned component conversions in ViDoRe and M2KR. [TableRAG paper](https://arxiv.org/abs/2410.04739) · [Upstream download issue](https://github.com/google-research/google-research/issues/3190)

November maintenance adds checked video entries, but [CFVBench](../dataset-cards/multimodal-rag/cfvbench.md)'s keypoints and [XVBench](../dataset-cards/multimodal-rag/xvbench.md)'s clip IDs still do not supply verified minimal temporal intervals; [LongerVideos](../dataset-cards/multimodal-rag/longervideos.md) lacks released reference answers. [MTRAG-UN](../dataset-cards/text-rag/mtrag-un.md)'s two unreleased domains, private ViDoRe v3 components, CiteRAG's unresolved data terms and larger same-name SGR releases with unconfirmed authorship remain explicit boundaries, not silently completed coverage. [ComplexWebQuestions](../dataset-cards/graph-rag/complexwebquestions.md)'s former homepage returned 404; its author code is linked while corrected data access still needs separate verification.

For any new candidate, use [the decision rule](benchmark-vs-dataset.md#decision-rule-for-new-entries) and [contribution checklist](../CONTRIBUTING.md). If a key fact is unknown, mark it unknown or keep the candidate here; never fill the gap with a secondary summary.
