#!/usr/bin/env bash
set -euo pipefail
BASE="/home/manuel/.openclaw/workspace/workspaces/erc8004-specialist"
OUT="$BASE/outbox"
TS=$(date +%F_%H%M%S)
ARCH="$BASE/archive/outbox/auto_$TS"
mkdir -p "$ARCH"

# Keep ACTIVE files declared in outbox/ACTIVE.list if present
if [ -f "$OUT/ACTIVE.list" ]; then
  mapfile -t KEEP < "$OUT/ACTIVE.list"
else
  KEEP=(
    "INDEX.md"
    "ERC8004_FULL_ANALYSIS_REPORT_2026-03-07.md"
    "ERC8004_FIGURE_BOOK_2026-03-07.md"
    "ERC8004_INTERPRETIVE_NOTES_2026-03-07.md"
    "ERC8004_figures_2026-03-07_full_analysis.zip"
    "figures"
  )
fi

for f in "$OUT"/*; do
  bn=$(basename "$f")
  keepit=0
  for k in "${KEEP[@]}"; do
    [[ "$bn" == "$k" ]] && keepit=1 && break
  done
  [[ $keepit -eq 0 ]] && mv "$f" "$ARCH/"
done

echo "OUTBOX_MAINTAIN_OK archive=$ARCH"
