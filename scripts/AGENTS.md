# AGENTS.md
Local guidance for `scripts/` in `aoa-playbooks`.

Scripts here validate authored playbooks and build generated playbook-owned
surfaces. The inherited root card supplies repository-wide boundaries.

## Local role
Scripts should be deterministic, repo-relative, and explicit about canonical
inputs. Prefer generator check mode such as `generate_* --check` before writing.

## Editing posture
Keep builders tied to authored playbooks, config, docs, and examples. Avoid
hidden network calls, hidden runtime assumptions, and silent writes outside the
repository.

## Hard no
Do not let a generator invent playbook meaning that is absent from source
surfaces.

## Validation
Run the touched builder or validator, then use root
[`VALIDATION.md`](../VALIDATION.md) for repository-shape and artifact-bundle
routes. If the owner-local stats port moves, use
[`stats/VALIDATION.md`](../stats/VALIDATION.md).
