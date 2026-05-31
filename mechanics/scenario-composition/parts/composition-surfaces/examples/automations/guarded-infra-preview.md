# Guarded Infra Preview

Playbook: `infra-change-guarded`

Use when infra drift or a risky config action should first pass through an approval and preview seam.

Suggested seed:

- classify authority with `aoa-approval-gate-check`
- prefer `aoa-dry-run-first`
- only recommend or apply the smallest next step through `aoa-safe-infra-change`
