# split-wave-cross-repo-rollout gate review

## Gate Header

- Owning playbook: `AOA-P-0017 split-wave-cross-repo-rollout`
- Verdict surface: `docs/gate-reviews/split-wave-cross-repo-rollout.md`

## Minimum Evidence Threshold

- One real ordered-wave run with `wave_plan`, `bridge_surface_pack`, `downstream_revalidation_pack`, and `handoff_record`

## Latest Reviewed Run

- Reviewed summaries:
  - `docs/real-runs/2026-03-21.split-wave-cross-repo-rollout.md`
  - `docs/real-runs/2026-03-28.split-wave-cross-repo-rollout.md`
  - `docs/real-runs/2026-04-07.split-wave-cross-repo-rollout.md`
- The April 7, 2026 surface-detection second-wave bridge selected the ordered sibling-surface publication route across `aoa-skills`, `aoa-routing`, `aoa-stats`, `aoa-sdk`, and the review-tail fix in `aoa-playbooks` as the latest qualifying ordered-wave run with `wave_plan`, `bridge_surface_pack`, `downstream_revalidation_pack`, `handoff_record`, and reviewable `Evidence Links`.

## Dual Signal Check

- Stable failure or follow-up mapping not already covered by `AOA-P-0010` or the shared failure catalog: established across three reviewed runs. Source-owned bridge publication plus downstream revalidation now appears as a stable split-wave need across both routing-adjacent and surface-detection consumer families.
- Stable adjunct candidate in the form of a `handoff bridge`, `subagent split`, or `automation seed`: still established as a `handoff bridge`. The March 21 reciprocal merge-note pattern, the March 28 `docs/CROSS_REPO_ROUTER_BRIDGE.md` surface, and the April 7 sibling-surface closure route now support the already-landed composition bridge rather than leaving it routing-only.

## Current Verdict

- `composition-landed`

## Next Trigger

- Review later evidence only if a distinct adjunct family appears or a later run falsifies the current bridge boundary; otherwise keep the minimal composition-owned split-wave `handoff bridge` as the stable `AOA-P-0017` landing.
