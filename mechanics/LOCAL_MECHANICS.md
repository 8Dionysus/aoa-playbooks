# Local Mechanics Roster

This roster names playbook-native mechanics that start inside `aoa-playbooks`.

They are local because their recurring operation is born from scenario
composition, generated playbook readers, review gates, or playbook portfolio
discipline rather than from center mechanic law.

This is a skeleton. It does not move payloads or claim child packages are
operational yet.

## Operating Card

| Field | Route |
| --- | --- |
| role | roster for playbook-native mechanics |
| input | recurring scenario-operation pressure inside `aoa-playbooks` |
| output | package candidate, source route, validator route, generated builder route, or stronger-owner handoff |
| owner | `aoa-playbooks` for playbook-local operation routes; source surfaces stay authoritative |
| next route | target playbook source, `generated/`, `config/`, review/gate docs, decision record, or sibling owner |
| validation | `python scripts/validate_mechanics_skeleton.py` |

## Acceptance Rule

A local mechanic can become a child package only when it has:

- repeatable playbook-layer operation pressure;
- a source surface, generated builder, config, schema, review surface, or
  playbook family this repo owns;
- clear inputs and outputs;
- stronger-owner stop-lines;
- local validation.

Until then, it remains a roster row.

## Candidate Roster

| Candidate | Local pressure | Source route | Current status |
| --- | --- | --- | --- |
| `activation` | make authored scenarios runtime-readable without making runtime state | `mechanics/activation/parts/activation-surface/docs/playbook-execution-seam.md`, `generated/playbook_activation_surfaces.min.json`, activation builder | package-active |
| `federation-closure` | keep cross-repo refs resolvable without owning sibling truth | `generated/playbook_federation_surfaces.min.json`, federation builder, `docs/BOUNDARIES.md` | package-active |
| `review-gate` | keep real-run evidence, gate review, review packets, landing governance, and Phase Alpha readiness readouts bounded | review-status, review-packet, review-intake, landing-governance, and Phase Alpha builders | package-active |
| `scenario-composition` | keep handoffs, failures, subagent recipes, automation seeds, and composition manifests source-linked | `mechanics/scenario-composition/parts/composition-surfaces/config/playbook_composition_overrides.json`, composition builder, `generated/playbook_*` composition surfaces | package-active |
| `portfolio-governance` | keep lifecycle, gap matrix, chooser tables, and operational families from overgrowing | `mechanics/portfolio-governance/parts/lifecycle-and-portfolio/docs/playbook-lifecycle.md`, `mechanics/portfolio-governance/parts/lifecycle-and-portfolio/docs/playbook-portfolio.md`, `mechanics/portfolio-governance/parts/operational-family/docs/playbook-operational-family.md` | package-active |
| `real-run-harvest` | turn run evidence into reviewable playbook-layer posture without becoming proof or memory truth | `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/playbook-real-run-workflow.md`, `mechanics/real-run-harvest/parts/harvest-template-source-store/docs/playbook-real-run-harvest.md`, `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/real-runs/`, `mechanics/real-run-harvest/parts/reviewed-run-source-store/docs/gate-reviews/`, `mechanics/real-run-harvest/parts/harvest-template-source-store/examples/harvests/` | package-active |
| `mechanics-skeleton` | keep the mechanics atlas itself checked before payload movement | `mechanics/README.md`, `HEAD_MECHANICS.md`, `LOCAL_MECHANICS.md`, `scripts/validate_mechanics_skeleton.py` | skeleton-active |

## Stop Lines

- Local mechanics do not become center mechanics by existing here.
- A local mechanic does not replace source playbooks, generated builders,
  review notes, schemas, or config.
- Local mechanics must not absorb skill execution, proof verdicts, memory
  truth, role authority, routing policy, stats truth, KAG substrate, runtime
  behavior, or center doctrine.
- Do not move flat docs into package homes until a package-specific owner
  split and validator exist.

## Next Route

Continue package creation from the clearest remaining owner split.
`activation`, `scenario-composition`, `federation-closure`, `review-gate`,
and `real-run-harvest` are already package-active. The next local package
candidate should come from a row whose owner split and validator can be proven
without moving authored playbook canon.
