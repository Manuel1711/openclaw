# SPECIALIST_FAILURE_MODES_2026-03-09

## FM-01 — Over-polish prima della consegna
- Trigger: fit/refinement prolungato senza artifact nuovi.
- Segnale: >20 min senza nuovi file.
- Prevenzione: fast-first obbligatorio (1 figura + 1 tabella), refinement solo post-milestone.

## FM-02 — Status without execution
- Trigger: messaggi di stato senza script/run attivi.
- Segnale: nessun nuovo `.py/.csv/.pdf` su disco.
- Prevenzione: regola "no artifact = no execution".

## FM-03 — Gap inbox→run
- Trigger: task in inbox letto ma run non partito.
- Segnale: CP0 presente, nessun processo/nuovi file.
- Prevenzione: watcher + trigger-runner auto (ACK + RUN + CPF_DONE + archive).

## FM-04 — Stop tra blocchi
- Trigger: fine CP1 senza avvio blocco successivo.
- Segnale: processo idle con task incompleto.
- Prevenzione: regola hard "finito blocco -> parte il successivo".

## FM-05 — Ambiguità stato (RUNNING vs STALLED)
- Trigger: processo running ma output fermi.
- Segnale: timestamp/size file non cambiano >10 min.
- Prevenzione: monitor 3 segnali (processo, crescita file, nuovi artifact).

## FM-06 — Inbox non archiviata a task chiuso
- Trigger: task concluso ma file ancora in inbox.
- Segnale: presenza TASK_*.md attivo dopo CPF_DONE.
- Prevenzione: archive immediato automatico in runner.

## FM-07 — Editing rischioso documenti esterni
- Trigger: modifica non insert-only.
- Segnale: perdita contenuto, restore manuale.
- Prevenzione: default insert-only; nessuna cancellazione senza richiesta esplicita + doppia conferma.

## FM-08 — Handoff incompleto a SC
- Trigger: report senza path file finali.
- Segnale: SC non trova rapidamente artifact.
- Prevenzione: template handoff unico con checklist path obbligatoria.
