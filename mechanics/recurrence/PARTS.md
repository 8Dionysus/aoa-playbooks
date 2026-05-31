# Recurrence Parts

## Active parts

| Part | Role | Source surfaces | Validation | Status |
| --- | --- | --- | --- | --- |
| `recurrence-discipline` | keep scenario return doctrine public and reviewable | `mechanics/recurrence/parts/recurrence-discipline/docs/playbook-recurrence-discipline.md` | package validator plus `validate_playbooks.py` | package-local |
| `observation-producers` | name what may produce recurrence observations without scheduler authority | `mechanics/recurrence/parts/observation-producers/docs/recurrence-live-observation-producers.md` | package validator | package-local |
| `review-decision-closure` | bind recurrence closure to review decisions | `mechanics/recurrence/parts/review-decision-closure/docs/recurrence-review-decision-closure.md` | package validator | package-local |
| `source-playbook-routes` | keep recurrence-bearing playbook canon authored | `playbooks/self-agency-continuity-cycle/`, `playbooks/component-refresh-cycle/` | `validate_playbooks.py` | source-playbook |
| `recurrence-manifests` | keep recurrence read models with their consuming mechanics | `mechanics/agon/parts/*/manifests/`, `mechanics/scenario-composition/parts/*/manifests/` | package validator | package-local |

## Deferred payloads

Payloads moved into package-local parts in this package landing.

Recurrence docs and manifests are active package-local routes. Former root
names are accepted-input legacy names.
