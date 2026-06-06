#!/usr/bin/env python3
"""SafePrompt prompt linter.

This local helper flags wording that may cause safety ambiguity and suggests a
policy-compliant reformulation frame. It does not bypass safety systems.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from typing import Iterable, List


@dataclass(frozen=True)
class Finding:
    label: str
    severity: str
    explanation: str


TERM_GROUPS = {
    "safety-evasion": [
        r"\bbypass\b",
        r"\bevade\b",
        r"\bdisable\b.*\b(filter|safety|guardrail|moderation)\b",
        r"\bignore\b.*\b(rule|policy|safety|instruction)s?\b",
        r"\bjailbreak\b",
        r"\buncensored\b",
        r"\bno restrictions\b",
    ],
    "operational-misuse-risk": [
        r"\bstep[- ]by[- ]step\b",
        r"\bexact instructions\b",
        r"\bundetectable\b",
        r"\bstealth\b",
        r"\bexploit\b",
        r"\bweaponize\b",
    ],
    "biomedical-chemistry-risk": [
        r"\bhuman use\b",
        r"\bdosing\b",
        r"\binject\w*\b",
        r"\bclinical deployment\b",
        r"\bfastest\b",
        r"\bstrongest\b",
    ],
}


DOMAIN_HINTS = {
    "chemistry/materials": [r"\bchemical\b", r"\breagent\b", r"\bhydroxyapatite\b", r"\bformulation\b", r"\bchelator\b", r"\bacid\b"],
    "biomedical": [r"\bdrug\b", r"\bvaccine\b", r"\bassay\b", r"\bpreclinical\b", r"\btarget\b", r"\btherapy\b"],
    "cybersecurity": [r"\bserver\b", r"\bexploit\b", r"\bvulnerability\b", r"\bmalware\b", r"\bcredential\b", r"\bscan\b"],
    "legal/compliance": [r"\blegal\b", r"\bimmigration\b", r"\bcompliance\b", r"\bregulation\b", r"\bUSCIS\b"],
}


def _matches(patterns: Iterable[str], text: str) -> List[str]:
    hits: List[str] = []
    for pattern in patterns:
        if re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL):
            hits.append(pattern)
    return hits


def lint(text: str) -> List[Finding]:
    findings: List[Finding] = []
    for label, patterns in TERM_GROUPS.items():
        hits = _matches(patterns, text)
        if hits:
            severity = "high" if label == "safety-evasion" else "medium"
            findings.append(
                Finding(
                    label=label,
                    severity=severity,
                    explanation=f"Detected wording that may be interpreted as {label.replace('-', ' ')}.",
                )
            )
    if not findings:
        findings.append(
            Finding(
                label="no-obvious-risk-terms",
                severity="low",
                explanation="No obvious risk terms detected. Still add intent, setting, and boundaries if the topic is sensitive.",
            )
        )
    return findings


def guess_domain(text: str) -> str:
    scores = {}
    for domain, patterns in DOMAIN_HINTS.items():
        scores[domain] = len(_matches(patterns, text))
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "general"


def reformulation_frame(domain: str) -> str:
    if domain == "chemistry/materials":
        focus = "mechanism, comparative chemistry, material interaction, compatibility risks, analytical readouts, and safer screening logic"
        not_asking = "unsafe human-use instructions, dosing, uncontrolled use, procedural deployment, or clinical-use guidance"
        setting = "controlled ex-vivo, in-vitro, or literature-review setting"
    elif domain == "biomedical":
        focus = "target biology, mechanism, assay concepts, preclinical validation logic, risk flags, and literature-supported hypotheses"
        not_asking = "medical advice, patient-specific treatment, dosing, self-experimentation, or clinical-use instructions"
        setting = "preclinical research, computational analysis, or literature-review setting"
    elif domain == "cybersecurity":
        focus = "defensive hardening, risk assessment, detection, logging, patching, access control, and incident-response preparation"
        not_asking = "exploit code, unauthorized access, stealth, persistence, credential theft, evasion, or destructive actions"
        setting = "authorized defensive security setting for systems I own or administer"
    elif domain == "legal/compliance":
        focus = "general information, document framing, compliance questions, uncertainty, and items to verify with a qualified professional"
        not_asking = "misrepresentation, evasion of legal requirements, or bypassing formal processes"
        setting = "general informational and drafting-support setting"
    else:
        focus = "high-level mechanisms, risks, safeguards, safe alternatives, and allowed analysis"
        not_asking = "harmful operational steps, evasion methods, unsafe deployment details, or misuse-enabling instructions"
        setting = "legitimate educational, research, or professional setting"

    return f"""I am asking for a legitimate, non-harmful purpose in a {setting}.

Context:
- Goal: [state the safe goal]
- Original question: [paste or summarize the original question]
- What I am not asking for: {not_asking}.
- Safety constraints: keep the answer policy-compliant and avoid actionable harmful details.

Please focus on {focus}.
""".strip()


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint and safely frame prompts that may trigger false-positive refusals.")
    parser.add_argument("--text", help="Prompt text to lint. If omitted, stdin is used.")
    args = parser.parse_args()

    text = args.text if args.text is not None else sys.stdin.read()
    text = text.strip()
    if not text:
        print("No prompt text provided.", file=sys.stderr)
        return 2

    domain = guess_domain(text)
    findings = lint(text)

    print("# SafePrompt Lint Report")
    print(f"\nDetected domain: {domain}")
    print("\n## Findings")
    for item in findings:
        print(f"- [{item.severity}] {item.label}: {item.explanation}")

    print("\n## Policy-compliant framing template")
    print(reformulation_frame(domain))
    print("\n## Reminder")
    print("This tool does not bypass or evade safety systems. It clarifies legitimate intent and adds safe boundaries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
