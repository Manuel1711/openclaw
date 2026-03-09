# INBOX / OUTBOX Housekeeping (vincolante)

## Inbox
- `inbox/` contiene solo task attivi/non eseguiti.
- Task completati vanno spostati in `inbox/archive/YYYY-MM-DD_done/`.

## Outbox
- `outbox/` contiene solo deliverable attivi recenti.
- Deliverable storici vanno spostati in `outbox/archive/YYYY-MM-DD_internal/`.
- `outbox/ACTIVE.list` deve elencare solo file correnti.
- `outbox/INDEX.md` deve riflettere stato lean + pointer archivio.

## Regola pratica
- Al termine di ogni milestone: aggiorna ACTIVE.list, INDEX.md, pulisci inbox task completati.
