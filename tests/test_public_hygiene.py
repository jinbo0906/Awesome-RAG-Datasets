from pathlib import Path
import re

from awesome_rag_datasets.hygiene import scan_public_files


def test_public_hygiene_reports_rule_without_exposing_value(tmp_path):
    (tmp_path / "README.md").write_text("Authorization: " + "Bearer placeholder-secret-token\n", encoding="utf-8")
    issues = scan_public_files(tmp_path, [Path("README.md")])
    assert issues == ["README.md:1: bearer-token"]


def test_public_hygiene_allows_public_links(tmp_path):
    (tmp_path / "README.md").write_text("https://github.com/example/project\n", encoding="utf-8")
    assert scan_public_files(tmp_path, [Path("README.md")]) == []


def test_public_markdown_relative_links_resolve():
    root = Path(__file__).resolve().parents[1]
    paths = [root / "README.md", root / "README.zh-CN.md", root / "CONTRIBUTING.md"]
    paths += list((root / "guides").rglob("*.md"))
    paths += list((root / "dataset-cards").rglob("*.md"))
    paths += list((root / "suite-cards").rglob("*.md"))
    missing = []
    for path in paths:
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if target.startswith(("https://", "http://", "#")):
                continue
            relative = target.split("#", 1)[0]
            if relative and not (path.parent / relative).exists():
                missing.append(f"{path.relative_to(root)} -> {target}")
    assert missing == []


def test_chinese_guides_link_to_chinese_cards():
    root = Path(__file__).resolve().parents[1]
    wrong = []
    for path in (root / "guides").rglob("*.zh-CN.md"):
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if ("dataset-cards/" in target or "suite-cards/" in target) and not target.endswith(".zh-CN.md"):
                wrong.append(f"{path.relative_to(root)} -> {target}")
    assert wrong == []
