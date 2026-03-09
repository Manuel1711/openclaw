# CHECKLIST_CASSIA_SETUP.md

Checklist operativo **minimo** per evitare i bug ricorrenti di setup/orchestrazione.
Usalo prima di ogni spawn thread-bound.

## 1) Scelta runtime (obbligatoria)
- Se serve sandbox scrivibile su workspace → **`runtime="subagent"`**.
- Se vuoi harness ACP puro → **`runtime="acp"`**.
- Regola dura: **mai** usare `sandbox="require"` con `runtime="acp"`.

## 2) Spawn path corretto
- ACP thread-bound: solo `sessions_spawn(runtime="acp", thread=true, mode="session")`.
- Non usare `message(...thread-create...)` per thread ACP.

## 3) Pre-flight 20s
- `agentId` esplicito (o `acp.defaultAgent` già valido).
- ACP attivo: `acpx enabled`, `acp.enabled=true`, `acp.backend="acpx"`, `acp.dispatch.enabled=true`.
- Discord thread bindings attivi: `channels.discord.threadBindings.enabled=true` + `spawnAcpSessions=true`.

## 4) Restart discipline
- Se tocchi config: patcha, poi **1 solo restart/hot-reload**.
- Attendi stato stabile (`openclaw status --all`) prima di spawnare.
- Vietati retry a raffica durante restart-drain.

## 5) Session hygiene (anti-duplicati)
- Per ogni ruolo: **1 sola sessione canonica** (label stabile).
- Prima e dopo spawn: chiudi sessioni stale/duplicate.
- Registra sempre la `sessionKey` canonica.

## 6) Retry policy
- Primo tentativo fallito → fix mirato.
- Poi **1 solo retry**.
- Se fallisce ancora: stop + diagnosi (niente retry storm).

## 7) Error map rapido
- `ACP target agent is not configured` → imposta `agentId`/`acp.defaultAgent`.
- `thread-bound ACP spawns are disabled` → abilita `spawnAcpSessions`.
- `ACP runtime backend is not configured` → verifica ACPX + backend/dispatch.
- `raw required` su config patch → usa payload `raw` JSON string.

## Done criteria (30s)
- Stato gateway stabile.
- Spawn accepted.
- Una sola sessione attiva per ruolo/label.
- Sessione canonica tracciata.
