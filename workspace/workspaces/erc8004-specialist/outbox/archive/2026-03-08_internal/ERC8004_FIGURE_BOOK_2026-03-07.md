# ERC8004 FIGURE BOOK — 2026-03-07

## 1) Method / Procedure
- Figure set generated from:
  - `working/data/raw/2026-03-07_1220_eth_validation_fix/ethereum_1/`
- Generation script:
  - `working/analysis/scripts/full_analysis_erc8004_2026_03_07.py`
- Final figure folder (deliverable):
  - `outbox/figures/2026-03-07_full_analysis/`
- Format policy respected: **PDF-only final figures**.

## 2) Key Results (Figure-by-figure)
### Figure 01 — `fig_01_cumulative_activity.pdf`
- Content: cumulative registrations and cumulative feedback events vs block number.
- Reading: registrations scale rapidly; feedback curve grows much slower.
- Main signal: adoption volume does not translate proportionally into reputation activity.

### Figure 02 — `fig_02_feedback_concentration_hist.pdf`
- Content: histogram of top-1 client share per agent.
- Reading: mass concentrated near high top-1 share values.
- Main signal: per-agent feedback is often dominated by one client.

### Figure 03 — `fig_03_client_concentration_lorenz.pdf`
- Content: Lorenz-style curve for client contribution concentration.
- Reading: strong deviation from equality diagonal.
- Main signal: global feedback issuance is concentrated among a minority of clients.

### Figure 04 — `fig_04_time_to_first_feedback_days.pdf`
- Content: distribution of time to first feedback (days, approximated from blocks).
- Reading: right-skewed distribution with non-trivial long tail.
- Main signal: trust activation is delayed for many agents.

### Figure 05 — `fig_05_feedback_tag1_top12.pdf`
- Content: top-12 tag1 categories by frequency.
- Reading: qualitative composition of feedback labels is uneven.
- Main signal: limited semantic diversity in observed feedback labels.

## 3) Limitations / Problems
- Time conversion in Figure 04 uses block-time approximation (12s/block), not exact block timestamps.
- Figures summarize Ethereum run only in this pass.
- Tag fields may include schema-level heterogeneity not yet normalized.

## 4) Confidence Level
- Figure 01/02/03: **High** (count-based, direct aggregations).
- Figure 04: **Medium** (timing proxy approximation).
- Figure 05: **Medium-high** (field-quality dependent but aggregation stable).

## 5) Next Actions
1. Add exact timestamp-enriched variant for Figure 04.
2. Add cohort split figures (newly registered vs older agents).
3. Add concentration robustness split by tag class and value bands.
4. Reproduce full figure set for additional chains when RPC coverage is available.
