# SC_REVIEW_ERC8004_FULL_ANALYSIS_2026-03-07

## 1) Method / Procedure
- Reviewed specialist package:
  - `workspaces/erc8004-specialist/outbox/ERC8004_FULL_ANALYSIS_REPORT_2026-03-07.md`
  - `workspaces/erc8004-specialist/outbox/ERC8004_FIGURE_BOOK_2026-03-07.md`
  - `workspaces/erc8004-specialist/outbox/ERC8004_INTERPRETIVE_NOTES_2026-03-07.md`
  - `workspaces/erc8004-specialist/outbox/figures/2026-03-07_full_analysis/`
- Verified figure artifacts exist (5 PDFs).
- Evaluation criteria: scientific rigor, reproducibility, caveat discipline, decision relevance.
- Overleaf-informed framing confirmed (descriptive-not-causal stance; adoption vs usage separation).

## 2) Key Results
- Coverage (Ethereum window):
  - registered agents: 28,380
  - feedback rows: 2,776
  - agents with >=1 feedback: 1,470 (~5.18%)
- Core signals:
  1. Adoption-usage decoupling is strong (registrations >> active reputation usage).
  2. Concentration risk is high (top-1 client share median 1.00; mean 0.948).
  3. Trust activation is delayed (median time-to-first-feedback ~12.31 days; proxy-based).
- Figure pointers:
  - `.../fig_01_cumulative_activity.pdf`
  - `.../fig_02_feedback_concentration_hist.pdf`
  - `.../fig_03_client_concentration_lorenz.pdf`
  - `.../fig_04_time_to_first_feedback_days.pdf`
  - `.../fig_05_feedback_tag1_top12.pdf`

## 3) Limitations / Problems
- Evidence is ETH-heavy in this cycle; cross-chain generalization not supported yet.
- Temporal metric currently uses block-time approximation (12s/block), reducing precision.
- `reputation_feedbackrevoked` and `identity_metadataset` are empty in observed window.
- Analysis is descriptive; no causal model or intervention effect identification in this pass.

## 4) Confidence Level
- Directional findings (sparse usage + concentration + activation delay): **Medium-High**.
- Exact temporal magnitudes: **Medium** (proxy limitation).
- Ecosystem-wide generalization: **Low** pending multi-chain replication.

## 5) Next Actions
1. Run timestamp-enriched temporal recomputation (owner: ERC8004-Specialist, D+1).
2. Execute multi-chain replication with same metrics/figures (owner: ERC8004-Specialist, D+2).
3. Add robustness splits (tag cohorts / activity cohorts / rolling windows) (owner: ERC8004-Specialist, D+2).
4. Produce intervention decision matrix (onboarding vs incentives vs anti-concentration controls) (owner: SC, D+3).

## Decision Gate
- **HOLD (conditional GO after temporal precision + multi-chain replication).**
- Rationale: current package is scientifically useful and decision-relevant, but not yet sufficient for strong business-side claims without cross-chain and timestamp-precision reinforcement.

## Learning Extraction
- Pattern riusabile: pairing concentration diagnostics (per-agent + global Lorenz) gives robust early warning for reputation-system fragility.
- Anti-pattern da evitare: deriving strategic urgency from single-chain descriptive stats without replication.
- Regola operativa aggiornata nel playbook: any decision-grade promotion to business requires (a) at least one temporal precision check and (b) one replication axis (chain or cohort).
