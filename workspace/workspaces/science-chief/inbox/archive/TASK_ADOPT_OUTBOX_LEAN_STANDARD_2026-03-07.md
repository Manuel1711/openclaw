# Specialist Outbox Lean Standard (2026-03-07)

Approved by Manuel for cross-bot adoption.

## Objective
Keep outbox decision-ready, non-redundant, and easy to navigate.

## Rules
1. Outbox root contains only ACTIVE bundle (decision-relevant docs + current figure pack).
2. Historical/process/preliminary docs must be archived under `archive/outbox/<stamp>/`.
3. Maintain `outbox/INDEX.md` with read order and status (ACTIVE vs ARCHIVED).
4. Maintain `outbox/ACTIVE.list` as source of truth for what remains in outbox root.
5. Preserve durable highlights in memory file (`MEMORY_OUTBOX_HIGHLIGHTS.md` or equivalent).
6. Final figures are PDF-only in active figure pack.
7. No duplicates/redundant run copies in active outbox.

## Suggested cadence
- Run cleanup at end of each major publication cycle (or daily).

## Minimal active layout
- `outbox/INDEX.md`
- `outbox/ACTIVE.list`
- Current main report(s)
- Current figure book / interpretive note (if applicable)
- Current `outbox/figures/<run_id>/`
