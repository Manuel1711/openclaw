# ERC8004 Specialist — Organizzazione definitiva (temporanea) e flussi

Stato: **attivo e vincolante** (richiesta Manuel, 2026-03-07)

## 1) Struttura cartelle (root)
- `inbox/` → task in ingresso
- `outbox/` → deliverable tecnici (dettagliati)
- `logs/` → log operativi/decisioni
- `runlogs/` → stdout/stderr run tecnici
- `working/` → area operativa unica
  - `working/data/`
    - `raw/` → output estrazione on-chain per run
    - `enriched/` → output arricchiti (blocktime/agentcards)
    - `analytics/` → dataset pronti per analisi
    - `latest/` → puntatori all’ultimo run valido
  - `working/analysis/`
    - `data_extraction/`
      - `code/` → script estrazione/enrichment
      - `config/` → env/config operative
      - `docs/` → runbook extraction
    - `analysis_code/` → script analitici e figure
  - `working/results/` → risultati finali + spiegazioni

## 2) Path canonici (confermati)
- Collector: `working/analysis/data_extraction/code/collect_erc8004_events.py`
- Blocktime: `working/analysis/data_extraction/code/add_blocktime_to_existing_csv.py`
- Agentcards: `working/analysis/data_extraction/code/fetch_agentcards_ethereum.py`
- Wrapper agentcards: `working/analysis/data_extraction/code/run_fetch_agentcards.sh`
- Codice analisi: `working/analysis/analysis_code/`
- Risultati finali: `working/results/`

## 3) Flusso operativo end-to-end
1. **Extract raw**
   - carica env da `working/analysis/data_extraction/config/.env`
   - imposta `OUT_DIR=$BASE/working/data/raw/<run_id>`
   - esegui collector
2. **Aggiorna latest raw**
   - `working/data/latest/raw -> ../raw/<run_id>`
3. **Enrich**
   - blocktime + agentcards verso `working/data/enriched/<run_id>`
4. **Build analytics datasets**
   - output in `working/data/analytics/<run_id>`
5. **Run analysis_code**
   - produce figure/tabelle/spiegazioni in `working/results/`
6. **Reporting**
   - dettagli tecnici in `outbox/`
   - run completi (debug) in `runlogs/`

## 4) Policy output figure
- Deliverable finali figure: **solo PDF** (obbligatorio).
- PNG/SVG solo intermedi tecnici non finali.

## 5) Guardrail anti-confusione
- Nessun codice in `working/results/`.
- Nessun output finale dentro cartelle `code/`.
- `working/data/` contiene solo dati.
- `outbox/` resta canale ufficiale report specialist.

## 6) Run-safety controls (mandatory)
- No structural refactors during active runs.
- Active run marker: `.run_active.lock` at workspace root.
- Mandatory preflight before extraction launch via:
  - `working/analysis/data_extraction/code/preflight_check.py`
- Recommended launcher:
  - `working/analysis/data_extraction/code/run_extraction.sh <run_id>`

