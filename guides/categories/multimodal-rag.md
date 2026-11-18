# Multimodal RAG: retrieval before visual reasoning

[简体中文](multimodal-rag.zh-CN.md)

This category covers source collections whose evidence crosses text, image, document layout, table, chart, audio or video. The decisive question is not whether an example contains an image; it is whether the released protocol lets a system **find** the necessary source evidence before answering. Begin with [the catalog section](../../README.md#multimodal-rag).

| Evidence setting | Inspect | Native label boundary |
|---|---|---|
| Page and region retrieval | [MMDocIR](../../dataset-cards/multimodal-rag/mmdocir.md), [ViDoRe](../../suite-cards/vidore.md) | MMDocIR/v1–v2 retrieval labels do not alone score generation; ViDoRe v3 additionally releases grounding and reference answers |
| Cross-page answer and citation | [MMDocRAG](../../dataset-cards/multimodal-rag/mmdocrag.md), [XL-DocBench](../../dataset-cards/multimodal-rag/xl-docbench.md), [MAVIS](../../dataset-cards/multimodal-rag/mavis.md) | Page, quote or fact citation at different granularities |
| Mixed image-text web evidence | [WebQA](../../dataset-cards/multimodal-rag/webqa.md), [MultiModalQA](../../dataset-cards/multimodal-rag/multimodalqa.md) | Source IDs; not necessarily question-specific pixels or cells |
| Supplied visual context | [ChartQA](../../dataset-cards/multimodal-rag/chartqa.md), [MP-DocVQA](../../dataset-cards/multimodal-rag/mp-docvqa.md), [InfoSeek](../../dataset-cards/multimodal-rag/infoseek.md) | Answers and some page/layout metadata; open retrieval is an adaptation |
| General multimodal retrieval | [M-BEIR](../../suite-cards/m-beir.md), [M2KR](../../suite-cards/m2kr.md) | Retrieval subsets and metrics; distinguish every converted variant from its source QA dataset |

For evidence fragmentation, model document → page → region → source element → atomic fact, plus typed relations such as caption-of, table-header-of and continued-on. Page recall and answer correctness can both be high while the link between a figure and its caption is missing. Score page, region, relation, complete chain and citation separately. A layout box may describe a page object without being a **question-specific** support label. Preserve original PDF or image coordinates and parser/OCR versions.

Video extends the model with time intervals, transcripts, frames and cross-modal synchronization. A video QA paper or algorithm repository is not sufficient evidence that a reusable video-RAG dataset, temporal qrels and original assets are public; this catalog adds video records only after that release boundary is checked. [Benchmark construction](../benchmark-construction.md) describes how to annotate missing chain labels.

## Recent-paper extensions

[HARP Audio QA](../../dataset-cards/multimodal-rag/harp-audio.md) evaluates recording-local QA using waveform or transcript evidence. [CASTELLA](../../dataset-cards/multimodal-rag/castella.md) scores sound localization with human timing labels. [One Fact, Many Places](../../dataset-cards/multimodal-rag/one-fact-many-places.md) audits alternative evidence in two visual document benchmarks.

The [paper adoption index](../recent-paper-index.md) shows whether a source dataset was used for training, evaluation or retrieval conversion. The expanded cards add the following controls:

| Setting | Added entry points | Evaluation boundary |
|---|---|---|
| Explicit open document retrieval | [OpenDocVQA](../../dataset-cards/multimodal-rag/opendocvqa.md) | Filtered source QA and a separately licensed/gated image corpus; not single-page DocVQA |
| Query rephrasing robustness | [REAL-MM-RAG](../../dataset-cards/multimodal-rag/real-mm-rag.md) | Four document subsets and synthetic page relevance; base queries, phrasing versions and Parquet rows are different units |
| Document reading and extraction | [DocVQA](../../dataset-cards/multimodal-rag/docvqa.md), [InfographicVQA](../../dataset-cards/multimodal-rag/infographicvqa.md), [DUDE](../../dataset-cards/multimodal-rag/dude.md), [TAT-DQA](../../dataset-cards/multimodal-rag/tat-dqa.md) | Supplied documents, possibly missing answer boxes and heuristic supporting facts |
| OCR cascade | [OHRBench](../../dataset-cards/multimodal-rag/ohrbench.md) | Transcription reference, page/quote evidence and LCS inclusion are distinct from region relevance |
| External visual knowledge | [MRAG-Bench](../../dataset-cards/multimodal-rag/mrag-bench.md), [Visual-RAG](../../dataset-cards/multimodal-rag/visual-rag.md), [Encyclopedic-VQA](../../dataset-cards/multimodal-rag/encyclopedic-vqa.md), [OK-VQA](../../dataset-cards/multimodal-rag/ok-vqa.md), [A-OKVQA](../../dataset-cards/multimodal-rag/a-okvqa.md) | Native images, gold retrieved knowledge and fixed candidate pools are different configurations |
| Interleaved generation and mixed tasks | [RAG-IGBench](../../dataset-cards/multimodal-rag/rag-igbench.md), [M²RAG](../../dataset-cards/multimodal-rag/m2rag.md) | Image choice/placement versus multimodal QA and verification |
| Perception/converted retrieval controls | [TextVQA](../../dataset-cards/multimodal-rag/textvqa.md), [ArXivQA](../../dataset-cards/multimodal-rag/arxivqa.md), [PlotQA](../../dataset-cards/multimodal-rag/plotqa.md) | Answer targets or OCR objects are not automatically question-specific retrieval judgments |

None of these additions makes captions, OCR boxes or textual rationales interchangeable with complete cross-modal evidence chains. Keep document families disjoint across custom splits and independently annotate missing source-element relations.

## Video and expanded evaluation contracts

| Resource | Distinct target | Released-label boundary |
|---|---|---|
| [CFVBench](../../dataset-cards/multimodal-rag/cfvbench.md) | Video retrieval and visual/transcript keypoint coverage | Source-video IDs and keypoints, not checked per-question temporal intervals |
| [XVBench](../../dataset-cards/multimodal-rag/xvbench.md) | Iterative retrieval with addressable support clips | Multiple clips do not imply multiple source videos; clip names are coarser than minimal temporal evidence |
| [LongerVideos](../../dataset-cards/multimodal-rag/longervideos.md) | Long-video collection synthesis and comparative judgments | Released questions have no reference answers or temporal qrels; auxiliary rather than full gold QA |
| [CRAG-MM](../../dataset-cards/multimodal-rag/crag-mm.md) | Image-plus-web single/multi-turn QA | Answer and abstention/session scoring; mock search results are not complete evidence labels |
| [UniDoc-Bench](../../dataset-cards/multimodal-rag/unidoc-bench.md), [ViDoRe v3](../../suite-cards/vidore.md) | Joint document evidence and grounding/answer evaluation | Preserve release-specific query counts, human-review scope, public/private components and evaluator |
| [M4-RAG](../../suite-cards/m4-rag.md) | Multilingual, multicultural retrieval-augmented VQA | Converted source QA and Wikipedia pools, not a new universal multilingual qrel collection |

Video remains in this source category with the existing `video`/`audio` modality tags; no separate top-level method category is needed. Explicit start/end timestamps, source-video identity, frame sampling and ASR/OCR snapshots are necessary for temporal-evidence comparison. None should be inferred merely because timestamps occur during dataset construction. See [capability routes](../selecting-a-benchmark.md#capability-routes) for cross-category selection.
