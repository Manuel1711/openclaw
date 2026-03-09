# TASK — ERC8004 Data Refresh + Preliminary Analysis

## From
- Manuel → Cassia → Science-Chief

## Priority
- P0 (today)

## Context
In `~/Documents/AI_agents` there is an existing data/analysis pipeline for ERC8004-related AI-agent registries.
This must become the operational starting point for `ERC8004-Specialist`.

Source folder (provided to team as snapshot, no direct source access required):
- Snapshot path for operations:
  - `/home/manuel/.openclaw/workspace/workspaces/erc8004-specialist/inputs/ai_agents_snapshot_2026-03-07`
- Original source (Cassia-only handling):
  - `/home/manuel/Documents/AI_agents`

Main contents detected:
- `analysis/erc8004_empirical_eth_make_panels_and_figures.py`
- `erc8004-data/collect_erc8004_events.py`
- `erc8004-data/fetch_agentcards_ethereum.py`
- `erc8004-data/add_blocktime_to_existing_csv.py`
- `erc8004-data/run_fetch_agentcards.sh`
- outputs under `erc8004-data/out*`

## Objective
1. Refresh datasets by rerunning the collection pipeline.
2. Produce a preliminary empirical analysis with first figures and qualitative findings about current registry dynamics.
3. Ensure SC supervises specialist execution closely.
4. Incorporate specialist external sources, including Overleaf context already available to ERC8004-Specialist.

## Execution constraints
- Do **not** operate directly on `/home/manuel/Documents/AI_agents`.
- Use only the provided snapshot in specialist workspace.
- Keep original source folder as reference handled by Cassia only.
- Handle secrets carefully (`.env` excluded from snapshot and must not be leaked).
- Log assumptions and data coverage limitations.

## Required SC workflow (mandatory)
1. Create delegated subtask in `workspaces/erc8004-specialist/inbox/` with explicit deliverables and timeline.
2. Trigger specialist execution and supervise checkpoints.
3. Validate outputs quality before escalation to Cassia.

## Deliverables required from ERC8004-Specialist
- `outbox/ERC8004_DATA_REFRESH_REPORT_<date>.md`
  - what was rerun
  - coverage (chains/events/time window)
  - failures/gaps
- `outbox/ERC8004_PRELIM_FIGURES_<date>.md`
  - list of generated figures + interpretation
- `outbox/ERC8004_PRELIM_INSIGHTS_<date>.md`
  - first qualitative findings
  - hypotheses to test next

## Deliverables required from Science-Chief to Cassia
- `outbox/SC_REVIEW_ERC8004_REFRESH_<date>.md`
  - quality review of specialist outputs
  - scientific confidence level
  - next 7-day plan
  - escalation points for business handoff

## Checkpoints
- C1 (fast): confirmation pipeline can run with current environment
- C2: refreshed datasets produced
- C3: preliminary figures generated
- C4: SC-reviewed synthesis completed

## Definition of done
- Data refreshed successfully (or blockers explicitly documented)
- At least one preliminary figure pack generated
- Initial qualitative interpretation produced
- SC supervision evidence present (review note + decisions)
