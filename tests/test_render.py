from pathlib import Path

from awesome_rag_datasets.generate import build_outputs
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


def test_readme_has_category_sections_in_navigation_order():
    graph = {**RECORD, "id": "graph-example", "name": "Graph Example",
             "classification": {**RECORD["classification"], "primary_category": "graph_rag"}}
    catalog = {"datasets": [RECORD, graph], "suites": [], "tasks": [], "corpora": [], "papers": []}
    readme = render_readme(catalog)
    assert "### Graph RAG (1)" in readme
    assert "### Table RAG (1)" in readme
    assert readme.index("### Graph RAG (1)") < readme.index("### Table RAG (1)")
    assert readme.index("### Graph RAG (1)") < readme.index("graph-rag/graph-example.md") < readme.index("### Table RAG (1)")
    assert '|\n\n<a name="table-rag"></a>\n\n### Table RAG (1)' in readme


def test_chinese_readme_keeps_category_and_dataset_navigation():
    catalog = {"datasets": [RECORD], "suites": [], "tasks": [], "corpora": [], "papers": []}
    readme = render_readme(catalog, locale="zh-CN")
    assert "[English](README.md)" in readme
    assert "## 数据集" in readme
    assert "### Table RAG (1)" in readme
    assert "guides/categories/table-rag.zh-CN.md" in readme
    assert "dataset-cards/table-rag/example.md" in readme


def test_generation_includes_both_language_readmes():
    catalog = {"datasets": [], "suites": [], "tasks": [], "corpora": [], "papers": []}
    outputs = build_outputs(catalog)
    assert Path("README.md") in outputs
    assert Path("README.zh-CN.md") in outputs


def test_chinese_readme_uses_localized_suite_summary():
    suite = {
        "id": "sample", "name": "Sample Suite", "status": "source_checked",
        "summary": "A collection of retrieval datasets.",
        "summary_zh": "多个检索数据集组成的评测套件。",
        "components": [], "access": {"official": "https://example.org"}, "sources": [],
    }
    catalog = {"datasets": [], "suites": [suite], "tasks": [], "corpora": [], "papers": []}
    readme = render_readme(catalog, locale="zh-CN")
    assert "多个检索数据集组成的评测套件。" in readme
    assert "A collection of retrieval datasets." not in readme


def test_category_links_use_stable_anchors_even_when_counts_change():
    catalog = {"datasets": [RECORD], "suites": [], "tasks": [], "corpora": [], "papers": []}
    for locale in ("en", "zh-CN"):
        readme = render_readme(catalog, locale=locale)
        assert '<a name="table-rag"></a>' in readme
        assert "guides/categories/cross-cutting" in readme


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
