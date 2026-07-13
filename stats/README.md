# aoa-playbooks local stats port

This directory exposes statistical questions whose domain meaning belongs to
`aoa-playbooks`. It uses the shared `aoa-stats` measurement grammar without
moving playbook review meaning or runtime truth into the central organ.

## Current reference measurement

| Measurement | Question | Reference value |
| --- | --- | --- |
| `aoa-playbooks/reviewed-run-reference-coverage-ratio` | What fraction of the current gate-reviewed playbook cohort has at least one referenced reviewed run? | `6 / 8` at source revision `1bfad256e2c7996d4cf81f63e641b01574919d6b` |

The reference packet is a census of the entries in
`generated/playbook_review_status.min.json`. That cohort is defined by the
current gate-review notes; it is not the complete authored playbook catalog.
An entry is counted in the numerator only when its `reviewed_run_count` is
greater than zero.

## Authority

The ratio reports the presence of referenced reviewed runs in the current
review-status cohort only. It does not establish run quality, proof, an eval
verdict, readiness, gate acceptance, execution success, runtime state, or a
scenario decision. `aoa-stats` may validate and compose the packet without
redefining playbook review meaning.

## Surfaces

- `port.manifest.json` declares the local question, measurement contract, and
  export.
- `packets/reviewed-run-reference-coverage-ratio.reference.json` records the
  evidence-linked reference observation.
- `generated/playbook_review_status.min.json` is the immediate owner read
  model.
- `mechanics/review-gate/parts/review-status/` owns its derivation and schema.
