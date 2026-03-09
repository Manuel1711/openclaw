# Working Area — ERC8004-Specialist

Questa cartella è il cantiere operativo (non deliverable finali).

## Struttura
- `src/` codice stabile (pipeline/utility/plot)
- `runs/YYYY-MM-DD_rX/` run riproducibili con:
  - `inputs/`
  - `logs/`
  - `intermediate/`
  - `figures_draft/`
  - `notes.md`
- `data/raw/` snapshot/input locali (read-only quando possibile)
- `data/processed/` dataset puliti
- `analysis/notebooks/` notebook esplorativi
- `analysis/scripts/` script ad-hoc
- `results/tables/` tabelle candidate
- `results/figures/` figure candidate
- `results/summaries/` sintesi tecniche candidate

## Regole
- `working/` contiene bozze, intermedi, debug.
- `outbox/` contiene solo deliverable finali pronti per review.
- Ogni nuovo run va sotto `runs/` con cartella datata.

## Cleanup 20260307_125051
- Legacy folders normalized:
  - results/explainers -> results/summaries
  - results/metrics -> results/tables (remaining dated trees archived)
  - data/analytics + data/enriched -> data/processed (remaining trees archived)
  - data/latest archived
- Backup for cleanup changes: /home/manuel/.openclaw/workspace/workspaces/erc8004-specialist/archive/cleanup_backup_20260307_125051
