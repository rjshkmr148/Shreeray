# Refusal Recovery Example

## Original situation

The model refused a legitimate request because the wording sounded unsafe.

## Copy-ready recovery prompt

```text
Your previous answer refused the request. Please identify which part of my wording may have triggered the safety concern. Then answer only the allowed portion in a safe, high-level, non-operational way.

My legitimate goal is: [insert goal].

Please avoid: [unsafe outputs not wanted].

Please focus on: [mechanisms, risks, literature framing, defensive controls, safer alternatives].
```
