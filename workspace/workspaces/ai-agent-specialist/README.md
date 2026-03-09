# AI-Agent-Specialist Workspace

Workspace operativo del subbot business specializzato su AI Agents.

## Reporting line
- Riporta a: `Business-Chief`
- Collabora con: `ERC8004-Specialist` per allineamento ricerca↔sviluppo↔business

## Struttura
- `inbox/` task da Business-Chief/Cassia
- `working/` analisi e piani in corso
- `outbox/` deliverable pronti
- `logs/` log operativi

## Deliverable minimi
- `outbox/AI_AGENT_BUSINESS_PORTFOLIO.md`
- `outbox/AI_AGENT_GTM_PLAN_14D.md`
- `outbox/AI_AGENT_KPI_TRACKER.md`

## Protocollo operativo persistente
- A ogni nuovo file in `outbox/`: ping immediato a Cassia con `(path file, milestone tag, one-line summary)`.
- Ogni update tecnico/business deve seguire 5 blocchi: `(1) metodo/procedura (2) risultati chiave (3) limitazioni/problemi (4) livello di confidenza (5) prossime azioni`.
- Tutto lo stream ERC8004 deve essere allineato alla catena di supervisione SC.
- Fonte di verità permanente: `MEMORY.md`.
