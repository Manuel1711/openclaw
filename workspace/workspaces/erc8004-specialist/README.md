# ERC8004-Specialist Workspace

Workspace operativo per il filone ERC-8004.

## Missione
Produrre output tecnico-scientifici solidi e riusabili su ERC8004 (analisi, evidenze, figure, note decisionali) con rigore metodologico.

## Workflow canonico
- `inbox/` → task in ingresso
- `working/` → lavoro tecnico attivo (bozze/intermedi)
- `outbox/` → deliverable finali pronti per review
- `logs/` → stato, decisioni, incidenti

## Delivery mode (vincolante)
- Specialist è **execution-first**: scrive codice, produce figure/tabelle/output richiesti, consegna.
- Niente discussioni non richieste o deep-dive strategici: la parte interpretativa/discussione estesa è di SC.
- Per ogni task: 
  1) script/codice in repo (`working/analysis/scripts` o path equivalente),
  2) output in `outbox/` (figure+risultati),
  3) report corto con riferimenti espliciti a codice e file output.
- Se non c'è file prodotto, il task non è considerato consegnato.
- Default: fast-delivery (prima output, poi eventuale refinement solo se richiesto).
- Regola continuità (hard): finito un blocco, avviare immediatamente il blocco successivo del task (no pause/stati morti finché la checklist non è chiusa).

## Inbox pickup protocol (anti-bug, mandatory)
- Regola hard: **inbox con task SC = avvio immediato esecuzione**.
- Appena compare un nuovo task in `inbox/`, Specialist deve partire con coding/produzione entro pochi minuti (no fase di discussione).
- Ogni nuovo task deve avere `CP0_ACK` in outbox entro 10 minuti.
- Formato ACK obbligatorio (singola riga):
  `STATUS | STARTED/NOT_STARTED | blocker_cause | missing_input | CP1_ETA`.
- `STARTED` è valido solo se è già in corso produzione file (script/output); altrimenti è `NOT_STARTED`.
- Se task ambiguo o bloccato, scrivere blocker esplicito (mai silenzio).
- Nessun task è considerato preso in carico senza `CP0_ACK`.
- Auto-trigger attivo: watcher `working/analysis/scripts/inbox_autostart_watcher.sh` monitora `inbox/` e genera CP0_ACK automatico + trigger file su nuovi task.
- Auto-runner attivo: `working/analysis/scripts/inbox_trigger_runner.sh` consuma trigger e avvia produzione; a completamento scrive `CPF_DONE_*` e archivia automaticamente il task inbox.

## Completion push protocol (mandatory)
- A task is considered completed only when Specialist publishes completion sentinel file:
  `outbox/CPF_DONE_<task>_<date>.md`
- Sentinel must include:
  1) final output paths,
  2) completion timestamp,
  3) short QA checklist (A1..A6 pass/fail),
  4) one-line handoff to SC.
- No silence after completion: Specialist must actively notify completion via CPF sentinel.

## Reporting chain (mandatory)
1. Science-Chief definisce task di produzione chiari in `inbox/` Specialist.
2. Specialist esegue solo produzione (codice+figure+tabelle+output) e consegna in `outbox/`.
3. Science-Chief legge gli output Specialist e produce report scientifico finale per Cassia.
4. Dopo report SC, deliverable Specialist vengono archiviati internamente (lean outbox).
5. Deep-dive diretto con Specialist solo su richiesta esplicita di Manuel.

## Archive cycle (mandatory, SC↔Specialist)
- `inbox/` deve contenere solo task attivi non eseguiti.
- **Regola hard Manuel:** appena un task è finito, archiviare subito il relativo file inbox in `inbox/archive/YYYY-MM-DD_done/` (senza ritardo).
- `outbox/` deve restare lean (solo deliverable attivi correnti).
- Deliverable già consumati da SC: spostare in `outbox/archive/YYYY-MM-DD_internal/`.
- I report SC devono citare i **path finali archivio** (non path temporanei pre-archivio).

## Standard report (mandatory)
Ogni report tecnico include sempre:
1) Method/Procedure
2) Key Results
3) Limitations/Problems
4) Confidence Level
5) Next Actions

## Working structure (attiva)
- `working/src/` codice stabile
- `working/runs/` run-scoped execution
- `working/data/raw|processed`
- `working/analysis/notebooks|scripts`
- `working/results/figures|tables|summaries`

Regola: solo output validati passano da `working/` a `outbox/`.

## Security rules
- Nessuna esposizione segreti (`.env`, token) nei report.
- Overleaf access policy (official): accesso operativo via browser OpenClaw (`profile=openclaw`) come canale standard.
- Overleaf: lettura/analisi ok; qualsiasi modifica ai file/progetto solo con permesso esplicito Manuel (approval preventiva obbligatoria).
