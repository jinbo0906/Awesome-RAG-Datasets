# Cross-cutting RAG: protocols that span source representations

Use `cross_cutting` only when a dataset's **native** evaluation cannot be assigned a useful primary source representation. A benchmark suite that aggregates text, image and table tasks belongs in `catalog/suites/`, not automatically in this dataset category. A paper that reports several datasets is not itself a new dataset.

Before adding a record, identify the released question set, source assets, retrieval boundary, answer and evidence labels, evaluator and version. Then ask whether the same examples actually require multiple representations, or whether the release is a bundle of separable text/table/image subsets. Keep separable subsets linked as variants and preserve their own protocols.

For research on chunking and fragmented evidence, report each source modality's anchor type and the cross-source relation that completes an answer. A common answer metric alone cannot identify which retrieval or joining step failed. See [the entity distinction](../benchmark-vs-dataset.md), [taxonomy](../taxonomy.md) and [evidence-ground-truth design](../evidence-ground-truth.md).
