# SC ↔ ERC8004-Specialist Default Procedure (MANDATORY)

Status: ACTIVE DEFAULT
Owner: Science-Chief
Scope: Every task assigned by Manuel to SC and delegated to ERC8004-Specialist.

## End-to-end flow (mandatory)
1) **SC Dispatch**
   - SC writes task to Specialist inbox with objective, deliverables, acceptance criteria, SLA.
   - State: `DISPATCHED`

2) **Specialist CP0 ACK (<=10 min)**
   - Specialist must publish: `outbox/CP0_ACK_<TASK>_<timestamp>.md`
   - State: `ACKED`
   - Without CP0_ACK: task = `SLA_AT_RISK`

3) **Specialist Execution (fast-first)**
   - Batch atomici, output reali su filesystem.
   - State: `IN_PROGRESS`

4) **Specialist Delivery Pack**
   - Required:
     - script/code path(s)
     - tables path(s)
     - figures PDF path(s)
     - technical note path
   - State: `DELIVERED`

5) **Specialist CPF sentinel (mandatory)**
   - Publish: `outbox/CPF_DONE_<TASK>_<date>.md`
   - Archive inbox task to `inbox/archive/YYYY-MM-DD_done/`
   - State: `CPF_DONE`

6) **SC Review Trigger**
   - SC starts review immediately on CPF_DONE.
   - State: `SC_REVIEWING`

7) **SC Final Report Package (hard rule)**
   - SC must publish in outbox/Reports:
     - `<TASK>.tex`
     - `<TASK>.pdf`
     - `figures/`, `tables/`
   - State: `SC_PUBLISHED`

8) **SC Closure**
   - SC publishes closure note with final decision.
   - State: `CLOSED`

## Message format (mandatory)
`PATH | STATO | NEXT | ETA`

## Blocker format (mandatory)
`BLOCKER | cause | missing_input | ETA`

## Hard closure constraints
- No `CLOSED` without SC final review package in `.tex + .pdf`.
- If review PDF missing => `BLOCKED | MISSING_SC_REVIEW_PDF`.

## Archive constraints
- Specialist inbox task must be archived after CPF_DONE.
- SC inbox task must be archived after closure.
- Specialist outbox task artifacts may be archived after SC closure.

## Source-of-truth rule
Filesystem artifacts and canonical sentinel files are authoritative over chat text.
