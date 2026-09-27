from pathlib import Path

import yaml

from awesome_rag_datasets.catalog import load_catalog, validate_catalog


def write_record(root: Path, folder: str, name: str, payload: dict) -> None:
    target = root / folder
    target.mkdir(parents=True, exist_ok=True)
    (target / name).write_text(yaml.safe_dump(payload, allow_unicode=True), encoding="utf-8")


def dataset(**overrides):
    base = {
        "id": "demo",
        "name": "Demo",
        "entity_type": "dataset",
        "status": "source_checked",
        "last_checked": "2026-09-28",
        "summary": "A question answering benchmark with source evidence.",
        "classification": {
            "rag_role": "rag_native",
            "primary_category": "text_rag",
            "tasks": ["multi_hop_qa"],
            "modalities": ["text"],
        },
        "data": {"corpus": "provided", "queries": "provided", "answers": "provided"},
        "ground_truth": {"levels": ["sentence"], "provenance": "human"},
        "evaluation": {"official_metrics": ["answer_f1"]},
        "access": {"official": "https://example.org/demo", "license": "unknown"},
        "use": {"best_for": ["evidence retrieval"], "caveats": ["synthetic example"]},
        "sources": [{"url": "https://example.org/demo", "type": "official", "fields": ["summary", "ground_truth.levels"]}],
    }
    base.update(overrides)
    return base


def test_catalog_accepts_valid_dataset_and_task(tmp_path):
    write_record(tmp_path, "datasets", "demo.yaml", dataset())
    write_record(tmp_path, "tasks", "multi_hop_qa.yaml", {
        "id": "multi_hop_qa", "name": "Multi-hop QA", "entity_type": "task",
        "summary": "Answer by combining multiple sources.",
        "sources": [{"url": "https://example.org/task", "type": "official", "fields": ["summary"]}],
    })
    assert validate_catalog(load_catalog(tmp_path)) == []


def test_catalog_rejects_duplicate_ids_and_unknown_tasks(tmp_path):
    write_record(tmp_path, "datasets", "first.yaml", dataset())
    write_record(tmp_path, "datasets", "second.yaml", dataset(name="Another"))
    problems = validate_catalog(load_catalog(tmp_path))
    assert any("duplicate id" in problem for problem in problems)
    assert any("unknown task multi_hop_qa" in problem for problem in problems)


def test_source_checked_requires_field_level_source(tmp_path):
    write_record(tmp_path, "datasets", "demo.yaml", dataset(sources=[]))
    problems = validate_catalog(load_catalog(tmp_path))
    assert any("source_checked" in problem for problem in problems)


def test_suite_component_must_exist(tmp_path):
    write_record(tmp_path, "suites", "sample.yaml", {
        "id": "sample", "name": "Sample", "entity_type": "suite",
        "summary": "A benchmark suite.", "status": "screened",
        "components": ["missing-dataset"],
        "access": {"official": "https://example.org/suite"},
        "sources": [{"url": "https://example.org/suite", "type": "official", "fields": ["summary"]}],
    })
    problems = validate_catalog(load_catalog(tmp_path))
    assert any("unknown component missing-dataset" in problem for problem in problems)


def test_filename_and_related_suite_are_checked(tmp_path):
    write_record(tmp_path, "datasets", "wrong-name.yaml", dataset(related_suites=["missing-suite"]))
    write_record(tmp_path, "tasks", "multi_hop_qa.yaml", {
        "id": "multi_hop_qa", "name": "Multi-hop QA", "entity_type": "task",
        "summary": "Answer by combining multiple sources.", "sources": [],
    })
    problems = validate_catalog(load_catalog(tmp_path))
    assert any("filename" in problem for problem in problems)
    assert any("unknown related suite" in problem for problem in problems)


def test_source_checked_requires_review_date(tmp_path):
    record = dataset()
    del record["last_checked"]
    write_record(tmp_path, "datasets", "demo.yaml", record)
    write_record(tmp_path, "tasks", "multi_hop_qa.yaml", {
        "id": "multi_hop_qa", "name": "Multi-hop QA", "entity_type": "task",
        "summary": "Answer by combining multiple sources.", "sources": [],
    })
    assert any("last_checked" in problem for problem in validate_catalog(load_catalog(tmp_path)))


def test_paper_target_must_exist(tmp_path):
    write_record(tmp_path, "papers", "paper.yaml", {
        "id": "paper", "name": "A benchmark paper", "entity_type": "paper",
        "url": "https://example.org/paper", "relation": "introduces",
        "targets": ["missing"], "sources": [],
    })
    assert any("unknown paper target" in problem for problem in validate_catalog(load_catalog(tmp_path)))


def test_review_date_must_be_calendar_date(tmp_path):
    write_record(tmp_path, "datasets", "demo.yaml", dataset(last_checked="2026-99-99"))
    write_record(tmp_path, "tasks", "multi_hop_qa.yaml", {
        "id": "multi_hop_qa", "name": "Multi-hop QA", "entity_type": "task",
        "summary": "Answer by combining multiple sources.", "sources": [],
    })
    assert any("last_checked" in problem for problem in validate_catalog(load_catalog(tmp_path)))
