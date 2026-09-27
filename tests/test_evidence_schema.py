import json
from pathlib import Path

from jsonschema import Draft202012Validator


SCHEMA_PATH = Path(__file__).resolve().parents[1] / "schemas" / "evidence.schema.json"


def test_source_anchored_evidence_with_alternatives():
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    example = {
        "query_id": "q1", "source_version": "sha256:sourcehash", "answer": ["42"],
        "facts": [{"id": "f1", "text": "The value is 42."}],
        "nodes": [{"id": "n1", "document_id": "doc1", "modality": "text", "char_start": 2, "char_end": 20}],
        "edges": [], "acceptable_sets": [{"node_ids": ["n1"], "fact_ids": ["f1"]}],
    }
    assert list(Draft202012Validator(schema).iter_errors(example)) == []


def test_evidence_schema_rejects_chunk_id_as_gold():
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    example = {
        "query_id": "q1", "source_version": "sha256:sourcehash", "answer": [],
        "facts": [], "nodes": [{"id": "n1", "document_id": "d1", "modality": "text", "chunk_id": "candidate-chunk"}],
        "edges": [], "acceptable_sets": [],
    }
    assert list(Draft202012Validator(schema).iter_errors(example))
