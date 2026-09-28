# Constructing a new RAG benchmark

[简体中文](benchmark-construction.zh-CN.md)

The catalog is a discovery and design aid, not a claim that existing labels can be freely recombined. Before building a benchmark, write a task contract: input, source pool, allowed retrieval actions, answer format, gold evidence granularity, metrics, split unit and access conditions. Publish a small example satisfying that contract before large-scale annotation.

## 1. Select the gap and source assets

Use the [selection guide](selecting-a-benchmark.md) to identify what existing datasets already score. Choose sources whose original bytes, page images or graph snapshots can be stably identified. Record URL, license, retrieval date, content hash, parser/OCR version, language, modality and document family. If raw assets cannot be redistributed, release stable IDs, hashes and lawful acquisition instructions instead. Never copy an original dataset license from an associated code repository.

## 2. Define query and evidence independently

Annotate the query, answerability, answer aliases, atomic facts and alternative minimal sufficient evidence sets against original source coordinates. For chunking, gold is a character/span/structural coordinate, not a chunk index. For visual documents, anchor pages and regions to the original PDF or image coordinate system. Record caption, table header/unit and cross-page dependency edges. A source page without a localized region should remain page-level truth; do not promote it to a cell-level label by a model guess.

## 3. Build reliable splits

Partition by source document, publisher, topic or time, depending on the intended generalization test; ensure near-duplicates and derived versions stay together. Check train/dev/test overlap at document and answer level. Preserve a locked test set. If the benchmark targets temporal freshness, preserve source capture times and disallow future documents in earlier evaluation windows.

## 4. Annotate and adjudicate

Write instructions for ambiguous evidence, negative claims, alternative reasoning paths, numerical operations, OCR disagreement and unanswerable queries. Use at least two independent passes on a stratified subset, adjudicate disagreements, and publish agreement by evidence level. Label whether each field is human, synthetic, distant or mixed. Model-generated candidates may accelerate annotation, but must not be called verified gold until checked against source assets.

## 5. Release evaluators and baselines

Release schema-valid examples and an evaluator with deterministic unit tests. Score retrieval, complete evidence, answer and citations separately; include oracle source/evidence conditions, a no-retrieval baseline, and at least two retrieval baselines. Fix token and latency budgets for chunking comparisons. For multimodal systems, report parsed/OCR and gold-layout oracle conditions. Report per-query paired scores, confidence intervals, failure taxonomy, compute cost and versioned model settings. Avoid a single composite score that hides where the system fails.

## 6. Publish a datasheet and maintenance contract

Describe source rights, intended use, excluded uses, known biases, artifact size, splits, evaluator version, update rules and contact for corrections. A changed source pool, annotation guideline or evaluator is a new benchmark version; never silently change published test labels. Ship a machine-readable checksum manifest and archive the benchmark card with its release tag.

This repository currently provides the [catalog schema](../schemas/dataset.schema.json), [evidence schema](../schemas/evidence.schema.json), [selection guide](selecting-a-benchmark.md) and [ground-truth design](evidence-ground-truth.md). It does **not** claim that a new chunking or multimodal evidence benchmark has already been annotated or reproduced.
