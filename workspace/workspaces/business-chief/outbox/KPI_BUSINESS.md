# KPI_BUSINESS

Data baseline: 2026-03-06
Owner: Business-Chief

## 3) KPI baseline e rischi

## KPI aggiuntivi di allineamento tecnico-business (ERC8004)
- **X-KPI1 C1-C4 Alignment Rate (% deliverable business mappati a C-gate)**
  - Baseline: 0%
  - Target D14: 100%
- **X-KPI2 Tech-to-GTM Decision Latency (giorni da output C2/C3 a decisione commerciale)**
  - Baseline: n.d.
  - Target D14: <=2 giorni
- **X-KPI3 ETH-first Compliance (% iniziative in linea con priorità ETH robustness)**
  - Baseline: 0%
  - Target D14: 100%


### KPI baseline per stream

#### A) Tokenization
- **A-KPI1 Product Thesis Complete (%)**
  - Baseline: 0%
  - Target D14: 100%
- **A-KPI2 Tokenomics Readiness Score (0-10)**
  - Baseline: 0
  - Target D14: >=7
- **A-KPI3 Compliance Readiness Checklist (%)**
  - Baseline: 0%
  - Target D14: >=70% (pre-legal)
- **A-KPI4 Scenario Robustness (n. scenari validati)**
  - Baseline: 0
  - Target D14: 3

#### B) AI Agents
- **B-KPI1 Throughput task/settimana (# task completati)**
  - Baseline: 0
  - Target D14: >=20 equivalenti/14 giorni
- **B-KPI2 Cycle Time mediano (h/task)**
  - Baseline: n.d.
  - Target D14: <=24h su task standard
- **B-KPI3 First-Pass Quality Rate (%)**
  - Baseline: 0%
  - Target D14: >=80%
- **B-KPI4 SLA Compliance (%)**
  - Baseline: 0%
  - Target D14: >=90%

#### C) Strategie
- **C-KPI1 Strategic Clarity Score (0-10)**
  - Baseline: 2
  - Target D14: >=8
- **C-KPI2 Priority Coverage (iniziative con owner+deadline / totale)**
  - Baseline: 0%
  - Target D14: 100%
- **C-KPI3 Decision Latency media (giorni per decisione critica)**
  - Baseline: n.d.
  - Target D14: <=2 giorni
- **C-KPI4 Risk Mitigation Coverage (% rischi con contromisura definita)**
  - Baseline: 0%
  - Target D14: >=85%

## Rischi principali (cross-stream)

1. **R1 — Ambiguità di priorità tra stream**
   - Impatto: Alto | Probabilità: Media
   - Trigger: backlog crescente, continui reprioritization
   - Mitigazione: matrice priorità unica + decision owner singolo

2. **R2 — Colli di bottiglia operativi nel layer agentico**
   - Impatto: Alto | Probabilità: Media-Alta
   - Trigger: ciclo task >48h, revisione ripetuta
   - Mitigazione: standard template + reviewer dedicato + regole escalation

3. **R3 — Assunzioni tokenomics non realistiche**
   - Impatto: Alto | Probabilità: Media
   - Trigger: scenari divergenti/non sostenibili
   - Mitigazione: stress test 3 scenari + kill criteria espliciti

4. **R4 — Rischio compliance/regolatorio sottostimato**
   - Impatto: Molto Alto | Probabilità: Media
   - Trigger: blocchi su distribuzione/marketing/prodotto
   - Mitigazione: compliance-by-design preliminare + review legale esterna early

5. **R5 — Dispersione strategica (troppi fronti)**
   - Impatto: Alto | Probabilità: Alta
   - Trigger: >3 iniziative core contemporanee senza capacità
   - Mitigazione: WIP limit e stop-rule su iniziative non core

## Semaforo attuale
- Tokenization: 🔴 (fase iniziale)
- AI Agents: 🟠 (struttura in definizione)
- Strategie: 🟠 (direzione impostata, dettagli da consolidare)
