# Coverage choices and candidate queue

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

## High-value follow-up checks

These are candidate investigations, **not** claims of completed review: verify publicly reproducible artifacts and licenses for TableRAG's ArcadeQA/BirdQA large-table variants ([paper](https://arxiv.org/abs/2410.04739), [upstream download issue](https://github.com/google-research/google-research/issues/3190)); separate versioned ViDoRe and M2KR component conversions; and audit video-RAG datasets for released temporal source coordinates, questions and evaluator. Additional domains—legal, finance, medical and code—should be selected through the same source/evidence tests, not become separate top-level categories by name alone.

For any new candidate, use [the decision rule](benchmark-vs-dataset.md#decision-rule-for-new-entries) and [contribution checklist](../CONTRIBUTING.md). If a key fact is unknown, mark it unknown or keep the candidate here; never fill the gap with a secondary summary.
