# ERC8004 Specialist — Stato lavoro, navigazione e note operative

Data: 2026-03-07
Autore: ERC8004-Specialist

## 1) Cosa è stato fatto (schematico)

### A. Diagnosi e fix pipeline estrazione
- Problema riprodotto su collector:
  - `_csv.Error: need to escape, but no escapechar set`
- Root cause identificata:
  - export CSV non robusto su campi con caratteri speciali.
- Fix validato nella copia operativa:
  - uso di scrittura CSV robusta con quoting+escape.
- Rerun Ethereum completato con successo (senza crash CSV).

### B. Riorganizzazione workspace (versione corrente)
- Struttura stabilizzata con separazione chiara tra:
  - codice estrazione,
  - codice analisi,
  - dati,
  - risultati.
- Cartelle legacy confusionarie rimosse.

### C. Allineamento policy output
- Figure finali: **solo PDF**.
- Ogni artefatto (codice/dato/risultato) deve essere spiegato.

---

## 2) Struttura attuale e come navigare

Root specialist:
- `inbox/` -> task in ingresso
- `outbox/` -> report tecnici pronti
- `logs/` -> log operativi e decisioni
- `runlogs/` -> log runtime stdout/stderr completi
- `working/` -> area operativa

Dentro `working/`:

### `working/analysis/`
- `data_extraction/`
  - `code/` -> script estrazione/enrichment
  - `config/` -> env/config
  - `docs/` -> runbook
- `analysis_code/` -> nuovi script analisi/figure (solo codice)

### `working/data/`
- `raw/` -> output grezzo collector per run
- `enriched/` -> dati arricchiti
- `analytics/` -> dataset pronti per analisi
- `latest/` -> puntatori all’ultimo run valido

### `working/results/`
- output finali (figure PDF, metriche, explainers)
- file guida provenance:
  - `working/results/CODE_PROVENANCE.md`

---

## 3) Dove sono i componenti principali (path rapidi)

### Codici estrazione dati
- `working/analysis/data_extraction/code/collect_erc8004_events.py`
- `working/analysis/data_extraction/code/add_blocktime_to_existing_csv.py`
- `working/analysis/data_extraction/code/fetch_agentcards_ethereum.py`
- `working/analysis/data_extraction/code/run_fetch_agentcards.sh`

### Codici analisi
- `working/analysis/analysis_code/build_metrics.py`
- `working/analysis/analysis_code/make_figures.py`

### Dati generati (run validato)
- `working/data/raw/2026-03-07_1129_eth/`
- `working/data/latest/raw -> ../raw/2026-03-07_1129_eth`

### Risultati
- `working/results/`

---

## 4) Problemi incontrati

1. **Errore CSV collector**
- Sintomo: crash in `df.to_csv(...)`
- Errore: `_csv.Error: need to escape, but no escapechar set`
- Impatto: refresh inizialmente parziale.

2. **Drift organizzativo durante refactor**
- Spostamenti multipli hanno creato temporaneamente path incoerenti.
- Un passaggio ha rimosso inavvertitamente il blocco codice extraction, poi ripristinato.

3. **Copertura chain incompleta**
- Alcune chain non eseguite per variabili RPC mancanti.

---

## 5) Osservazioni tecniche

- Separare rigidamente `analysis_code` da `data_extraction` riduce errori operativi.
- Tenere `working/data/latest/` accelera i run senza perdere tracciabilità.
- `runlogs/` è utile per debug; `logs/` per governance (entrambi necessari).

---

## 6) Spunti e next-step

1. Stabilizzare script con CLI unificata (`run_extract.sh`, `run_analysis.sh`).
2. Aggiungere validatore path pre-run (fail-fast se cartelle mancanti).
3. Standardizzare explainers automatici accanto a ogni risultato.
4. Introdurre check di coerenza su naming run_id.
5. Estendere multi-chain quando RPC env sono complete.

---

## 7) Direttiva operativa attiva (Manuel)

- Nuovi codici analisi -> `working/analysis/analysis_code/`
- Codici estrazione -> `working/analysis/data_extraction/`
- Nuovi dati -> `working/data/`
- Nuovi risultati -> `working/results/`
- Ogni artefatto deve essere spiegato.
