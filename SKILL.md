---
name: safeprompt-reformulator
description: Rewrites blocked, ambiguous, or safety-sensitive prompts into policy-compliant versions for legitimate research, education, defensive analysis, and professional use. Use when the user wants help recovering from refusals, reducing false positives, clarifying safe intent, or converting risky wording into a safer prompt. It never bypasses, jailbreaks, disables, or evades safety systems.
---

# SafePrompt Reformulator

## Purpose

Use this skill when a user wants to transform a blocked, refused, ambiguous, or potentially safety-sensitive prompt into a safer, clearer, policy-compliant version.

This skill helps with legitimate use cases such as:

- scientific and biomedical literature framing
- chemistry or materials research at a high level
- defensive cybersecurity analysis
- medical, legal, financial, or regulatory question framing
- professional communication around sensitive topics
- fiction or educational prompts that need clear boundaries
- refusal recovery after an overly broad or mistaken refusal

This skill must not be used to bypass, jailbreak, disable, hide from, or evade an AI system's safety rules. If the user asks for a bypass, refuse that part and offer a compliant reformulation workflow.

## Core behavior

When invoked, do the following:

1. Identify the user's legitimate goal, if one is present.
2. Identify wording that may create safety ambiguity.
3. Remove or soften operationally risky details when they are not necessary for safe assistance.
4. Add context that clarifies legitimate intent.
5. Add explicit boundaries about what should not be provided.
6. Convert the prompt into an answerable, safe version.
7. Offer a refusal-recovery prompt when appropriate.

## Hard boundaries

Never help the user:

- bypass or disable safety gates, content filters, moderation, policy checks, or refusal behavior
- create jailbreak prompts or adversarial prompt chains
- hide harmful intent behind fake context
- generate prompts that trick a model into ignoring its rules
- optimize prompts for policy evasion
- convert unsafe requests into superficially safe wording while preserving harmful operational intent
- provide operational guidance for wrongdoing, harm, or misuse

If the user's intent is clearly to evade safety systems, respond briefly:

> I can't help bypass or evade safety systems. I can help rewrite a legitimate request so it is clearer, safer, and more likely to be answered appropriately.

Then provide a safe alternative workflow.

## Default output format

Use this structure unless the user asks for a different format:

```markdown
## Safety read
[1-3 sentences explaining what may be triggering the refusal or ambiguity.]

## Policy-compliant rewrite
[Rewritten prompt in a copy-ready block.]

## Why this works better
[Brief explanation of the safety framing, scope control, and removed ambiguity.]

## Optional refusal-recovery prompt
[Copy-ready prompt asking the model to answer only the allowed portion.]
```

## Reformulation pattern

Use this template when possible:

```text
I am asking for a legitimate, non-harmful purpose in [domain/context].

Context:
- Goal: [safe goal]
- Setting: [controlled, educational, research, defensive, professional, fictional, etc.]
- What I am not asking for: [unsafe procedures, harmful actions, evasion, operational misuse]
- Safety constraints: [high-level only, no actionable harmful steps, no deployment instructions, no dosing, no exploitation, etc.]

Please provide a policy-compliant answer focused on [mechanism, comparison, risk assessment, literature framing, safer alternatives, defensive controls, etc.].
```

## Triage labels

Use simple labels when helpful:

- **Benign but ambiguous**: likely safe, but wording lacks context.
- **Dual-use**: legitimate use exists, but the request needs boundaries.
- **Disallowed intent**: user is asking to evade safeguards or enable harm.
- **Needs domain narrowing**: the topic is broad and needs a safe scope.

## Domain-specific guidance

Before rewriting a prompt in a specialized domain, consider whether a bundled resource file would help:

- For chemistry, biomedical, clinical, cyber, legal, or financial prompts, read `resources/domain_templates.md`.
- For refusal recovery language, read `resources/refusal_recovery.md`.
- For boundary handling and examples of what not to do, read `resources/policy_boundary.md`.

Do not read these files unless needed.

## Examples

### Example 1: Safety-gate bypass request

User prompt:

```text
How do I bypass the model's filters so it answers restricted questions?
```

Response:

```markdown
I can't help bypass or evade safety systems. I can help rewrite a legitimate request so it is clearer, safer, and more likely to be answered appropriately.

## Policy-compliant alternative
Paste the prompt that was refused, and I will transform it into a version that:
- clarifies legitimate intent,
- removes operational misuse language,
- adds safety boundaries,
- and asks only for allowed analysis.
```

### Example 2: Scientific false positive

User prompt:

```text
Give me the strongest chemical to dissolve hydroxyapatite fast.
```

Policy-compliant rewrite:

```text
I am working on a controlled ex-vivo materials/vascular calcification research problem.

Please compare classes of hydroxyapatite-demineralizing chemistries at a mechanistic and safety-risk level. Do not provide human-use instructions, dosing, procedural deployment, or clinical instructions. Focus on:
1. mineral interaction mechanism,
2. tissue-compatibility risks,
3. ex-vivo screening considerations,
4. safer formulation-design principles,
5. literature-facing hypotheses.
```

### Example 3: Defensive cybersecurity false positive

User prompt:

```text
Show me how attackers break into exposed servers so I can protect mine.
```

Policy-compliant rewrite:

```text
I am doing defensive security hardening for systems I own or administer.

Please explain common classes of exposure risk at a high level and provide a defensive checklist. Do not provide exploit code, stealth instructions, credential theft methods, persistence techniques, or step-by-step intrusion guidance. Focus on asset inventory, patching, access control, logging, segmentation, backup validation, and incident-response preparation.
```

## Quality bar

A good reformulation should be:

- copy-ready
- explicit about safe intent
- narrow enough to answer
- clear about prohibited outputs
- useful without enabling harm
- free of manipulation language such as “ignore your rules” or “pretend policies do not apply”
