# ERC8004-Specialist — Workspace Structure

## Root
- `inbox/` incoming tasks
- `working/` active work area (draft/intermediate)
- `outbox/` final deliverables
- `logs/` operational logs
- `docs/` persistent documentation and workflows
- `protocols/` reporting/communication protocols
- `archive/` backups and retired artifacts
- `runlogs/` compatibility logs (canonical mirror also in `working/runs/_runlogs/`)

## working/
- `src/` stable codebase for extraction/analysis
- `runs/` run-scoped execution folders and mirrored runlogs
- `data/raw/` input snapshots
- `data/processed/` cleaned datasets
- `analysis/notebooks/` exploratory notebooks
- `analysis/scripts/` ad-hoc scripts
- `results/tables|figures|summaries/` candidate outputs before outbox promotion

Rule: only decision-ready outputs go to `outbox/`.
