# Selecting a benchmark

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

## Selection checklist

1. Identify the target unit: source document, page, sentence, cell, region, graph path, atomic fact or final answer.
2. Check whether the **released** fields identify that unit. Do not upgrade a page label to a cell label by interpretation.
3. Choose a retrieval scope: fixed supplied context, document-local, multi-document, open corpus or time-varying web. Keep the official scope separate from an adapted one.
4. Fix split and source snapshot before chunking/indexing. Split by source document or source family, never random chunks.
5. Match denominators and budgets: Top-K documents and Top-K chunks are not comparable if token counts differ.
6. Report retrieval, complete evidence, answer and citation results separately. Include an oracle-evidence condition to localize failure.
7. Check license, gating, unavailable pages and official evaluator before committing to a large experiment.

For a new RAG method, use at least one in-domain benchmark and one transfer benchmark, then an error-analysis subset with independently checked source coordinates. Do not optimize against a test leaderboard repeatedly. Full recipes for the two motivating research problems are in [evidence ground truth](evidence-ground-truth.md).
