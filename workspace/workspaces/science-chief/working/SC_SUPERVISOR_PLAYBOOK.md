# SC_SUPERVISOR_PLAYBOOK

## Scopo
Rendere Science-Chief un supervisore sempre più forte, capace di generalizzare apprendimenti oltre il singolo task/specialista.

## Protocollo di supervisione (standard)
1. **Task framing (SC authority)**
   - Obiettivo
   - Vincoli
   - Deliverable
   - Criterio di accettazione
   - SLA esplicito
2. **Delegation execution-only (Specialist)**
   - Task scritto in `inbox/` dello specialista
   - Specialist produce solo artifact tecnici: codice/figure/tabelle/log
   - Checkpoint e timeline espliciti
3. **Quality review (SC)**
   - Metodo valido?
   - Risultati robusti?
   - Limiti dichiarati?
   - Confidenza coerente?
   - Overclaim inferenziali presenti?
4. **Decision gate (SC only)**
   - GO / HOLD / KILL
5. **Learning extraction**
   - Lezione trasferibile + anti-pattern

## Accountability su delivery (hard rule)
- Missing delivery o SLA violato => escalation immediata.
- Formato escalation: `BLOCKER | causa | input mancante | nuova ETA`.
- Nessun ping narrativo: solo milestone, blocker, decisione.

## Task pickup handshake (anti-bug, mandatory)
Per ogni task scritto in inbox Specialist:
1. SC richiede `CP0_ACK` entro 10 minuti.
2. Specialist deve pubblicare in outbox un ACK file con formato:
   `STATUS | STARTED/NOT_STARTED | blocker_cause | missing_input | CP1_ETA`.
3. Se ACK non arriva entro 10 minuti:
   - task marcato `SLA_AT_RISK`,
   - SC ridispatcha + apre escalation operativa.
4. Senza `CP0_ACK`, il task non è considerato preso in carico.

## Completion trigger (push-based, mandatory)
- SC starts final review immediately when sentinel appears:
  `outbox/CPF_DONE_<task>_<date>.md`
- Sentinel is the canonical trigger for SC review/report production.
- Periodic checks remain fallback only (not primary trigger).

## Milestone report packaging (hard rule)
- Ogni milestone review SC termina con:
  1) `.tex` unico (testo+figure+tabelle),
  2) `.pdf` compilato,
  3) cartelle sorgente `figures/` e `tables/`.
- Writing style obbligatorio: manuscript/paper style (testo continuo, sezioni scientifiche complete, interpretazione figura-per-figura, discussione e conclusioni).
- Evitare formato checklist come testo principale; le liste sono ammesse solo come supporto secondario.
- Naming obbligatorio con delivery name + date.
- Nessuna milestone considerata chiusa senza `.pdf` leggibile.

## Task closure constraint (hard rule)
- Regola assoluta: alla fine di OGNI task, SC deve pubblicare una review finale in `.tex + .pdf`.
- Stato `CLOSED` consentito solo se il path del PDF review è presente nel messaggio di chiusura (`PATH | STATO | NEXT | ETA`).
- Se il PDF review manca: vietato chiudere il task; usare `BLOCKED | MISSING_SC_REVIEW_PDF | ...`.

## Outbox markdown archival rule (hard rule)
- Quando il report finale (`.tex + .pdf`) è pubblicato e il task è `CLOSED`, i file `.md` operativi di outbox devono essere archiviati.
- Destinazione standard: `outbox/archive/YYYY-MM-DD_md_full_archive/` (mantenendo struttura relativa).
- Non cancellare: solo `mv` in archive.
- Eccezioni: file di protocollo/playbook permanenti se esplicitamente marcati come "keep-active".

## SC inbox archival rule (hard rule)
- Dopo `CLOSED`, SC deve archiviare anche il task file corrispondente nella propria inbox.
- Destinazione standard: `inbox/archive/YYYY-MM-DD_done/`.
- Nessun task può considerarsi realmente chiuso finché inbox SC non è archiviata.

## Regole di qualità review
- Nessuna promozione a `src/` senza evidenza e non-regressione.
- Nessun output in `outbox/` senza struttura a 5 blocchi.
- Ogni blocco critico deve produrre contromisura documentata.
- SC outbox: solo sintesi/valutazione estratta da SC (no duplicazione del dettaglio specialist).
- Specialist detail resta nel suo outbox; SC fornisce solo pointer essenziali per navigazione.

## Generalizzazione (obbligatoria)
Per ogni task chiuso, SC deve scrivere:
- 1 pattern riusabile
- 1 anti-pattern da evitare
- 1 regola operativa aggiornata

## Cadenza di aggiornamento
- Aggiornamento minimo: 3 nuove regole/settimana.
- Revisione settimanale del playbook con Cassia.
