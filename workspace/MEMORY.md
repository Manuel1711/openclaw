# MEMORY.md - Long-Term Memory

## Identity & Relationship
- Assistant name: **Cassia**.
- Human: **Manuel**.
- Cassia reports directly to Manuel.
- Operating style requested by Manuel: **very precise, direct, fast**.
- Timezone baseline: **Europe/Rome**.

## Strategic Direction (early)
- Manuel wants to build a company directed by Cassia.
- Preferred org model: **pyramid hierarchy**.
- Top level: Manuel.
- Under Manuel: Cassia (orchestration/command).
- Under Cassia: multiple AI bot leads, each responsible for a specific section/function.
- Company target model: dual engine with **R&D** + **Business Applications**.

## Manuel Profile (work)
- Researcher at **Scuola Normale di Pisa**.
- Background domains:
  - Theoretical physics
  - Inverse problems
  - Quantitative finance
  - Blockchain
  - DeFi
  - Tokenization

## Operating Notes
- Persist important decisions in memory files, not only chat context.
- Keep communication concise and execution-oriented.

## Decision Log
- **D-001 (2026-03-06):** Bootstrap identity completed.
- **D-002 (2026-03-06):** Company governance model set as pyramid hierarchy (Manuel -> Cassia -> Lead Bots).
- **D-003 (2026-03-06):** Strategic company architecture confirmed as dual-track: R&D + Business Applications.
- **D-004 (2026-03-06):** Initial lead-bot structure launched with 4 leads (RD-Scientist, RD-Builder, Biz-Product, Biz-Growth) and shared operating system templates.
- **D-005 (2026-03-06):** Workspace model switched to hybrid: central control workspace + dedicated workspace per lead bot.
- **D-006 (2026-03-06):** R&D leadership restructured: merge RD-Scientist + RD-Builder into one lead `Science-Chief` with dedicated scientific subbots per research line.
- **D-007 (2026-03-06):** Discord thread-bound ACP execution enabled for operations (`channels.discord.threadBindings.spawnAcpSessions=true`).
- **D-008 (2026-03-06):** ACP stack enabled and configured with Codex (`plugins.entries.acpx.enabled=true`, `acp.enabled=true`, `acp.backend='acpx'`, `acp.defaultAgent='codex'`, `acp.allowedAgents=['codex']`, `acp.dispatch.enabled=true`).
- **D-009 (2026-03-06):** `Science-Chief` launched as persistent thread-bound ACP session.
- **D-010 (2026-03-06):** For writable, low-friction file editing, `Science-Chief` operational mode switched to thread-bound **subagent sandbox** (workspace-scoped), because ACP runtime does not support `sandbox=require`.
- **D-011 (2026-03-06):** Canonical active `Science-Chief` session set to `agent:main:subagent:144c0421-eb53-4996-980a-238c56c4985b`; stale prior SC session was terminated.
- **D-012 (2026-03-06):** Added reusable runbook `RUNBOOK_ACP_DISCORD.md` for deterministic ACP/Discord setup and recovery.
- **D-013 (2026-03-06):** Business leadership restructured: merged `Biz-Product` + `Biz-Growth` into single lead `Business-Chief`.
- **D-014 (2026-03-06):** Business execution model fixed into 3 core streams under one supervisor: `Tokenization`, `AI Agents`, `Strategie`.
- **D-015 (2026-03-06):** Legacy business bot specs/workspaces archived (`company/bots/archive/`, `workspaces/archive/`) and new dedicated workspace initialized at `workspaces/business-chief/`.
- **D-016 (2026-03-07):** Business subbot `AI-Agent-Specialist` created under `Business-Chief` to build business around AI agents.
- **D-017 (2026-03-07):** Operating link formalized: `AI-Agent-Specialist` collaborates frequently with `ERC8004-Specialist` for research↔development↔business loop.
- **D-018 (2026-03-07):** Governance clarified by Manuel: Manuel is company head; Cassia always reports to Manuel. `Science-Chief` and `Business-Chief` report by default to Cassia, and may also report directly to Manuel when Manuel engages them directly.
- **D-019 (2026-03-07):** Horizontal communication explicitly enabled between `Science-Chief` and `Business-Chief` to generate cross-domain insights for both R&D and Business.
- **D-020 (2026-03-07):** Reporting symmetry locked at L3: `ERC8004-Specialist` under `Science-Chief`, `AI-Agent-Specialist` under `Business-Chief`.
- **D-021 (2026-03-07):** Real-time orchestration protocol enforced: every new `outbox/` file from SC, BC, and AI-Agent-Specialist must trigger immediate ping to Cassia with path + milestone/checkpoint tag + one-line summary.
- **D-022 (2026-03-07):** ERC8004 reporting chain locked: Specialist publishes detailed technical updates → SC reviews and compresses to decision-grade summary → Cassia reports to Manuel; deep-dive with bots only on Manuel request.
- **D-023 (2026-03-07):** Reporting quality standard reinforced by Manuel: reports must be punctual, precise, and scientifically rigorous (methods, results, limitations, blockers, next actions). This standard applies to SC/BC and all specialists.
- **D-016 (2026-03-07):** SC/BC orchestration closure hardened with mandatory canonical registry + explicit multi-role exit criteria in runbook/playbook to prevent ambiguous handoff states.

## Bugs & Preventive Playbook
- **B-001 (2026-03-06):** ACP spawn failed: `ACP target agent is not configured`.
  - **Cause:** Missing `agentId`/`acp.defaultAgent`.
  - **Prevention:** Always pass explicit `agentId` for ACP spawn unless default is verified.
- **B-002 (2026-03-06):** ACP thread spawn blocked on Discord.
  - **Cause:** `channels.discord.threadBindings.spawnAcpSessions` not enabled.
  - **Prevention:** Pre-flight check this flag before any Discord ACP thread spawn.
- **B-003 (2026-03-06):** ACP runtime unavailable (`acpx` backend not configured).
  - **Cause:** ACPX plugin disabled + ACP backend incomplete.
  - **Prevention:** Pre-flight checklist order: (1) plugin `acpx` loaded, (2) `acp.enabled=true`, (3) `acp.backend='acpx'`, (4) `acp.dispatch.enabled=true`, (5) agent allowlist/default set.
- **B-004 (2026-03-06):** `gateway config.patch` call failed with `raw required`.
  - **Cause:** Tool invocation used structured patch instead of `raw` string in this environment.
  - **Prevention:** For gateway config patching, default to `raw` JSON payload.
- **B-005 (2026-03-06):** ACP remained unavailable during restart-drain window.
  - **Cause:** Gateway hot-reload/restart deferred while active operations were still running.
  - **Prevention:** After ACP/plugin config changes, wait for restart completion and then retry spawn once (no rapid retry loops).
- **B-006 (2026-03-06):** Requested writable sandbox for ACP failed (`sandbox=require` unsupported for `runtime='acp'`).
  - **Cause:** ACP sessions run outside sandbox controls.
  - **Prevention:** If writable sandbox is required, spawn with `runtime='subagent'` and keep ACP for non-sandboxed harness execution.
- **B-007 (2026-03-06):** Spawning with `sandbox='require'` failed until sandboxed target runtime/agent path was valid.
  - **Cause:** Policy/runtime mismatch during spawn mode transition.
  - **Prevention:** Use `sandbox='inherit'` when defaults are already sandbox-enabled, or verify sandbox-capable spawn target before `require`.
- **B-008 (2026-03-06):** Duplicate `Science-Chief` sessions created during retries/relaunches caused confusion/latency perception.
  - **Cause:** Multiple active sessions with same label after iterative recovery.
  - **Prevention:** Keep one canonical SC session key, kill stale duplicates immediately, avoid repeated relaunch without status check.
- **B-009 (2026-03-07):** ERC8004 thread appeared present but specialist runtime was not live/responding.
  - **Cause:** Session/thread visibility drift vs active runtime continuity.
  - **Prevention:** Keep ERC8004-Specialist on persistent `subagent` runtime, enforce canonical session checks, relaunch on drop, and clean stale duplicates.
- **B-009 (2026-03-06):** Retry storms after config changes created noisy failures before services were ready.
  - **Cause:** Spawn attempts executed before restart/hot-reload completion.
  - **Prevention:** Enforce ordered flow: config -> restart complete -> status check -> single spawn -> max one retry.
- **B-010 (2026-03-06):** ACP thread/session creation path drifted across tools.
  - **Cause:** Mixing generic thread creation habits with ACP lifecycle.
  - **Prevention:** For ACP thread creation, use only `sessions_spawn(runtime='acp', thread=true, mode='session')`; never `message thread-create`.
- **B-011 (2026-03-07):** Final SC deliverable was published but Cassia did not proactively push the report to Manuel immediately.
  - **Cause:** Status-check response loop without enforced auto-report handoff on C4 completion.
  - **Prevention:** On C4 done (SC review file present), trigger immediate Manuel update in fixed format (Method, Results, Problems, Confidence, Next Actions + figure pointers) within one turn.
- **B-012 (2026-03-07):** After model switch/restart, Discord chat path became unstable while terminal path still responded, causing inconsistent user experience.
  - **Cause:** Runtime path split (CLI session vs Discord gateway/thread binding) during/after restart and model override changes.
  - **Prevention:** Enforce post-switch stabilization protocol: (1) apply model change, (2) wait for restart settle, (3) send explicit "stabilized ✅" message in Discord, (4) run quick echo test in channel, (5) only then resume critical task flow.
