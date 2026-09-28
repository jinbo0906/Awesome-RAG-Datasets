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
CATEGORY_SECTIONS = (
    ("text_rag", "Text RAG", "text-rag", "Text sources, evidence retrieval, reasoning and grounded answers.", "文本来源的证据检索、推理与有依据的回答。"),
    ("multimodal_rag", "Multimodal RAG", "multimodal-rag", "Visual and document evidence across source modalities; video candidates remain under review.", "跨模态的视觉与文档证据；视频候选仍在核查中。"),
    ("graph_rag", "Graph RAG", "graph-rag", "Graph-based retrieval and knowledge-base reasoning; graph use alone does not establish path gold.", "图结构检索与知识库推理；使用图并不意味着具有路径真值。"),
    ("table_rag", "Table RAG", "table-rag", "Structured tables and their links to prose, pages and answer derivations.", "结构化表格及其与文本、页面和答案推导的关联。"),
    ("cross_cutting", "Cross-cutting", "cross-cutting", "Benchmarks not naturally assigned to one source representation.", "无法归入单一来源表示形式的评测数据。"),
)


def card_path(record: dict) -> Path:
    return Path("dataset-cards") / CATEGORY_PATHS[record["classification"]["primary_category"]] / f"{record['id']}.md"


def render_card(record: dict) -> str:
    return ENV.get_template("dataset-card.md.j2").render(d=record)


def suite_card_path(record: dict) -> Path:
    return Path("suite-cards") / f"{record['id']}.md"


def render_suite_card(record: dict, datasets: list[dict] | None = None) -> str:
    component_links = {item["id"]: "../" + card_path(item).as_posix() for item in (datasets or [])}
    return ENV.get_template("suite-card.md.j2").render(s=record, component_links=component_links)


def render_readme(catalog: dict[str, list[dict]], locale: str = "en") -> str:
    if locale not in {"en", "zh-CN"}:
        raise ValueError(f"unsupported README locale: {locale}")
    datasets = sorted(catalog["datasets"], key=lambda d: d["name"].casefold())
    groups = [
        {"title": title, "slug": slug, "summary": summary, "summary_zh": summary_zh,
         "datasets": [record for record in datasets if record["classification"]["primary_category"] == key]}
        for key, title, slug, summary, summary_zh in CATEGORY_SECTIONS
    ]
    groups = [group for group in groups if group["datasets"]]
    suites = sorted(catalog["suites"], key=lambda d: d["name"].casefold())
    template = "readme.zh-CN.md.j2" if locale == "zh-CN" else "readme.md.j2"
    return ENV.get_template(template).render(datasets=datasets, groups=groups, suites=suites, card_path=card_path, suite_card_path=suite_card_path)
