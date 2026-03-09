import pandas as pd
from pathlib import Path

BASE = Path('/home/manuel/.openclaw/workspace/workspaces/erc8004-specialist')
SRC = BASE / 'working/data/raw/2026-03-07_1220_eth_validation_fix/ethereum_1/reputation_newfeedback.csv'
OUT = BASE / 'working/results/tables/2026-03-08_q3_v2'
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(SRC, usecols=['blockNumber','agentId']).dropna()
df['blockNumber']=df['blockNumber'].astype(int)
df['agentId']=df['agentId'].astype(int)

blocks = sorted(df['blockNumber'].unique())
qs = [0, .25, .5, .75, 1.0]
cuts = sorted(set(int(df['blockNumber'].quantile(q)) for q in qs))
if len(cuts) < 5:
    cuts = [min(blocks), *[int(min(blocks)+(max(blocks)-min(blocks))*p) for p in (0.25,0.5,0.75)], max(blocks)]

rows=[]
prev_top=None
for i in range(4):
    lo, hi = cuts[i], cuts[i+1]
    sli = df[(df['blockNumber']>=lo) & (df['blockNumber']<=hi)]
    top = set(sli['agentId'].value_counts().head(20).index.tolist())
    overlap = len(top & prev_top)/20 if prev_top is not None else None
    rows.append({'slice':i+1,'block_lo':lo,'block_hi':hi,'n_events':len(sli),'overlap_prev_top20':overlap})
    prev_top = top

pd.DataFrame(rows).to_csv(OUT/'q3_v2_temporal_stability.csv', index=False)
print('written temporal stability')
