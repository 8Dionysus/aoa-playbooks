# Review Gate Distillation Log

## 2026-05-31 - Builder implementations moved

- Moved review-status, review-packet-contracts, review-intake,
  landing-governance, and Phase Alpha readiness builder implementations from
  root `scripts/` into `mechanics/review-gate/parts/*/scripts/`.
- Left root command paths as compatibility wrappers.
- Left evidence directories, source config, schemas, examples, and generated
  outputs at root-public paths.
