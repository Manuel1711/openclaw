import os, json
import requests
from datetime import datetime, timezone
from collections import Counter, defaultdict
from itertools import combinations

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
from scipy.cluster.hierarchy import linkage, dendrogram

from tag_source import default_tag_paths, normalize_tag, canonicalize_tag, classify_tag1

P = default_tag_paths(raw_rel='2026-03-07_1220_eth_validation_fix/ethereum_1', out_rel='tag')
ROOT = P['root']
INCSV = P['incsv']
OUT_RESULTS = P['out_results']
OUT_TABLES = P['out_tables']
OUT_FIGS = P['out_figs']
os.makedirs(OUT_TABLES, exist_ok=True)
os.makedirs(OUT_FIGS, exist_ok=True)


def classify_tag1_llm_batch(tags):
    api_key = os.getenv('OPENROUTER_API_KEY') or os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise RuntimeError('Missing OPENROUTER_API_KEY/OPENAI_API_KEY for Codex classification')

    base_url = os.getenv('OPENAI_BASE_URL', 'https://openrouter.ai/api/v1').rstrip('/')
    model = os.getenv('TAG_LLM_MODEL', 'openai-codex/gpt-5.3-codex')
    url = f"{base_url}/chat/completions"

    system_prompt = (
        "Classify each tag into exactly one category id: "
        "1=Characteristic(not adjective), "
        "2=WorkArea(not adjective, action/interest area), "
        "3=AdjectiveOpinion(single-word or phrase evaluation), "
        "4=Unclassified(none of previous). "
        "Return ONLY JSON object: {\"items\":[{\"tag\":\"...\",\"category_id\":1|2|3|4}]}."
    )
    user_prompt = "Tags to classify:\n" + "\n".join(tags)

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    payload = {
        'model': model,
        'temperature': 0,
        'response_format': {'type': 'json_object'},
        'messages': [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt}
        ]
    }

    resp = requests.post(url, headers=headers, json=payload, timeout=120)
    resp.raise_for_status()
    data = resp.json()
    content = data['choices'][0]['message']['content']
    parsed = json.loads(content)

    out = {}
    for item in parsed.get('items', []):
        tag = canonicalize_tag(item.get('tag', ''))
        cid = int(item.get('category_id', 4))
        out[tag] = cid
    return out


raw = pd.read_csv(INCSV)
for c in ['tag1', 'tag2']:
    raw[c] = raw[c].fillna('').astype(str).apply(canonicalize_tag)

# tag1 completeness (requested: include empty-field count)
n_total_rows = int(len(raw))
n_tag1_empty = int((raw['tag1'] == '').sum())
n_tag1_nonempty = n_total_rows - n_tag1_empty
completeness_df = pd.DataFrame([
    {'status': 'tag1_nonempty', 'count': n_tag1_nonempty, 'share': n_tag1_nonempty / max(1, n_total_rows)},
    {'status': 'tag1_empty', 'count': n_tag1_empty, 'share': n_tag1_empty / max(1, n_total_rows)},
])
completeness_df.to_csv(f'{OUT_TABLES}/tag1_field_completeness.csv', index=False)

# Build per-feedback tags for legacy co-occurrence figures
rows=[]
for _,r in raw.iterrows():
    tags=[]
    if r['tag1']: tags.append(r['tag1'])
    if r['tag2']: tags.append(r['tag2'])
    tags=sorted(set([t for t in tags if t]))
    if tags:
        rows.append({'tags':tags})

freq=Counter()
contexts=defaultdict(set)
for i,row in enumerate(rows):
    for t in row['tags']:
        freq[t]+=1
        contexts[t].add(i)

inv_df=pd.DataFrame([
    {'tag':t,'frequency':int(c),'n_contexts':int(len(contexts[t])),'example_1':'','example_2':''}
    for t,c in freq.items()
]).sort_values(['frequency','tag'], ascending=[False,True])
if inv_df.empty:
    inv_df=pd.DataFrame(columns=['tag','frequency','n_contexts','example_1','example_2'])
inv_df.to_csv(f'{OUT_TABLES}/tag_inventory.csv', index=False)

co=Counter()
for row in rows:
    for a,b in combinations(row['tags'],2):
        co[(a,b)] += 1
N=max(1,len(rows))
co_rows=[]
for (a,b),cnt in co.items():
    pa=freq[a]/N; pb=freq[b]/N; pab=cnt/N
    pmi=np.log((pab+1e-9)/((pa*pb)+1e-9))
    co_rows.append({'tag_a':a,'tag_b':b,'cooccurrence_count':int(cnt),'assoc_score':float(pmi)})
co_df=pd.DataFrame(co_rows)
if co_df.empty:
    co_df=pd.DataFrame(columns=['tag_a','tag_b','cooccurrence_count','assoc_score'])
else:
    co_df=co_df.sort_values(['cooccurrence_count','assoc_score'], ascending=[False,False])
co_df.to_csv(f'{OUT_TABLES}/tag_cooccurrence.csv', index=False)

# New clustering requested by Manuel: multi-label 3-family categorization on tag1
tag1_freq = raw[raw['tag1']!='']['tag1'].value_counts().rename_axis('tag').reset_index(name='frequency')
if tag1_freq.empty:
    tag1_freq = pd.DataFrame(columns=['tag','frequency'])

mem_rows=[]
tags_for_llm = [canonicalize_tag(t) for t in tag1_freq['tag'].tolist()]
try:
    llm_map = classify_tag1_llm_batch(tags_for_llm)
except Exception:
    llm_map = None

for _,r in tag1_freq.iterrows():
    tag = canonicalize_tag(r['tag'])

    if llm_map is not None:
        cid = int(llm_map.get(tag, 4))
        is_spec = int(cid == 1)
        is_domain = int(cid == 2)
        is_eval = int(cid == 3)
        if cid == 1:
            label = 'Characteristic to evaluate (no adjectives)'
        elif cid == 2:
            label = 'Work area (no adjectives)'
        elif cid == 3:
            label = 'Adjectives only'
        else:
            label = 'Unclassified'
        version = 'v5_codex_four_category'
    else:
        cls = classify_tag1(tag)
        is_spec = cls['is_value_spec_dimension']
        is_domain = cls['is_bot_domain_area']
        is_eval = cls['is_verbal_evaluation']
        label = cls['assigned_labels']
        version = 'v6_bot_curated_rules'

    mem_rows.append({
        'tag': tag,
        'frequency': int(r['frequency']),
        'is_value_spec_dimension': is_spec,
        'is_bot_domain_area': is_domain,
        'is_verbal_evaluation': is_eval,
        'assigned_labels': label,
        'rule_version': version
    })

membership_df = pd.DataFrame(mem_rows).sort_values(['frequency','tag'], ascending=[False,True])
if membership_df.empty:
    membership_df = pd.DataFrame(columns=['tag','frequency','is_value_spec_dimension','is_bot_domain_area','is_verbal_evaluation','assigned_labels','rule_version'])
membership_df.to_csv(f'{OUT_TABLES}/tag1_category_membership.csv', index=False)

summary_rows = [
    {
        'category': 'Characteristic to evaluate (no adjectives)',
        'frequency': int(membership_df.loc[membership_df['is_value_spec_dimension']==1, 'frequency'].sum())
    },
    {
        'category': 'Work area (no adjectives)',
        'frequency': int(membership_df.loc[membership_df['is_bot_domain_area']==1, 'frequency'].sum())
    },
    {
        'category': 'Adjectives only',
        'frequency': int(membership_df.loc[membership_df['is_verbal_evaluation']==1, 'frequency'].sum())
    },
    {
        'category': 'Unclassified (none of the above)',
        'frequency': int(membership_df.loc[membership_df['assigned_labels']=='Unclassified', 'frequency'].sum())
    }
]
summary_df = pd.DataFrame(summary_rows).sort_values('frequency', ascending=False)
summary_df.to_csv(f'{OUT_TABLES}/tag1_category_summary.csv', index=False)

# overlap summary
ov = membership_df.copy()
ov['overlap_count'] = ov[['is_value_spec_dimension','is_bot_domain_area','is_verbal_evaluation']].sum(axis=1)
overlap_df = ov.groupby('overlap_count', as_index=False)['frequency'].sum().sort_values('overlap_count')
overlap_df.to_csv(f'{OUT_TABLES}/tag1_category_overlap_summary.csv', index=False)

# cluster map json now mirrors 4 categories
cluster_map = []
for cid, cat in enumerate(['Characteristic to evaluate (no adjectives)', 'Work area (no adjectives)', 'Adjectives only', 'Unclassified']):
    if cat == 'Characteristic to evaluate (no adjectives)':
        mask = membership_df['is_value_spec_dimension']==1
    elif cat == 'Work area (no adjectives)':
        mask = membership_df['is_bot_domain_area']==1
    elif cat == 'Adjectives only':
        mask = membership_df['is_verbal_evaluation']==1
    else:
        mask = membership_df['assigned_labels']=='Unclassified'
    tags = membership_df.loc[mask].sort_values('frequency', ascending=False)['tag'].tolist()
    cluster_map.append({
        'cluster_id': cid,
        'cluster_label': cat,
        'cluster_definition': f'Manual semantic family with overlap enabled: {cat}',
        'tags': tags,
        'candidate_aliases': [],
        'borderline_tags': [],
        'confidence': 0.82
    })
with open(f'{OUT_TABLES}/cluster_map_v1.json','w') as f:
    json.dump(cluster_map, f, indent=2)

plt.rcParams['pdf.fonttype']=42

# fig01 cooccurrence network
plt.figure(figsize=(7,5))
if not co_df.empty:
    top=co_df.head(min(25,len(co_df)))
    uniq=sorted(set(top['tag_a']).union(set(top['tag_b'])))
    theta=np.linspace(0,2*np.pi,len(uniq),endpoint=False)
    pos={t:(np.cos(a),np.sin(a)) for t,a in zip(uniq,theta)}
    for _,r in top.iterrows():
        x1,y1=pos[r['tag_a']]; x2,y2=pos[r['tag_b']]
        lw=0.5+2.5*(r['cooccurrence_count']/max(1,top['cooccurrence_count'].max()))
        plt.plot([x1,x2],[y1,y2],alpha=0.35,color='tab:blue',linewidth=lw)
    sizes=[80+25*freq[t] for t in uniq]
    plt.scatter([pos[t][0] for t in uniq],[pos[t][1] for t in uniq],s=sizes,c='tab:orange',alpha=0.9)
    for t in uniq:
        plt.text(pos[t][0],pos[t][1],t,fontsize=8,ha='center',va='center')
else:
    plt.text(0.5,0.5,'No co-occurrence edges found',ha='center',va='center')
plt.axis('off'); plt.title('Tag Co-occurrence Network (top edges)'); plt.tight_layout()
plt.savefig(f'{OUT_FIGS}/fig01_cooccurrence_network.pdf'); plt.close()

# fig02 heatmap
plt.figure(figsize=(8,6))
tags = inv_df['tag'].tolist()
if len(tags)>=1:
    idx={t:i for i,t in enumerate(tags)}
    M=np.zeros((len(tags),len(tags)))
    for _,r in co_df.iterrows():
        if r['tag_a'] in idx and r['tag_b'] in idx:
            i,j=idx[r['tag_a']],idx[r['tag_b']]
            M[i,j]=M[j,i]=r['cooccurrence_count']
    np.fill_diagonal(M, [freq[t] for t in tags])
    plt.imshow(M, cmap='viridis')
    plt.colorbar(label='count')
    plt.xticks(range(len(tags)), tags, rotation=90, fontsize=7)
    plt.yticks(range(len(tags)), tags, fontsize=7)
    plt.title('Tag Context/Co-occurrence Heatmap')
else:
    plt.text(0.5,0.5,'No tags',ha='center')
plt.tight_layout(); plt.savefig(f'{OUT_FIGS}/fig02_tag_context_heatmap.pdf'); plt.close()

# fig03 dendrogram (lexical)
plt.figure(figsize=(8,5))
if len(tags)>=2:
    vec=TfidfVectorizer(ngram_range=(1,2), min_df=1)
    X=vec.fit_transform(tags).toarray()
    Z=linkage(X, method='ward', metric='euclidean')
    dendrogram(Z, labels=tags, leaf_rotation=90, leaf_font_size=8)
    plt.title('Tag Dendrogram (lexical)')
else:
    plt.text(0.5,0.5,'Insufficient tags for dendrogram',ha='center')
plt.tight_layout(); plt.savefig(f'{OUT_FIGS}/fig03_dendrogram.pdf'); plt.close()

# fig04 embedding
plt.figure(figsize=(7,5))
if len(tags)>=2:
    vec=TfidfVectorizer(ngram_range=(1,2), min_df=1)
    X=vec.fit_transform(tags).toarray()
    if len(tags) >= 3:
        best_k=2; best_s=-1
        for k in range(2, min(6, len(tags)-1)+1):
            try:
                lab=AgglomerativeClustering(n_clusters=k, metric='euclidean', linkage='ward').fit_predict(X)
                s=silhouette_score(X, lab, metric='euclidean')
                if s>best_s: best_s=s; best_k=k
            except Exception:
                pass
        labels=AgglomerativeClustering(n_clusters=best_k, metric='euclidean', linkage='ward').fit_predict(X)
    else:
        labels=np.zeros(len(tags), dtype=int)
    emb=PCA(n_components=2, random_state=42).fit_transform(X)
    for cid in sorted(set(labels.tolist())):
        pts=emb[labels==cid]
        plt.scatter(pts[:,0],pts[:,1],label=f'cluster {cid}',alpha=0.8)
    for (x,y),t in zip(emb,tags):
        plt.text(x,y,t,fontsize=8)
    plt.legend(fontsize=8)
    plt.title('Tag Embedding (PCA proxy for UMAP)')
else:
    plt.text(0.5,0.5,'Insufficient tags for embedding',ha='center')
plt.tight_layout(); plt.savefig(f'{OUT_FIGS}/fig04_embedding_umap.pdf'); plt.close()

# fig06 (reused filename): words per requested 3 families with overlaps
families = [
    ('Characteristic to evaluate (no adjectives)', 'is_value_spec_dimension', 'tab:blue', False),
    ('Work area (no adjectives)', 'is_bot_domain_area', 'tab:orange', False),
    ('Adjectives only', 'is_verbal_evaluation', 'tab:green', False),
    ('Unclassified', None, 'tab:gray', True),
]
total_bars = 0
for _, col, _, is_unclassified in families:
    if membership_df.empty:
        continue
    if is_unclassified:
        total_bars += int((membership_df['assigned_labels']=='Unclassified').sum())
    else:
        total_bars += int((membership_df[col]==1).sum())
fig_h = max(12, min(60, 0.22 * total_bars))
fig, axes = plt.subplots(nrows=4, ncols=1, figsize=(10, fig_h), squeeze=False)
ov_idx = ov.set_index('tag') if not ov.empty else pd.DataFrame()
for i, (title, col, color, is_unclassified) in enumerate(families):
    ax = axes[i,0]
    if is_unclassified:
        sub = membership_df[membership_df['assigned_labels']=='Unclassified'].sort_values('frequency', ascending=True)
    else:
        sub = membership_df[membership_df[col]==1].sort_values('frequency', ascending=True)
    if sub.empty:
        ax.text(0.5,0.5,'No tags',ha='center',va='center')
        ax.set_title(title)
        continue
    labels = list(sub['tag'])
    ax.barh(labels, sub['frequency'], color=color, alpha=0.85)
    ax.set_title(f'{title} — all tag1 words')
    ax.set_xlabel('Occurrences')
    ax.tick_params(axis='y', labelsize=7)
fig.suptitle('Tag1 clustering requested for product navigation (all tags + unclassified)', fontsize=12)
plt.tight_layout(rect=[0,0,1,0.98])
plt.savefig(f'{OUT_FIGS}/fig06_tag1_macroarea_distribution.pdf'); plt.close()

# fig07 (upgraded): temporal heatmap of tag1 completeness/category shares over block bins
label_map = dict(zip(membership_df['tag'], membership_df['assigned_labels']))
raw_plot = raw.copy()
raw_plot['tag1_label'] = raw_plot['tag1'].map(label_map)
raw_plot.loc[raw_plot['tag1'] == '', 'tag1_label'] = 'Tag1 empty'
raw_plot.loc[(raw_plot['tag1'] != '') & (raw_plot['tag1_label'].isna()), 'tag1_label'] = 'Unclassified'
raw_plot['blockNumber'] = pd.to_numeric(raw_plot.get('blockNumber', np.nan), errors='coerce')

cats_ord = [
    'Tag1 empty',
    'Unclassified',
    'Work area (no adjectives)',
    'Adjectives only',
    'Characteristic to evaluate (no adjectives)',
]

if raw_plot['blockNumber'].notna().sum() >= 30:
    rb = raw_plot.dropna(subset=['blockNumber']).copy()
    n_bins = min(28, max(10, int(np.sqrt(len(rb)) // 2)))
    rb['bin'] = pd.qcut(rb['blockNumber'], q=n_bins, duplicates='drop')
    grp = rb.groupby(['bin', 'tag1_label']).size().unstack(fill_value=0)
    grp = grp.reindex(columns=cats_ord, fill_value=0)
    shares = grp.div(grp.sum(axis=1), axis=0).fillna(0.0)

    fig, (ax_top, ax_heat) = plt.subplots(2, 1, figsize=(11, 5.8), gridspec_kw={'height_ratios':[1.1, 2.2]})
    x = np.arange(len(shares))
    ax_top.plot(x, shares['Tag1 empty'].values, color='#6c757d', linewidth=2.2, label='Tag1 empty share')
    ax_top.fill_between(x, 0, shares['Tag1 empty'].values, color='#6c757d', alpha=0.18)
    ax_top.set_ylim(0, max(0.2, shares['Tag1 empty'].max()*1.15))
    ax_top.set_ylabel('Share')
    ax_top.legend(frameon=False, loc='upper right')

    M = shares[cats_ord].to_numpy().T
    im = ax_heat.imshow(M, aspect='auto', cmap='viridis', vmin=0, vmax=max(0.35, M.max()))
    ax_heat.set_yticks(np.arange(len(cats_ord)))
    ax_heat.set_yticklabels(['Empty', 'Unclassified', 'Work area', 'Adjectives', 'Characteristic'])
    ax_heat.set_xlabel('Block-quantile bin index (early → late)')
    ax_heat.set_xticks(np.linspace(0, len(shares)-1, num=min(8, len(shares))).astype(int))
    cbar = plt.colorbar(im, ax=ax_heat, fraction=0.02, pad=0.02)
    cbar.set_label('Within-bin share')
    plt.tight_layout()
    plt.savefig(f'{OUT_FIGS}/fig07_tag1_field_completeness.pdf'); plt.close()
else:
    plt.figure(figsize=(7.2, 4.6))
    vals = completeness_df.set_index('status').reindex(['tag1_nonempty', 'tag1_empty'])['count'].fillna(0).astype(int)
    bars = plt.bar(['Tag1 non-empty', 'Tag1 empty'], vals.values, color=['#2a9d8f', '#9aa0a6'], alpha=0.9)
    for b, v in zip(bars, vals.values):
        plt.text(b.get_x() + b.get_width()/2, v, f'{int(v):,}', ha='center', va='bottom', fontsize=10)
    plt.ylabel('Rows')
    plt.title('Tag1 field completeness')
    plt.tight_layout()
    plt.savefig(f'{OUT_FIGS}/fig07_tag1_field_completeness.pdf'); plt.close()

# fig08 (upgraded): Marimekko-style composition with explicit empty vs non-empty split
cat_counts = {
    'Characteristic': int(membership_df.loc[membership_df['assigned_labels']=='Characteristic to evaluate (no adjectives)', 'frequency'].sum()),
    'Work area': int(membership_df.loc[membership_df['assigned_labels']=='Work area (no adjectives)', 'frequency'].sum()),
    'Adjectives': int(membership_df.loc[membership_df['assigned_labels']=='Adjectives only', 'frequency'].sum()),
    'Unclassified': int(membership_df.loc[membership_df['assigned_labels']=='Unclassified', 'frequency'].sum()),
}
N_total = max(1, n_total_rows)
w_nonempty = n_tag1_nonempty / N_total
w_empty = n_tag1_empty / N_total
inner_order = ['Characteristic', 'Adjectives', 'Work area', 'Unclassified']
inner_colors = {'Characteristic':'#457b9d','Adjectives':'#2a9d8f','Work area':'#f4a261','Unclassified':'#8d99ae'}

fig, ax = plt.subplots(figsize=(10.5, 4.8))
# non-empty column (left)
ax.add_patch(plt.Rectangle((0,0), w_nonempty, 1, facecolor='white', edgecolor='black', linewidth=1.0))
y0 = 0.0
for k in inner_order:
    h = cat_counts[k] / max(1, n_tag1_nonempty)
    ax.add_patch(plt.Rectangle((0, y0), w_nonempty, h, facecolor=inner_colors[k], edgecolor='white', linewidth=1.2))
    if h > 0.08:
        ax.text(w_nonempty*0.5, y0 + h/2, f"{k}\n{cat_counts[k]:,} ({100*h:.1f}% of non-empty)",
                ha='center', va='center', fontsize=9, color='white' if k!='Work area' else 'black')
    y0 += h

# empty column (right)
ax.add_patch(plt.Rectangle((w_nonempty,0), w_empty, 1, facecolor='#bdbdbd', edgecolor='black', linewidth=1.0))
ax.text(w_nonempty + w_empty/2, 0.5, f"Tag1 empty\n{n_tag1_empty:,}\n({100*w_empty:.1f}% of all rows)",
        ha='center', va='center', fontsize=9)

# cosmetics
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_xticks([w_nonempty/2, w_nonempty + w_empty/2])
ax.set_xticklabels(['Non-empty tag1 block', 'Empty tag1 block'])
ax.set_yticks([])
ax.set_xlabel('Width = share over all feedback rows')
plt.tight_layout()
plt.savefig(f'{OUT_FIGS}/fig08_tag1_composition_including_empty.pdf'); plt.close()

# fig09: principal tag1 terms by category (Top-N per class)
N_TOP = 12
cats = [
    ('Characteristic to evaluate (no adjectives)', '#457b9d'),
    ('Adjectives only', '#2a9d8f'),
    ('Work area (no adjectives)', '#f4a261'),
    ('Unclassified', '#8d99ae'),
]
fig, axes = plt.subplots(2, 2, figsize=(12, 8), squeeze=False)
for ax, (cat, col) in zip(axes.flatten(), cats):
    sub = membership_df[membership_df['assigned_labels'] == cat].nlargest(N_TOP, 'frequency').copy()
    if sub.empty:
        ax.text(0.5, 0.5, 'No tags', ha='center', va='center')
        ax.set_xticks([]); ax.set_yticks([])
        continue
    sub = sub.sort_values('frequency', ascending=True)
    ax.barh(sub['tag'], sub['frequency'], color=col, alpha=0.9)
    ax.set_ylabel(cat.replace(' (no adjectives)',''))
    ax.tick_params(axis='y', labelsize=8)
    for y, v in enumerate(sub['frequency'].tolist()):
        ax.text(v, y, f' {int(v)}', va='center', ha='left', fontsize=8)
for ax in axes[1, :]:
    ax.set_xlabel('Occurrences')
plt.tight_layout()
plt.savefig(f'{OUT_FIGS}/fig09_tag1_top_terms_by_category.pdf'); plt.close()

# summary
ts=datetime.now(timezone.utc).isoformat()
with open(f'{OUT_RESULTS}/summaries/phase1_summary.md','w') as f:
    f.write('# Tag Clustering Phase 1 — Summary (v2)\n\n')
    f.write(f'- Timestamp (UTC): {ts}\n')
    f.write('- Scope: tag1 clustering into three semantic families with overlap support.\n')
    f.write(f'- Tag1 unique labels: {tag1_freq.shape[0]}\n')
    f.write('- Families: Value-specification dimension / Bot domain-area / Verbal evaluation\n')
    f.write('- Tables: tag1_category_membership.csv, tag1_category_summary.csv, tag1_category_overlap_summary.csv, tag1_field_completeness.csv, cluster_map_v1.json\n')
    f.write('- Figures added: fig07_tag1_field_completeness.pdf, fig08_tag1_composition_including_empty.pdf, fig09_tag1_top_terms_by_category.pdf\n')

print('DONE', OUT_RESULTS)
