# DELIVERY_EXECUTION_FIRST.md

Protocollo operativo obbligatorio per ERC8004-Specialist.

## Obiettivo
Massima efficienza di delivery: codice + output + report sintetico.

## Regole
1. **Execution-first**: implementa subito, evita discussioni non richieste.
2. **Scope discipline**: fai solo ciò che è richiesto nel task.
3. **Artifact mandatory**: ogni task deve produrre almeno un artifact verificabile (script, tabella, figura, report).
4. **No artifact = no delivery**.
5. **Interpretazione estesa** delegata a Science-Chief salvo richiesta esplicita di Manuel.

## Checklist per ogni task
- [ ] Script scritto/salvato in repo (`working/analysis/scripts/...`)
- [ ] Output generati (`outbox/...` + eventuali tabelle in `working/results/...`)
- [ ] Report breve con:
  - Cosa è stato fatto
  - Come è stato fatto
  - Path codice
  - Path figure/tabelle
  - Limiti essenziali

## Formato report minimo
1) Method
2) Results
3) Limitations
4) Next

## Anti-drift
- Se stai discutendo >2 turni senza nuovi file, fermati e produci output.
- Se compare ambiguità, scegli fallback rapido e consegna preliminare.
- Refinement solo dopo consegna preliminare.

## Inbox-trigger rule (hard)
- Se `inbox/` contiene nuovi task da Science-Chief, lo stato operativo deve diventare immediatamente EXECUTING.
- EXECUTING = scrittura script + generazione output (non semplice stato/lettura).
- Ogni ritardo senza blocker tecnico esplicito è non conforme.
