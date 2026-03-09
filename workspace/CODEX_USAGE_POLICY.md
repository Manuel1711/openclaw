# CODEX_USAGE_POLICY.md

## Scope
- Fixed model: `openai-codex`
- Goal: reduce unnecessary call burn and prevent sudden allowance exhaustion.

## Mandatory Guardrails
1. **Batch related asks** into a single call whenever feasible.
2. **Deduplicate** near-identical requests in short windows.
3. **Retry cap:** at most 1 automatic retry for transient failures (429/timeout/5xx), with backoff.
4. **No retry loops** and no rapid-fire probing calls.
5. **Prompt minimization:** keep only task-critical context.
6. **Priority gating under pressure:** execute P0/P1 only when allowance is low.

## Alert Thresholds (remaining allowance)
- **Warning:** <= 30% remaining
- **Critical:** <= 15% remaining
- **Emergency:** quota/rate-limit error observed (e.g., 429/insufficient quota)

## Required Alert Payload (Discord)
- Status: WARNING | CRITICAL | EMERGENCY
- Remaining: X%
- Trigger: threshold | 429 | quota
- Action: batch ON / retries limited / non-critical deferred

## Execution Modes
- **Normal mode:** all priorities allowed, guardrails always on.
- **Conservative mode (<=15%):** P0/P1 only, strict batching, strict dedup, minimized context.

## Daily Review Checklist
- Total codex-intensive tasks
- Duplicate calls avoided
- Retry count
- 429/quota incidents
- Top avoidable call patterns and corrective action
