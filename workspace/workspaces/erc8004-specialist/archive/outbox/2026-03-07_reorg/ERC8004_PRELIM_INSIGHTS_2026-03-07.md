# ERC8004 Preliminary Insights — 2026-03-07

## Snapshot metrics (Ethereum panel)
- Agents in panel: **26,398**
- Feedback rows: **2,163**
- Agents with >=1 feedback: **1,064**
- Median feedback per agent: **0**
- Mean top-1 client concentration (agents with feedback): **~0.95**
- Median time-to-first-feedback: **~11.98 days**
- Mint window observed: **2026-01-29 → 2026-02-23**
- Feedback window observed: **2026-01-29 → 2026-02-21**

## Qualitative findings
1. **Adoption asymmetry:** many registered identities, but small fraction receives reputation activity.
2. **Concentration risk:** reputation input appears dominated by top clients for many agents.
3. **Delayed trust bootstrap:** first feedback arrival often lags registration by ~days-to-weeks.
4. **Potential anomaly vectors:** burst events may indicate campaign-like behavior or coordinated usage spikes.

## Hypotheses to test next
- H1: high top-1 concentration predicts lower long-run reputation resilience.
- H2: shorter time-to-first-feedback correlates with higher sustained activity.
- H3: burst-heavy trajectories associate with higher revocation/churn risk.

## Caveats
- Current run is Ethereum-only and partially refreshed.
- Full refresh blocked by CSV escaping issue in collector.
- Findings are preliminary/descriptive, not causal.
