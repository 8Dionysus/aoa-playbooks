# Playbook Execution Seam

This document defines the bounded execution seam for `aoa-playbooks`.

The goal is not to turn the playbook layer into runtime implementation.
The goal is to expose a small derived activation surface that a runtime can read without replacing the authored playbook bundle, while keeping a separate federation-readable surface for cross-repo closure checks.

## Core rule

`aoa-playbooks` owns executable scenario composition at the playbook layer.

It does not own:

- agent taxonomy
- skill execution
- eval doctrine
- memory taxonomy
- routing logic
- runtime or network implementation

Those neighboring layers stay authoritative for their own objects.

## Canonical source of truth

The canonical authored surfaces remain:

- `generated/playbook_registry.min.json`
- `playbooks/*/PLAYBOOK.md`

The activation surface is derived from those source-owned objects.
It exists to make recurring scenarios runtime-readable without adding a second authored playbook object.
The current compiled activation output lives at `generated/playbook_activation_surfaces.min.json` and is produced by `scripts/generate_playbook_activation_surfaces.py`.

The current compiled federation output lives at `generated/playbook_federation_surfaces.min.json` and is produced by `scripts/generate_playbook_federation_surfaces.py`.
It is a validator-facing closure surface, not a runtime execution interface.
The current compact reviewed-evidence output lives at `generated/playbook_review_status.min.json` and is produced by `scripts/generate_playbook_review_status.py`.
It is an evidence-posture surface for downstream readers, not a replacement for authored reviewed summaries or gate-review notes.
The current review-track landing gate lives at `generated/playbook_landing_governance.min.json` and is produced by `scripts/generate_playbook_landing_governance.py`.
It is a release-facing governance surface for the review-governed experimental layer only, not a verdict engine for the whole playbook corpus.
The current derived composition outputs live at `generated/playbook_handoff_contracts.json`, `generated/playbook_failure_catalog.json`, `generated/playbook_subagent_recipes.json`, `generated/playbook_automation_seeds.json`, and `generated/playbook_composition_manifest.json`, and are produced by `scripts/generate_playbook_composition_surfaces.py`.
They are scenario-owned projections for downstream readers, not persisted execution state.

## Activation surface

The derived activation surface should stay compact.
It should expose only the fields a runtime needs to understand:

- which playbook this is
- which scenario it names
- when it triggers
- which agents participate
- which skill families are expected
- which artifacts should exist
- which evaluation and memory posture apply
- which fallback mode governs the route
- which compact return hints govern an honest re-entry when the route loses axis

It should not expose:

- execution state
- tool bindings
- MCP or A2A transport
- prompt-tool-server details
- runtime-local memory
- hidden wiring or infrastructure assumptions

If protocol examples are mentioned elsewhere, treat them as examples only, not as playbook canon.

## Current activation scenarios

The current activation-eligible scenarios for this seam are:

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
- `AOA-P-0026 owner-followthrough-campaign`
- `AOA-P-0027 reviewed-automation-followthrough`
- `AOA-P-0025 session-growth-cycle`
- `AOA-P-0028 trusted-rollout-operations`
- `AOA-P-0029 self-agency-continuity-cycle`
- `AOA-P-0030 component-refresh-cycle`
- `AOA-P-0031 a2a-summon-return-checkpoint`
- `AOA-P-0032 runtime-chaos-recovery`

These runtime-readable playbooks already define:

- explicit triggers
- participating agents
- expected artifacts
- evaluation posture
- memory posture
- bounded fallback posture
- compact return posture where the route may need governed re-entry

The activation surface may project:
- `return_posture`
- `return_anchor_artifacts`
- `return_reentry_modes`
- `memo_recall_modes`
- `memo_scope_default`
- `memo_scope_ceiling`
- `memo_read_path`
- `memo_checkpoint_posture`
- `memo_source_route_policy`

These fields describe where the scenario may return, not how a runtime performs that return.
The memo fields describe bounded default recall posture only; they do not move memo search, ranking, or truth-judgment logic into the playbook layer.

The shared-root Codex-plane deployment continuity lane for `AOA-P-0028` keeps
one companion route card in `docs/CODEX_PLANE_ROLLOUT_CYCLE.md` plus
`examples/codex_plane_rollout_lane.example.json`.
That companion note is not a second activation surface, federation surface, or
persisted execution packet.
`AOA-P-0029 self-agency-continuity-cycle` is activation-readable because the
route needs compact return posture around reviewed anchors, revision windows,
and explicit reanchor, but it still does not become runtime autonomy or a
hidden retry runner.
`AOA-P-0030 component-refresh-cycle` is activation-readable because the route
needs compact return posture around reviewed drift hints, owner-law refresh
decisions, and rollback/safe-stop return, but it is not scheduler authority,
not a hidden runner, and not autonomous self-maintenance.
`AOA-P-0031 a2a-summon-return-checkpoint` is activation-readable because the
route needs compact return posture around summon request, SDK A2A decision,
Codex-local target, reviewed child result, checkpoint bridge, proof, memo
writeback, and runtime dry-run receipt, but it is not live child automation or
runtime execution authority.
`AOA-P-0032 runtime-chaos-recovery` is activation-readable because the route
needs compact return posture around runtime receipt, degraded lane, explicit
re-entry gate, source-first regrounding, and proof-facing handoff, but it is
not runtime repair authority, KAG health truth, or a verdict engine.

Their derived activation entries are validated against the generated collection and the matching fixture examples in `examples/`.

## Federation surface

The federation surface should stay compact.
It should expose only the fields needed to check cross-repo closure:

- which playbook this is
- which agents participate
- which exact skills must resolve in `aoa-skills`
- which eval anchors must resolve in `aoa-evals`
- which memo contracts must resolve in `aoa-memo`
- which memo writeback kinds the route allows
- which bounded memo-read default the runtime-facing cohort is allowed to assume

It should not expose:

- runtime execution state
- transport details
- hidden cross-repo wiring
- new memo or skill semantics invented inside `aoa-playbooks`

## Composition surfaces

The derived composition surfaces should stay compact.
They may expose only the fields needed to support playbook-owned composition:

- playbook-to-skill handoff bridges
- shared failure codes and their recommended follow-up skills
- explicit subagent split recipes
- example-only automation prompt seeds

They should not expose:

- persisted run state
- tool bindings
- execution packets
- router meaning
- observability protocols
- runtime recovery engines

## Current federation-checked cohort

The current federation-checked playbooks for this seam are:

- `AOA-P-0006 self-agent-checkpoint-rollout`
- `AOA-P-0007 witness-to-compost-pilot`
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
- `AOA-P-0026 owner-followthrough-campaign`
- `AOA-P-0025 session-growth-cycle`
- `AOA-P-0028 trusted-rollout-operations`
- `AOA-P-0029 self-agency-continuity-cycle`
- `AOA-P-0030 component-refresh-cycle`
- `AOA-P-0031 a2a-summon-return-checkpoint`
- `AOA-P-0032 runtime-chaos-recovery`

Their derived federation entries are validated against `aoa-skills/generated/governance_backlog.json` and the referenced `aoa-memo/examples/*.json` contracts.
For the runtime-facing memo cohort, they also carry flat memo recall defaults so downstream runtimes can derive `inspect`, `capsule`, and `expand` posture without inventing new playbook semantics.
`AOA-P-0006 self-agent-checkpoint-rollout` is intentionally federation-checked without joining the activation cohort because its route is still governed by approval and rollback checkpoints rather than a compact runtime-readable activation seam.
`AOA-P-0016 atm10-bounded-change` remains activation-readable and composition-managed, and is now federation-checked because its ATM10 overlay skills reconcile as `project_overlay_federation_ready` in `aoa-skills` while still remaining thin project overlays without a governance lane there.

## Boundary to preserve

The activation surface may help a runtime read playbooks.
It must not turn the playbook layer into:

- an agent registry
- a skill runner
- an eval engine
- a memory store
- a transport spec
- a persisted orchestration runtime

The playbook still owns the recurring scenario route.
The runtime only reads a bounded projection of that route.
