# SC ↔ ERC8004-Specialist Default Procedure (MANDATORY)

Status: ACTIVE DEFAULT
Owner: ERC8004-Specialist (execution) + Science-Chief (review/closure)
Scope: Every task delegated by SC.

## Required state sequence
`DISPATCHED -> ACKED -> IN_PROGRESS -> DELIVERED -> CPF_DONE -> SC_REVIEWING -> SC_PUBLISHED -> CLOSED`

## What Specialist must do every time
1. Receive task in inbox.
2. Publish `CP0_ACK` within 10 minutes.
3. Execute and produce real artifacts (code/tables/figures).
4. Publish delivery technical note with exact paths.
5. Publish `CPF_DONE` sentinel.
6. Archive inbox task in `inbox/archive/YYYY-MM-DD_done/`.

## Handoff to SC is valid only if
- artifacts exist at declared paths,
- technical note exists,
- CPF_DONE exists.

## Messaging format (mandatory)
`PATH | STATO | NEXT | ETA`

## Blocker format
`BLOCKER | cause | missing_input | ETA`

## Closure rule
Task is not closed by Specialist. Final closure is SC responsibility after SC `.tex + .pdf` review package is published.
