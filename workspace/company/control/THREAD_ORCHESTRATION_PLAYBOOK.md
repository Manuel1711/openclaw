# THREAD_ORCHESTRATION_PLAYBOOK.md

Playbook operativo rapido per Cassia su orchestrazioni thread-bound multi-ruolo.

## Scopo
Ridurre regressioni su:
- ordine di spawn non deterministico
- restart fatti fuori sequenza
- accumulo di sessioni stale/duplicate

## Protocollo standard per ogni ruolo

1. **Lock ruolo (soft freeze)**
   - Non avviare nuovi task durante spawn/restart del ruolo.

2. **Deterministic input set**
   - Definisci in modo esplicito: `runtime`, `agentId` (se ACP), `label`, `cwd` (se subagent), `thread=true`, `mode=session`.
   - Non variare label tra tentativi.

3. **Pre-flight + restart discipline**
   - Verifica prerequisiti runtime.
   - Se serve patch config: applica patch, restart una sola volta, poi readiness gate.

4. **Stale cleanup pre-spawn**
   - Se trovi più sessioni della stessa label, mantieni solo la canonica e chiudi stale.

5. **Single spawn**
   - Esegui uno spawn unico.
   - Se fallisce: fix mirato + 1 retry massimo.

6. **Post-spawn canonicalization**
   - Salva sessionKey canonica del ruolo.
   - Verifica unicità sessione attiva per label.

## Deterministic spawn queue (multi-ruolo)
Quando devi avviare più ruoli nello stesso ciclo:
- Usa ordine fisso dichiarato nel piano (evita ordinamenti "al volo").
- Processa serialmente: un ruolo alla volta.
- Non interleavare restart di ruoli diversi.

Ordine operativo standard consigliato:
1. `Business-Chief`
2. `Science-Chief`
3. `ERC8004-Specialist` (solo se incluso nel ciclo)

Nota stabilità:
- Se un ruolo fallisce anche dopo il retry unico, **ferma la coda** e apri incident note.

## Regole anti-drift
- ACP thread spawn: solo `sessions_spawn(runtime="acp", thread=true, mode="session")`.
- Mai creare thread ACP via `message.thread-create`.
- Cambio runtime (ACP↔Subagent): obbligo di chiusura esplicita sessione precedente.
- No polling loop aggressivi su session list: check solo on-demand.

## Incident note template (da usare nei log)
- **Ruolo:**
- **Timestamp:**
- **Fase fallita:** (pre-flight / restart gate / spawn / post-spawn)
- **Errore osservato:**
- **Fix applicato:**
- **Retry eseguito:** (sì/no)
- **Esito finale:**
- **Sessione canonica attuale:**

## Exit criteria del ciclo SC/BC
Un pass è chiuso solo se:
- esiste una sola sessione canonica per `Science-Chief`;
- esiste una sola sessione canonica per `Business-Chief`;
- runtime effettivo coerente con quello pianificato per entrambi;
- sessionKey canoniche annotate nel log giornaliero.

## Riferimenti
- Runbook tecnico dettagliato: `/home/manuel/.openclaw/workspace/RUNBOOK_ACP_DISCORD.md`
