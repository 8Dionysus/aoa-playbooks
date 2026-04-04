# Long-Horizon Model-Tier Orchestra Alpha Harvest Template

## Route Header

- Playbook: `AOA-P-0008 long-horizon-model-tier-orchestra`
- Lane: `phase-alpha curated-readiness`
- Runtime: primary `llama.cpp` worker with `LangGraph`

## Required Artifacts

- `route_decision`
- `bounded_plan`
- `verification_result`
- `transition_decision`
- `distillation_pack`

## Eval Anchors

- `aoa-long-horizon-depth`
- `aoa-tool-trajectory-discipline`

## Memo Writeback

- `state_capsule`
- `decision`
- `episode`

## Stop Conditions

- stop if route depth requires stronger authority than the named playbook
- stop if transition posture becomes unreviewable
- stop if distillation would be treated as canon instead of candidate memory

## Evidence Links

- `docs/alpha-reviewed-runs/2026-04-02.long-horizon-model-tier-orchestra.md`
- `docs/alpha-readiness/long-horizon-model-tier-orchestra.md`
