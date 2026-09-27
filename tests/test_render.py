from pathlib import Path

from awesome_rag_datasets.render import render_card, render_readme, render_suite_card


RECORD = {
    "id": "example", "name": "Example", "entity_type": "dataset",
    "status": "screened", "summary": "A test benchmark.",
    "classification": {"rag_role": "rag_convertible", "primary_category": "table_rag", "tasks": ["table_qa"], "modalities": ["table", "text"]},
    "data": {"corpus": "provided", "queries": "provided", "answers": "provided"},
    "ground_truth": {"levels": ["table_cell"], "provenance": "human"},
    "evaluation": {"official_metrics": ["accuracy"]},
    "access": {"official": "https://example.org/data", "license": "unknown"},
    "use": {"best_for": ["table cell reasoning"], "caveats": ["No fixed retrieval pool."]},
    "sources": [{"url": "https://example.org/data", "type": "official", "fields": ["summary"]}],
}


def test_card_exposes_gold_and_limitations():
    card = render_card(RECORD)
    assert "table_cell" in card
    assert "No fixed retrieval pool." in card
    assert "https://example.org/data" in card
    assert "source_checked" not in card


def test_readme_links_to_generated_card():
    catalog = {"datasets": [RECORD], "suites": [], "tasks": [], "corpora": [], "papers": []}
    readme = render_readme(catalog)
    assert "dataset-cards/table-rag/example.md" in readme
    assert "rag_convertible" in readme


def test_suite_card_explains_protocol_and_components():
    suite = {
        "id": "sample", "name": "Sample Suite", "status": "source_checked",
        "summary": "A collection of retrieval datasets.",
        "components": ["first"], "protocol": "Use fixed qrels.",
        "access": {"official": "https://example.org"},
        "sources": [{"url": "https://example.org", "type": "official", "fields": ["summary"]}],
    }
    content = render_suite_card(suite)
    assert "Use fixed qrels." in content
    assert "first" in content
