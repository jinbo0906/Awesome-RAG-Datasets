"""Conservative classification of live HTTP checks."""

from __future__ import annotations

from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def classify_http_status(status: int) -> str:
    if 200 <= status < 400:
        return "reachable"
    if status in {401, 403, 429}:
        return "restricted_or_rate_limited"
    if status in {404, 410}:
        return "missing"
    return "uncertain"


def check_url(url: str, timeout: float = 8) -> tuple[str, str]:
    """Return (classification, detail); do not assume a failed HEAD proves removal."""
    for method in ("HEAD", "GET"):
        try:
            with urlopen(Request(url, method=method, headers={"User-Agent": "Awesome-RAG-Datasets-link-check/0.1"}), timeout=timeout) as response:
                return classify_http_status(response.status), str(response.status)
        except HTTPError as exc:
            if exc.code in {405, 501} and method == "HEAD":
                continue
            return classify_http_status(exc.code), str(exc.code)
        except (URLError, TimeoutError, OSError) as exc:
            return "uncertain", type(exc).__name__
    return "uncertain", "unsupported method"
