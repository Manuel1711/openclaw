# INTERAGENT_COMMS_MIN_PROTOCOL_V1

Obiettivo: ridurre ping ridondanti e accelerare decisioni.

## Regole minime
1. Ping solo su eventi utili:
   - milestone deliverable,
   - blocker hard,
   - decisione GO/HOLD/KILL.
2. Niente heartbeat narrativi o update non-azionabili.
3. Checkpoint standard:
   - `CP0` start,
   - `CP1` first artifact,
   - `CPF` final.
4. Formato ping (una riga):
   - `PATH | STATO | NEXT | ETA`.
5. Se rischio quota/token:
   - inviare solo semaforo decisionale + 1 motivazione.

## Escalation
- Timeout > SLA: 1 ping blocker con input mancante esplicito.
- Nessun loop di sollecito.
