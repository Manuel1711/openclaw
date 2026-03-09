# M1_PROJECT_BRIEF_ARCH_V1_2026-03-08

## Method
- Input base incorporata da ricerca/SC review:
  - `workspaces/science-chief/outbox/SC_REVIEW_ERC8004_FULL_ANALYSIS_2026-03-07.md`
  - `workspaces/erc8004-specialist/outbox/ERC8004_FULL_ANALYSIS_REPORT_2026-03-07.md`
  - `workspaces/business-chief/outbox/BC_SUPERVISION_ERC8004_M1_CHECKPOINT.md`
- Vincoli usati per design M1:
  1) ETH L1-first, auditabilità alta.
  2) Score v1 aritmetico, completamente spiegabile.
  3) Nessun claim GTM forte finché restano limiti SC (single-chain, temporal proxy).
- Principio architetturale adottato: separare **identity state**, **reputation aggregates**, **feedback events** per ridurre accoppiamento e rendere monetizzabili metriche future senza cambiare il core model.

## Results
### 1) Identity + Reputation View (M1)
- **Identity View (per agent_id)**
  - campi minimi: `agent_id`, `owner`, `registered_block`, `last_transfer_block`, `transfers_count`.
- **Reputation View (per agent_id)**
  - campi minimi: `feedback_count_total`, `unique_clients_total`, `first_feedback_block`, `last_feedback_block`, `top1_client_share`, `tag1_mode`.
- **Output UX/business M1**: scheda unica "Agent Trust Snapshot" con lettura rapida: stato identità + stato reputazionale + concentrazione.

### 2) Score v1 aritmetico esplicabile
Score normalizzato in [0,100], senza black-box:

`Score_v1 = 100 * (0.45*F + 0.25*U + 0.20*T + 0.10*D)`

Dove:
- `F = min(feedback_count_total / 20, 1)`  (saturazione attività)
- `U = min(unique_clients_total / 10, 1)`   (diversità clienti)
- `T = 1 - min(top1_client_share, 1)`       (anti-concentrazione)
- `D = min(agent_age_blocks / 100000, 1)`   (maturità temporale)

Note operative:
- Formula intentionally semplice e auditabile (coerente con richiesta BC).
- `top1_client_share` entra in modo penalizzante per incorporare learning SC su rischio concentrazione.
- In assenza timestamp enriched, `D` resta block-based (esplicitato come limite).

### 3) Feedback Registry pronto a metriche monetizzabili
Schema evento M1 (append-only, compatibile analytics):
- chiave: `feedback_event_id`
- campi: `agent_id`, `client_id`, `block_number`, `tx_hash`, `tag1`, `score_raw` (se presente), `registry_version`, `ingested_at`

Aggregati derivati (ready-for-monetization, non ancora commercializzati):
- **Coverage KPI**: `% agent con >=1 feedback`
- **Activation KPI**: `time_to_first_feedback_blocks` (poi timestamp)
- **Concentration KPI**: `top1_client_share`, `lorenz_gini_proxy`
- **Quality KPI (proto-SLA)**: `% feedback validati`, `% record completi`, latenza ingestione

M1 produce già questi dataset:
- `identity_snapshot_v1`
- `reputation_snapshot_v1`
- `feedback_registry_v1`
- `agent_score_v1`

## Limitations
- Evidenza corrente ETH-heavy; generalizzazione cross-chain non supportata.
- Dinamica temporale ancora proxy-based (12s/block): precisione non finale.
- Dataset `reputation_feedbackrevoked` e `identity_metadataset` vuoti nella finestra osservata: limitano feature avanzate.
- Score v1 è un ranking operativo iniziale, non una misura causale di qualità economica.
- Nessuna promessa commerciale hard (pricing/uplift/ROI) emessa in M1, in linea con gate SC/BC.

## Confidence
- **Architettura M1 (data model + separazione viste): High**
- **Score v1 explainability/auditability: High**
- **Direzione segnali business (sparsità, concentrazione, attivazione lenta): Medium-High**
- **Magnitudine temporale e claim di mercato: Medium-Low** (fino a timestamp enrichment + replication)

## Next
1. **M1.1 (D+1)**: timestamp enrichment e ricalcolo activation metrics.
2. **M1.2 (D+2)**: replica pipeline su almeno 1 asse aggiuntivo (chain o cohort) per de-risk claim.
3. **M1.3 (D+2)**: introdurre `feedback_revoked` handling nel registry (stato evento: active/revoked).
4. **M1.4 (D+3)**: pubblicare Scorecard spec (input, formula, edge cases, audit log).
5. **Decision gate BC/SC**: GO M2 solo se superati check precisione temporale + replicazione minima; altrimenti HOLD/REWORK mirato.