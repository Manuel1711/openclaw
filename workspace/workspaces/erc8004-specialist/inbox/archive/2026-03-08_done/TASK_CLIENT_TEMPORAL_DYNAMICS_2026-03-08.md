# TASK — Client Temporal Dynamics (execution-only)

## Role boundary (MANDATORY)
Execution only: produce code, tables, figures, technical note.
No scientific interpretation, no strategy, no GO/HOLD/KILL.

## Objective
Characterize how feedback issuance is distributed over time at client level, with focus on burst behavior and post-burst inactivity.

## Input data (fixed)
- `working/data/raw/2026-03-07_1220_eth_validation_fix/ethereum_1/reputation_newfeedback.csv`
- Optional timestamp enrichment via block lookup (if available in current pipeline).

## Required outputs

### Code
- `working/analysis/scripts/client_temporal_dynamics.py`

### Tables (folder)
`working/results/tables/2026-03-08_client_temporal/`

Required files:
1. `client_time_series_by_blockbin.csv`  (client, bin, count)
2. `client_interevent_stats.csv` (mean/median inter-event block gap, cv, burstiness proxy)
3. `client_lifetime_stats.csv` (first_block, last_block, active_span_blocks, total_feedback)
4. `client_burst_metrics.csv` (peak_count_window, avg_rate, peak_over_avg)
5. `client_behavior_clusters.csv` (label: sprinter/steady/episodic/whale_dormant)
6. `client_dropout_flags.csv` (inactive_after_peak flag by threshold)

### Figures (PDF-only final)
`outbox/figures/2026-03-08_client_temporal/`

Required files:
1. `client_activity_heatmap_top50.pdf`
2. `client_cumulative_feedback_top20.pdf`
3. `client_interevent_distribution.pdf`
4. `client_peak_vs_lifetime_scatter.pdf`
5. `client_behavior_cluster_distribution.pdf`

### Technical outbox note
- `outbox/CLIENT_TEMPORAL_DYNAMICS_TECHNICAL_2026-03-08.md`
Content: method, paths, QA checks, computational limits only.

## Method constraints
- Use block-based temporal bins (explicit bin size in output, e.g. 1000 blocks).
- Compute top clients both by total feedback and by peak burst.
- Define burst metric explicitly in table metadata.
- Define inactivity/dropout threshold explicitly (in blocks) and store in note.

## Acceptance criteria (hard)
A1) All required files exist in exact names/paths.
A2) Figures are valid PDF files.
A3) Time-series table has non-empty rows and includes bin metadata.
A4) Inter-event stats computed for clients with >=2 events.
A5) Cluster table has deterministic rule labels (no free text).
A6) Technical note includes parameter values (bin size, dropout threshold).

## SLA
- CP0_ACK in 10 min (mandatory)
- CP1 (code + first 2 tables) in 90 min
- CPF full delivery in 4h

If blocked:
`BLOCKER | cause | missing input | new ETA`
