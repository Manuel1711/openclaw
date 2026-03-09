#!/usr/bin/env bash
set -euo pipefail

BASE="/home/manuel/.openclaw/workspace/workspaces/erc8004-specialist"
CODE="$BASE/working/analysis/data_extraction/code"
LOCK="$BASE/.run_active.lock"
RUN_ID="${1:-$(date +%F_%H%M%S)_eth}"
OUT_DIR="$BASE/working/data/raw/$RUN_ID"
LOG="$BASE/runlogs/${RUN_ID}.log"

python3 "$CODE/preflight_check.py"

if [ -e "$LOCK" ]; then
  echo "RUN_ABORT: lock already exists: $LOCK"
  exit 10
fi

echo "pid=$$ run_id=$RUN_ID started=$(date -Is)" > "$LOCK"
cleanup() { rm -f "$LOCK"; }
trap cleanup EXIT

set -a
source "$BASE/working/analysis/data_extraction/config/.env"
set +a
export OUT_DIR
mkdir -p "$OUT_DIR"

python3 "$CODE/collect_erc8004_events.py" 2>&1 | tee "$LOG"

if [ -d "$OUT_DIR/ethereum_1" ]; then
  mkdir -p "$BASE/working/data/latest"
  ln -sfn ../raw/$RUN_ID "$BASE/working/data/latest/raw"
fi

echo "RUN_OK $RUN_ID"
