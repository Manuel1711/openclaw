# BUSINESS_EXECUTION_PROTOCOL_V1

Data: 2026-03-08
Owner: Business-Chief
Scope: orchestration BC ↔ AI-Agent-Specialist ↔ Science-Chief (SC)

## Obiettivo
Eliminare colli di bottiglia tra input tecnico, decisione business e rilascio GTM.

## Flusso operativo (single-thread per iniziativa)
1. **BC - Intake & framing (T0-T+30m)**
   - Definisce obiettivo business, KPI target, vincoli (ETH-first, C-gate).
   - Output: `TASK_BRIEF` con acceptance criteria.

2. **AI-Agent-Specialist - Build & evidence (T+30m-T+6h)**
   - Produce asset MVP/analisi secondo brief.
   - Output minimo: metodo, risultati, limiti, confidenza, next.

3. **SC - Scientific/technical review (SLA <=2h dalla consegna specialist)**
   - Verifica robustezza tecnica, assunzioni e rischi di ricerca.
   - Output: `SC_REVIEW` con GO/HOLD tecnico su gate corrente.

4. **BC - Business gate decision (SLA <=1h da SC_REVIEW)**
   - Emana decisione: GO M+1 / HOLD / REWORK.
   - Se GO: autorizza pacchetto business/GTM compatibile col gate tecnico.

5. **Execution sync**
   - Handoff operativo con owner, deadline, KPI misurabili.

## Anticolli di bottiglia (hard rules)
- Un solo owner decisionale per step (RACI esplicita).
- Nessun task senza acceptance criteria e ETA.
- Nessuna proposta GTM se gate tecnico non supera soglia minima.
- Timeout escalation automatica: 90 min senza risposta -> escalation a BC.
- Template unico report 5 blocchi mandatory.

## SLA operativi
- Intake BC: <=30 min
- Specialist first delivery: <=6h
- SC review: <=2h
- BC decision: <=1h
- Latency tecnica->decisione business target: <=24h (stretch <=8h)

## KPI orchestration
- O-KPI1: Cycle time end-to-end (target <=24h)
- O-KPI2: Rework rate (target <25%)
- O-KPI3: Decision latency post-review (target <=1h)
- O-KPI4: % task con owner+deadline+acceptance (target 100%)

## RACI sintetica
- **BC:** Accountable decisione business e priorità
- **AI-Agent-Specialist:** Responsible delivery tecnica/business operativa
- **SC:** Responsible validazione scientifico-tecnica
