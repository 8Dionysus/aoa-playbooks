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
- an exact partition between reviewed scenario-input artifacts and
  step-produced artifacts
- typed input, approval, and reviewed-boolean condition binding modes, but no
  concrete inputs, approvals, or condition values
- checkpoint, retry, and rollback policy contours
- one evidence requirement per expected artifact
- an owner-qualified eval catalog reference plus the exact frontmatter eval
  anchor, and memo input references already named by frontmatter
- terminal closeout reference requirements

The generator fails closed when frontmatter drifts, a dependency points
forward, an artifact role overlaps, a required input is never bound, an output
is absent or produced twice, an output-producing step lacks direct scenario
input provenance or an explicit dependency output, a guarded requirement
disagrees with its step, a requirement points outside the contour, or an
executable key appears at any depth.

## Consumer contract

A consumer such as `aoa-sdk` must:

1. select the admitted `playbook_registry_bundle` through the fail-closed
   registry/latest trust gate and materialized subject store;
2. pin the exact `aoa-playbooks` revision and contour/schema digests;
3. validate the public JSON against the declared ABI before compiling;
4. bind an eligible route decision and exact `ScenarioBinding`;
5. bind every declared scenario condition to an exact reviewed boolean and
   provenance reference;
6. resolve agent, capability, input, approval, eval, memo, and runtime
   provenance from their owning surfaces;
7. select the active contour by pruning false guarded steps and their guarded
   evidence, eval, and retention requirements;
8. remove dependency and checkpoint references to pruned steps while
   preserving the relative order and dependencies of retained steps;
9. produce a new consumer-owned immutable plan snapshot and `RunPlan`;
10. reject blocked routes, missing or extra condition bindings, provenance
    mismatch, unsupported effects, or owner drift instead of guessing.

The generated contour is not itself a runnable plan, execution packet, or
receipt. Its IDs and references remain abstract until the consumer performs
the owner-qualified binding.

`all_scenario_inputs` is reserved for a contour with no typed input artifact
partition. It means the compiler copies every exact generic
`ScenarioBinding.input_ref` into that plan step and rejects an empty binding
when the active contour requires it.

`selected_scenario_inputs` means the compiler selects exactly the
`input_artifact_kinds` named by the step from a typed
`artifact_kind -> ProvenanceRef` scenario-input binding. The SDK binding must
map every contour-level input artifact kind exactly once, reject missing,
duplicate, and extra kinds, and preserve each selected reference's owner
provenance. A generic tuple of references or positional matching is not a
substitute for this mapping.

An effectful step that needs the requested operation must bind inputs unless an
earlier guard-compatible step produces an explicit artifact carrying the
request; DAG order alone is not input provenance. The same rule applies to
read-only derivations. Merely depending on an input-inspection step with no
output does not carry the inspected input forward.

`input_artifact_kinds` names the reviewed artifacts already present in the
scenario binding. They are never `expected_output_kinds`. Evidence for one of
these artifacts uses `artifact_binding=scenario_input`; evidence for a step
result uses `artifact_binding=step_output`. The compiler must preserve the
input artifact's owner provenance and must not accept a newly emitted artifact
as a substitute.

Each `scenario_conditions` entry declares an owner-named
`reviewed_boolean`. `guard_condition_id=null` is unconditional; a named guard
activates its step or requirement only when the exact reviewed binding is
true. The compiler must not infer guard truth from artifact presence, prose,
defaults, or runtime behavior. A dependency on a false guarded step is pruned
with that step; a dependency between retained steps remains mandatory.
Guarded evidence cannot be terminally required, and an unconditional closeout
cannot require a guarded artifact.

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
