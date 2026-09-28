# Catalog maintenance policy

[简体中文](maintenance-policy.zh-CN.md)

The machine-readable files under `catalog/` are the source of truth. `README.md`, `README.zh-CN.md`, `dataset-cards/` and `suite-cards/` are generated views. Make a factual correction in YAML with a field-level primary source, then run the generator. The public repo stores descriptions and links, not upstream datasets or credentials.

## Review cycle

- On each contribution: schema/reference checks, generated-file check, secret/path scan and tests must pass. A maintainer checks changes to dataset role, evidence granularity, scale, license and official metrics against the linked source.
- Quarterly when feasible: revisit access URLs, archived/deprecated notices, official data cards, license and unresolved conflicting counts. `last_checked` is a **field review date**, not proof of a successful download.
- For an upstream release: compare versions and split protocol before editing the existing record; create a distinct variant when semantics or evaluation changes. Do not overwrite historical results.

HTTP 403, 429, authentication requirements and robots restrictions are not proof that a dataset vanished. Mark access issues with date and method; do not delete a record on one failed request. Broken links should be replaced by an author-controlled canonical source or archived reference only after verification.

## Correction and promotion

Open a correction with the exact field, current value, proposed value, primary URL, source excerpt or line, date checked and affected versions. For conflicting official counts, keep both units/variants and explain which release the catalog describes. A reviewer can move `screened` to `source_checked` after key fields are checked. `reproduced` requires a recorded loader/evaluator run; `verified` requires a second independent review. No scheduled job can infer these states from link reachability alone.

Source links support claims but external pages can change. Pin a paper DOI/arXiv identifier or release tag when possible, and note retrieval date. Dataset-specific licenses override any license on catalog text. Do not mirror source documents, hidden labels or gated files without explicit rights.

## Release and compatibility

Schema changes are versioned in release notes. Additive optional fields are compatible; changing enum meaning or required fields requires a migration note and validator update. Generated Markdown is checked for drift in CI. Release notes should state record counts by review status, new/removed records and corrected facts, rather than implying full ecosystem coverage.
