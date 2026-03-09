import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path('/home/manuel/.openclaw/workspace/workspaces/erc8004-specialist')
FB = BASE / 'working/data/raw/2026-03-07_1220_eth_validation_fix/ethereum_1/reputation_newfeedback.csv'
TAB_DIR = BASE / 'working/results/tables/2026-03-08_q3'
FIG_DIR = BASE / 'outbox/figures/2026-03-08_q3'
TAB_DIR.mkdir(parents=True, exist_ok=True)
FIG_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(FB, usecols=['agentId', 'clientAddress']).dropna()
df['agentId'] = df['agentId'].astype(int)
df['clientAddress'] = df['clientAddress'].astype(str).str.lower()

# Bipartite edges: client -> agent, weighted by number of feedbacks
edges = df.groupby(['clientAddress', 'agentId']).size().reset_index(name='weight')
edges.to_csv(TAB_DIR / 'q3_bipartite_edges_weighted.csv', index=False)

# Agent weighted in-degree (total feedback count)
agent_deg = edges.groupby('agentId')['weight'].sum().reset_index(name='weighted_in_degree')
agent_deg = agent_deg.sort_values('weighted_in_degree', ascending=False)
agent_deg.to_csv(TAB_DIR / 'q3_agent_weighted_degree.csv', index=False)

# Top 20 for micro-delivery
top20 = agent_deg.head(20).copy()
top20.to_csv(TAB_DIR / 'q3_degree_top20.csv', index=False)

# Exploratory figure
plt.figure(figsize=(9, 5))
plt.bar(top20['agentId'].astype(str), top20['weighted_in_degree'], color='#4C78A8')
plt.xticks(rotation=75, fontsize=8)
plt.ylabel('Weighted in-degree (feedback count)')
plt.xlabel('Agent ID')
plt.title('Q3 Exploratory Network: Top-20 agents by weighted in-degree')
plt.tight_layout()
plt.savefig(FIG_DIR / 'q3_network_degree_top20.pdf', bbox_inches='tight')

print('done')
print(TAB_DIR / 'q3_degree_top20.csv')
print(FIG_DIR / 'q3_network_degree_top20.pdf')
