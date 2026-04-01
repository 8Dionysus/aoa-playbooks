# Spark Swarm Recipe — aoa-playbooks

Рекомендуемый путь назначения: `Spark/SWARM.md`

## Для чего этот рой
Используй Spark здесь для одного scenario seam: recurring operational recipe, multi-step composition, fallback path, validation posture или playbook registry entry. Этот рой должен собирать сценарий, а не превращать playbook в skill archive.

## Читать перед стартом
- `README.md`
- `CHARTER.md`
- `docs/PLAYBOOK_MODEL.md`
- `docs/BOUNDARIES.md`
- `ROADMAP.md`

## Форма роя
- **Coordinator**: выбирает один scenario-shaped seam
- **Scout**: картографирует involved skills/agents/evals/memo surfaces
- **Builder**: делает минимальный playbook-level diff
- **Verifier**: запускает `python scripts/validate_playbooks.py`
- **Boundary Keeper**: держит грань между playbook и соседними слоями

## Параллельные дорожки
- Lane A: scenario recipe text or structure
- Lane B: fallback / rollback / evidence posture
- Lane C: registry update and validation
- Не запускай больше одного пишущего агента на одну и ту же семью файлов.

## Allowed
- оформить или починить один recurring operational scenario
- прояснить decision points and fallback paths
- сделать evidence/validation posture explicit
- обновить compact playbook registry entry

## Forbidden
- превращать playbook в single skill bundle
- всасывать сюда proof, memory или routing meaning as primary truth
- плодить giant script archives pretending to be operations
- оставлять fallback/rollback implied instead of named

## Launch packet для координатора
```text
We are working in aoa-playbooks with a one-repo one-swarm setup.
Pick exactly one scenario seam.
Return:
1. the scenario
2. skills/agents/evals/memo surfaces involved
3. exact files to touch
4. fallback and validation posture to clarify

The swarm must keep this as scenario composition, not a skill bundle.
```

## Промпт для Scout
```text
Map only. Do not edit.
Return:
- exact files involved
- neighboring layer surfaces referenced
- fallback and rollback gaps
- whether this really belongs in playbooks or should stay a skill/eval/agent document
```

## Промпт для Builder
```text
Make the smallest reviewable change.
Rules:
- keep the playbook as scenario composition
- make fallback and rollback explicit
- make evaluation posture visible
- do not absorb neighboring layer meaning
```

## Промпт для Verifier
```text
Run:
- python -m pip install -r requirements-dev.txt
- python scripts/validate_playbooks.py
Then report:
- commands run
- registry changes if any
- any unresolved scenario ambiguity
```

## Промпт для Boundary Keeper
```text
Review only for anti-scope.
Check:
- playbook is not a skill
- no neighbor layer swallowed
- fallback and rollback posture named
- evaluation posture visible
- no giant script archive behavior
```

## Verify
```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_playbooks.py
```

## Done when
- один scenario seam стал explicit and reviewable
- fallback/rollback/evidence posture названы
- validator реально прогнан
- playbook остался higher-level scenario recipe

## Handoff
Если сценарий распадается на один bounded workflow, follow-up почти всегда нужно в `aoa-skills`.
