# AGENTS.md
Local guidance for `scripts/` in `aoa-playbooks`.

Read the root `AGENTS.md` first. Scripts here validate authored playbooks and
build generated playbook-owned surfaces.

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
Run the touched builder or validator, then `python scripts/release_check.py`
when repository shape changes. If the owner-local stats port moves, run
`python scripts/validate_local_stats_port.py`. If playbook registry, generated
readout, or artifact-bundle identity changes, also run
`python scripts/validate_abyss_machine_playbook_bundle.py`.
