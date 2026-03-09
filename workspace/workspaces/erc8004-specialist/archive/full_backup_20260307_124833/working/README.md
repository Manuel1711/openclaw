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
