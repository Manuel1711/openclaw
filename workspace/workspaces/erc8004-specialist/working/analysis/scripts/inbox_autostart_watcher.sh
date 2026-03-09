#!/usr/bin/env bash
set -euo pipefail

BASE="/home/manuel/.openclaw/workspace/workspaces/erc8004-specialist"
INBOX="$BASE/inbox"
OUTBOX="$BASE/outbox"
LOGDIR="$BASE/logs"
STATE="$BASE/working/.inbox_autostart_state"
TRIG="$BASE/working/triggers"
mkdir -p "$LOGDIR" "$TRIG"

touch "$STATE"

while true; do
  while IFS= read -r task; do
    [ -z "$task" ] && continue
    fname="$(basename "$task")"
    if ! grep -Fxq "$fname" "$STATE"; then
      ts="$(date +%Y-%m-%d_%H%M)"
      ack="$OUTBOX/CP0_ACK_AUTO_${ts}.md"
      printf 'STATUS | STARTED | auto_inbox_trigger | none | CP1_ETA=~90m\nTASK=%s\n' "$fname" > "$ack"
      touch "$TRIG/START_${fname%.md}.flag"
      echo "$(date -Is) AUTO-TRIGGER $fname -> $ack" >> "$LOGDIR/inbox-autostart.log"
      echo "$fname" >> "$STATE"
    fi
  done < <(find "$INBOX" -maxdepth 1 -type f -name 'TASK_*.md' | sort)
  sleep 30
done
