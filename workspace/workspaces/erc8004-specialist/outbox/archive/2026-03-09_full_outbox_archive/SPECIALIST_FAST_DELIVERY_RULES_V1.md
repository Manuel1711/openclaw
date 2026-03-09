# SPECIALIST_FAST_DELIVERY_RULES_V1

## Regole operative (misurabili)
1) Inbox task ricevuto -> CP0_ACK <= 10 min.
2) STARTED valido solo con nuovo file creato (`.py/.csv/.pdf/.md`).
3) Batch atomico: max 1 figura + 1 tabella per micro-run.
4) Fast-first: prima consegna minima funzionante, poi refinement.
5) Nessun blocco >20 min senza nuovi artifact.
6) Fine blocco => avvio automatico blocco successivo (no idle).
7) Task completato => `CPF_DONE_*` + archive inbox immediato.
8) Outbox lean: attivo in root, storico in `outbox/archive/...`.
9) Update di stato solo in formato proof-by-files (path reali).
10) In caso errore: `BLOCKER | cause | missing_input | ETA` entro 2 min.

## KPI minimi
- T_CP0 <= 10 min
- T_first_artifact <= 20 min
- Idle_gap <= 5 min tra blocchi
- Archive_delay <= 2 min dopo CPF_DONE
