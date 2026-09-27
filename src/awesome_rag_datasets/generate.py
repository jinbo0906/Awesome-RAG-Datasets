"""Write or compare deterministic catalog outputs."""

from __future__ import annotations

from pathlib import Path

from .render import card_path, render_card, render_readme, render_suite_card, suite_card_path


def build_outputs(catalog: dict[str, list[dict]]) -> dict[Path, str]:
    outputs = {Path("README.md"): render_readme(catalog)}
    for record in catalog["datasets"]:
        outputs[card_path(record)] = render_card(record)
    for record in catalog["suites"]:
        outputs[suite_card_path(record)] = render_suite_card(record, catalog["datasets"])
    return outputs


def check_outputs(root: Path, outputs: dict[Path, str]) -> list[Path]:
    return sorted(path for path, content in outputs.items() if not (root / path).exists() or (root / path).read_text(encoding="utf-8") != content)


def write_outputs(root: Path, outputs: dict[Path, str]) -> None:
    for path, content in outputs.items():
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8", newline="\n")
