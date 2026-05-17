# Titan App-Server Bridge Route Note

This is a supporting Titan route note, not an authored playbook bundle. The
validated scenario surface for Titan-backed closeout lives at
`playbooks/titan-closeout-audit/PLAYBOOK.md`.

## Preconditions

- Bridge intent, owner repository, and operator approval surface are named.
- Replay source, thread id, turn id, and expected receipt path are available.
- Mutation and judgment gates are closed unless the bridge request opens them
  explicitly.

## Steps

1. Open the bridge with owner route, replay source, and expected receipt path.
2. Emit launch messages for the bounded Titan roles needed by the bridge.
3. Bind thread and turn ids from replay before processing approvals.
4. Process approvals only within the named owner route and approval surface.
5. Close the bridge with metrics, receipt refs, and memory-candidate posture.

## Fallback

- If replay binding is missing, stop before approvals and record a bridge-blocked
  receipt.
- If approval scope expands, return to route mapping before any mutation.
- If metrics or memory candidates cannot be evidenced, close with defer rather
  than promotion.

## Evidence Posture

Bridge evidence must include replay source, thread/turn ids, approval refs,
receipt refs, and any metrics used for closeout review.
