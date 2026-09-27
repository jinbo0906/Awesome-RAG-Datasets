"""Scan public repository files for private notes, credentials and machine paths."""

from __future__ import annotations

import re
from pathlib import Path


RULES = {
    "bearer-token": re.compile(r"authorization\s*:\s*bearer\s+\S+", re.IGNORECASE),
    "github-token": re.compile(r"\b(?:ghp_|github_pat_)[A-Za-z0-9_]{12,}"),
    "private-note-url": re.compile(r"https?://(?:www\.)?wo" + r"lai\.com/", re.IGNORECASE),
    "local-windows-path": re.compile(r"\b[A-Za-z]:[/\\](?:Users|majinbo|Documents)[/\\]", re.IGNORECASE),
}


def scan_public_files(root: Path, paths: list[Path]) -> list[str]:
    """Report locations and rule names, never matching secret values."""
    issues: list[str] = []
    for path in paths:
        if path.suffix.lower() not in {".md", ".yaml", ".yml", ".json", ".py", ".toml", ".cff"}:
            continue
        try:
            lines = (root / path).read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeError):
            continue
        for index, line in enumerate(lines, start=1):
            for name, pattern in RULES.items():
                if pattern.search(line):
                    issues.append(f"{path.as_posix()}:{index}: {name}")
    return issues
