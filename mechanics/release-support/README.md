# Release Support Mechanic

## Mechanic card

| Field | Route |
| --- | --- |
| class | head-fed and local |
| role | keep release, deployment, installation, rollback, promotion, retention, and publication support explicit |
| trigger | release-check change, releasing-doc change, rollback/deployment/install contract change, or promotion/retention route change |
| playbooks owns | repo release-support posture and public operator docs |
| stronger owner split | GitHub/CI owns CI execution; runtime owners own deployment; support/business process owners own live support policy |
| inputs | `docs/RELEASING.md`, release docs, root release check, schemas/examples, source playbooks |
| outputs | checked package-local release-support posture |
| must not claim | CI authority, runtime deployment authority, package publication promise, or support desk ownership |
| validation | `python mechanics/release-support/scripts/validate_release_support_package.py` |
| next route | root release doc, release check, source playbook, runtime owner, or GitHub/CI |

## Active route

This package is active as package-local release-support posture.

Release-support docs, schemas, and examples are package-local.
`docs/RELEASING.md` and `scripts/release_check.py` remain root operator
entrypoints; the package validates that split explicitly.

## Source surfaces

- `docs/RELEASING.md`
- `scripts/release_check.py`
- release, deployment, installation, rollback, promotion, and retention docs
  under `mechanics/release-support/parts/*/docs/`
- release-support schemas/examples under `mechanics/release-support/parts/*/`

## Growth posture

Future release-support parts can move helper implementation payloads, but root
operator commands and release-law docs need compatibility wrappers or explicit
retention.
