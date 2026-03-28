# Playbook Recurrence Discipline

This document defines the playbook-layer landing of the AoA `Recurrence Principle`.

It does not create a new layer.
It does not replace `PLAYBOOK_MODEL`, `PLAYBOOK_BUNDLE_CONTRACT`, or `PLAYBOOK_EXECUTION_SEAM`.
It names how the playbook layer should carry the federation law when a recurring scenario route loses continuity honestly enough that it must step back to a valid anchor.

## Core rule

At the playbook layer, `recurrence` is the standing law.
`return` is the concrete recovery move inside that law.

When a scenario route loses its axis, ownership boundary, expected artifact contract, or reviewable restart posture, the playbook should require a governed return to the last valid scenario anchor.

Return is not retry.
Return is not vague continuity.
Return is not permission to load more raw context and hope the route becomes honest again.

Return means:
- detect scenario drift or boundary loss
- return to a named anchor
- re-enter through an explicit scenario-approved mode
- stop honestly if return no longer preserves the route

## What the playbook layer owns

At the playbook layer, recurrence should stay scenario-owned.

`aoa-playbooks` may own:
- return-trigger language for scenario-shaped drift
- anchor language for the artifacts or checkpoints a route may return to
- re-entry language for how a route may re-enter after return
- fallback relation between return and existing fallback modes
- evidence expectations for why a return happened and what changed after it

A playbook may say:
- which conditions count as loss of route shape
- which artifacts count as valid anchors
- whether return goes to a previous phase, router-style re-entry, checkpoint relaunch, review gate, rollback gate, or safe stop
- when repeated failed return should stop the route rather than simulate continuity

## What the playbook layer does not own

Recurrence discipline in `aoa-playbooks` must not absorb neighboring ownership.

`aoa-playbooks` does not own:
- `transition_decision` artifact schema
- role-to-tier runtime binding
- routing implementation
- memory-object canon
- context rebuild policy
- vendor or transport behavior
- stack-level wrapper logic

Those stay elsewhere:
- `aoa-agents` owns runtime-facing artifact contracts and tier bindings
- `aoa-routing` owns navigation and dispatch posture
- `aoa-memo` owns memory-object meaning and writeback doctrine
- `abyss-stack` owns runtime body, context budgeting, and wrapper implementation

## Recurrence versus fallback

Return and fallback are related, but they are not the same thing.

- `Return` is a governed move back to a valid anchor.
- `Handoff` is a transfer to another role, tier, or route owner.
- `Rollback` reverses or abandons a change path after mutation risk or failure.
- `Review required` stops autonomous continuation until review clears the next move.
- `Safe stop` ends the route honestly rather than pretending continuity.

A scenario may use return before fallback.
A scenario may also use fallback because return failed, because anchors are missing, or because the route boundary itself no longer holds.

## Valid anchor classes at the playbook layer

A playbook may name return anchors through compact scenario-facing classes.

### Artifact anchors

Return to the last valid route artifact for the scenario, such as:
- `route_decision`
- `bounded_plan`
- `verification_result`
- `boundary_map`
- `rollout_decision`

### Checkpoint anchors

Return to a restartable checkpoint pack, such as:
- `inquiry_checkpoint`
- `decision_ledger`
- `contradiction_map`
- `next_pass_brief`

### Review anchors

Return to the last explicit approval, review, or gating boundary before new motion.

A playbook may reference source-owned surfaces in prose, but should not redefine neighboring-layer contracts to do so.

## Re-entry modes

A playbook may name compact re-entry modes such as:
- `same_phase`
- `previous_phase`
- `router_reentry`
- `checkpoint_relaunch`
- `review_gate`
- `rollback_gate`
- `safe_stop`

These are scenario-readable route modes, not runtime implementation details.

## Minimal authored discipline

When a playbook relies on return, the authored bundle should make four things legible inside existing sections:

1. what kind of drift or loss triggers return
2. which artifacts count as valid anchors
3. which re-entry modes are allowed
4. when repeated failed return yields to fallback or stop

This does not require a new mandatory bundle section.
At the current layer, it is cleaner to keep return explicit inside:
- `Decision points`
- `Handoffs`
- `Fallback and rollback posture`
- `Expected evidence posture`
- `Canonical route`

That keeps authored bundles compact and avoids turning return into a second workflow grammar.

## Activation projection rule

For activation-eligible playbooks, the derived activation surface may project a compact return hint when that hint is already canonical in the playbook layer.

The compact activation projection may include:
- `return_posture`
- `return_anchor_artifacts`
- `return_reentry_modes`

These fields should remain:
- compact
- scenario-facing
- derived from canonical playbook inputs
- free of runtime-local wiring

They must not become a second authored route.

## Current return-capable cohort

The current playbooks that clearly justify recurrence discipline are:
- `AOA-P-0008 long-horizon-model-tier-orchestra`
- `AOA-P-0009 restartable-inquiry-loop`
- `AOA-P-0010 cross-repo-boundary-rollout`
- `AOA-P-0011 bounded-change-safe`
- `AOA-P-0012 infra-change-guarded`
- `AOA-P-0013 invariants-first-refactor`
- `AOA-P-0014 local-stack-diagnosis`
- `AOA-P-0015 source-truth-then-share`
- `AOA-P-0016 atm10-bounded-change`
- `AOA-P-0017 split-wave-cross-repo-rollout`
- `AOA-P-0018 validation-driven-remediation`
- `AOA-P-0019 release-migration-cutover`
- `AOA-P-0020 incident-recovery-routing`

A secondary, non-activation example is:
- `AOA-P-0006 self-agent-checkpoint-rollout`

## Anti-patterns

Avoid these failures:
- treating return as a synonym for `try again`
- using return to hide that the route no longer has a valid trigger
- moving runtime artifact-schema meaning into playbook docs
- adding giant new sections instead of tightening existing scenario sections
- inventing stack-level context rebuild semantics in `aoa-playbooks`
- using return as an excuse to ignore ownership drift
- using checkpoint language to fake continuity without portable artifacts

## Compact rule

A playbook should say where a route returns, not become the runtime that performs the return.

The playbook layer carries the scenario law of recurrence.
The runtime may later read a compact projection of that law.
