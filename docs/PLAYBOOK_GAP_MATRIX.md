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
| `release-prep` | `R` | `R` | Medium | Defer uplift and cover the stronger near-term need with later cutover or migration work. |
| `memory-curation-pass` | `R` | `R` | Low | Keep as the umbrella until a standalone non-witness memory route recurs. |
| `self-agent-checkpoint-rollout` | `A` | `A+F` | Medium | Queue a later federation pass without making it activation-eligible. |
| `witness-to-compost-pilot` | `A+F` | `A+F` | Low | Keep as a federation-only pilot rather than widening it into activation. |
| `long-horizon-model-tier-orchestra` | `A+Act+F` | `A+Act+F` | Low | Hold steady and add composition only if stable operational adjuncts recur. |
| `restartable-inquiry-loop` | `A+Act+F` | `A+Act+F` | Low | Hold steady as the restartable recurrence reference route. |
| `cross-repo-boundary-rollout` | `A+Act+F` | `A+Act+F` | High | Keep as the generic single-wave baseline and branch split-wave choreography into `AOA-P-0017`. |
| `bounded-change-safe` | `A+Act+F+C` | `A+Act+F+C` | Low | Keep in steady state. |
| `infra-change-guarded` | `A+Act+F+C` | `A+Act+F+C` | Low | Keep in steady state. |
| `invariants-first-refactor` | `A+Act+F+C` | `A+Act+F+C` | Low | Keep in steady state. |
| `local-stack-diagnosis` | `A+Act+F+C` | `A+Act+F+C` | Low | Keep in steady state. |
| `source-truth-then-share` | `A+Act+F+C` | `A+Act+F+C` | Low | Keep in steady state. |
| `atm10-bounded-change` | `A+Act+F+C` | `A+Act+F+C` | Low | Keep in steady state. |

## Current portfolio move

For this wave, the main portfolio advance is not mass graduation.

The main move is:
- add `AOA-P-0017 split-wave-cross-repo-rollout` as `A+Act+F`
- keep `AOA-P-0010 cross-repo-boundary-rollout` as the generic single-wave baseline
- leave composition out of scope for `AOA-P-0017` until ordered-wave adjuncts are stable enough to justify managed composition surfaces

## Discipline

Use this matrix to decide whether the next honest move is:
- stay smaller
- author the route
- make the route runtime-readable through activation
- make the route cross-repo checkable through federation
- add composition only when bounded handoff, failure, subagent, or automation adjuncts truly recur

Do not use this matrix to force growth for its own sake.
