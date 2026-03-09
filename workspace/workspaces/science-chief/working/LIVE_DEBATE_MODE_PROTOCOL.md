# LIVE_DEBATE_MODE_PROTOCOL (SC ↔ Specialist)

Status: ACTIVE (requested by Manuel, 2026-03-07)

## Objective
Enable real-time technical dialogue between Science-Chief and ERC8004-Specialist for complex interpretive tasks.

## Flow
1. SC posts debate prompt (technical question set).
2. Specialist replies with point-by-point technical position.
3. SC sends counter-questions/challenges.
4. Specialist responds with evidence + caveats.
5. SC issues final synthesis (Metodo/Risultati/Problemi/Confidenza/Next Actions).

## Logging
- Save transcript snapshot in `workspaces/science-chief/logs/`.
- Save final technical outputs in Specialist outbox + SC outbox.

## Current topic
- `tag1` interpretation and NA semantics (`raw_missing`, `parse_error`, `unmapped`).
