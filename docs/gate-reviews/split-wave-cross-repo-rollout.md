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
- The March 28, 2026 different-family sourcing pass selected the March 28, 2026 wave-9 tiny-router bridge route across `aoa-skills` and `aoa-routing` as the second qualifying ordered-wave run with `wave_plan`, `bridge_surface_pack`, `downstream_revalidation_pack`, `handoff_record`, and reviewable `Evidence Links`.

## Dual Signal Check

- Stable failure or follow-up mapping not already covered by `AOA-P-0010` or the shared failure catalog: established across two different-family runs; sibling-surface consumer waves now show a stable need for explicit merge-order constraints and downstream revalidation against updated upstream state
- Stable adjunct candidate in the form of a `handoff bridge`, `subagent split`, or `automation seed`: established as a `handoff bridge` candidate; the March 21 reciprocal merge-note pattern and the March 28 `docs/CROSS_REPO_ROUTER_BRIDGE.md` surface now support later composition review

## Current Verdict

- `ready-for-composition-review`

## Next Trigger

- Open a bounded composition review for `AOA-P-0017` focused on a split-wave `handoff bridge` adjunct, while leaving `config/playbook_composition_overrides.json` unchanged until that later review lands.
