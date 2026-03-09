#!/usr/bin/env python3
import os
import json
import pandas as pd

BASE = "/home/manuel/.openclaw/workspace/workspaces/erc8004-specialist"
RAW_DIR = os.getenv("RAW_DIR", f"{BASE}/working/data/latest/raw/ethereum_1")
OUT_DIR = os.getenv("OUT_DIR", f"{BASE}/working/results/metrics")
os.makedirs(OUT_DIR, exist_ok=True)

reg = pd.read_csv(os.path.join(RAW_DIR, "identity_registered.csv"))
fb_path = os.path.join(RAW_DIR, "reputation_newfeedback.csv")
fb = pd.read_csv(fb_path) if os.path.exists(fb_path) else pd.DataFrame()

metrics = {
    "agents_registered": int(reg["agentId"].nunique()) if "agentId" in reg.columns else int(len(reg)),
    "feedback_rows": int(len(fb)),
}

with open(os.path.join(OUT_DIR, "metrics_summary.json"), "w", encoding="utf-8") as f:
    json.dump(metrics, f, indent=2)

print("Saved:", os.path.join(OUT_DIR, "metrics_summary.json"))
