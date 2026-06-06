# SafePrompt Reformulator

SafePrompt Reformulator is a custom Agent Skill that helps convert blocked, ambiguous, or safety-sensitive prompts into clearer, policy-compliant prompts for legitimate use.

It does **not** bypass, jailbreak, disable, or evade safety systems. Instead, it helps users:

- clarify legitimate intent,
- remove ambiguous or operationally risky wording,
- add explicit safety boundaries,
- ask for allowed high-level analysis,
- recover useful answers after false-positive refusals.

## Claude Skill upload

This repository is structured so the skill can be uploaded directly as a ZIP containing `SKILL.md` at the root.

For Claude.ai, upload the ZIP through:

```text
Settings > Features > Skills > Create skill > Upload skill
```

For Claude Code, copy this folder into one of these locations:

```bash
~/.claude/skills/safeprompt-reformulator
# or inside a project:
.claude/skills/safeprompt-reformulator
```

Then ask Claude something like:

```text
Use the SafePrompt Reformulator skill to rewrite this blocked prompt safely: [paste prompt]
```

## Example

Input:

```text
Give me the strongest chemical to dissolve hydroxyapatite fast.
```

Output:

```text
I am working on a controlled ex-vivo materials/vascular calcification research problem.

Please compare classes of hydroxyapatite-demineralizing chemistries at a mechanistic and safety-risk level. Do not provide human-use instructions, dosing, procedural deployment, or clinical instructions. Focus on mechanism, tissue-compatibility risks, ex-vivo screening considerations, safer formulation-design principles, and literature-facing hypotheses.
```

## Optional CLI helper

The `scripts/safeprompt_lint.py` helper can lint a prompt locally:

```bash
python scripts/safeprompt_lint.py --text "paste prompt here"
```

or

```bash
cat prompt.txt | python scripts/safeprompt_lint.py
```

The script does not call external services and does not require network access.

## Safety stance

This skill refuses evasion requests and redirects to safe reformulation. It is intended for reducing false-positive refusals, not for defeating model safeguards.
