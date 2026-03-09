# TASK — ERC8004 Data Refresh + Preliminary Analysis (R2, security-constrained)

## Priority
P0

## Mandatory data boundary
Operate **ONLY** on:
`/home/manuel/.openclaw/workspace/workspaces/erc8004-specialist/inputs/ai_agents_snapshot_2026-03-07`

Direct access to `/home/manuel/Documents/AI_agents` is forbidden for this run.

## C1..C4 checkpoints
- C1 (<=20m): verify snapshot integrity + runnable pipeline from snapshot paths.
- C2 (<=2h): execute refresh attempt from snapshot and log coverage/gaps.
- C3 (<=3h): generate preliminary figures/panels from snapshot-derived data.
- C4 (<=4h): finalize specialist synthesis for SC review.

## Deliverables
- outbox/ERC8004_DATA_REFRESH_REPORT_2026-03-07.md (update with R2 boundary)
- outbox/ERC8004_PRELIM_FIGURES_2026-03-07.md (update with R2 boundary)
- outbox/ERC8004_PRELIM_INSIGHTS_2026-03-07.md (update with R2 boundary)

## Specialist reporting requirement (mandatory)
- Outbox updates must be **detailed technical reports** (methods, commands, assumptions, diagnostics, limitations, evidence tables/figures paths).
- Do **not** compress to high-level executive summaries at specialist layer.
- High-level compression is reserved for SC summary to Cassia.

## Constraints
- No secrets leakage; `.env` is excluded by design.
- Document assumptions and limitations explicitly.
- Include Overleaf-informed methodological framing.
