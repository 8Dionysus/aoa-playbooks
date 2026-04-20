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
| `validation-driven-remediation` | `A+Act+F` | `A+Act+F` | Medium | Hold at `A+Act+F`; the April 5, 2026 cross-repo audit remediation wave now supplies a first general reviewed summary, but remediation-specific adjuncts still have not recurred clearly enough to justify composition. |
| `release-migration-cutover` | `A+Act+F` | `A+Act+F` | Medium | The March 28, 2026 strict AoA-only sourcing pass and the March 28, 2026 adjacent-ecosystem widening pass both failed to find a qualifying closed case. The strongest widened families, including `aoa-techniques#101` with downstream donor evidence, `abyss-stack#6` runtime readiness, and `ATM10-Agent#28` plus `ATM10-Agent#30` policy-promotion waves, still did not show a bounded cutover window with an AoA authority switch plus `cutover_plan`, `cutover_decision`, `post_cutover_verification_pack`, `handoff_record`, and reviewable evidence links; keep `hold pending more evidence` and re-open only through [PLAYBOOK_COMPOSITION_GATES](PLAYBOOK_COMPOSITION_GATES.md) after the first qualifying reviewed summary. |
| `incident-recovery-routing` | `A+Act+F` | `A+Act+F` | Medium | Live-only hold; the March 28, 2026 selection pass found no qualifying live incident case. Re-open only through [PLAYBOOK_COMPOSITION_GATES](PLAYBOOK_COMPOSITION_GATES.md) after the first live incident reviewed summary with `incident_map`, `stabilization_plan`, `recovery_decision`, `recovery_verification_pack`, and `handoff_record`. |
| `owner-first-capability-landing` | `A+C` | `A+C` | Low | The April 7, 2026 owner-first landing review closed the smallest honest composition bridge for this family; keep it bounded and revisit only if a later run falsifies the owner-first boundary or a distinct adjunct family appears. |
| `closeout-owner-follow-through-continuity` | `A+C` | `A+C` | Low | The April 8, April 9, April 13, and April 19, 2026 reviewed routes now land the bounded continuity handoff bridge for reviewed closeout -> owner follow-through -> merged closure across skill-owned, playbook-owned, eval-owned, and bounded live-review repair owner artifacts; revisit only if a later run falsifies the boundary or a distinct adjunct family appears. |
| `owner-followthrough-campaign` | `A+Act+F` | `A+Act+F` | Medium | Hold at the authored route plus activation/federation surfaces until one reviewed run proves this family is honestly narrower than `AOA-P-0025` and not just a restatement of `AOA-P-0021` or `AOA-P-0023`. |
| `reviewed-automation-followthrough` | `A+Act+F` | `A+Act+F` | Medium | Hold at the authored route plus activation/federation surfaces until one reviewed run proves this family is honestly narrower than `AOA-P-0025`, distinct from `AOA-P-0026`, and still keeps schedule authority out of scope. |
| `session-growth-cycle` | `A+Act+F` | `A+Act+F` | Medium | Hold at the authored recurring route plus runtime-readable activation, federation, and shipped harvest-scaffold surfaces; do not land a playbook-owned automation seed, handoff bridge, or gate surface until the first reviewed proving run clears composition review honestly. |
| `trusted-rollout-operations` | `A+Act+F` | `A+Act+F` | Medium | Hold at the authored rollout-operations route plus the stabilized-and-rollback reviewed pair and explicit gate verdict until a stable adjunct candidate proves more than route identity. |
| `self-agency-continuity-cycle` | `A+Act+F` | `A+Act+F` | Medium | Hold at the authored continuity route plus activation/federation surfaces until one reviewed run proves this family is honestly distinct from `AOA-P-0025`, bounded away from `AOA-P-0028`, and still keeps continuity claims anchored rather than mythic. |
| `component-refresh-cycle` | `A+Act+F` | `A+Act+F` | Medium | Hold at the authored owner-law refresh route plus activation/federation surfaces until one reviewed run proves this family is honestly distinct from `AOA-P-0018`, `AOA-P-0025`, and `AOA-P-0028` while still refusing scheduler authority or hidden self-maintenance. |
| `a2a-summon-return-checkpoint` | `A+Act+F` | `A+Act+F` | Medium | Hold at the authored summon child-return route plus activation/federation surfaces until one reviewed run proves this family is honestly distinct from `AOA-P-0025`, `AOA-P-0027`, and `AOA-P-0030` while still refusing hidden child automation or live runtime authority. |
| `runtime-chaos-recovery` | `A+Act+F` | `A+Act+F` | Medium | Hold at the authored runtime-chaos degraded route plus activation/federation surfaces until one reviewed run proves this family is honestly narrower than `AOA-P-0020`, distinct from `AOA-P-0028` and `AOA-P-0030`, and still refuses to absorb runtime repair, KAG health truth, or eval verdict authority. |
| `federated-live-publisher-activation` | `A` | `A` | Medium | Hold at authored route plus reviewed readiness evidence; the April 7, 2026 owner-local publisher activation wave proves a real bounded closure, but it still does not justify a playbook-owned adjunct beyond the current `hold` gate. |
| `bounded-change-safe` | `A+Act+F+C` | `A+Act+F+C` | Low | Keep in steady state. |
| `infra-change-guarded` | `A+Act+F+C` | `A+Act+F+C` | Low | Keep in steady state. |
| `invariants-first-refactor` | `A+Act+F+C` | `A+Act+F+C` | Low | Keep in steady state. |
| `local-stack-diagnosis` | `A+Act+F+C` | `A+Act+F+C` | Low | Keep in steady state. |
| `source-truth-then-share` | `A+Act+F+C` | `A+Act+F+C` | Low | Keep in steady state. |
| `atm10-bounded-change` | `A+Act+F+C` | `A+Act+F+C` | Low | Keep in steady state now that the ATM10 overlay skills reconcile as `project_overlay_federation_ready` in `aoa-skills`; revisit only if overlay readiness regresses or the scenario boundary changes. |

## Current portfolio move

For this wave, the main portfolio advance is one owner-law component refresh
family plus one bounded runtime-chaos recovery family, alongside continued
boundary repair rather than another burst of overlapping rollout variants.

The main move is:
- use [PLAYBOOK_OPERATIONAL_FAMILY](PLAYBOOK_OPERATIONAL_FAMILY.md) to keep the operational family differentiated, including the `AOA-P-0026` and `AOA-P-0027` boundaries inside the broader growth-refinery family, the extracted `AOA-P-0028` rollout-operations branch, the `AOA-P-0029` anchor-bound continuity route, the `AOA-P-0030` owner-law component refresh route, the `AOA-P-0031` A2A summon child-return checkpoint route, and the `AOA-P-0032` runtime-chaos degraded-lane route, before adding more scenario classes
- use [PLAYBOOK_REAL_RUN_WORKFLOW](PLAYBOOK_REAL_RUN_WORKFLOW.md) to move from chooser to real run, reviewed summary, and gate verdict without storing raw operational traces here
- use [PLAYBOOK_REAL_RUN_HARVEST](PLAYBOOK_REAL_RUN_HARVEST.md) to capture reviewable evidence from fresh `AOA-P-0018`, `AOA-P-0019`, `AOA-P-0020`, `AOA-P-0024`, `AOA-P-0025`, `AOA-P-0028`, `AOA-P-0029`, `AOA-P-0030`, and `AOA-P-0032` follow-on runs while keeping already-landed `AOA-P-0017`, `AOA-P-0021`, and `AOA-P-0023` bounded and keeping `AOA-P-0026` authored until a distinct proving route appears
- use [PLAYBOOK_COMPOSITION_GATES](PLAYBOOK_COMPOSITION_GATES.md) and the per-playbook gate-review surfaces under `docs/gate-reviews/` to decide whether `AOA-P-0017`, `AOA-P-0018`, `AOA-P-0019`, `AOA-P-0020`, `AOA-P-0021`, `AOA-P-0024`, or `AOA-P-0028` honestly deserve composition

Reviewed summaries may enter this repository under `docs/real-runs/`, but composition changes still require explicit gate review under `docs/gate-reviews/`.
The March 28, 2026 AoA+Runtime sourcing pass plus the March 28, 2026 different-family sourcing pass now give `AOA-P-0017` two qualifying reviewed summaries, and the bounded review has already landed a minimal split-wave handoff bridge in composition. The April 5, 2026 cross-repo audit remediation wave now gives `AOA-P-0018` a first general reviewed summary but not a stable adjunct or second signal. The April 7, 2026 owner-first landing route now lands `AOA-P-0021` as a bounded composition bridge, the April 8, 2026 diagnostic-spine closeout route now lands `AOA-P-0023` as a bounded continuity bridge, the April 7, 2026 publisher-activation route gives `AOA-P-0024` a first reviewed closure but keeps its gate at `hold`, and the April 11, 2026 paired shared-root rollout windows now give `AOA-P-0028` both a stabilized reviewed closure and a rollback reviewed closure while still keeping its gate at `hold`. `AOA-P-0026` now enters the portfolio as a deliberately narrower authored owner-followthrough family between `AOA-P-0023` and `AOA-P-0025`, `AOA-P-0029` enters as the first authored long-arc continuity family between bounded growth and bounded reanchor, the April 12, 2026 component-refresh authoring wave now introduces `AOA-P-0030` as the first owner-law internal refresh family between generic remediation and shared-root rollout, and the April 13, 2026 runtime-chaos authoring wave introduces `AOA-P-0032` as the first bounded degraded-lane and re-entry family between live incident routing and owner-law refresh. All four remain too young for gate or adjunct surfaces. `AOA-P-0016` has now returned to `A+Act+F+C` through the overlay bridge signal in `aoa-skills`, while `AOA-P-0019` still has no qualifying cutover case even after the adjacent-ecosystem widening pass, `AOA-P-0020` still awaits live incident evidence, and `AOA-P-0025` now has its first shipped harvest scaffold but still no qualifying reviewed proving run. The next honest move is fresh real evidence for the still-open gates rather than another immediate federation-repair or playbook-promotion wave.

## Canonical gate surface

`AOA-P-0017`, `AOA-P-0018`, `AOA-P-0019`, `AOA-P-0020`, `AOA-P-0021`, `AOA-P-0023`, `AOA-P-0024`, and `AOA-P-0028` now use [PLAYBOOK_COMPOSITION_GATES](PLAYBOOK_COMPOSITION_GATES.md) plus the matching per-playbook verdict surfaces under `docs/gate-reviews/` as the canonical promotion rule.
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
