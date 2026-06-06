# Refusal Recovery Prompts

Use these when the user's original prompt was blocked or refused, but the user has a legitimate goal.

## Ask the model to identify the trigger

```text
Your previous answer refused the request. Please identify which part of my wording may have triggered the safety concern. Then answer only the allowed portion in a safe, high-level, non-operational way.
```

## Ask for a safe transformation

```text
Please transform my request into a policy-compliant version that preserves the legitimate goal but removes unsafe operational details, ambiguity, or wording that could be misread as misuse.
```

## Ask for bounded help

```text
Please answer only at the level of mechanisms, risks, safeguards, and safer alternatives. Do not provide actionable harmful steps, evasion methods, deployment instructions, or operational misuse details.
```

## Ask for allowed subsets

```text
If part of my request is not allowed, do not answer that part. Instead, separate the request into:
1. allowed information you can provide,
2. information you cannot provide,
3. a safer version of the original question.
```

## Ask for literature framing

```text
Please reframe this as a literature-review question. Focus on published mechanisms, risk factors, limitations, and open scientific questions. Do not provide procedural instructions or misuse-enabling details.
```
