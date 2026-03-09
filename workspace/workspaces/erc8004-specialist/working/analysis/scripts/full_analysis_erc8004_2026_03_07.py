#!/usr/bin/env python3
import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

BASE = "/home/manuel/.openclaw/workspace/workspaces/erc8004-specialist"
RUN_ID = "2026-03-07_full_analysis"
RAW_DIR = f"{BASE}/working/data/raw/2026-03-07_1220_eth_validation_fix/ethereum_1"
FIG_DIR = f"{BASE}/outbox/figures/{RUN_ID}"
TAB_DIR = f"{BASE}/working/results/tables/{RUN_ID}"
SUM_DIR = f"{BASE}/working/results/summaries/{RUN_ID}"

os.makedirs(FIG_DIR, exist_ok=True)
os.makedirs(TAB_DIR, exist_ok=True)
os.makedirs(SUM_DIR, exist_ok=True)

reg = pd.read_csv(f"{RAW_DIR}/identity_registered.csv")
fb = pd.read_csv(f"{RAW_DIR}/reputation_newfeedback.csv")
tr = pd.read_csv(f"{RAW_DIR}/identity_transfer.csv")

# ------------ Basic audit ------------
audit = {
    "registered_rows": int(len(reg)),
    "registered_agents": int(reg['agentId'].nunique()),
    "feedback_rows": int(len(fb)),
    "feedback_agents": int(fb['agentId'].nunique()),
    "transfer_rows": int(len(tr)),
    "block_min": int(min(reg['blockNumber'].min(), fb['blockNumber'].min() if len(fb) else reg['blockNumber'].min())),
    "block_max": int(max(reg['blockNumber'].max(), fb['blockNumber'].max() if len(fb) else reg['blockNumber'].max())),
}
with open(f"{SUM_DIR}/data_audit_summary.json", "w", encoding="utf-8") as f:
    json.dump(audit, f, indent=2)

# ------------ Figure 1: cumulative activity over blocks ------------
reg_counts = reg.groupby('blockNumber').size().sort_index().cumsum()
fb_counts = fb.groupby('blockNumber').size().sort_index().cumsum() if len(fb) else pd.Series(dtype=float)

plt.figure(figsize=(8,4.5))
plt.plot(reg_counts.index, reg_counts.values, label='Cumulative registrations', linewidth=2)
if len(fb_counts):
    plt.plot(fb_counts.index, fb_counts.values, label='Cumulative feedback events', linewidth=2)
plt.xlabel('Block number')
plt.ylabel('Cumulative count')
plt.title('ERC8004 cumulative activity (Ethereum)')
plt.legend()
plt.tight_layout()
plt.savefig(f"{FIG_DIR}/fig_01_cumulative_activity.pdf")
plt.close()

# ------------ Concentration diagnostics ------------
if len(fb):
    ctab = fb.groupby(['agentId', 'clientAddress']).size().rename('n').reset_index()
    tot = ctab.groupby('agentId')['n'].sum().rename('tot')
    top = ctab.groupby('agentId')['n'].max().rename('top')
    conc = pd.concat([tot, top], axis=1).reset_index()
    conc['top1_share'] = conc['top'] / conc['tot']
    conc.to_csv(f"{TAB_DIR}/feedback_concentration_by_agent.csv", index=False)

    plt.figure(figsize=(7,4.5))
    plt.hist(conc['top1_share'], bins=25)
    plt.xlabel('Top-1 client share per agent')
    plt.ylabel('Number of agents')
    plt.title('Feedback concentration distribution')
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/fig_02_feedback_concentration_hist.pdf")
    plt.close()

    # Lorenz-like curve of client contributions
    client_tot = fb.groupby('clientAddress').size().sort_values(ascending=False)
    w = client_tot.values.astype(float)
    w = w / w.sum()
    cum_clients = np.arange(1, len(w)+1) / len(w)
    cum_feedback = np.cumsum(np.sort(w))

    plt.figure(figsize=(5.8,5.2))
    plt.plot(cum_clients, cum_feedback, label='Empirical')
    plt.plot([0,1],[0,1], '--', label='Equality')
    plt.xlabel('Client percentile')
    plt.ylabel('Cumulative feedback share')
    plt.title('Client contribution concentration (Lorenz-style)')
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/fig_03_client_concentration_lorenz.pdf")
    plt.close()

# ------------ Dynamics: time-to-first-feedback ------------
first_reg = reg.groupby('agentId')['blockNumber'].min().rename('reg_block')
if len(fb):
    first_fb = fb.groupby('agentId')['blockNumber'].min().rename('fb_block')
    ttf = pd.concat([first_reg, first_fb], axis=1, join='inner').dropna().reset_index()
    ttf['ttf_blocks'] = ttf['fb_block'] - ttf['reg_block']
    ttf = ttf[ttf['ttf_blocks'] >= 0]
    ttf['ttf_days_approx'] = ttf['ttf_blocks'] * 12.0 / 86400.0
    ttf.to_csv(f"{TAB_DIR}/time_to_first_feedback.csv", index=False)

    plt.figure(figsize=(7,4.5))
    plt.hist(ttf['ttf_days_approx'], bins=40)
    plt.xlabel('Time to first feedback (approx days, 12s/block)')
    plt.ylabel('Number of agents')
    plt.title('Distribution of time-to-first-feedback')
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/fig_04_time_to_first_feedback_days.pdf")
    plt.close()

# ------------ Robustness check: tag distribution ------------
if len(fb) and 'tag1' in fb.columns:
    tag = fb['tag1'].fillna('NA').astype(str)
    top_tags = tag.value_counts().head(12)
    top_tags.to_csv(f"{TAB_DIR}/feedback_tag1_top12.csv", header=['count'])

    plt.figure(figsize=(8.2,4.8))
    plt.bar(top_tags.index, top_tags.values)
    plt.xticks(rotation=35, ha='right')
    plt.ylabel('Count')
    plt.title('Top feedback tag1 categories')
    plt.tight_layout()
    plt.savefig(f"{FIG_DIR}/fig_05_feedback_tag1_top12.pdf")
    plt.close()

# Save quick metrics summary
summary = {
    "agents_registered": int(reg['agentId'].nunique()),
    "agents_with_feedback": int(fb['agentId'].nunique()) if len(fb) else 0,
    "feedback_events": int(len(fb)),
}
if len(fb):
    summary["feedback_coverage_ratio"] = float(summary["agents_with_feedback"] / max(1, summary["agents_registered"]))

    ctab = fb.groupby(['agentId', 'clientAddress']).size().rename('n').reset_index()
    tot = ctab.groupby('agentId')['n'].sum().rename('tot')
    top = ctab.groupby('agentId')['n'].max().rename('top')
    conc = pd.concat([tot, top], axis=1)
    conc['top1_share'] = conc['top'] / conc['tot']
    summary["median_top1_share"] = float(conc['top1_share'].median())
    summary["mean_top1_share"] = float(conc['top1_share'].mean())

with open(f"{SUM_DIR}/key_metrics_summary.json", "w", encoding='utf-8') as f:
    json.dump(summary, f, indent=2)

print('FULL_ANALYSIS_DONE')
print('FIG_DIR=', FIG_DIR)
print('TAB_DIR=', TAB_DIR)
print('SUM_DIR=', SUM_DIR)
