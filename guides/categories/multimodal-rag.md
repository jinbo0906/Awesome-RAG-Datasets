# Multimodal RAG: retrieval before visual reasoning

This category covers source collections whose evidence crosses text, image, document layout, table, chart, audio or video. The decisive question is not whether an example contains an image; it is whether the released protocol lets a system **find** the necessary source evidence before answering. Begin with [the catalog section](../../README.md#multimodal-rag).

| Evidence setting | Inspect | Native label boundary |
|---|---|---|
| Page and region retrieval | [MMDocIR](../../dataset-cards/multimodal-rag/mmdocir.md), [ViDoRe](../../suite-cards/vidore.md) | Retrieval labels; they do not alone score answer generation |
| Cross-page answer and citation | [MMDocRAG](../../dataset-cards/multimodal-rag/mmdocrag.md), [XL-DocBench](../../dataset-cards/multimodal-rag/xl-docbench.md), [MAVIS](../../dataset-cards/multimodal-rag/mavis.md) | Page, quote or fact citation at different granularities |
| Mixed image-text web evidence | [WebQA](../../dataset-cards/multimodal-rag/webqa.md), [MultiModalQA](../../dataset-cards/multimodal-rag/multimodalqa.md) | Source IDs; not necessarily question-specific pixels or cells |
| Supplied visual context | [ChartQA](../../dataset-cards/multimodal-rag/chartqa.md), [MP-DocVQA](../../dataset-cards/multimodal-rag/mp-docvqa.md), [InfoSeek](../../dataset-cards/multimodal-rag/infoseek.md) | Answers and some page/layout metadata; open retrieval is an adaptation |
| General multimodal retrieval | [M-BEIR](../../suite-cards/m-beir.md), [M2KR](../../suite-cards/m2kr.md) | Retrieval subsets and metrics; distinguish every converted variant from its source QA dataset |

For evidence fragmentation, model document → page → region → source element → atomic fact, plus typed relations such as caption-of, table-header-of and continued-on. Page recall and answer correctness can both be high while the link between a figure and its caption is missing. Score page, region, relation, complete chain and citation separately. A layout box may describe a page object without being a **question-specific** support label. Preserve original PDF or image coordinates and parser/OCR versions.

Video extends the model with time intervals, transcripts, frames and cross-modal synchronization. A video QA paper or algorithm repository is not sufficient evidence that a reusable video-RAG dataset, temporal qrels and original assets are public; this catalog adds video records only after that release boundary is checked. [Benchmark construction](../benchmark-construction.md) describes how to annotate missing chain labels.
