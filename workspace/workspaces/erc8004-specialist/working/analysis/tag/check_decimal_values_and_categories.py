import pandas as pd

from tag_source import ROOT, attach_category

RAW_CSV = f"{ROOT}/working/data/raw/2026-03-07_1220_eth_validation_fix/ethereum_1/reputation_newfeedback.csv"
MEMBERSHIP_CSV = f"{ROOT}/working/results/tag/tables/tag1_category_membership.csv"


def main():
    raw = pd.read_csv(RAW_CSV)
    membership = pd.read_csv(MEMBERSHIP_CSV)

    raw['value_num'] = pd.to_numeric(raw['value'], errors='coerce')
    raw['value_decimals_num'] = pd.to_numeric(raw['valueDecimals'], errors='coerce')

    # A) valueDecimals > 0 (criterio operativo richiesto)
    nonzero_decimals = raw[raw['value_decimals_num'].fillna(0) > 0].copy()

    # B) value fuori range [0,100] su valore normalizzato da valueDecimals
    scaled = raw['value_num'] / (10 ** raw['value_decimals_num'].fillna(0))
    out_of_range = raw[(scaled < 0) | (scaled > 100)].copy()
    out_of_range['scaled_value'] = scaled[(scaled < 0) | (scaled > 100)]

    # Intersezione A ∩ B
    both = nonzero_decimals.loc[nonzero_decimals.index.intersection(out_of_range.index)].copy()

    # map categories
    nonzero_decimals = attach_category(nonzero_decimals, membership)
    out_of_range = attach_category(out_of_range, membership)
    both = attach_category(both, membership)

    print('=== REQUESTED CHECKS ===')
    print(f'total_rows={len(raw)}')
    print(f'valueDecimals_gt_0={len(nonzero_decimals)}')
    print(f'value_outside_[0,100]_after_scaling={len(out_of_range)}')
    print(f'intersection_valueDecimals_gt_0_AND_out_of_range={len(both)}')

    print('\n=== CATEGORY DISTRIBUTION: valueDecimals > 0 ===')
    print(nonzero_decimals['tag1_category'].value_counts().to_string())

    print('\n=== CATEGORY DISTRIBUTION: value fuori [0,100] ===')
    if len(out_of_range):
        print(out_of_range['tag1_category'].value_counts().to_string())
    else:
        print('none')

    print('\n=== CATEGORY DISTRIBUTION: intersezione ===')
    if len(both):
        print(both['tag1_category'].value_counts().to_string())
    else:
        print('none')

    if len(out_of_range):
        cols = ['blockNumber', 'transactionHash', 'feedbackIndex', 'value', 'valueDecimals', 'scaled_value', 'tag1', 'tag1_category']
        print('\n=== OUT-OF-RANGE ROWS DETAIL ===')
        print(out_of_range[cols].to_string(index=False))


if __name__ == '__main__':
    main()
