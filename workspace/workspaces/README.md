# Bot Workspaces

Questa cartella contiene i workspace operativi separati per i lead bot e i sottobot specialistici.

## Struttura standard per ogni bot
- `inbox/` -> task ricevuti da Cassia
- `working/` -> lavoro in corso
- `outbox/` -> deliverable finali pronti per review
- `logs/` -> log operativi del bot

## Workspace attivi
- `science-chief/` (lead R&D)
- `business-chief/` (lead Business)
- `erc8004-specialist/` (sottobot scientifico; riporta a Science-Chief)
- `ai-agent-specialist/` (sottobot business; riporta a Business-Chief)

## Regola di simmetria L3 (vincolante)
- `ERC8004-Specialist` è sotto `Science-Chief`.
- `AI-Agent-Specialist` è sotto `Business-Chief`.
- Nessun cambio reporting L3 senza decisione esplicita di Manuel.

## Archivio
- `archive/` contiene workspace non più attivi (es. vecchia separazione `rd-scientist` / `rd-builder` e `biz-product` / `biz-growth`).

## SOP minime di coordinamento
- Orchestrazioni thread-bound multi-ruolo: seguire `company/control/THREAD_ORCHESTRATION_PLAYBOOK.md`.
- `ai-agent-specialist` lavora in loop con `erc8004-specialist` per allineare business↔sviluppo.
- Per `erc8004-specialist`: nessuna modifica Overleaf senza permesso esplicito di Manuel.

## Regola operativa
Ogni bot lavora nel proprio workspace e pubblica output in `outbox/`.
Cassia raccoglie e consolida nel workspace centrale (`company/control`).
