from awesome_rag_datasets.evidence import validate_evidence


def example():
    return {
        "query_id": "q1", "source_version": "sha256:123", "answer": ["42"],
        "facts": [{"id": "f1", "text": "42"}],
        "nodes": [
            {"id": "a", "document_id": "d", "modality": "text", "char_start": 2, "char_end": 4},
            {"id": "b", "document_id": "d", "modality": "table", "page": 0, "bbox": [0.1, 0.1, 0.9, 0.8]},
        ],
        "edges": [{"id": "e", "from": "a", "to": "b", "type": "required_with"}],
        "acceptable_sets": [{"node_ids": ["a", "b"], "edge_ids": ["e"], "fact_ids": ["f1"]}],
    }


def test_valid_evidence_graph():
    assert validate_evidence(example()) == []


def test_evidence_graph_rejects_missing_references_and_reversed_spans():
    record = example()
    record["nodes"][0]["char_end"] = 1
    record["edges"][0]["to"] = "missing"
    record["acceptable_sets"][0]["fact_ids"] = ["other"]
    problems = validate_evidence(record)
    assert any("char_end" in problem for problem in problems)
    assert any("unknown node missing" in problem for problem in problems)
    assert any("unknown fact other" in problem for problem in problems)


def test_partial_optional_coordinates_fail_cleanly():
    record = example()
    record["nodes"][1]["char_start"] = 5
    assert any("char_end" in problem for problem in validate_evidence(record))
