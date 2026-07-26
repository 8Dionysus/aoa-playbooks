# Playbook Plan-Contour Contract

## Purpose

`aoa_playbook_plan_contour_v1` is the playbook-owned seam between authored
scenario meaning and a downstream control-plane compiler. It expresses what
the scenario requires without expressing how a runtime performs it.

The canonical input is
`mechanics/scenario-composition/parts/plan-contours/config/playbook_plan_contours.json`.
The public derived output is `generated/playbook_plan_contours.min.json`, and
its closed schema is
`mechanics/scenario-composition/parts/plan-contours/schemas/playbook-plan-contours.schema.json`.

## Contour meaning

Each contour binds one exact `PLAYBOOK.md` source and repeats these frontmatter
fields exactly:

- playbook ID, name, and scenario
- participating agent IDs
- required capability IDs
- expected artifact kinds

It then adds the smallest scenario-owned planning structure:

- a topologically ordered DAG of abstract operation and effect classes
- input and approval binding modes, but no concrete inputs or approvals
- checkpoint, retry, and rollback policy contours
- one evidence requirement per expected artifact
- an owner-qualified eval catalog reference plus the exact frontmatter eval
  anchor, and memo input references already named by frontmatter
- terminal closeout reference requirements

The generator fails closed when frontmatter drifts, a dependency points
forward, an artifact is absent or produced twice, a requirement points outside
the contour, or an executable key appears at any depth.

## Consumer contract

A consumer such as `aoa-sdk` must:

1. select the admitted `playbook_registry_bundle` through the fail-closed
   registry/latest trust gate and materialized subject store;
2. pin the exact `aoa-playbooks` revision and contour/schema digests;
3. validate the public JSON against the declared ABI before compiling;
4. bind an eligible route decision and exact `ScenarioBinding`;
5. resolve agent, capability, input, approval, eval, memo, and runtime
   provenance from their owning surfaces;
6. produce a new consumer-owned immutable plan snapshot and `RunPlan`;
7. reject blocked routes, provenance mismatch, unsupported effects, or owner
   drift instead of guessing.

The generated contour is not itself a runnable plan, execution packet, or
receipt. Its IDs and references remain abstract until the consumer performs
the owner-qualified binding.

`docs/artifact-bundles/playbook_registry.bundle.json` admits both
`generated/playbook_plan_contours.min.json` and the contour schema as trusted
subjects. Reading the working-tree files directly is not evidence that the
registry/latest admission and subject-store materialization succeeded.

For eval requirements, `artifact_ref` names the generated `aoa-evals` catalog
and `eval_anchor` selects the catalog entry by its exact `name`. The contour
does not invent a JSON fragment or replace the entry's owner-authored
`eval_path`.

## Prohibited transfer

Neither source config nor generated output may contain:

- commands, shell or scripts
- prompts
- tool names or tool arguments
- MCP, network, or transport bindings
- model selection
- scheduler or retry implementation
- mutable run state
- proof verdicts or memory truth

Playbook prose must not be parsed at runtime to recover missing contour
meaning, and downstream consumers must not hardcode substitute scenario
meaning when the ABI is absent or stale.

## Ownership after compilation

The boundary is intentionally layered:

- `aoa-playbooks` owns recurring scenario meaning and this abstract contour;
- `aoa-sdk` owns deterministic compilation and control-plane contracts;
- routing surfaces own route eligibility and approval requirements;
- agent and capability owners supply identities and provenance;
- `aoa-evals` owns verdict meaning;
- `aoa-memo` owns retention and recall meaning;
- runtime owners execute bounded effects and emit receipts.

Green contour validation proves source alignment and ABI shape only. It does
not prove that a downstream compiler invoked the route, that a runtime
executed it, or that the route reduced operational cost.
