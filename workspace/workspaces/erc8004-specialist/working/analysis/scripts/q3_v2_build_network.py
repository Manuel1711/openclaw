import pandas as pd
import networkx as nx
from pathlib import Path

BASE = Path('/home/manuel/.openclaw/workspace/workspaces/erc8004-specialist')
SRC = BASE / 'working/data/raw/2026-03-07_1220_eth_validation_fix/ethereum_1/reputation_newfeedback.csv'
OUT = BASE / 'working/results/tables/2026-03-08_q3_v2'
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(SRC, usecols=['agentId','clientAddress']).dropna()
df['agentId'] = df['agentId'].astype(int)
df['clientAddress'] = df['clientAddress'].astype(str).str.lower()

# 1) bipartite weighted edges
bip = df.groupby(['clientAddress','agentId']).size().reset_index(name='weight')
bip.to_csv(OUT / 'q3_v2_bipartite_edges_weighted.csv', index=False)

# 2) agent projection via shared clients (weighted by shared-client count)
client_agents = bip.groupby('clientAddress')['agentId'].apply(list)
weights = {}
for agents in client_agents:
    uniq = sorted(set(agents))
    for i in range(len(uniq)):
        for j in range(i+1, len(uniq)):
            k = (uniq[i], uniq[j])
            weights[k] = weights.get(k, 0) + 1

proj = pd.DataFrame([(a,b,w) for (a,b),w in weights.items()], columns=['agent_i','agent_j','shared_clients'])
if len(proj)==0:
    proj = pd.DataFrame(columns=['agent_i','agent_j','shared_clients','jaccard'])
else:
    # jaccard normalization
    client_sets = bip.groupby('agentId')['clientAddress'].apply(set).to_dict()
    jac = []
    for _,r in proj.iterrows():
        a,b = int(r['agent_i']), int(r['agent_j'])
        sa,sb = client_sets.get(a,set()), client_sets.get(b,set())
        den = len(sa|sb)
        jac.append((len(sa&sb)/den) if den else 0.0)
    proj['jaccard'] = jac

proj.to_csv(OUT / 'q3_v2_agent_projection_weighted.csv', index=False)

# 3) centrality on projection (weighted degree + betweenness + pagerank fallback)
G = nx.Graph()
for _,r in proj.iterrows():
    G.add_edge(int(r['agent_i']), int(r['agent_j']), weight=float(r['shared_clients']))

if G.number_of_nodes() == 0:
    cen = pd.DataFrame(columns=['agentId','weighted_degree','betweenness','pagerank'])
else:
    wdeg = dict(G.degree(weight='weight'))
    btw = nx.betweenness_centrality(G, weight='weight', normalized=True)
    pr = nx.pagerank(G, weight='weight')
    cen = pd.DataFrame({'agentId': list(G.nodes())})
    cen['weighted_degree'] = cen['agentId'].map(wdeg)
    cen['betweenness'] = cen['agentId'].map(btw)
    cen['pagerank'] = cen['agentId'].map(pr)

cen = cen.sort_values('weighted_degree', ascending=False)
cen.to_csv(OUT / 'q3_v2_agent_centrality.csv', index=False)
cen.head(20).to_csv(OUT / 'q3_v2_top20_multi_metric.csv', index=False)

print('written:', OUT)
