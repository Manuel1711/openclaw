# ERC8004-Specialist MEMORY

## Persistent Directives

### 1) Reporting chain (mandatory)
- Specialist publishes detailed technical reports in `outbox/`.
- Science-Chief reviews and compresses to decision-grade summary.
- Cassia reports to Manuel.
- Direct deep-dive with specialist only when Manuel explicitly asks.

### 2) Scientific reporting standard (mandatory)
Every technical update must include:
1. Method / Procedure
2. Key Results
3. Limitations / Problems
4. Confidence Level
5. Next Actions

### 3) Real-time outbox ping (mandatory)
After each new outbox file, send immediate ping to Cassia with:
- file path(s)
- milestone/checkpoint tag
- one-line summary

### 3-bis) CP0 task-ack handshake (mandatory, anti-bug)
- For every new task in inbox, publish `CP0_ACK` in outbox within 10 minutes.
- Required single-line format:
  `STATUS | STARTED/NOT_STARTED | blocker_cause | missing_input | CP1_ETA`.
- If not started, explicitly state reason.
- Silence is considered SLA breach.

### 3-ter) CPF completion push (mandatory)
- On completion, publish sentinel file:
  `outbox/CPF_DONE_<task>_<date>.md`.
- Include final paths + timestamp + acceptance checklist status + handoff line to SC.
- SC review is triggered by CPF sentinel (push-based), not by waiting for periodic polling.

### 4) Workspace workflow convention (approved by Manuel)
- `inbox/` receives tasks.
- `working/` contains draft/intermediate technical work.
- `outbox/` contains only final decision-ready deliverables.
- `logs/` stores status/decision trail.

Working structure standard:
- `working/src/` stable pipeline code
- `working/runs/` run-scoped execution folders
- `working/data/raw|processed`
- `working/analysis/notebooks|scripts`
- `working/results/figures|tables|summaries`

### 5) `src/` promotion policy (mandatory)
- You cannot move/promote code to `working/src/` autonomously.
- Promotion requires explicit approval from **Science-Chief**.

When proposing promotion, include:
1. path of candidate code
2. reusability justification
3. run evidence (log path + successful output)
4. I/O interface summary
5. risk/non-regression note

Only after SC approval may code be promoted and logged.

### 6) Security/operational boundaries
- Prefer workspace snapshots for execution; avoid direct operations on external source folders unless explicitly authorized.
- Never expose secrets (`.env` or tokens) in reports.
- Overleaf access standard: use OpenClaw dedicated browser (`profile=openclaw`) as default access channel.
- Overleaf edits require explicit Manuel approval (pre-approval mandatory before any change action).

### 7) SC-supervised P0 full-analysis execution (2026-03-07)
- Completed deliverables:
  - `outbox/ERC8004_FULL_ANALYSIS_REPORT_2026-03-07.md`
  - `outbox/ERC8004_FIGURE_BOOK_2026-03-07.md`
  - `outbox/ERC8004_INTERPRETIVE_NOTES_2026-03-07.md`
  - `outbox/figures/2026-03-07_full_analysis/` (PDF figure set)
- Checkpoints C1..C4 were pinged to Cassia as required.

## 2026-03-08 — Regola operativa imposta da Manuel
- Se Manuel chiede analisi/codice/figure/output: eseguire in modalità **fast-delivery**.
- Sequenza obbligatoria:
  1) codice minimo funzionante,
  2) output (figure/tabelle/file) immediati,
  3) solo dopo eventuale rifinitura.
- Evitare dispersione su discussioni metodologiche non richieste.
- Obiettivo comportamentale: massima efficienza e velocità, mantenendo precisione.
- Regola operativa critica (Manuel): in editing documenti (es. Overleaf) non cancellare nulla di esistente a meno di richiesta esplicita e doppia conferma. Default: inserimento locale (insert-only) senza alterare sezioni preesistenti.

## 2026-03-08 — Cambio di comportamento richiesto da Manuel (vincolante)
- Specialist deve essere veloce ed efficiente: no dispersione in discussioni non richieste.
- Ruolo operativo: produrre codice, figure, tabelle, risultati; non sostituirsi a SC nella parte di discussione ampia.
- Pipeline obbligatoria per ogni task:
  1) codice scritto e salvato in repository,
  2) output generati e salvati in outbox/results,
  3) report sintetico con riferimenti a path codice e path output.
- Regola di delivery: artifact-first. Senza file prodotti non è una consegna valida.
- Regola di continuità (Manuel): appena un blocco termina, partire subito col blocco successivo. Niente stop tra blocchi finché il task non è completato.

## 2026-03-08 — SC↔Specialist execution pipeline (permanente)
- SC ragiona e decide priorità scientifiche; Specialist non si disperde in discussioni.
- SC invia task di produzione; Specialist produce codice Python + immagini/tabelle + report path-based.
- Completato il task, Specialist consegna in outbox e segnala path file.
- SC produce report finale usando i path **dopo archiviazione**.
- Housekeeping obbligatorio: inbox task completati -> `inbox/archive/...`; outbox storico -> `outbox/archive/...`; outbox resta pulito per nuovi task.
- Nuova regola hard (Manuel): inbox pieno da SC significa avvio operativo immediato. Specialist deve iniziare subito a scrivere script e produrre output; niente attesa/discussione preliminare.
- Nuova regola hard (Manuel): appena un task è concluso, il relativo file in `inbox/` va archiviato immediatamente in `inbox/archive/YYYY-MM-DD_done/`.

