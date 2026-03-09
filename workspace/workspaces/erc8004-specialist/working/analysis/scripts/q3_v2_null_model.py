import pandas as pd, numpy as np
from pathlib import Path

BASE = Path('/home/manuel/.openclaw/workspace/workspaces/erc8004-specialist')
SRC = BASE / 'working/data/raw/2026-03-07_1220_eth_validation_fix/ethereum_1/reputation_newfeedback.csv'
OUT = BASE / 'working/results/tables/2026-03-08_q3_v2'
OUT.mkdir(parents=True, exist_ok=True)

rng=np.random.default_rng(42)
df=pd.read_csv(SRC, usecols=['agentId','clientAddress']).dropna()
df['agentId']=df['agentId'].astype(int)
obs = df['agentId'].value_counts()
obs_top20_share = obs.head(20).sum()/len(df)
obs_mod_proxy = (obs**2).sum()/(len(df)**2)

runs=[]
agents=obs.index.to_numpy()
probs=(obs/obs.sum()).to_numpy()
for r in range(100):
    sim=rng.choice(agents,size=len(df),replace=True,p=probs)
    c=pd.Series(sim).value_counts()
    runs.append({'run':r+1,'top20_share':c.head(20).sum()/len(df),'modularity_proxy':(c**2).sum()/(len(df)**2)})
res=pd.DataFrame(runs)

p_top=(res['top20_share']>=obs_top20_share).mean()
p_mod=(res['modularity_proxy']>=obs_mod_proxy).mean()
summary=pd.DataFrame([{'n_runs':100,'obs_top20_share':obs_top20_share,'obs_modularity_proxy':obs_mod_proxy,'p_top20_share':p_top,'p_modularity_proxy':p_mod}])
res.to_csv(OUT/'q3_v2_null_model_runs.csv',index=False)
summary.to_csv(OUT/'q3_v2_null_model_test.csv',index=False)
print('written null model')
