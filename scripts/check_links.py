"""Optional live check of canonical catalog URLs. Network errors are not removal proof."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from awesome_rag_datasets.catalog import load_catalog
from awesome_rag_datasets.links import check_url


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0, help="check only the first N sorted URLs (0 = all)")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    catalog = load_catalog(root / "catalog")
    urls = sorted({record["access"]["official"] for kind in ("datasets", "suites", "corpora") for record in catalog[kind]})
    if args.limit > 0:
        urls = urls[: args.limit]
    with ThreadPoolExecutor(max_workers=8) as pool:
        outcomes = list(pool.map(check_url, urls))
    for url, (classification, detail) in zip(urls, outcomes):
        print(f"{classification:27} {detail:12} {url}")
    missing = sum(classification == "missing" for classification, _ in outcomes)
    print(f"Checked {len(urls)} URLs: {missing} reported missing; review manually before editing records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
