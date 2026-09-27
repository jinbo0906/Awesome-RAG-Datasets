"""Deterministic human-readable views of the catalog."""

from __future__ import annotations

from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined


ROOT = Path(__file__).resolve().parents[2]
ENV = Environment(loader=FileSystemLoader(ROOT / "templates"), undefined=StrictUndefined, autoescape=False, keep_trailing_newline=True, trim_blocks=True, lstrip_blocks=True)
CATEGORY_PATHS = {
    "text_rag": "text-rag", "multimodal_rag": "multimodal-rag",
    "graph_rag": "graph-rag", "table_rag": "table-rag", "cross_cutting": "cross-cutting",
}


def card_path(record: dict) -> Path:
    return Path("dataset-cards") / CATEGORY_PATHS[record["classification"]["primary_category"]] / f"{record['id']}.md"


def render_card(record: dict) -> str:
    return ENV.get_template("dataset-card.md.j2").render(d=record)


def suite_card_path(record: dict) -> Path:
    return Path("suite-cards") / f"{record['id']}.md"


def render_suite_card(record: dict, datasets: list[dict] | None = None) -> str:
    component_links = {item["id"]: "../" + card_path(item).as_posix() for item in (datasets or [])}
    return ENV.get_template("suite-card.md.j2").render(s=record, component_links=component_links)


def render_readme(catalog: dict[str, list[dict]]) -> str:
    datasets = sorted(catalog["datasets"], key=lambda d: (d["classification"]["primary_category"], d["name"].casefold()))
    suites = sorted(catalog["suites"], key=lambda d: d["name"].casefold())
    return ENV.get_template("readme.md.j2").render(datasets=datasets, suites=suites, card_path=card_path, suite_card_path=suite_card_path)
