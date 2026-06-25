# Playbook Artifact Bundles

This directory declares OS Abyss artifact bundle inputs for playbook-owned public
registry and generated readout surfaces.

The current bundle is `playbook_registry.bundle.json`.

It is intentionally scoped to playbook metadata and playbook-owned generated
composition/readout surfaces. It does not sign memo truth, proof verdicts,
routing authority, skill semantics, live runtime state, or private run evidence.

Consumer admission is fail-closed: a registry/latest reader must see a promoted
record with durable source metadata, a materialized subject store, and an
`allow`/`deny` trust-gate verdict before using the registry bundle.

Current controls:

- ABI signature: required for `generated/playbook_registry.min.json`
- SLSA/in-toto: required for the registry/readout bundle subject set
- SBOM: deferred until `aoa-playbooks` publishes a package or release bundle
- Sigstore/Cosign: deferred until signed release assets exist
- C2PA: deferred to public PDF/media/content exports
