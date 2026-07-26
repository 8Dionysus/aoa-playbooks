# Release Support Mechanic

## Mechanic card

| Field | Route |
| --- | --- |
| class | head-fed/local |
| role | keep release, deployment, installation, rollback, promotion, retention, and publication support explicit |
| trigger | release-check change, releasing-doc change, rollback/deployment/install contract change, or promotion/retention route change |
| playbooks owns | repo release-support posture and public operator docs |
| stronger owner split | GitHub/CI owns CI execution; runtime owners own deployment; support/business process owners own live support policy |
| inputs | `docs/RELEASING.md`, release docs, root release check, schemas/examples, source playbooks |
| outputs | checked package-local release-support posture |
| must not claim | CI authority, runtime deployment authority, package publication promise, or support desk ownership |
| validation | package executable owners; focused order in `AGENTS.md` |
| next route | root release doc, release check, source playbook, runtime owner, or GitHub/CI |

## Active route

This package is active as package-local release-support posture.

Release-support docs, schemas, and examples are package-local.
`docs/RELEASING.md` and `scripts/release_check.py` remain root operator
entrypoints; the package validates that split explicitly.

## Parts

| Part | Role | Source surfaces | Validation | Status |
| --- | --- | --- | --- | --- |
| `repo-release-gate` | keep repo release validation operator-facing | `docs/RELEASING.md`, `scripts/release_check.py` | package validator plus release check | root-entrypoint |
| `deployment-and-installation` | keep deployment/install records public | package-local deployment/install docs, schemas, and examples | package validator | package-local |
| `rollback-and-regression` | keep rollback, drill, veto, stay, and regression posture public | package-local rollback/regression docs, schemas, and examples | package validator | package-local |
| `promotion-and-retention` | keep promotion, first-release, and retention posture public | package-local promotion/retention docs, schemas, and examples | package validator | package-local |

Payloads moved into package-local parts. `docs/RELEASING.md` and
`scripts/release_check.py` remain operator entrypoints, not mechanic payload
homes. All parts route through the package validator.

## Provenance

Release-support is head-fed as publication posture and local as repo release
validation. Runtime deployment and CI execution stay with stronger owners.

Mechanic payload moved into package-local parts on 2026-05-31. The active
decision is package-local; the root release doc and command remain
accepted-input routes. Former root release-support doc, schema, and example
names are accepted-input legacy names, while active payload stays under
`mechanics/release-support/parts/`.

## Growth posture

Future release-support parts can move helper implementation payloads, but root
operator commands and release-law docs need compatibility wrappers or explicit
retention.
