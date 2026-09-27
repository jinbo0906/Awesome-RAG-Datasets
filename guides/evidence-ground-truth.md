# Evidence ground truth without privileged chunks

There is usually no context-free “correct chunk boundary.” A boundary depends on the question, source structure, retriever and token budget. Scoring a candidate chunker against chunk IDs produced by another chunker makes the benchmark circular. Anchor gold evidence to immutable upstream source coordinates and treat chunk outputs as **predictions** that cover—or fail to cover—those coordinates.

## Source-anchored evidence record

Store the source asset hash/version, document ID, parser version, page and coordinate system. A text node may use UTF-8 byte or Unicode character offsets, but the choice must be explicit; a visual node may use normalized page `bbox`, a stable cell ID or figure ID. Retain the original file and an OCR/parsed view separately. An answer is accompanied by atomic facts and one or more acceptable evidence sets. A multi-hop answer requires every fact in at least one accepted set. Equivalent support paths stay distinct.

The [evidence JSON Schema](../schemas/evidence.schema.json) defines a small interchange object. `awesome_rag_datasets.evidence.validate_evidence` additionally checks node/edge/fact references and coordinate order. It does not assert that current catalog datasets already contain all these labels. Conversion adapters must leave unavailable fields absent and record any lossy mapping.

## Chunking experiment

| Layer | Metric | Interpretation |
|---|---|---|
| Structure | boundary precision/recall, fact-split rate | Diagnostic only; a heading boundary is not itself sufficient evidence |
| Retrieval | Evidence-set Recall@K; first-complete rank | Counts a query only when at least one complete accepted set is covered |
| Efficiency | gold-token ratio, non-gold token overhead, index size, latency | Prevents a whole-document chunk from winning through unlimited context |
| Answer | fact coverage, answer EM/F1, citation support | Evaluates downstream usefulness without conflating it with retrieval |
| Oracle gap | answer with gold evidence vs retrieved evidence | Separates generation failure from retrieval failure |

Fix the source documents, queries, embedding model, retriever, reranker, generator and token budget in the primary comparison; change only chunking. Then repeat with at least two retriever/generator backbones for sensitivity. Report paired per-query differences and uncertainty, not only an aggregate mean. Compare by retrieved **tokens** as well as chunks. Handle duplicate and overlapping predictions explicitly. Never define gold using the evaluated chunker's output.

Good pilot candidates are HiCBench for structural boundaries and QA, HotpotQA/2WikiMultiHopQA for sentence support, QASPER for long-paper evidence, and CLAP NQ for non-contiguous sentence support. These are complementary, not interchangeable: sentence support is often too coarse for an atomic fact and too fine for a coherent chunk.

## Multimodal evidence graph

Represent evidence nodes as source-backed text spans, page regions, figures, captions, table cells, chart marks, equations or video intervals. Record typed edges such as `supports`, `required_with`, `caption_of`, `row_header_of`, `column_header_of`, `continued_on`, `refers_to`, `corefers_with` and `temporal_before`. A chain is complete only when all required nodes **and** relationships for one accepted chain are present.

Score document/page retrieval, node recall, edge correctness, complete-chain recall, answer correctness and fact-to-source citation separately. For region matching, define coordinate normalization and IoU threshold before evaluation. Distinguish parser/OCR errors from retriever errors by comparing a gold-layout oracle, the parsed view and the final pipeline. A caption-only retrieval or a table value without its header/units may have high node recall but fail complete-chain recall.

MMDocIR supplies page/layout retrieval labels, MMDocRAG adds answer/evidence analysis, XL-DocBench has page and snippet evidence, and MAVIS targets fact-level multimodal citation. SlideVQA has evidence-page labels but its general layout boxes are not all question-specific. These facts determine which components of the graph can be scored directly and which need new annotation.

## Building new labels responsibly

Start with 200–500 stratified examples, including text-only, table-text, figure-caption, cross-page and cross-document cases. Have annotators work against immutable source assets, record alternative minimal sufficient evidence sets, include unanswerable and misleading-evidence cases, and adjudicate disagreements. Publish annotation instructions, source hashes, split logic, inter-annotator agreement, accepted alternatives and a small manually inspected example. Keep any model-assisted proposals marked as proposals until human review. The benchmark is publishable only when its source coordinates, licensing, evaluator and baseline outputs can be independently checked.
