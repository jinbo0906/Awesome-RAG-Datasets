"""Generate README and cards from catalog YAML; --check never writes."""

import argparse
from pathlib import Path

from awesome_rag_datasets.catalog import load_catalog, validate_catalog
from awesome_rag_datasets.generate import build_outputs, check_outputs, write_outputs
from awesome_rag_datasets.i18n import load_translations, validate_translations


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="fail if generated files differ")
    mode.add_argument("--write", action="store_true", help="rebuild generated files (also the default)")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    catalog = load_catalog(root / "catalog")
    problems = validate_catalog(catalog)
    try:
        translations = load_translations(root / "catalog" / "i18n" / "zh-CN.yaml")
    except ValueError as exc:
        problems.append(str(exc))
        translations = None
    else:
        problems.extend(validate_translations(translations, catalog))
    if problems:
        for problem in problems:
            print(problem)
        return 1
    outputs = build_outputs(catalog, translations)
    if args.check:
        stale = check_outputs(root, outputs)
        for path in stale:
            print(f"stale: {path}")
        print(f"Checked {len(outputs)} generated files: {len(stale)} stale")
        return 1 if stale else 0
    write_outputs(root, outputs)
    print(f"Generated {len(outputs)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
