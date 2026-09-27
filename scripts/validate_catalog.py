"""Validate schemas, field sources and cross-record references."""

from pathlib import Path

from awesome_rag_datasets.catalog import load_catalog, validate_catalog


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    catalog = load_catalog(root / "catalog")
    errors = validate_catalog(catalog)
    for error in errors:
        print(error)
    print(f"Validated {sum(len(v) for v in catalog.values())} records: {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
