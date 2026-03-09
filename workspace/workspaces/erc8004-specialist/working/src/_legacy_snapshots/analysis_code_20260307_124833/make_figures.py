#!/usr/bin/env python3
import os
import pandas as pd
import matplotlib.pyplot as plt

BASE = "/home/manuel/.openclaw/workspace/workspaces/erc8004-specialist"
RAW_DIR = os.getenv("RAW_DIR", f"{BASE}/working/data/latest/raw/ethereum_1")
RUN_ID = os.getenv("RUN_ID", "latest_eth")
OUT_DIR = os.getenv("OUT_DIR", f"{BASE}/working/results/figures/{RUN_ID}")
os.makedirs(OUT_DIR, exist_ok=True)

reg = pd.read_csv(os.path.join(RAW_DIR, "identity_registered.csv"))

# Figure 1: registrations over blockNumber (proxy timeline)
if "blockNumber" in reg.columns:
    s = reg.groupby("blockNumber").size().cumsum()
    plt.figure(figsize=(7,4))
    s.plot()
    plt.title("Cumulative registrations (by block)")
    plt.xlabel("blockNumber")
    plt.ylabel("cumulative agents")
    plt.tight_layout()
    out = os.path.join(OUT_DIR, "fig_01_cumulative_registrations.pdf")
    plt.savefig(out)
    plt.close()
    print("Saved:", out)

# Explanation stub
exp = os.path.join(f"{BASE}/working/results/explainers", f"{RUN_ID}_figures.md")
os.makedirs(os.path.dirname(exp), exist_ok=True)
with open(exp, "w", encoding="utf-8") as f:
    f.write("# Figure explanations\n\n")
    f.write("## fig_01_cumulative_registrations.pdf\n")
    f.write("- Question: come cresce la registrazione agent nel tempo (proxy blocchi).\n")
    f.write("- Input: identity_registered.csv (latest/raw/ethereum_1).\n")
    f.write("- Limit: asse x in blockNumber, non tempo civile.\n")
print("Saved:", exp)
