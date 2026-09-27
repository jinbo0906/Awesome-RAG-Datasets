"""Validate source-anchored evidence graphs before a benchmark release."""

from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator


SCHEMA = json.loads((Path(__file__).resolve().parents[2] / "schemas" / "evidence.schema.json").read_text(encoding="utf-8"))


def validate_evidence(record: dict) -> list[str]:
    """Check JSON shape, source coordinates and graph references."""
    problems = [f"schema {'.'.join(map(str, issue.absolute_path))}: {issue.message}" for issue in Draft202012Validator(SCHEMA).iter_errors(record)]
    if problems:
        return sorted(problems)

    facts = {fact["id"] for fact in record["facts"]}
    nodes = {node["id"] for node in record["nodes"]}
    edges = {edge["id"] for edge in record["edges"]}
    for label, ids, items in (("fact", facts, record["facts"]), ("node", nodes, record["nodes"]), ("edge", edges, record["edges"])):
        if len(ids) != len(items):
            problems.append(f"duplicate {label} id")
    for node in record["nodes"]:
        if ("char_start" in node) != ("char_end" in node):
            problems.append(f"node {node['id']}: char_start and char_end must appear together")
        elif "char_start" in node and node["char_start"] >= node["char_end"]:
            problems.append(f"node {node['id']}: char_end must exceed char_start")
        if "bbox" in node:
            x1, y1, x2, y2 = node["bbox"]
            if x1 >= x2 or y1 >= y2:
                problems.append(f"node {node['id']}: bbox must have positive area")
        if ("time_start_ms" in node) != ("time_end_ms" in node):
            problems.append(f"node {node['id']}: time_start_ms and time_end_ms must appear together")
        elif "time_start_ms" in node and node["time_start_ms"] >= node["time_end_ms"]:
            problems.append(f"node {node['id']}: time_end_ms must exceed time_start_ms")
    for edge in record["edges"]:
        for endpoint in ("from", "to"):
            if edge[endpoint] not in nodes:
                problems.append(f"edge {edge['id']}: unknown node {edge[endpoint]}")
    for index, accepted in enumerate(record["acceptable_sets"]):
        for name, known in (("node_ids", nodes), ("edge_ids", edges), ("fact_ids", facts)):
            for item in accepted.get(name, []):
                if item not in known:
                    problems.append(f"acceptable_sets[{index}]: unknown {name[:-4]} {item}")
    return sorted(problems)
