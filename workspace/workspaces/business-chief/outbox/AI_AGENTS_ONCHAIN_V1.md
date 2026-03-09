# AI_AGENTS_ONCHAIN_V1

Data: 2026-03-07 (notturno)
Owner: Business-Chief
Milestone tag: ADHOC-NIGHT
Scope: Linea AI Agents onchain integrabili in ERC8004 e monetizzabili

## 1) Use-case shortlist (valore economico vs complessità)

### UC1 — Treasury Rebalancer Agent (ETH-first)
- **Servizio:** ribilanciamento policy-based di treasury onchain (ETH/LST/stable) con guardrail.
- **Cliente target:** DAO, treasury manager, protocolli early-stage.
- **Valore economico:** riduzione drawdown + efficienza capitale; willingness-to-pay alta su asset in custodia.
- **Complessità:** Media-Alta (strategie + risk controls + integrazione execution).
- **Priorità:** P1 (forte allineamento ETH robustness).

### UC2 — Compliance & Policy Sentinel Agent
- **Servizio:** monitor transazioni/controparti/rule violations + alert/auto-freeze policy-based.
- **Cliente target:** emittenti tokenizzati, desk operativi, entità con obblighi KYC/AML.
- **Valore economico:** riduzione rischio operativo/regolatorio; costo evitato elevato.
- **Complessità:** Media (rule engine + data providers + reporting audit).
- **Priorità:** P1 (abilita enterprise readiness).

### UC3 — Liquidity Routing Agent for Tokenized Assets
- **Servizio:** routing intelligente ordini/liquidità su venue consentite con minimizzazione slippage/costi.
- **Cliente target:** issuer di asset tokenizzati, market maker, treasury.
- **Valore economico:** spread migliore + execution cost down.
- **Complessità:** Alta (venue integration, failover, latency constraints).
- **Priorità:** P2.

### UC4 — Yield/Risk Strategy Agent (permissioned mandates)
- **Servizio:** esecuzione strategie rendimento con limiti rischio e mandate predefiniti.
- **Cliente target:** treasury professionali, fondi digital asset.
- **Valore economico:** alpha/efficienza operativa; fee-based revenue.
- **Complessità:** Alta (model risk + policy governance).
- **Priorità:** P2.

### UC5 — Onchain Reporting & Proof Agent
- **Servizio:** generazione report verificabili (proof-of-action/proof-of-policy) per auditor/partner.
- **Cliente target:** issuer, partner istituzionali, compliance teams.
- **Valore economico:** riduce costi reporting e accelera deal enterprise.
- **Complessità:** Media.
- **Priorità:** P1.5 (supporto trasversale).

## 2) Architettura prodotto/servizio

### 2.1 Capabilities core agente
1. **Perception Layer:** ingest dati onchain + market + policy/config.
2. **Reasoning/Planning Layer:** policy-constrained planning, scoring opzioni.
3. **Execution Layer:** signer abstraction / relayer / tx builder con simulation pre-trade.
4. **Control Layer:** risk limits, circuit breaker, human override, allowlist contracts.
5. **Evidence Layer:** log immutabili, attestazioni azioni, report audit-ready.

### 2.2 Execution loop standard
1. Observe (stato chain + KPI)
2. Evaluate (policy + risk + expected value)
3. Simulate (dry-run tx + stress checks)
4. Approve (auto if within mandate; human-in-the-loop over threshold)
5. Execute (onchain tx)
6. Verify (post-trade checks)
7. Report (proof + SLA log)

### 2.3 Risk/Compliance-by-design
- Policy engine con regole hard (exposure limit, venue allowlist, stop-loss/circuit breaker).
- Segregazione ruoli e chiavi (proposal key vs execution key).
- Mandatory simulation prima di ogni azione economica significativa.
- Audit trail completo (decision rationale + tx hash + policy match).
- KYC/AML hooks per flussi permissioned dove richiesto.

## 3) Modello ricavi (pricing, SLA, GTM iniziale)

### 3.1 Pricing
- **Setup fee** (integrazione + policy onboarding)
- **Subscription mensile** per monitoraggio/automazione base
- **Performance fee** (opzionale) su risparmio costi o miglioramento execution
- **Tier enterprise** con SLA premium + reporting avanzato

### 3.2 SLA iniziali
- Uptime service target: 99.5%
- P95 decision-to-action latency: <=120s (uc dipendente)
- Incident response: <=30 min (critical)
- Audit log completeness: 100%

### 3.3 Go-to-market iniziale (ETH-first)
- Fase 1: 3 design partner (DAO/issuer/treasury) su UC1+UC2
- Fase 2: pilot pagati con metriche chiare (saving/risk reduction)
- Fase 3: case study + pacchetto standardizzato per onboarding rapido

## 4) Roadmap 14 giorni con priorità e KPI

### D1-D3 (Design lock)
- Selezione 2 use-case core: UC1 + UC2
- Definizione mandate templates + risk policies v0
- KPI:
  - K1: Use-case selection finalized (100%)
  - K2: Policy template completeness >=80%

### D4-D7 (Prototype)
- Prototype execution loop con simulation + circuit breaker
- Definizione schema report/proof
- KPI:
  - K3: End-to-end simulated runs >=20
  - K4: Policy violation catch rate >=95% in test set

### D8-D10 (Pilot packaging)
- Pricing v1 + SLA v1 + pilot contract template
- Target list 10 prospect + shortlist 3 design partner
- KPI:
  - K5: Pilot pack complete (100%)
  - K6: Design partner conversations avviate >=3

### D11-D14 (Commercial readiness)
- Playbook rollout (onboarding, incident, reporting)
- GO/HOLD decision per UC1/UC2
- KPI:
  - K7: Decision latency da segnale tecnico a decisione commerciale <=48h
  - K8: Pre-commitment commerciale (LOI/intent) >=1

## 5) Rischi principali + mitigazioni

1. **Smart contract / execution risk** (Impatto Molto Alto)
- Mitigazione: simulation obbligatoria, canary limits, manual override, phased capital limits.

2. **Regolatorio/compliance ambiguity** (Impatto Alto)
- Mitigazione: policy permissioned, KYC hooks, legal review prioritaria su casi target.

3. **Model risk / false positives-negatives** (Impatto Alto)
- Mitigazione: threshold conservativi iniziali, human-in-the-loop su trade high value.

4. **Latency/infrastructure failures** (Impatto Medio-Alto)
- Mitigazione: failover providers, retry logic, graceful degradation mode.

5. **Insufficient willingness-to-pay** (Impatto Alto)
- Mitigazione: packaging ROI-first, pilot pagati con KPI di valore misurabile.

---

## Reporting (standard)

### Method/Procedure
Approccio top-down business engineering: (i) selezione use-case per valore economico e fattibilità ETH-first, (ii) definizione reference architecture con control-by-design, (iii) costruzione modello ricavi/SLA/GTM, (iv) roadmap 14 giorni con KPI e gate decisionali.

### Key Results
- Shortlist 5 use-case con priorità operative (P1: UC1/UC2).
- Architettura prodotto definita con execution loop e guardrail risk/compliance.
- Revenue model multi-componente (setup + subscription + performance).
- Roadmap 14 giorni con 8 KPI misurabili.
- Registro rischi con mitigazioni eseguibili.

### Limitations/Problems
- Mancano ancora dati reali da pilot per calibrare pricing finale e performance fee.
- Requisiti legali specifici per giurisdizione non ancora validati con counsel.
- KPI tecnici dipendono dalla maturità dei milestone ERC8004 C2/C3.

### Confidence Level
**Medium-High** su design business-operativo; **Medium** su stime economiche finché non chiudiamo design partner e test reali.

### Next Actions
1. Lock UC1+UC2 come linea prioritaria (oggi).
2. Avviare 3 design-partner conversations con script ROI/SLA (entro 48h).
3. Costruire pilot pack contrattuale e pricing v1 testabile (entro D7).
4. Allineare gate commerciali a evidenze C2/C3 con SC (continuo).

## Decisioni consigliate per Manuel
1. **APPROVE** focus iniziale su UC1 (Treasury Rebalancer) + UC2 (Compliance Sentinel).
2. **APPROVE** strategia ETH-first: nessun cross-chain commerciale prima di gate C3 positivo.
3. **APPROVE** modello pricing ibrido (setup + subscription + optional performance).
4. **MANDATE** legal fast-track su perimetro compliance dei primi 2 use-case.
