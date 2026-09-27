from awesome_rag_datasets.links import classify_http_status


def test_link_status_keeps_access_restrictions_distinct_from_missing():
    assert classify_http_status(200) == "reachable"
    assert classify_http_status(302) == "reachable"
    assert classify_http_status(403) == "restricted_or_rate_limited"
    assert classify_http_status(429) == "restricted_or_rate_limited"
    assert classify_http_status(404) == "missing"
    assert classify_http_status(503) == "uncertain"
