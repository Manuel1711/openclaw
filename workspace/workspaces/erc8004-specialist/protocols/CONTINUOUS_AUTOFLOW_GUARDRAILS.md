# CONTINUOUS_AUTOFLOW_GUARDRAILS.md

Obiettivo: garantire flusso continuo Inbox -> Coding -> Output -> SC handoff -> Archive senza pause.

## Regole hard
1. Nuovo `TASK_*.md` in inbox => start automatico immediato.
2. Stato valido = produzione file (script/csv/pdf/md), non solo messaggi.
3. Fine blocco => inizio blocco successivo automatico.
4. Task completato => scrittura `CPF_DONE_*` + archiviazione immediata file inbox.
5. Outbox sempre lean; storico in `outbox/archive/...`.

## Handoff a SC (obbligatorio)
Ogni delivery deve includere:
- path script usati
- path tabelle/figure
- nota tecnica con parametri/limiti
- marker `CPF_DONE_*`

## Anti-regressione
- Nessun task può restare in `inbox/` dopo `CPF_DONE`.
- Nessun "STARTED" senza nuovi file su disco.
- In caso errore runtime: `BLOCKER | cause | missing input | ETA`.

## Mini-test consigliato
Eseguire smoke test con task inbox semplice per verificare trigger automatico end-to-end.
