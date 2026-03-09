# Standard Proposal for Science-Chief — Specialist Workflow Baseline (v1)

## Purpose
Promote the operational pattern validated with ERC8004-Specialist to a reusable standard for future specialist bots under Science-Chief.

## Why this standard
The current cycle exposed two major failure classes:
1) structural drift during active runs,
2) inconsistent output organization and redundant artifacts.

Both are now controlled with explicit rules, run guards, and path conventions.

---

## Standard v1 (mandatory for new specialists)

### A) Canonical workspace layout
At specialist root:
- `inbox/` tasks in
- `outbox/` technical deliverables out
- `logs/` operational decisions
- `runlogs/` full execution logs
- `working/` execution area

Inside `working/`:
- `analysis/data_extraction/` for extraction/enrichment code
  - `code/`, `config/`, `docs/`
- `analysis/analysis_code/` for analysis scripts only
- `data/` for generated datasets only
  - `raw/`, `enriched/`, `analytics/`, `latest/`
- `results/` for final outputs only
  - `figures/` (PDF), `metrics/`, `explainers/`

### B) Path discipline
- New extraction code -> `working/analysis/data_extraction/`
- New analysis code -> `working/analysis/analysis_code/`
- New generated data -> `working/data/`
- New final results -> `working/results/`

### C) Lean-results policy
- Keep only required artifacts in `results/`.
- No redundant run copies in active results area.
- Archive superseded artifacts outside active results.

### D) Figure format policy
- Final figures must be PDF.
- PNG/SVG allowed only as intermediate artifacts (not final deliverables).

### E) Explainability policy
Every new artifact (code/data/result) must be explained:
- what it is,
- input dependencies,
- how produced,
- limitations.

### F) Run-safety controls
- Structural refactors forbidden during active runs.
- Active run marker: `.run_active.lock`.
- Mandatory preflight before extraction launch.

Implemented controls:
- `working/analysis/data_extraction/code/preflight_check.py`
- `working/analysis/data_extraction/code/run_extraction.sh <run_id>`

### G) Reporting standard (specialist layer)
Outbox reports must include:
1) methods/procedure,
2) exact paths and commands,
3) outputs generated,
4) diagnostics/issues,
5) assumptions/limits,
6) next actions.

---

## Migration checklist for any new specialist bot
1. Create canonical folder tree (as above).
2. Install preflight + run wrapper for extraction pipelines.
3. Add `WORKFLOWS.md` and runbook with path guardrails.
4. Enforce PDF-only final figures.
5. Enable lean-results cleanup routine.
6. Require explainers for outputs.

---

## Evidence this standard is field-tested
Validated in ERC8004 cycle:
- reproduced and fixed CSV serialization regression,
- re-ran extraction successfully,
- produced metrics + PDF figure + explainer,
- cleaned redundant outputs,
- stabilized workspace workflow.

---

## Request to Science-Chief
Adopt this as default template for all future R&D specialists unless explicitly overridden by Manuel.
