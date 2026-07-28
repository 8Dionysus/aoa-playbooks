# Guarded Infra Preview

Playbook: `infra-change-guarded`

Use when infra drift or a risky config action should first pass through an approval and preview seam.

Suggested seed:

- classify authority with `guard.operations.approval`
- prefer `guard.operations.preview`
- only recommend or apply the smallest next step through `workflow.operations.safe-infra-change`
