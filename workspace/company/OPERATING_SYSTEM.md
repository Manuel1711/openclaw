# Operating System v1 (Cassia)

## 1) Ciclo operativo standard
1. **Decide** (Manuel + Cassia)
   - Definizione obiettivo
   - Owner unico
   - Deadline
   - KPI di successo
2. **Delegate** (Cassia -> Lead Bot)
   - Brief standardizzato
   - Vincoli
   - Deliverable atteso
3. **Deliver** (Lead Bot -> Cassia)
   - Consegna strutturata
   - Evidenze
   - Rischi + next step
4. **Review** (Cassia)
   - Quality gate
   - Sintesi executive per Manuel

## 2) SLA interni
- Presa in carico task: entro 15 minuti (task rapidi) / 2 ore (task complessi)
- Aggiornamento stato: almeno 1 checkpoint per task > 4 ore
- Escalation ritardi: immediata se rischio su deadline > 20%

## 3) Regole hard
- Un solo owner per task
- Output in formato unico
- Niente azioni esterne sensibili senza approvazione Manuel
- Ogni decisione significativa va nel Decision Log

## 4) Escalation
- Livello 1: Lead Bot risolve
- Livello 2: Cassia interviene con riassegnazione/prioritizzazione
- Livello 3: Manuel decide (go/no-go)

## 5) Cadence
- Daily brief (asincrono): stato KPI e blocchi
- Weekly review: 30-45 min, colli di bottiglia e riallocazione
- Monthly strategy: 60 min, obiettivi e roadmap

## 6) SOP di orchestrazione (SC/BC)
- Per avvio/restart sessioni thread-bound multi-ruolo: seguire `company/control/THREAD_ORCHESTRATION_PLAYBOOK.md`.
- Mantenere una sola sessione canonica attiva per ruolo (`Science-Chief`, `Business-Chief`, eventuali sottobot L3).
- Cleanup sessioni stale obbligatorio prima/dopo spawn quando rilevate.
