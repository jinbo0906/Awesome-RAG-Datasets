# Text RAG: from source retrieval to grounded answers

[简体中文](text-rag.zh-CN.md)

Text RAG includes document, paragraph and sentence retrieval; answer generation; multi-hop evidence; citation; robustness; and temporal or conversational variants. These are different protocols, not interchangeable scores. Start with [the dataset table](../../README.md#text-rag) and read each card's native retrieval scope before building an index.

| Subtrack | Good starting points | What is actually labeled |
|---|---|---|
| Multi-hop and chunking | [HotpotQA](../../dataset-cards/text-rag/hotpotqa.md), [2WikiMultiHopQA](../../dataset-cards/text-rag/2wikimultihopqa.md), [StrategyQA](../../dataset-cards/text-rag/strategyqa.md), [HiCBench](../../dataset-cards/text-rag/hicbench.md) | Sentence, paragraph or hierarchy labels, with differing construction methods |
| Long-source evidence | [QASPER](../../dataset-cards/text-rag/qasper.md), [CLAP NQ](../../dataset-cards/text-rag/clapnq.md), [NarrativeQA](../../dataset-cards/text-rag/narrativeqa.md) | Paper/passages or source documents; NarrativeQA does not supply minimal spans |
| Dialogue | [MTRAG](../../dataset-cards/text-rag/mtrag.md) | Turn-level answers and relevance under separate reference and full-RAG conditions |
| Robustness and grounding | [RGB](../../dataset-cards/text-rag/rgb.md), [RAGTruth](../../dataset-cards/text-rag/ragtruth.md), [RAGBench](../../dataset-cards/text-rag/ragbench.md) | Fixed-context answers, response-side error spans or support metadata—not one common retrieval qrel |
| Time-sensitive answers | [FreshQA](../../dataset-cards/text-rag/freshqa.md), [RealTime QA](../../dataset-cards/text-rag/realtimeqa.md) | Dated answer keys; source snapshots require explicit control |
| Retrieval-only control | [BEIR](../../suite-cards/beir.md), [MS MARCO Passage Ranking](../../dataset-cards/text-rag/msmarco-passage.md), [BRIGHT](../../dataset-cards/text-rag/bright.md) | Corpus-query relevance, not answer faithfulness |
| Specialist domain | [BioASQ Task 14b](../../dataset-cards/text-rag/bioasq-14b.md), [PUBHEALTH](../../dataset-cards/text-rag/pubhealth.md) | Biomedical source snippets versus health-claim labels/explanations |

For chunking research, compare candidates against immutable document/paragraph/sentence coordinates and a fixed token budget. A supporting sentence is not a unique correct chunk boundary. Prefer a paired analysis of complete-evidence retrieval, overhead and answer quality. For answer research, report a gold-evidence oracle and actual retrieval separately. RGB and RAGTruth are useful *diagnostics* but should not be presented as full open-corpus retrieval tests. A dynamically updated answer dataset must be pinned by date, including source capture time.

The full [evidence ground-truth guide](../evidence-ground-truth.md) specifies the source-coordinate and alternative-evidence rules. Domain is an independent filter: biomedical and public-health entries belong here because their released evidence is textual, not because “medical RAG” is a separate data representation.

## Recent-paper extensions

The [2025–2026 adoption index](../recent-paper-index.md) records exact paper settings, including native-source variants and sampled splits. Important additions cover different failure modes:

| Subtrack | Added starting points | Keep separate |
|---|---|---|
| Open-domain and long-tail | [TriviaQA](../../dataset-cards/text-rag/triviaqa.md), [PopQA](../../dataset-cards/text-rag/popqa.md), [AmbigQA](../../dataset-cards/text-rag/ambigqa.md), [Bamboogle](../../dataset-cards/text-rag/bamboogle.md) | Answer aliases/disambiguation versus source evidence; corpus snapshots are often external |
| Conversational retrieval | [QReCC](../../dataset-cards/text-rag/qrecc.md), [TopiOCQA](../../dataset-cards/text-rag/topiocqa.md), [OR-QuAC](../../dataset-cards/text-rag/or-quac.md), [MultiDoc2Dial](../../dataset-cards/text-rag/multidoc2dial.md), [ChatRAG Bench](../../suite-cards/chatrag-bench.md) | History, standalone rewrites, turn-level supporting passages and suite conversions |
| Multilingual retrieval/QA | [MIRACL](../../dataset-cards/text-rag/miracl.md), [NoMIRACL](../../dataset-cards/text-rag/nomiracl.md), [MKQA](../../dataset-cards/text-rag/mkqa.md) | MIRACL qrels, NoMIRACL binary relevance assessment and MKQA multilingual answers are different labels |
| Chunking and context routing | [GutenQA](../../dataset-cards/text-rag/gutenqa.md), [LaRA](../../dataset-cards/text-rag/lara.md), [LongBench v2](../../dataset-cards/text-rag/longbench-v2.md) | Substring-anchored retrieval versus answer-only RAG/long-context comparisons |
| Security and conflicting evidence | [SafeRAG](../../dataset-cards/text-rag/saferag.md), [RAGuard](../../dataset-cards/text-rag/raguard.md), [ConfRAG](../../dataset-cards/text-rag/confrag.md) | Constructed attacks, misleading retrieval and conflicting answer/reason coverage |
| Specialist sources | [LegalBench-RAG](../../dataset-cards/text-rag/legalbench-rag.md), [MIRAGE](../../suite-cards/mirage.md), [LFRQA](../../dataset-cards/text-rag/lfrqa.md), [CRUD-RAG](../../dataset-cards/text-rag/crud-rag.md) | Legal span retrieval, medical choice accuracy, cross-domain long-form grading and Chinese generation tasks |
