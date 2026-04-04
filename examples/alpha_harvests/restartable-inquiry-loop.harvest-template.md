# Restartable Inquiry Loop Alpha Harvest Template

## Route Header

- Playbook: `AOA-P-0009 restartable-inquiry-loop`
- Lane: `phase-alpha curated-readiness`
- Runtime: primary `llama.cpp` worker with bounded return posture

## Required Artifacts

- `inquiry_checkpoint`
- `decision_ledger`
- `contradiction_map`
- `memory_delta`
- `canon_delta`
- `next_pass_brief`

## Eval Anchors

- `aoa-long-horizon-depth`
- `aoa-return-anchor-integrity`

## Memo Writeback

- `state_capsule`
- `decision`
- `provenance_thread`

## Stop Conditions

- stop if checkpoint continuity is lost
- stop if contradiction handling widens into unbounded canon work
- stop if the next pass brief cannot name a bounded return anchor

## Evidence Links

- `docs/alpha-reviewed-runs/2026-04-02.restartable-inquiry-loop.md`
- `docs/alpha-readiness/restartable-inquiry-loop.md`
