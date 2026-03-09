# Data Extraction Runbook (stable)

## Rule 1 — Change freeze during active runs
When extraction is running, structural refactors are forbidden.
Active run is indicated by lock file:
- `/home/manuel/.openclaw/workspace/workspaces/erc8004-specialist/.run_active.lock`

## Rule 2 — Mandatory preflight before every launch
Use preflight checker before any extraction:
```bash
python3 working/analysis/data_extraction/code/preflight_check.py
```

## Standard launch (recommended)
Use wrapper (it runs preflight + lock + extraction + log + latest pointer):
```bash
working/analysis/data_extraction/code/run_extraction.sh <run_id>
```
Example:
```bash
working/analysis/data_extraction/code/run_extraction.sh 2026-03-07_1235_eth
```

## Outputs
- Raw: `working/data/raw/<run_id>/...`
- Log: `runlogs/<run_id>.log`
- Latest pointer: `working/data/latest/raw -> ../raw/<run_id>`

## Figure policy
Final figure deliverables must be PDF.
