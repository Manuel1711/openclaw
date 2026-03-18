import re
from pathlib import Path
import pandas as pd

ROOT = str(Path(__file__).resolve().parents[3])


def default_tag_paths(raw_rel: str = '2026-03-07_1220_eth_validation_fix/ethereum_1', out_rel: str = 'tag') -> dict:
    """Canonical path builder for tag pipeline.

    Args:
        raw_rel: relative folder under working/data/raw containing chain data
        out_rel: relative folder under working/results for tag outputs
    """
    base = f'{ROOT}/working'
    out_results = f'{base}/results/{out_rel}'
    return {
        'root': ROOT,
        'incsv': f'{base}/data/raw/{raw_rel}/reputation_newfeedback.csv',
        'out_results': out_results,
        'out_tables': f'{out_results}/tables',
        'out_figs': f'{out_results}/figures',
    }


def normalize_tag(s: str) -> str:
    s = '' if s is None else str(s).strip().lower()
    s = s.replace('_', ' ').replace('-', ' ').replace('/', ' ').replace(',', ' ').replace('.', ' ')
    s = re.sub(r'\s+', ' ', s)
    return s


def canonicalize_tag(s: str) -> str:
    t = normalize_tag(s)
    if not t or t == 'nan':
        return ''

    t = re.sub(r'\b([a-z]{3,})\d+\b', r'\1', t)

    typo_map = {
        'gud tek': 'good tech',
        'succesrate': 'successrate',
        'success rate': 'successrate',
        'reliability': 'reliable',
        'chat quality ': 'chat quality',
        'best ai ': 'best ai',
        'powerfull': 'powerful',
        'usefull': 'useful',
        'thrustworthy': 'trustworthy',
        'trustworthy': 'trusted',
        'game changere': 'game changer',
        'gamechanger': 'game changer',
    }
    return typo_map.get(t, t)


def classify_tag1(tag: str):
    t = canonicalize_tag(tag)
    toks = set(t.split())

    adjective_words = {
        'interesting', 'best', 'composable', 'innovative', 'good',
        'great', 'excellent', 'nice', 'inactive', 'bad', 'poor',
        'amazing', 'smart', 'intelligent', 'fast', 'useful',
        'accurate', 'helpful', 'reliable', 'efficient', 'professional',
        'analytical', 'reachable', 'scalable', 'stable', 'secure',
        'okay', 'ok', 'fastest', 'faster', 'slowest', 'slower', 'trusted',
        'smooth', 'friendly', 'user friendly', 'safe', 'powerful',
        'prominent', 'outstanding', 'precise', 'open', 'wonderful',
        'unique', 'transparent', 'convenient', 'cheap', 'beautiful',
        'awesome', 'advanced', 'cool', 'bold', 'based', 'creative',
        'insightful', 'expecting', 'easy to use', 'easy for anybody',
        'gas efficient', 'good value', 'good agent', 'best rates',
        'alpha packed', 'all in one', 'deep research', 'fast analysis',
        'great ui ux', 'great ui/ux', 'ownerverified', 'solid', 'game changer'
    }
    adjective_suffixes = ('ive', 'al', 'ous', 'able', 'ible', 'ful', 'less', 'ic', 'ary', 'est')

    characteristic_words = {
        'quality', 'trust', 'liveness', 'reachability', 'successrate',
        'performance', 'latency', 'security', 'privacy', 'service',
        'overall', 'starred', 'rating', 'availability', 'uptime',
        'satisfaction', 'experience', 'excellence', 'accuracy', 'speed',
        'responsetime', 'value', 'engagement', 'behavior', 'memory',
        'revenues', 'innovation', 'yield'
    }

    domain_words = {
        'oracle', 'screening', 'web', 'a2a', 'x402',
        'optimization', 'portfolio', 'management', 'trading',
        'defi', 'analytics', 'research', 'chat', 'agent',
        'infrastructure', 'automation', 'compliance', 'finance', 'gaming',
        'football', 'sports', 'blockchain', 'web3', 'wallet', 'ai',
        'erc8004', 'erc 8004', 'ecosystem', 'bot', 'task', 'genesis',
        'defai', 'gekko', 'autopilot', 'ai defi', 'ai agent', 'vibe trading',
        'liquidity pools'
    }

    has_adj = (
        (t in adjective_words)
        or (len(toks & adjective_words) > 0)
        or any(tok.endswith(adjective_suffixes) for tok in toks)
    )

    is_eval = False
    is_spec = False
    is_domain = False

    if has_adj:
        is_eval = True
    else:
        has_spec_kw = (t in characteristic_words) or (len(toks & characteristic_words) > 0)
        has_domain_kw = (t in domain_words) or (len(toks & domain_words) > 0)

        if has_spec_kw and not has_domain_kw:
            is_spec = True
        elif has_domain_kw and not has_spec_kw:
            is_domain = True
        elif has_spec_kw and has_domain_kw:
            # keep same tie-break used in current pipeline
            is_domain = True

    if is_eval:
        label = 'Adjectives only'
    elif is_spec:
        label = 'Characteristic to evaluate (no adjectives)'
    elif is_domain:
        label = 'Work area (no adjectives)'
    else:
        label = 'Unclassified'

    return {
        'is_value_spec_dimension': int(is_spec),
        'is_bot_domain_area': int(is_domain),
        'is_verbal_evaluation': int(is_eval),
        'assigned_labels': label
    }


def attach_category(df: pd.DataFrame, membership: pd.DataFrame) -> pd.DataFrame:
    """Attach `tag1_category` using membership mapping and normalized tag1."""
    m = membership.copy()
    m['tag_norm'] = m['tag'].astype(str).map(normalize_tag)
    tag_to_cat = dict(zip(m['tag_norm'], m['assigned_labels']))

    out = df.copy()
    out['tag1_norm'] = out['tag1'].fillna('').astype(str).map(normalize_tag)
    out['tag1_category'] = out['tag1_norm'].map(tag_to_cat)
    out.loc[out['tag1_norm'] == '', 'tag1_category'] = 'Unclassified'
    out['tag1_category'] = out['tag1_category'].fillna('MISSING_IN_MEMBERSHIP')
    return out
