# Playbook Gap Matrix

This document records the current lifecycle posture of the playbook portfolio and the next bounded graduation move for each playbook.

The point is not to push every playbook upward.
The point is to keep the smallest honest form for each scenario while making the next portfolio move explicit.

Legend:
- `R` = registry
- `A` = authored
- `Act` = activation
- `F` = federation
- `C` = composition

## Current matrix

| Playbook | Current | Target | Priority | Next move |
| --- | --- | --- | --- | --- |
| `repo-bootstrap` | `R` | `R` | Low | Keep as a registry placeholder until the next real bootstrap route recurs. |
| `safe-change-rollout` | `R` | `R` | Low | Keep as the umbrella archetype and do not duplicate `AOA-P-0011`, `AOA-P-0012`, or `AOA-P-0016`. |
| `bounded-research-pass` | `R` | `R` | Low | Hold until a repeated short research route appears that is distinct from `AOA-P-0009`. |
| `release-prep` | `R` | `R` | Low | Keep as the registry umbrella for checklist-style prep and do not widen it into `AOA-P-0019`. |
| `memory-curation-pass` | `R` | `R` | Low | Keep as the umbrella until a standalone non-witness memory route recurs. |
| `self-agent-checkpoint-rollout` | `A+F` | `A+F` | Low | Keep it federation-checked but intentionally non-activation unless a runtime-readable checkpoint seam becomes honest. |
| `witness-to-compost-pilot` | `A+F` | `A+F` | Low | Keep as a federation-only pilot rather than widening it into activation. |
| `long-horizon-model-tier-orchestra` | `A+Act+F` | `A+Act+F` | Low | Hold steady and add composition only if stable operational adjuncts recur. |
| `restartable-inquiry-loop` | `A+Act+F` | `A+Act+F` | Low | Hold steady as the restartable recurrence reference route. |
| `cross-repo-boundary-rollout` | `A+Act+F` | `A+Act+F` | High | Keep as the generic single-wave baseline and branch split-wave choreography into `AOA-P-0017`. |
| `split-wave-cross-repo-rollout` | `A+Act+F+C` | `A+Act+F+C` | Low | The March 28, 2026 two-run record cleared bounded composition review and landed a minimal split-wave `handoff bridge` through the composition-owned handoff contract surface; revisit only if a non-routing third run or a distinct adjunct candidate appears. |
| `validation-driven-remediation` | `A+Act+F` | `A+Act+F` | Medium | Hold at `A+Act+F` until remediation-specific adjuncts recur clearly enough to justify composition. |
| `release-migration-cutover` | `A+Act+F` | `A+Act+F` | Medium | The March 28, 2026 strict AoA-only sourcing pass reviewed the strongest visible AoA candidate families, including the `aoa-techniques#101` donor-evidence promotion chain, routing activation waves such as `aoa-routing#20`, and single-repo default-entrypoint promotions such as `aoa-techniques#115`, and still found no qualifying closed case with `cutover_plan`, `cutover_decision`, `post_cutover_verification_pack`, `handoff_record`, and reviewable evidence links; keep `hold pending more evidence` and re-open only through [PLAYBOOK_COMPOSITION_GATES](PLAYBOOK_COMPOSITION_GATES.md) after the first qualifying reviewed summary. |
| `incident-recovery-routing` | `A+Act+F` | `A+Act+F` | Medium | Live-only hold; the March 28, 2026 selection pass found no qualifying live incident case. Re-open only through [PLAYBOOK_COMPOSITION_GATES](PLAYBOOK_COMPOSITION_GATES.md) after the first live incident reviewed summary with `incident_map`, `stabilization_plan`, `recovery_decision`, `recovery_verification_pack`, and `handoff_record`. |
| `bounded-change-safe` | `A+Act+F+C` | `A+Act+F+C` | Low | Keep in steady state. |
| `infra-change-guarded` | `A+Act+F+C` | `A+Act+F+C` | Low | Keep in steady state. |
| `invariants-first-refactor` | `A+Act+F+C` | `A+Act+F+C` | Low | Keep in steady state. |
| `local-stack-diagnosis` | `A+Act+F+C` | `A+Act+F+C` | Low | Keep in steady state. |
| `source-truth-then-share` | `A+Act+F+C` | `A+Act+F+C` | Low | Keep in steady state. |
| `atm10-bounded-change` | `A+Act+C` | `A+Act+F+C` | Medium | Intentional repo-first hold outside federation while `atm10-source-of-truth-check` and `atm10-change-protocol` remain `project_overlay_eval_ready` in `aoa-skills`; revisit only after both become federation-eligible there. |

## Current portfolio move

For this wave, the main portfolio advance is consolidation rather than catalog growth.

The main move is:
- use [PLAYBOOK_OPERATIONAL_FAMILY](PLAYBOOK_OPERATIONAL_FAMILY.md) to keep the operational family differentiated before adding more scenario classes
- use [PLAYBOOK_REAL_RUN_WORKFLOW](PLAYBOOK_REAL_RUN_WORKFLOW.md) to move from chooser to real run, reviewed summary, and gate verdict without storing raw operational traces here
- use [PLAYBOOK_REAL_RUN_HARVEST](PLAYBOOK_REAL_RUN_HARVEST.md) to capture reviewable evidence from the first real `AOA-P-0017`, `AOA-P-0019`, and `AOA-P-0020` runs
- use [PLAYBOOK_COMPOSITION_GATES](PLAYBOOK_COMPOSITION_GATES.md) and the per-playbook gate-review surfaces under `docs/gate-reviews/` to decide whether `AOA-P-0017`, `AOA-P-0019`, or `AOA-P-0020` honestly deserve composition

No new playbook should enter the portfolio just to fill space while these chooser, harvest, and gate surfaces are still the next honest move.
Reviewed summaries may enter this repository under `docs/real-runs/`, but composition changes still require explicit gate review under `docs/gate-reviews/`.
The March 28, 2026 AoA+Runtime sourcing pass plus the March 28, 2026 different-family sourcing pass now give `AOA-P-0017` two qualifying reviewed summaries, and the bounded review has already landed a minimal split-wave handoff bridge in composition. `AOA-P-0019` still has no qualifying cutover case and `AOA-P-0020` still awaits live incident evidence, so the next honest move is continued evidence capture for those remaining gates rather than another immediate `AOA-P-0017` promotion wave.

## Canonical gate surface

`AOA-P-0017`, `AOA-P-0019`, and `AOA-P-0020` now use [PLAYBOOK_COMPOSITION_GATES](PLAYBOOK_COMPOSITION_GATES.md) plus the matching per-playbook verdict surfaces under `docs/gate-reviews/` as the canonical promotion rule.
This matrix keeps only the lifecycle summary.
The gate doc owns the required artifact sets, minimum evidence threshold, dual-signal rule, and the default non-promotion posture.

## Discipline

Use this matrix to decide whether the next honest move is:
- stay smaller
- author the route
- make the route runtime-readable through activation
- make the route cross-repo checkable through federation
- add composition only when bounded handoff, failure, subagent, or automation adjuncts truly recur

Do not use this matrix to force growth for its own sake.
