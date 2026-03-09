# Q3_V2 Technical Delivery — 2026-03-08

## Method (technical)
- Input fixed files:
  - `working/data/raw/2026-03-07_1220_eth_validation_fix/ethereum_1/reputation_newfeedback.csv`
  - optional join support from `identity_registered.csv` (temporal slicing support)
- Built weighted bipartite client→agent edge list.
- Built weighted agent projection via shared clients (+ normalized score field).
- Computed centrality metrics from projection graph.
- Computed temporal top20 overlap across >=4 slices.
- Ran null-model Monte Carlo (100 runs) and computed empirical p-values.
- Computed community membership from projection graph.

## Produced code
- `working/analysis/scripts/q3_v2_build_network.py`
- `working/analysis/scripts/q3_v2_temporal_slices.py`
- `working/analysis/scripts/q3_v2_null_model.py`

## Produced tables
- `working/results/tables/2026-03-08_q3_v2/q3_v2_bipartite_edges_weighted.csv`
- `working/results/tables/2026-03-08_q3_v2/q3_v2_agent_projection_weighted.csv`
- `working/results/tables/2026-03-08_q3_v2/q3_v2_agent_centrality.csv`
- `working/results/tables/2026-03-08_q3_v2/q3_v2_community_membership.csv`
- `working/results/tables/2026-03-08_q3_v2/q3_v2_temporal_stability.csv`
- `working/results/tables/2026-03-08_q3_v2/q3_v2_null_model_test.csv`
- `working/results/tables/2026-03-08_q3_v2/q3_v2_top20_multi_metric.csv`
- extra run-detail: `working/results/tables/2026-03-08_q3_v2/q3_v2_null_model_runs.csv`

## Produced figures (PDF)
- `outbox/figures/2026-03-08_q3_v2/q3_v2_degree_distribution.pdf`
- `outbox/figures/2026-03-08_q3_v2/q3_v2_centrality_top20.pdf`
- `outbox/figures/2026-03-08_q3_v2/q3_v2_community_size_distribution.pdf`
- `outbox/figures/2026-03-08_q3_v2/q3_v2_temporal_stability.pdf`
- `outbox/figures/2026-03-08_q3_v2/q3_v2_null_model_comparison.pdf`

## QA checks (technical)
- All required Q3_v2 table filenames present.
- All required Q3_v2 PDF figure filenames present.
- `q3_v2_agent_centrality.csv`: unique `agentId` entries.
- Temporal stability table includes 4 slices.
- Null model includes >=100 runs (`q3_v2_null_model_runs.csv`) and p-values (`q3_v2_null_model_test.csv`).
- Weight consistency check performed at build stage (bipartite weights aggregate from source events).

## Computational limits
- Projection graph is large; exact centrality can be runtime-expensive.
- Current run uses practical metrics that complete under workstation constraints.
