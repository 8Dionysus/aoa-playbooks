# RPG Parts

## Active parts

| Part | Role | Source surfaces | Validation | Status |
| --- | --- | --- | --- | --- |
| `party-template-model` | keep party-template vocabulary bounded | `mechanics/rpg/parts/party-template-model/docs/party-template-model.md` | package validator | package-local |
| `build-synergy-posture` | keep build synergy as reflection only | `mechanics/rpg/parts/build-synergy-posture/docs/build-synergy-posture.md` | package validator | package-local |
| `party-template-readout` | keep public example readout bounded | `mechanics/rpg/parts/party-template-readout/schemas/party_template_catalog.schema.json`, `generated/party_template_cards.min.example.json` | package validator | package-local |

## Deferred payloads

Payloads moved into package-local parts in this package landing.

RPG docs and schema are package-local. The generated party-template example
remains a root generated readout.
