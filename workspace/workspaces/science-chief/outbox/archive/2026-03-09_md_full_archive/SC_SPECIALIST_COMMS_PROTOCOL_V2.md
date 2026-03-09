# SC_SPECIALIST_COMMS_PROTOCOL_V2

Status: CP1 STRUCTURE READY (to be finalized by 07:15)

## Objectives
- Zero ambiguity on task state
- Zero silent stalls
- Minimum messaging overhead
- Preserve `.tex + .pdf` reporting flow

## Canonical states (single state machine)
1. DISPATCHED
2. ACKED (CP0_ACK)
3. IN_PROGRESS (CP1)
4. DELIVERED (artifact pack complete)
5. CPF_DONE (sentinel published)
6. SC_REVIEWING
7. SC_PUBLISHED (.tex + .pdf sent)
8. CLOSED
9. BLOCKED

## Mandatory files/signals
- CP0: `outbox/CP0_ACK_<task>_<timestamp>.md`
- CPF: `outbox/CPF_DONE_<task>_<date>.md`
- Blocker: `BLOCKER | cause | missing_input | new_ETA`

## Single handoff contract
Specialist -> SC handoff is valid only when all are true:
1) required artifacts exist in declared paths
2) technical delivery note exists
3) CPF_DONE sentinel exists

## SLA (default)
- CP0 <= 10 min
- CP1 <= task-specific target
- CPF <= task-specific target

## Escalation ladder
- SLA_AT_RISK at first breach
- Redelivery order with forced ETA
- Escalate to Cassia if second breach

## Message format (mandatory)
`PATH | STATO | NEXT | ETA`

## Anti-redundancy rules
- No narrative pings
- Only milestone/blocker/completion messages
- Filesystem is source of truth

## Post-closure outbox hygiene (hard rule)
- After `CLOSED` with SC `.tex + .pdf` present, archive outbox `.md` operational files.
- Target path: `outbox/archive/YYYY-MM-DD_md_full_archive/`.
- Archive only (no deletion).

## Mandatory SC final review artifact (hard rule)
- Every task MUST end with an SC review package in `.tex + .pdf`.
- Minimal required review outputs:
  - `outbox/Reports/<TASK_NAME>/<TASK_NAME>.tex`
  - `outbox/Reports/<TASK_NAME>/<TASK_NAME>.pdf`
- `CLOSED` state is valid only if the SC review PDF exists and is readable.
- If PDF is missing, state must be `BLOCKED` (reason: `MISSING_SC_REVIEW_PDF`).
