# aoa-playbooks

`aoa-playbooks` is the scenario and composition layer of the AoA ecosystem.

It exists to make recurring operational recipes explicit, reviewable, and reusable. A playbook is not a skill. A skill is a bounded workflow. A playbook coordinates multiple surfaces, handoffs, fallbacks, and evidence expectations across a recurring scenario.

> Current release: `v0.3.1`. See [CHANGELOG](CHANGELOG.md) for release notes.

## Start here

Use the shortest route by need:

- docs map: [docs/README](docs/README.md)
- role, boundaries, and conceptual model: [CHARTER](CHARTER.md), [docs/PLAYBOOK_MODEL](docs/PLAYBOOK_MODEL.md), and [docs/BOUNDARIES](docs/BOUNDARIES.md)
- authored bundle and activation seam: [docs/PLAYBOOK_BUNDLE_CONTRACT](docs/PLAYBOOK_BUNDLE_CONTRACT.md), [docs/PLAYBOOK_EXECUTION_SEAM](docs/PLAYBOOK_EXECUTION_SEAM.md), [docs/PLAYBOOK_OPERATIONAL_FAMILY](docs/PLAYBOOK_OPERATIONAL_FAMILY.md), [docs/PLAYBOOK_RECURRENCE_DISCIPLINE](docs/PLAYBOOK_RECURRENCE_DISCIPLINE.md), [docs/PLAYBOOK_LIFECYCLE](docs/PLAYBOOK_LIFECYCLE.md), and [docs/PLAYBOOK_PORTFOLIO](docs/PLAYBOOK_PORTFOLIO.md)
- evidence, gates, and release posture: [docs/PLAYBOOK_REAL_RUN_WORKFLOW](docs/PLAYBOOK_REAL_RUN_WORKFLOW.md), [docs/PLAYBOOK_REAL_RUN_HARVEST](docs/PLAYBOOK_REAL_RUN_HARVEST.md), [docs/PLAYBOOK_COMPOSITION_GATES](docs/PLAYBOOK_COMPOSITION_GATES.md), [docs/PLAYBOOK_GAP_MATRIX](docs/PLAYBOOK_GAP_MATRIX.md), and [docs/RELEASING](docs/RELEASING.md)
- sovereign shared-root rollout route plus companion lane: [playbooks/trusted-rollout-operations/PLAYBOOK.md](playbooks/trusted-rollout-operations/PLAYBOOK.md), [docs/CODEX_PLANE_ROLLOUT_CYCLE](docs/CODEX_PLANE_ROLLOUT_CYCLE.md), [docs/TRUSTED_ROLLOUT_CAMPAIGN_CADENCE](docs/TRUSTED_ROLLOUT_CAMPAIGN_CADENCE.md), and [examples/codex_plane_rollout_lane.example.json](examples/codex_plane_rollout_lane.example.json)
- long-arc continuity and explicit reanchor route: [AOA-P-0029 self-agency-continuity-cycle](playbooks/self-agency-continuity-cycle/PLAYBOOK.md)
- additive stress-lane and re-entry doctrine: [docs/PLAYBOOK_STRESS_LANES](docs/PLAYBOOK_STRESS_LANES.md) and [docs/PLAYBOOK_STRESS_HARVEST](docs/PLAYBOOK_STRESS_HARVEST.md)
- adjunct outline seam: [docs/QUESTLINE_AND_CAMPAIGN_MODEL](docs/QUESTLINE_AND_CAMPAIGN_MODEL.md)
- live authored examples: [playbooks/self-agent-checkpoint-rollout/PLAYBOOK.md](playbooks/self-agent-checkpoint-rollout/PLAYBOOK.md), [playbooks/witness-to-compost-pilot/PLAYBOOK.md](playbooks/witness-to-compost-pilot/PLAYBOOK.md), [playbooks/session-growth-cycle/PLAYBOOK.md](playbooks/session-growth-cycle/PLAYBOOK.md), [playbooks/owner-followthrough-campaign/PLAYBOOK.md](playbooks/owner-followthrough-campaign/PLAYBOOK.md), [AOA-P-0027 reviewed-automation-followthrough](playbooks/reviewed-automation-followthrough/PLAYBOOK.md), [AOA-P-0028 trusted-rollout-operations](playbooks/trusted-rollout-operations/PLAYBOOK.md), and [AOA-P-0029 self-agency-continuity-cycle](playbooks/self-agency-continuity-cycle/PLAYBOOK.md) inside the wider `playbooks/*/PLAYBOOK.md` family
- current direction: [ROADMAP](ROADMAP.md)

## Route by need

- source-authored playbook truth: `playbooks/*/PLAYBOOK.md` for scenario routes and `generated/playbook_registry.min.json` for compact registry metadata
- activation, federation, and review-governed landing surfaces: `generated/playbook_activation_surfaces.min.json`, `generated/playbook_federation_surfaces.min.json`, `generated/playbook_review_status.min.json`, `generated/playbook_review_intake.min.json`, `generated/playbook_review_packet_contracts.min.json`, and `generated/playbook_landing_governance.min.json`
- shared-root rollout operations route and companion lane: `playbooks/trusted-rollout-operations/PLAYBOOK.md`, `docs/CODEX_PLANE_ROLLOUT_CYCLE.md`, `docs/TRUSTED_ROLLOUT_CAMPAIGN_CADENCE.md`, and `examples/codex_plane_rollout_lane.example.json`
- long-arc continuity and explicit reanchor route: `playbooks/self-agency-continuity-cycle/PLAYBOOK.md`
- handoff, failure, automation, and subagent adjuncts: `generated/playbook_handoff_contracts.json`, `generated/playbook_failure_catalog.json`, `generated/playbook_automation_seeds.json`, `generated/playbook_subagent_recipes.json`, [docs/HANDOFF_CONTRACTS](docs/HANDOFF_CONTRACTS.md), [docs/FAILURE_RECOVERY](docs/FAILURE_RECOVERY.md), [docs/AUTOMATION_SEEDS](docs/AUTOMATION_SEEDS.md), and [docs/SUBAGENT_PATTERNS](docs/SUBAGENT_PATTERNS.md)
- additive stress-lane adjuncts: `schemas/playbook_stress_lane_v1.json`, `schemas/playbook_reentry_gate_v1.json`, `examples/playbook_stress_lane.example.json`, `examples/playbook_reentry_gate.example.json`, [docs/PLAYBOOK_STRESS_LANES](docs/PLAYBOOK_STRESS_LANES.md), and [docs/PLAYBOOK_STRESS_HARVEST](docs/PLAYBOOK_STRESS_HARVEST.md)
- via negativa pruning checklist: [docs/VIA_NEGATIVA_CHECKLIST](docs/VIA_NEGATIVA_CHECKLIST.md)
- real-run and gate-review evidence: `docs/real-runs/`, `docs/gate-reviews/`, `examples/harvests/`, [docs/PLAYBOOK_REAL_RUN_WORKFLOW](docs/PLAYBOOK_REAL_RUN_WORKFLOW.md), and [docs/PLAYBOOK_COMPOSITION_GATES](docs/PLAYBOOK_COMPOSITION_GATES.md)
- owner-local live receipt publication for closeout/stats integration: `scripts/publish_live_receipts.py` and `.aoa/live_receipts/playbook-receipts.jsonl`
- live authored bundles and activation examples: `playbooks/*/PLAYBOOK.md` and `examples/playbook_activation.*.example.json`
- full non-mutating verify path: the eight `generate_* --check` builders, `python scripts/validate_playbooks.py`, and `python -m pytest -q tests`

## What `aoa-playbooks` owns

This repository is the source of truth for:

- recurring operational scenarios
- multi-step compositions across skills, roles, memory posture, and proof posture
- scenario-level handoff, fallback, rollback, and return posture
- expected evidence and validation posture for recurring routes
- compact playbook registries and derived playbook-owned composition surfaces

## What it does not own

Do not treat this repository as the main home for:

- reusable techniques
- single bounded skill bundles
- proof doctrine or verdict logic
- routing surfaces
- primary memory objects
- infrastructure implementation details
- giant prompt scripts pretending to be operations

When a route is really one bounded workflow, keep it in `aoa-skills` instead of inflating it into a playbook.

## Current public surfaces

The committed public surfaces group into four families:

- source-authored playbook canon: `playbooks/*/PLAYBOOK.md` for route meaning and `generated/playbook_registry.min.json` for compact registry metadata
- derived activation, federation, review-status, review-packet, review-intake, and landing-governance surfaces such as `generated/playbook_activation_surfaces.min.json`, `generated/playbook_federation_surfaces.min.json`, `generated/playbook_review_status.min.json`, `generated/playbook_review_packet_contracts.min.json`, `generated/playbook_review_intake.min.json`, and `generated/playbook_landing_governance.min.json`
- playbook-owned composition adjuncts such as `generated/playbook_handoff_contracts.json`, `generated/playbook_failure_catalog.json`, `generated/playbook_subagent_recipes.json`, `generated/playbook_automation_seeds.json`, and `generated/playbook_composition_manifest.json`
- bounded evidence and readiness adjuncts under `docs/real-runs/`, `docs/gate-reviews/`, `generated/phase_alpha_review_packets.min.json`, `generated/phase_alpha_run_matrix.min.json`, and `QUESTBOOK.md`

Real-run harvest templates under `examples/harvests/` and review notes under `docs/real-runs/` and `docs/gate-reviews/` stay bounded evidence surfaces. They do not turn this repository into a runtime log substrate.

## Go here when...

- you need a single bounded execution unit: [`aoa-skills`](https://github.com/8Dionysus/aoa-skills)
- you need role and handoff contracts: [`aoa-agents`](https://github.com/8Dionysus/aoa-agents)
- you need proof surfaces or evidence framing: [`aoa-evals`](https://github.com/8Dionysus/aoa-evals)
- you need explicit memory objects or recall posture: [`aoa-memo`](https://github.com/8Dionysus/aoa-memo)
- you need the smallest next object or dispatch hint: [`aoa-routing`](https://github.com/8Dionysus/aoa-routing)
- you need the ecosystem center and boundary doctrine: [`Agents-of-Abyss`](https://github.com/8Dionysus/Agents-of-Abyss)

## Build and validate

To validate the current playbook-layer surface locally, run:

```bash
python -m pip install -r requirements-dev.txt
python scripts/generate_playbook_activation_surfaces.py --check
python scripts/generate_playbook_federation_surfaces.py --check
python scripts/generate_playbook_review_status.py --check
python scripts/generate_playbook_review_packet_contracts.py --check
python scripts/generate_playbook_review_intake.py --check
python scripts/generate_playbook_landing_governance.py --check
python scripts/generate_playbook_composition_surfaces.py --check
python scripts/generate_phase_alpha_surfaces.py --check
python scripts/validate_playbooks.py
python -m pytest -q tests
```

The validator auto-discovers authored bundles under `playbooks/*/PLAYBOOK.md`, checks registry alignment, resolves federation-facing references into neighboring repositories, and validates the review-governed experimental landing layer, Phase Alpha, questbook, and local guidance surfaces including `playbooks/AGENTS.md` and `generated/AGENTS.md`.

## Current contour

`aoa-playbooks` is currently at `v0.3.1` and has moved beyond its initial public baseline. The current honest move is evidence-led maturation rather than bootstrap growth for its own sake.

The runtime-facing extension stays intentionally bounded: selected playbooks may publish explicit memo-read defaults and activation-readable surfaces, but memo truth, routing ownership, and source skill meaning remain in their owning repositories.

Questline and campaign reflection also remains adjunct-only. It is a reviewed outline seam, not a runtime ledger or quest authority surface.

## License

Apache-2.0
