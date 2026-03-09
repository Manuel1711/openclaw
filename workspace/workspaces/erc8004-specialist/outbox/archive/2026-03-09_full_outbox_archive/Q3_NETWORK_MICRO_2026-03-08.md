# Q3 Network Micro-Deliverable — 2026-03-08

## Method
- Built a bipartite network from `reputation_newfeedback.csv` with:
  - node type A: `clientAddress`
  - node type B: `agentId`
  - edge: feedback event from client to agent
- Aggregated weighted edges (`weight = number of feedback events on client→agent pair`).
- Computed agent weighted in-degree as total received feedback.
- Produced top-20 ranking and exploratory bar plot.

## Results
- Script:
  - `working/analysis/scripts/q3_network_micro.py`
- Tables:
  - `working/results/tables/2026-03-08_q3/q3_bipartite_edges_weighted.csv`
  - `working/results/tables/2026-03-08_q3/q3_agent_weighted_degree.csv`
  - `working/results/tables/2026-03-08_q3/q3_degree_top20.csv`
- Figure:
  - `outbox/figures/2026-03-08_q3/q3_network_degree_top20.pdf`

## Limitations
- This is a phase-1 exploratory cut (degree-focused only).
- No centrality (betweenness/eigenvector) or community detection yet.
- No temporal slicing yet (static aggregate only).

## Next
1. Add centrality metrics on projected agent graph.
2. Run community detection (Louvain/Leiden) and export membership table.
3. Add one exploratory community figure.
