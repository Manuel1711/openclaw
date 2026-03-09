# TASK SPEC — Q3_v2 Network Inference Pack (Execution-Only)

## 0) Role boundary (MANDATORY)
You are execution layer only.
Produce code, figures, and tables.
Do not provide scientific narrative, strategic interpretation, or GO/HOLD/KILL decisions.

## 1) Objective
Build Q3_v2 network artifacts from ERC8004 feedback data for SC inferential review:
- bipartite client→agent network
- agent projected network
- centrality metrics
- community detection
- temporal stability slices
- null-model significance checks

## 2) Input data (fixed)
Use only:
- `working/data/raw/2026-03-07_1220_eth_validation_fix/ethereum_1/reputation_newfeedback.csv`
- optional join: `working/data/raw/2026-03-07_1220_eth_validation_fix/ethereum_1/identity_registered.csv`

No new extraction in this task.

## 3) Deliverables (required)
### 3.1 Code
- `working/analysis/scripts/q3_v2_build_network.py`
- `working/analysis/scripts/q3_v2_temporal_slices.py`
- `working/analysis/scripts/q3_v2_null_model.py`

### 3.2 Tables
Output folder: `working/results/tables/2026-03-08_q3_v2/`

Required files:
1. `q3_v2_bipartite_edges_weighted.csv`
2. `q3_v2_agent_projection_weighted.csv`
3. `q3_v2_agent_centrality.csv`
4. `q3_v2_community_membership.csv`
5. `q3_v2_temporal_stability.csv`
6. `q3_v2_null_model_test.csv`
7. `q3_v2_top20_multi_metric.csv`

### 3.3 Figures (PDF-only final)
Output folder: `outbox/figures/2026-03-08_q3_v2/`

Required files:
1. `q3_v2_degree_distribution.pdf`
2. `q3_v2_centrality_top20.pdf`
3. `q3_v2_community_size_distribution.pdf`
4. `q3_v2_temporal_stability.pdf`
5. `q3_v2_null_model_comparison.pdf`

### 3.4 Outbox note (technical only)
- `outbox/Q3_V2_TECHNICAL_DELIVERY_2026-03-08.md`
Allowed content: method steps, paths, QA checks, computational limits.
No interpretation beyond technical caveats.

## 4) Technical requirements
### 4.1 Network construction
- Bipartite graph: clientAddress → agentId
- Edge weight = feedback event count per pair

### 4.2 Agent projection
- Build agent-agent projection via shared clients
- Provide weighted projection with at least one normalized weighting (cosine or Jaccard)

### 4.3 Centrality
Compute per agent at least:
- weighted degree
- betweenness
- eigenvector (or PageRank if convergence issues)

### 4.4 Communities
- Run Louvain or Leiden
- Export community id per agent
- Export community size table

### 4.5 Temporal stability
- Minimum 4 time slices (block windows)
- Report overlap of top-k central nodes across slices (k=20)

### 4.6 Null model
- Randomized comparison preserving degree sequence (or nearest feasible approximation)
- Minimum 100 random runs
- Report empirical p-values for at least:
  - modularity
  - concentration metric (e.g., top20 share)

## 5) Acceptance criteria (hard)
A1) All required files exist in exact paths/names above.
A2) Figures are PDF and readable.
A3) `q3_v2_agent_centrality.csv` has no duplicated `agentId`.
A4) Temporal table includes >=4 slices and overlap@20.
A5) Null model table includes >=100 runs and p-values.
A6) Total feedback consistency check: sum bipartite weights == total feedback events in source.

## 6) SLA
- CP1 (skeleton + first 2 tables): 90 min
- CPF (full pack): 4h
If blocked, send one line:
`BLOCKER | cause | missing input | new ETA`

## 7) Forbidden scope
- No policy suggestions
- No business recommendations
- No scientific conclusions
- No GO/HOLD/KILL
