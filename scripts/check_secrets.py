"""Check public files without printing credential material."""

import subprocess
from pathlib import Path

from awesome_rag_datasets.hygiene import scan_public_files


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=root, capture_output=True, check=True,
    )
    paths = [Path(item.decode("utf-8")) for item in result.stdout.split(b"\0") if item]
    paths = [path for path in paths if path.parts[0] not in {"tests", "docs"}]
    issues = scan_public_files(root, paths)
    for issue in issues:
        print(issue)
    print(f"Scanned {len(paths)} public paths: {len(issues)} issue(s)")
    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())
