"""Load and validate the machine-readable catalog."""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

import yaml
from jsonschema import Draft202012Validator, FormatChecker


KINDS = {"datasets": "dataset", "suites": "suite", "tasks": "task", "corpora": "corpus", "papers": "paper"}
ROOT = Path(__file__).resolve().parents[2]


def load_catalog(root: Path) -> dict[str, list[dict]]:
    """Read one YAML mapping per catalog file, preserving filename for diagnostics."""
    catalog: dict[str, list[dict]] = {kind: [] for kind in KINDS}
    for folder in KINDS:
        for path in sorted((root / folder).glob("*.yaml")):
            try:
                record = yaml.safe_load(path.read_text(encoding="utf-8"))
            except (OSError, yaml.YAMLError) as exc:
                record = {"_load_error": str(exc)}
            if not isinstance(record, dict):
                record = {"_load_error": "expected a YAML mapping"}
            record["_path"] = str(path)
            catalog[folder].append(record)
    return catalog


def _valid_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme in {"https", "http"} and bool(parsed.netloc)


def _field_exists(record: dict, dotted: str) -> bool:
    part: object = record
    for segment in dotted.split("."):
        if not isinstance(part, dict) or segment not in part:
            return False
        part = part[segment]
    return True


def validate_catalog(catalog: dict[str, list[dict]]) -> list[str]:
    """Return actionable validation errors without contacting external sites."""
    problems: list[str] = []
    all_ids: dict[str, str] = {}
    ids_by_kind = {kind: {r.get("id") for r in records} for kind, records in catalog.items()}
    for folder, expected_type in KINDS.items():
        schema_path = ROOT / "schemas" / f"{expected_type}.schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        for record in catalog.get(folder, []):
            path = record.get("_path", folder)
            if "_load_error" in record:
                problems.append(f"{path}: {record['_load_error']}")
                continue
            public_record = {k: v for k, v in record.items() if not k.startswith("_")}
            for issue in validator.iter_errors(public_record):
                at = ".".join(str(x) for x in issue.absolute_path)
                problems.append(f"{path}: schema {at}: {issue.message}")
            record_id = record.get("id")
            if not isinstance(record_id, str):
                continue
            if Path(path).stem != record_id:
                problems.append(f"{path}: filename must match id {record_id}")
            if record_id in all_ids:
                problems.append(f"{path}: duplicate id {record_id} (first: {all_ids[record_id]})")
            else:
                all_ids[record_id] = path
            if record.get("entity_type") != expected_type:
                problems.append(f"{path}: wrong entity_type for {folder}")
            if record.get("status") in {"source_checked", "reproduced", "verified"} and not record.get("sources"):
                problems.append(f"{path}: source_checked or higher requires field-level sources")
            if folder == "datasets" and record.get("status") in {"source_checked", "reproduced", "verified"} and not record.get("last_checked"):
                problems.append(f"{path}: source_checked or higher requires last_checked")
            for source in record.get("sources", []):
                if not isinstance(source, dict):
                    continue
                if not _valid_url(str(source.get("url", ""))):
                    problems.append(f"{path}: invalid source URL")
                for field in source.get("fields", []):
                    if not _field_exists(record, field):
                        problems.append(f"{path}: source references missing field {field}")
            if folder == "datasets":
                for task in record.get("classification", {}).get("tasks", []):
                    if task not in ids_by_kind["tasks"]:
                        problems.append(f"{path}: unknown task {task}")
                for suite in record.get("related_suites", []):
                    if suite not in ids_by_kind["suites"]:
                        problems.append(f"{path}: unknown related suite {suite}")
            if folder == "suites":
                for component in record.get("components", []):
                    if component not in ids_by_kind["datasets"]:
                        problems.append(f"{path}: unknown component {component}")
            if folder == "papers":
                valid_targets = ids_by_kind["datasets"] | ids_by_kind["suites"] | ids_by_kind["corpora"]
                for target in record.get("targets", []):
                    if target not in valid_targets:
                        problems.append(f"{path}: unknown paper target {target}")
    return sorted(problems)
