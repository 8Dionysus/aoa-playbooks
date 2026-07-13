# AGENTS.md

## Applies to

Everything under `stats/` in `aoa-playbooks`.

## Role

This directory owns playbook-local statistical questions, their embedded
measurement contracts, and evidence-linked reference packets. Shared
statistical grammar and cross-owner composition remain owned by `aoa-stats`.

## Read before editing

1. Root `AGENTS.md`, `README.md`, and `DESIGN.md`.
2. `stats/README.md` and `stats/port.manifest.json`.
3. `generated/playbook_review_status.min.json` and its owner builder and schema
   under `mechanics/review-gate/parts/review-status/`.
4. The central measurement and packet contracts under `aoa-stats/stats/`.

## Boundaries

- `port.manifest.json` owns the playbook-local question and measurement
  meaning.
- Reference packets are derived snapshots and remain weaker than the
  review-status source chain.
- Reviewed-run reference coverage reports whether a current gate-reviewed
  playbook entry references at least one reviewed run. It does not report run
  quality, proof, an eval verdict, readiness, gate acceptance, execution
  success, runtime state, or a scenario decision.
- Keep packet refs repository-relative and raw reviewed-run content out of
  packets.

## Validation

Inspect the owner read model first:

```bash
python -c 'import json, pathlib; p=json.loads(pathlib.Path("generated/playbook_review_status.min.json").read_text()); rows=p["playbooks"]; covered=sum(row["reviewed_run_count"] > 0 for row in rows); print({"population": len(rows), "covered": covered, "ratio": covered / len(rows)})'
```

Then validate the port and its packet with the central contract owner:

```bash
python scripts/validate_local_stats_port.py
```

## Closeout

Report the question or contract changed, the owner evidence inspected, whether
the reference packet was refreshed, and which validation route ran.
