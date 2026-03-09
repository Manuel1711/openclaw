# CLIENT TEMPORAL DYNAMICS — Technical Delivery

## Method
- Source: `/home/manuel/.openclaw/workspace/workspaces/erc8004-specialist/working/data/raw/2026-03-07_1220_eth_validation_fix/ethereum_1/reputation_newfeedback.csv`
- Bin size: 1000 blocks
- Dropout threshold: 20000 blocks
- Peak window: 5 bins

## Outputs
- Tables in `working/results/tables/2026-03-08_client_temporal/`
- Figures in `outbox/figures/2026-03-08_client_temporal/`

## QA
- Time-series non-empty with bin metadata
- Inter-event stats only for clients with >=2 events
- Deterministic cluster labels
- Dropout flags include threshold column

## Computational limits
- Block-based time proxy; no wall-clock conversion in this run.
