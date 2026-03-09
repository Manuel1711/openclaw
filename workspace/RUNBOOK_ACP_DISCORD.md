# RUNBOOK_ACP_DISCORD.md

Runbook operativo anti-regressione per orchestrazioni thread-bound (Discord).
Obiettivo: eliminare bug ricorrenti su spawn, restart e sessioni stale.

## Quick start (operatore)
Per esecuzione rapida usa prima: **`CHECKLIST_CASSIA_SETUP.md`**.
Poi apri questo runbook solo per diagnosi/incident.

## 0) Guardrail hard (non negoziabili)
- Spawn ACP thread-bound: **solo** `sessions_spawn(runtime="acp", thread=true, mode="session")`.
- **Mai** `message(action="thread-create")` per creare thread ACP.
- Retry budget globale: **1 solo retry** dopo fix/restart completato.
- **Una sola sessione canonica per ruolo** (label stabile + sessionKey registrata).
- Vietato lanciare nuovi spawn se il gateway non è in stato chiaramente stabile.

## 1) Deterministic spawn order (ordine vincolato)
Eseguire sempre in questo ordine, senza salti:

1. **Freeze del ruolo**
   - blocca nuovi task per quel ruolo durante la finestra di spawn/restart.
2. **Pre-flight config**
   - valida runtime + thread bindings + agent allowlist.
3. **Restart discipline**
   - applica patch config (se necessaria), poi restart/hot-reload singolo.
4. **Readiness gate**
   - controlla stato (`openclaw status --all`) finché stabile.
5. **Stale cleanup gate**
   - prima dello spawn, chiudi eventuali duplicati/stale per la stessa label.
6. **Single spawn attempt**
   - un solo `sessions_spawn` con parametri deterministici.
7. **Post-spawn canonicalization**
   - registra sessione canonica e verifica unicità.
8. **(Solo se fallisce) One-shot recovery**
   - fix mirato + 1 retry; se fallisce ancora: stop/escalation.

## 2) Pre-flight ACP (obbligatorio)
Checklist minima prima di qualsiasi spawn ACP:
- `plugins.entries.acpx.enabled = true`
- `acp.enabled = true`
- `acp.backend = "acpx"`
- `acp.dispatch.enabled = true`
- `acp.allowedAgents` contiene l'agent richiesto
- `agentId` esplicito nello spawn *(oppure `acp.defaultAgent` valido)*
- `channels.discord.threadBindings.enabled = true`
- `channels.discord.threadBindings.spawnAcpSessions = true`

## 3) Pre-flight Subagent sandbox (se runtime=subagent)
- `agents.defaults.sandbox.mode = "non-main"` *(o `all`)*
- `agents.defaults.sandbox.workspaceAccess = "rw"`
- `agents.defaults.sandbox.scope = "session"`
- Spawn consigliato: `sandbox="inherit"` (più robusto in transizione)

## 4) Restart discipline (anti-race)
- Applica tutte le patch necessarie in batch logico unico.
- Avvia **un solo** restart/hot-reload.
- Non spawnare durante restart in corso.
- Gate obbligatorio dopo restart:
  - `openclaw status --all` coerente/stabile
  - plugin ACPX `loaded` se runtime ACP
- Solo dopo gate positivo: procedi allo spawn.

## 5) Spawn templates (deterministici)
### A) ACP thread-bound persistente
- `runtime: "acp"`
- `agentId: "codex"` *(o altro consentito)*
- `thread: true`
- `mode: "session"`
- `label: "Science-Chief"` *(stabile e univoca per ruolo)*

### B) Subagent thread-bound persistente
- `runtime: "subagent"`
- `thread: true`
- `mode: "session"`
- `cwd: /home/manuel/.openclaw/workspace/workspaces/<role>`
- `sandbox: "inherit"`
- `label: "Science-Chief"` *(stabile e univoca per ruolo)*

## 6) Stale-session cleanup policy (prima e dopo spawn)
Per ogni ruolo/label:
1. Elenca sessioni attive pertinenti (on-demand, no polling loop).
2. Se >1 sessione con stessa label:
   - mantieni quella più recente valida/coerente con runtime atteso;
   - termina le altre come stale.
3. Se cambia runtime (ACP ↔ Subagent):
   - chiudi/archivia esplicitamente la sessione precedente prima del nuovo spawn.
4. Registra sempre la sessionKey canonica nel log operativo/memory.

## 7) Errori noti → fix immediato
- **ACP target agent is not configured**
  - Passa `agentId` esplicito o imposta `acp.defaultAgent`.
- **Discord thread-bound ACP spawns are disabled**
  - `channels.discord.threadBindings.spawnAcpSessions=true`.
- **ACP runtime backend is not configured**
  - Verifica ACPX + `acp.enabled` + `acp.backend="acpx"` + `acp.dispatch.enabled`.
- **raw required** su patch config
  - Usa payload `raw` JSON string.
- **sandbox=require unsupported for runtime="acp"**
  - Se serve sandbox, usa `runtime="subagent"`.
- **sandbox=require needs a sandboxed target runtime**
  - Usa `sandbox="inherit"` con defaults sandbox già attivi.

## 8) Recovery policy (single-shot)
Se il primo spawn fallisce:
1. identifica causa specifica;
2. applica fix mirato;
3. se necessario restart + readiness gate;
4. esegui **un solo retry**.

Se anche il retry fallisce: **stop**, niente retry storm. Apri diagnosi con log e stato.

## 9) Validazione finale (30s)
- `openclaw plugins info acpx` → `loaded` (se ACP)
- `openclaw status --all` → gateway running + config attiva
- spawn → `status: accepted`
- post-spawn → esiste **1 sola** sessione attiva per label/ruolo
- sessionKey canonica registrata in memoria operativa

## 10) Registro canonico SC/BC (obbligatorio)
Dopo ogni spawn/restart aggiorna un registro minimale (in log operativo o memory giornaliera) con:
- `role`: `Science-Chief` | `Business-Chief`
- `runtime`: `acp` | `subagent`
- `label` stabile usata nello spawn
- `sessionKey` canonica
- `timestamp` ultimo cambio stato

Regola di stabilità:
- Se il registro non è aggiornato, la procedura è considerata **non chiusa**.
- Mai avviare un nuovo ciclo multi-ruolo con registro ambiguo/incompleto.

## 11) Chiusura ciclo multi-ruolo (SC/BC)
Done solo se tutte vere:
- SC in stato coerente con runtime atteso e sessione unica.
- BC in stato coerente con runtime atteso e sessione unica.
- Nessuna sessione stale residua per label SC/BC.
- Eventuali incident note compilate (se c'è stato un errore).
- Memory giornaliera aggiornata con esito e sessionKey canoniche.

## 12) Anti-drop specialist (ERC8004)
- `ERC8004-Specialist` va tenuto in `runtime="subagent"` thread-bound persistente (non ACP) per continuità chat.
- Se il thread esiste ma non risponde: trattare come session drop runtime.
- Recovery standard immediata:
  1) relaunch con stessa `label` e stesso `cwd`
  2) verifica `status: accepted`
  3) chiusura eventuali sessioni stale con stessa label
  4) aggiornamento registro canonico (role/runtime/sessionKey/timestamp)
- Obiettivo: evitare “thread visibile ma bot non operativo”.
