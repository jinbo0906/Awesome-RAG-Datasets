# Contributing

Corrections and new dataset records are welcome. This is a source-audited catalog, so a small, well-supported correction is more valuable than an unsupported large list.

1. Choose the correct entity: dataset, suite, corpus, task or paper. Do not label an IR-only suite as a complete RAG benchmark.
2. Add or edit one YAML record under `catalog/`. The file stem must equal `id`. Use `unknown` where a license or fact cannot be confirmed; never infer missing evidence labels.
3. State the native task and any proposed RAG conversion separately. Describe source pool, queries, answers, evidence level, metric, best use and caveats. Counts need a unit, variant/split and primary source.
4. Put official paper, author project, author repository or official dataset-card URLs under `sources`; list the supported field paths. Start at `screened` if key fields have not been checked. Use `source_checked` only with a review date and field-level references; do not claim `reproduced` without a recorded run.
5. Run the commands below and commit generated README/cards alongside the YAML. Do not manually edit generated files.

```bash
python -m pip install -e ".[dev]"
python -m scripts.validate_catalog
python -m scripts.generate --write
python -m scripts.generate --check
python -m scripts.check_secrets
python -m pytest -q
```

For a factual correction, include the record ID, exact field, old/new value, official source and date checked. For a new record, explain why it is RAG-native, convertible or auxiliary. Do not submit dataset binaries, access tokens, private research notes or machine-specific paths. Original datasets retain their own terms; this repository's license applies only to original catalog code and prose.
