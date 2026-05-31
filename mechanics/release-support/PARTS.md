# Release Support Parts

## Active parts

| Part | Role | Source surfaces | Validation | Status |
| --- | --- | --- | --- | --- |
| `repo-release-gate` | keep repo release validation operator-facing | `docs/RELEASING.md`, `scripts/release_check.py` | package validator plus release check | root-entrypoint |
| `deployment-and-installation` | keep deployment/install records public | `mechanics/release-support/parts/deployment-and-installation/docs/deployment-runbook.md`, `mechanics/release-support/parts/deployment-and-installation/docs/installation-runbook.md`, matching schemas/examples | package validator | package-local |
| `rollback-and-regression` | keep rollback, safe rollback, drill, veto, stay, and regression posture public | rollback/regression docs and schemas/examples | package validator | package-local |
| `promotion-and-retention` | keep release candidate, ring promotion, first release, and post-release retention public | promotion/retention docs and schemas/examples | package validator | package-local |

## Deferred payloads

Payloads moved into package-local parts in this package landing.

Release-support docs, schemas, and examples are package-local. The root release
doc and release command are operator entrypoints, not mechanic payload homes.
