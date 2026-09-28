"""Load and validate human-maintained catalog translations."""

from __future__ import annotations

from pathlib import Path

import yaml


def _has_han(value: str) -> bool:
    return any("\u3400" <= char <= "\u9fff" for char in value)


def load_translations(path: Path) -> dict:
    """Read the Chinese narrative manifest without changing catalog facts."""
    try:
        translations = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        raise ValueError(f"{path}: {exc}") from exc
    if not isinstance(translations, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return translations


def validate_translations(translations: dict, catalog: dict[str, list[dict]]) -> list[str]:
    """Require a nonempty translation for each released narrative field."""
    issues: list[str] = []
    if not isinstance(translations, dict):
        return ["translations: expected a mapping"]
    for kind in ("datasets", "suites"):
        entries = translations.get(kind)
        if not isinstance(entries, dict):
            issues.append(f"translations.{kind}: expected a mapping")
            continue
        records = {record["id"]: record for record in catalog[kind] if isinstance(record.get("id"), str)}
        for missing in sorted(records.keys() - entries.keys()):
            issues.append(f"translations.{kind}.{missing}: missing record")
        for extra in sorted(entries.keys() - records.keys()):
            issues.append(f"translations.{kind}.{extra}: unknown record")
        for record_id in sorted(records.keys() & entries.keys()):
            record, entry = records[record_id], entries[record_id]
            prefix = f"translations.{kind}.{record_id}"
            if not isinstance(entry, dict):
                issues.append(f"{prefix}: expected a mapping")
                continue
            if kind == "suites":
                required = {"protocol"} if "protocol" in record else set()
                if not isinstance(record.get("summary_zh"), str) or not _has_han(record["summary_zh"]):
                    issues.append(f"{prefix}: source suite lacks summary_zh")
            else:
                required = {"summary", "best_for", "caveats"}
                for source_field, target_field in (
                    (record.get("data", {}), "data_description"),
                    (record.get("data", {}), "size"),
                    (record.get("data", {}), "splits"),
                    (record.get("ground_truth", {}), "ground_truth_description"),
                    (record.get("evaluation", {}), "evaluation_protocol"),
                ):
                    source_key = target_field.removeprefix("data_").removeprefix("ground_truth_").removeprefix("evaluation_")
                    if source_key in source_field:
                        required.add(target_field)
            for field in sorted(required - entry.keys()):
                issues.append(f"{prefix}.{field}: missing translation")
            for field in sorted(entry.keys() - required):
                issues.append(f"{prefix}.{field}: unexpected translation field")
            for field in sorted(required & entry.keys()):
                value = entry[field]
                if field in {"best_for", "caveats"}:
                    source_items = record.get("use", {}).get(field, [])
                    if not isinstance(value, list) or len(value) != len(source_items) or any(not isinstance(item, str) or not _has_han(item) for item in value):
                        issues.append(f"{prefix}.{field}: expected {len(source_items)} nonempty translated items")
                elif not isinstance(value, str) or not _has_han(value):
                    issues.append(f"{prefix}.{field}: expected Chinese narrative text")
    for extra_kind in sorted(translations.keys() - {"datasets", "suites"}):
        issues.append(f"translations.{extra_kind}: unexpected section")
    return sorted(issues)
