import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path('/home/manuel/.openclaw/workspace/workspaces/erc8004-specialist')
SRC = BASE / 'working/data/raw/2026-03-07_1220_eth_validation_fix/ethereum_1/reputation_newfeedback.csv'
TAB = BASE / 'working/results/tables/2026-03-08_client_temporal'
FIG = BASE / 'outbox/figures/2026-03-08_client_temporal'
OUTBOX = BASE / 'outbox'
TAB.mkdir(parents=True, exist_ok=True)
FIG.mkdir(parents=True, exist_ok=True)

BIN = 1000
DROP_THR = 20000
WINDOW_BINS = 5

# Load
df = pd.read_csv(SRC, usecols=['clientAddress', 'blockNumber', 'agentId']).dropna()
df['clientAddress'] = df['clientAddress'].astype(str).str.lower()
df['blockNumber'] = df['blockNumber'].astype(int)
df = df.sort_values(['clientAddress', 'blockNumber'])

min_b, max_b = int(df['blockNumber'].min()), int(df['blockNumber'].max())
df['bin'] = ((df['blockNumber'] - min_b) // BIN).astype(int)

# 1) client_time_series_by_blockbin.csv
ts = df.groupby(['clientAddress', 'bin']).size().reset_index(name='count')
ts['bin_start_block'] = min_b + ts['bin'] * BIN
ts['bin_size_blocks'] = BIN
ts.to_csv(TAB / 'client_time_series_by_blockbin.csv', index=False)

# 2) client_interevent_stats.csv
inter_rows = []
for c, g in df.groupby('clientAddress'):
    b = g['blockNumber'].values
    if len(b) < 2:
        continue
    gaps = np.diff(b)
    mean_gap = float(np.mean(gaps))
    med_gap = float(np.median(gaps))
    cv = float(np.std(gaps) / mean_gap) if mean_gap > 0 else np.nan
    burst = float((np.std(gaps) - np.mean(gaps)) / (np.std(gaps) + np.mean(gaps))) if (np.std(gaps) + np.mean(gaps)) > 0 else np.nan
    inter_rows.append([c, mean_gap, med_gap, cv, burst, len(gaps)])
inter = pd.DataFrame(inter_rows, columns=['clientAddress','mean_interevent_gap','median_interevent_gap','cv_interevent_gap','burstiness_proxy','n_gaps'])
inter.to_csv(TAB / 'client_interevent_stats.csv', index=False)

# 3) client_lifetime_stats.csv
life = df.groupby('clientAddress').agg(
    first_block=('blockNumber', 'min'),
    last_block=('blockNumber', 'max'),
    total_feedback=('blockNumber', 'size')
).reset_index()
life['active_span_blocks'] = life['last_block'] - life['first_block']
life.to_csv(TAB / 'client_lifetime_stats.csv', index=False)

# 4) client_burst_metrics.csv
pivot = ts.pivot(index='clientAddress', columns='bin', values='count').fillna(0)
roll = pivot.rolling(window=WINDOW_BINS, axis=1, min_periods=1).sum()
peak_window = roll.max(axis=1)
avg_rate = pivot.sum(axis=1) / np.maximum(1, pivot.shape[1])
burst = pd.DataFrame({
    'clientAddress': pivot.index,
    'peak_count_window': peak_window.values,
    'avg_rate': avg_rate.values,
    'peak_over_avg': (peak_window.values / np.maximum(1e-9, avg_rate.values))
})
burst.to_csv(TAB / 'client_burst_metrics.csv', index=False)

# 5) client_behavior_clusters.csv
m = life.merge(burst, on='clientAddress', how='left')
m['inactive_after_peak'] = (max_b - m['last_block'] >= DROP_THR)

def label(row):
    if row['peak_over_avg'] >= 4 and row['inactive_after_peak']:
        return 'whale_dormant'
    if row['peak_over_avg'] >= 4:
        return 'sprinter'
    if row['active_span_blocks'] >= 50000 and row['peak_over_avg'] < 2:
        return 'steady'
    return 'episodic'

m['label'] = m.apply(label, axis=1)
clusters = m[['clientAddress','label']]
clusters.to_csv(TAB / 'client_behavior_clusters.csv', index=False)

# 6) client_dropout_flags.csv
drop = m[['clientAddress','inactive_after_peak']].copy()
drop['dropout_threshold_blocks'] = DROP_THR
drop.to_csv(TAB / 'client_dropout_flags.csv', index=False)

# FIGURES
# top clients by total feedback
top50 = life.sort_values('total_feedback', ascending=False).head(50)['clientAddress'].tolist()
heat = ts[ts['clientAddress'].isin(top50)].copy()
heat_p = heat.pivot(index='clientAddress', columns='bin', values='count').fillna(0)
heat_p = heat_p.reindex(top50)
plt.figure(figsize=(11,8))
plt.imshow(heat_p.values, aspect='auto', interpolation='nearest')
plt.colorbar(label='count')
plt.yticks(range(len(heat_p.index)), heat_p.index, fontsize=6)
plt.xlabel(f'bin (size={BIN} blocks)')
plt.ylabel('clientAddress (top50)')
plt.title('Client activity heatmap top50')
plt.tight_layout()
plt.savefig(FIG / 'client_activity_heatmap_top50.pdf', bbox_inches='tight')
plt.close()

# cumulative top20
top20 = life.sort_values('total_feedback', ascending=False).head(20)['clientAddress'].tolist()
cum_df = ts[ts['clientAddress'].isin(top20)].copy()
cum_df = cum_df.sort_values(['clientAddress','bin'])
cum_df['cum'] = cum_df.groupby('clientAddress')['count'].cumsum()
plt.figure(figsize=(10,6))
for c, g in cum_df.groupby('clientAddress'):
    plt.plot(g['bin'], g['cum'], linewidth=1)
plt.xlabel(f'bin (size={BIN} blocks)')
plt.ylabel('cumulative feedback')
plt.title('Client cumulative feedback top20')
plt.tight_layout()
plt.savefig(FIG / 'client_cumulative_feedback_top20.pdf', bbox_inches='tight')
plt.close()

# interevent distribution
if len(inter):
    plt.figure(figsize=(8,5))
    plt.hist(inter['mean_interevent_gap'], bins=40)
    plt.xlabel('mean inter-event gap (blocks)')
    plt.ylabel('clients')
    plt.title('Client interevent distribution')
    plt.tight_layout()
    plt.savefig(FIG / 'client_interevent_distribution.pdf', bbox_inches='tight')
    plt.close()

# peak vs lifetime
plt.figure(figsize=(8,5))
plt.scatter(m['active_span_blocks'], m['peak_count_window'], alpha=0.5, s=12)
plt.xlabel('active span (blocks)')
plt.ylabel('peak_count_window')
plt.title('Client peak vs lifetime')
plt.tight_layout()
plt.savefig(FIG / 'client_peak_vs_lifetime_scatter.pdf', bbox_inches='tight')
plt.close()

# cluster distribution
cd = clusters['label'].value_counts()
plt.figure(figsize=(7,4))
plt.bar(cd.index, cd.values)
plt.ylabel('clients')
plt.title('Client behavior cluster distribution')
plt.tight_layout()
plt.savefig(FIG / 'client_behavior_cluster_distribution.pdf', bbox_inches='tight')
plt.close()

# technical note
note = OUTBOX / 'CLIENT_TEMPORAL_DYNAMICS_TECHNICAL_2026-03-08.md'
note.write_text(
    "# CLIENT TEMPORAL DYNAMICS — Technical Delivery\n\n"
    "## Method\n"
    f"- Source: `{SRC}`\n"
    f"- Bin size: {BIN} blocks\n"
    f"- Dropout threshold: {DROP_THR} blocks\n"
    f"- Peak window: {WINDOW_BINS} bins\n\n"
    "## Outputs\n"
    "- Tables in `working/results/tables/2026-03-08_client_temporal/`\n"
    "- Figures in `outbox/figures/2026-03-08_client_temporal/`\n\n"
    "## QA\n"
    "- Time-series non-empty with bin metadata\n"
    "- Inter-event stats only for clients with >=2 events\n"
    "- Deterministic cluster labels\n"
    "- Dropout flags include threshold column\n\n"
    "## Computational limits\n"
    "- Block-based time proxy; no wall-clock conversion in this run.\n"
)

print('DONE client temporal full pack')
