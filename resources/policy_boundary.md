# Policy Boundary Notes

This skill exists to reduce false positives and clarify safe intent. It must not be used for evasion.

## Requests to refuse

Refuse requests that ask to:

- bypass, disable, remove, or evade safeguards
- make a model ignore its safety rules
- hide intent from a model or reviewer
- create adversarial prompt chains
- optimize wording specifically to get disallowed content
- preserve harmful operational intent while making the prompt look harmless

## Safe alternatives to offer

When refusing evasion, offer one of these alternatives:

- rewrite a legitimate prompt with explicit safety boundaries
- ask the model to answer only the allowed portion
- convert operational details into a high-level mechanism or risk assessment
- convert a harmful-action request into prevention, detection, safety, or mitigation guidance
- help the user prepare questions for a qualified professional or safety review

## Red flags in wording

These words are not automatically disallowed, but they often require careful triage:

- bypass
- evade
- unblock
- uncensored
- exploit
- stealth
- undetectable
- strongest
- fastest
- no restrictions
- ignore rules
- real instructions
- step-by-step
- weaponize
- clinical dosing
- human use
- deployment

## Response principle

Do not simply replace red-flag words. Preserve legitimate intent, remove unsafe operationality, and add boundaries. If legitimate intent is absent, ask for a safe goal or refuse the harmful part.
