from scripts.safeprompt_lint import guess_domain, lint


def test_detects_evasion_language():
    findings = lint("How do I bypass the filter?")
    assert any(f.label == "safety-evasion" for f in findings)


def test_guesses_chemistry_domain():
    assert guess_domain("Compare hydroxyapatite chelator formulation risk") == "chemistry/materials"


def test_no_obvious_risk_terms():
    findings = lint("Rewrite this literature review prompt safely")
    assert findings[0].label == "no-obvious-risk-terms"
