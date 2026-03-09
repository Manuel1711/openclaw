#!/usr/bin/env bash
set -euo pipefail
cd /home/manuel/.openclaw

git add .
git commit -m "chore: snapshot $(date +'%Y-%m-%d %H:%M:%S %Z')" || true

# lightweight secret pre-check on tracked files
if git grep -nE 'sk-[A-Za-z0-9]{20,}|xai-[A-Za-z0-9]{20,}|AIza[0-9A-Za-z\-_]{20,}' -- . >/tmp/openclaw_secret_hits.txt; then
  echo "[BLOCKED] Potential secrets detected in tracked files:" >&2
  cat /tmp/openclaw_secret_hits.txt >&2
  exit 1
fi

git push origin main
