#!/usr/bin/env bash
set -euo pipefail

BASE="/home/manuel/.openclaw/workspace/workspaces/erc8004-specialist"
TRIG="$BASE/working/triggers"
LOGDIR="$BASE/logs"
OUTBOX="$BASE/outbox"
mkdir -p "$TRIG" "$LOGDIR"

run_task() {
  local task_name="$1"
  local ts
  ts="$(date +%Y-%m-%d_%H%M%S)"
  local log="$LOGDIR/runner_${task_name}_${ts}.log"

  if [[ "$task_name" == *"CLIENT_TEMPORAL_DYNAMICS"* ]]; then
    echo "$(date -Is) RUN $task_name -> client_temporal_dynamics.py" >> "$LOGDIR/inbox-trigger-runner.log"
    nohup bash -lc "python3 '$BASE/working/analysis/scripts/client_temporal_dynamics.py' && printf 'CPF_DONE | %s | DONE | %s\n' '$task_name' '$(date +%Y-%m-%d_%H%M)' > '$OUTBOX/CPF_DONE_${task_name}_$(date +%Y-%m-%d).md' && mkdir -p '$BASE/inbox/archive/$(date +%Y-%m-%d)_done' && [ -f '$BASE/inbox/${task_name}.md' ] && mv '$BASE/inbox/${task_name}.md' '$BASE/inbox/archive/$(date +%Y-%m-%d)_done/' && echo "$(date -Is) DONE $task_name" >> '$LOGDIR/inbox-trigger-runner.log'" >"$log" 2>&1 &
  elif [[ "$task_name" == *"Q3_V2_NETWORK_INFERENCE_PACK"* ]]; then
    echo "$(date -Is) RUN $task_name -> q3_v2 pipeline" >> "$LOGDIR/inbox-trigger-runner.log"
    nohup bash -lc "python3 '$BASE/working/analysis/scripts/q3_v2_build_network.py' && python3 '$BASE/working/analysis/scripts/q3_v2_temporal_slices.py' && python3 '$BASE/working/analysis/scripts/q3_v2_null_model.py' && printf 'CPF_DONE | %s | DONE | %s\n' '$task_name' '$(date +%Y-%m-%d_%H%M)' > '$OUTBOX/CPF_DONE_${task_name}_$(date +%Y-%m-%d).md' && mkdir -p '$BASE/inbox/archive/$(date +%Y-%m-%d)_done' && [ -f '$BASE/inbox/${task_name}.md' ] && mv '$BASE/inbox/${task_name}.md' '$BASE/inbox/archive/$(date +%Y-%m-%d)_done/' && echo "$(date -Is) DONE $task_name" >> '$LOGDIR/inbox-trigger-runner.log'" >"$log" 2>&1 &
  else
    echo "$(date -Is) SKIP $task_name (no mapping)" >> "$LOGDIR/inbox-trigger-runner.log"
    printf 'STATUS | NOT_STARTED | no_runner_mapping | %s | CP1_ETA=manual\n' "$task_name" > "$OUTBOX/CP0_ACK_AUTORUN_MISSING_$(date +%Y-%m-%d_%H%M).md"
  fi
}

while true; do
  shopt -s nullglob
  for f in "$TRIG"/START_*.flag; do
    b="$(basename "$f")"
    task="${b#START_}"
    task="${task%.flag}"
    run_task "$task"
    mv "$f" "$TRIG/PROCESSED_${task}_$(date +%s).flag"
  done
  shopt -u nullglob
  sleep 10
done
