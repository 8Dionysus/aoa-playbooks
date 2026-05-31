# Experience Parts

## Active parts

| Part | Role | Source surfaces | Validation | Status |
| --- | --- | --- | --- | --- |
| `adoption-and-retention` | keep adoption, retention, rollback, pattern, shadow, and shared-pattern contract pairs public | `mechanics/experience/parts/adoption-and-retention/{docs,schemas,examples}/` | package validator plus Experience tests | package-local |
| `certification-and-governance` | keep certification, governance, dossier, and owner quest routes public | `mechanics/experience/parts/certification-and-governance/{docs,schemas,examples}/` | package validator plus Experience tests | package-local |
| `service-and-office` | keep office, service mesh, watchtower, canary, and operator console routes public | `mechanics/experience/parts/service-and-office/{docs,schemas,examples}/` | package validator | package-local |
| `agonic-adoption-handoff` | keep Agonic trial adoption with the Agon mechanic | `mechanics/agon/parts/adoption/` | Agon and Experience validators | transferred-to-agon |

## Deferred payloads

Payloads moved into package-local parts in this package landing.

Experience contract pairs are active public package-local routes. The Agonic
adoption pair is intentionally package-local under `mechanics/agon/`.
