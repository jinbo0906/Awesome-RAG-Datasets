from awesome_rag_datasets.i18n import validate_translations


CATALOG = {
    "datasets": [{
        "id": "example", "summary": "Example summary",
        "data": {"description": "Source construction", "size": "120 questions"},
        "ground_truth": {"description": "Source evidence"},
        "evaluation": {"protocol": "Use the fixed split"},
        "use": {"best_for": ["retrieval"], "caveats": ["supplied context"]},
    }],
    "suites": [{"id": "suite", "summary_zh": "套件说明", "protocol": "Fixed qrels"}],
}

TRANSLATIONS = {
    "datasets": {"example": {
        "summary": "样本摘要", "data_description": "来源构建",
        "size": "120 个问题", "ground_truth_description": "来源证据",
        "evaluation_protocol": "使用固定划分", "best_for": ["检索"],
        "caveats": ["已给定上下文"],
    }},
    "suites": {"suite": {"protocol": "固定相关性标注"}},
}


def test_translation_manifest_covers_every_record_and_narrative_field():
    assert validate_translations(TRANSLATIONS, CATALOG) == []
    missing = {**TRANSLATIONS, "datasets": {}}
    assert any("example" in issue for issue in validate_translations(missing, CATALOG))
    missing_field = {**TRANSLATIONS, "datasets": {"example": {"summary": "样本摘要"}}}
    assert any("data_description" in issue for issue in validate_translations(missing_field, CATALOG))


def test_translation_manifest_rejects_list_count_mismatch_and_untracked_id():
    wrong = {**TRANSLATIONS, "datasets": {
        "example": {**TRANSLATIONS["datasets"]["example"], "caveats": []},
        "stray": TRANSLATIONS["datasets"]["example"],
    }}
    issues = validate_translations(wrong, CATALOG)
    assert any("caveats" in issue for issue in issues)
    assert any("stray" in issue for issue in issues)


def test_translation_manifest_rejects_english_only_narrative():
    english_only = {**TRANSLATIONS, "datasets": {
        "example": {**TRANSLATIONS["datasets"]["example"], "summary": "English only"},
    }}
    assert any("summary" in issue for issue in validate_translations(english_only, CATALOG))
