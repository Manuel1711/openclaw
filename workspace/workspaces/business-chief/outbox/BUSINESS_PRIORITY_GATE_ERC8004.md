# BUSINESS_PRIORITY_GATE_ERC8004

Data: 2026-03-08
Owner: Business-Chief
Principio: ETH robustness first, cross-chain second

## Priorità business (ordine vincolante)
P1. Servizi AI agents onchain su ETH L1 con utilità immediata (identity/reputation, scoring, feedback proof)
P2. Pilot monetizzabili su clienti design-partner
P3. Standardizzazione packaging commerciale (SLA/pricing/onboarding)
P4. Estensioni cross-chain (solo post gate tecnico sufficiente)

## Gate tecnici minimi per decisione business

### GATE C1 (Foundational readiness)
**Minimo tecnico richiesto:**
- Architettura MVP documentata
- Scope funzionale chiaro (identity+reputation view, score v1 aritmetico, feedback registry)
- Test base passati in ambiente controllato

**Decisione business:**
- GO: solo discovery interna + prep GTM materiale
- HOLD: se architettura incompleta o scope ambiguo

### GATE C2 (Evidence v1)
**Minimo tecnico richiesto:**
- Demo funzionante ETH L1 su casi test
- Metriche iniziali qualità/affidabilità tracciate
- SC review positiva con limiti espliciti

**Decisione business:**
- GO: avvio design-partner outreach e pilot discovery
- HOLD: se affidabilità non ripetibile o metriche incoerenti

### GATE C3 (Evidence v2 / robustness)
**Minimo tecnico richiesto:**
- Stabilità dimostrata su set di test esteso
- Incident/risk controls operativi (circuit breaker, override, logging)
- Riduzione criticità bloccanti da SC

**Decisione business:**
- GO: pilot pagati + pricing test + pre-sales
- HOLD: se mancano controlli rischio o stabilità

### GATE C4 (Production-grade)
**Minimo tecnico richiesto:**
- Readiness operativa e runbook incident
- Audit trail completo
- KPI tecnici sopra soglia target

**Decisione business:**
- GO: rollout commerciale progressivo
- HOLD: se non garantibile SLA minimo

## Regola anti-spreco
Qualsiasi iniziativa business non mappata a C-gate corrente = **STOP**.

## KPI gate alignment
- G-KPI1: % task business mappati a gate tecnico (target 100%)
- G-KPI2: % GO decision supportate da evidenze C2/C3 (target 100%)
- G-KPI3: Work-waste ratio (task cancellati per gate fail) target <15%
