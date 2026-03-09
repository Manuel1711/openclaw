# SPEED_PLAN_24H

Status: CP1 STRUCTURE READY (to be finalized by 07:15)

## Goal
Maximize operational speed while preserving report quality and reproducibility.

## KPI targets (24h)
1. Handoff latency (dispatch->CP0): <= 10 min (p95)
2. Retry rate (tasks needing redispatch): < 10%
3. Closure rate (tasks closed with CPF): > 90%
4. Throughput (SC reports completed/24h): +30% vs previous day
5. False-status rate (chat says done, files not done): 0

## Execution plan
- Standardized task templates with acceptance criteria
- Strict CP0/CPF sentinel enforcement
- Milestone-only messaging (no chatter)
- Immediate SC trigger on CPF_DONE
- Pre-defined report scaffold for faster `.tex -> .pdf` publication

## 24h timeline
- T0-T4h: protocol hardening and template rollout
- T4-T12h: run with active tasks, collect KPI traces
- T12-T20h: fix bottlenecks and enforce zero-silence policy
- T20-T24h: finalize KPI readout + recommendations

## Measurement sources
- Inbox/outbox timestamps
- Artifact creation times
- Report publish timestamps
