#!/usr/bin/env python3
import os
import json
import pandas as pd
from web3 import Web3

BASE = "/home/manuel/.openclaw/workspace/workspaces/erc8004-specialist"
RAW_DIR = f"{BASE}/working/data/raw/2026-03-07_1220_eth_validation_fix/ethereum_1"
OUT_SUM = f"{BASE}/working/results/summaries/2026-03-07_step1"
OUT_TAB = f"{BASE}/working/results/tables/2026-03-07_step1"
OUT_FIG = f"{BASE}/outbox/figures/2026-03-07_step1_dynamics"
os.makedirs(OUT_SUM, exist_ok=True)
os.makedirs(OUT_TAB, exist_ok=True)
os.makedirs(OUT_FIG, exist_ok=True)

# load env from specialist config
env_path = f"{BASE}/working/src/data_extraction/config/.env"
if os.path.exists(env_path):
    for line in open(env_path, "r", encoding="utf-8"):
        s = line.strip()
        if not s or s.startswith("#") or "=" not in s:
            continue
        k, v = s.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip())

rpc = os.getenv("RPC_URL_ETHEREUM", "").strip()
if not rpc:
    raise SystemExit("Missing RPC_URL_ETHEREUM")

w3 = Web3(Web3.HTTPProvider(rpc, request_kwargs={"timeout": 60}))
if not w3.is_connected():
    raise RuntimeError("RPC not connected")

files = [
    "identity_registered.csv",
    "identity_transfer.csv",
    "reputation_newfeedback.csv",
]

# cache
cache_path = f"{OUT_SUM}/block_times_cache.csv"
cache = {}
if os.path.exists(cache_path) and os.path.getsize(cache_path) > 0:
    c = pd.read_csv(cache_path)
    if {"blockNumber", "blockTime"}.issubset(c.columns):
        cache = {int(b): int(t) for b, t in zip(c["blockNumber"], c["blockTime"])}


def ts_for_block(b: int) -> int:
    if b in cache:
        return cache[b]
    ts = int(w3.eth.get_block(int(b))["timestamp"])
    cache[b] = ts
    return ts

for fn in files:
    p = f"{RAW_DIR}/{fn}"
    df = pd.read_csv(p)
    if "blockNumber" not in df.columns:
        continue
    blks = pd.to_numeric(df["blockNumber"], errors="coerce").dropna().astype(int)
    uniq = sorted(blks.unique().tolist())
    for b in uniq:
        ts_for_block(int(b))
    df["blockTime"] = blks.map(cache)
    df["blockDateUTC"] = pd.to_datetime(df["blockTime"], unit="s", utc=True)
    df.to_csv(p, index=False)

pd.DataFrame(sorted(cache.items()), columns=["blockNumber", "blockTime"]).to_csv(cache_path, index=False)

# rerun dynamics with enriched timestamps
reg = pd.read_csv(f"{RAW_DIR}/identity_registered.csv")
fb = pd.read_csv(f"{RAW_DIR}/reputation_newfeedback.csv")
reg["blockDateUTC"] = pd.to_datetime(reg["blockDateUTC"], utc=True, errors="coerce")
fb["blockDateUTC"] = pd.to_datetime(fb["blockDateUTC"], utc=True, errors="coerce")

first_reg = reg.groupby("agentId")["blockDateUTC"].min().rename("reg_time")
first_fb = fb.groupby("agentId")["blockDateUTC"].min().rename("fb_time")
ttf = pd.concat([first_reg, first_fb], axis=1, join="inner").dropna().reset_index()
ttf["ttf_days"] = (ttf["fb_time"] - ttf["reg_time"]).dt.total_seconds() / 86400.0
ttf = ttf[ttf["ttf_days"] >= 0]
ttf.to_csv(f"{OUT_TAB}/time_to_first_feedback_days_exact.csv", index=False)

import matplotlib.pyplot as plt
plt.figure(figsize=(7,4.5))
plt.hist(ttf["ttf_days"], bins=40)
plt.xlabel("Time to first feedback (days, exact block timestamp)")
plt.ylabel("Number of agents")
plt.title("Step1 dynamics rerun: time-to-first-feedback")
plt.tight_layout()
plt.savefig(f"{OUT_FIG}/fig_step1_ttf_exact_days.pdf")
plt.close()

summary = {
    "ttf_n_agents": int(len(ttf)),
    "ttf_median_days": float(ttf["ttf_days"].median()) if len(ttf) else None,
    "ttf_mean_days": float(ttf["ttf_days"].mean()) if len(ttf) else None,
    "ttf_p90_days": float(ttf["ttf_days"].quantile(0.9)) if len(ttf) else None,
    "cache_blocks": int(len(cache)),
}
with open(f"{OUT_SUM}/step1_timestamp_dynamics_summary.json", "w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)

print("STEP1_DONE")
print(summary)
