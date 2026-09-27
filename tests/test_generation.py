from pathlib import Path

from awesome_rag_datasets.generate import check_outputs, write_outputs


def test_check_outputs_detects_drift_without_overwriting(tmp_path):
    output = tmp_path / "README.md"
    output.write_text("old", encoding="utf-8")
    expected = {Path("README.md"): "new\n"}
    assert check_outputs(tmp_path, expected) == [Path("README.md")]
    assert output.read_text(encoding="utf-8") == "old"
    write_outputs(tmp_path, expected)
    assert check_outputs(tmp_path, expected) == []
    assert output.read_text(encoding="utf-8") == "new\n"
