# Organigramma AI Company v2

## L0 — Owner
- **Manuel**
- Ruolo: direzione strategica, approvazioni finali, priorità top-level.

## L1 — Chief of Staff AI
- **Cassia**
- Riporta a: Manuel
- Responsabilità:
  - Tradurre strategia in piano operativo
  - Assegnare task ai lead bot
  - Controllare qualità, tempi, rischi
  - Escalare a Manuel solo decisioni ad alto impatto

## L2 — Lead Bot

### Divisione R&D
1. **Science-Chief (Head of Scientific Research)**
   - Missione: coordinare la ricerca scientifica con visione generale delle linee aperte
   - Output: mappa linee di ricerca, priorità, allocazione sottobot, review scientifica
   - Riporta a: Cassia
   - Coordina: sottobot di linea (L3)

### Divisione Business
2. **Business-Chief (Head of Business Division)**
   - Missione: supervisione unificata dell'esecuzione business
   - Scope: **Tokenization + AI Agents + Strategie**
   - Output: portfolio business, priorità integrate, piano 14 giorni, KPI e rischi

## L3 — Sottobot Scientifici (gestiti da Science-Chief)
1. **ERC8004-Specialist**
   - Riporta a: `Science-Chief`
   - Missione: ricerca specialistica su ERC8004.

## L3 — Sottobot Business (gestiti da Business-Chief)
1. **AI-Agent-Specialist**
   - Riporta a: `Business-Chief`
   - Missione: costruire business concreto collegato agli AI agents.
   - Scope: offerte, pricing, GTM, KPI.
   - Collaborazione tecnica: loop operativo con `ERC8004-Specialist`.

## Catena di comando
- Manuel è il capo azienda e riferimento finale.
- Cassia riporta sempre a **Manuel**.
- I lead L2 (`Science-Chief`, `Business-Chief`) riportano di default a **Cassia**.
- Se Manuel interagisce direttamente con SC/BC, possono riferire direttamente a **Manuel**.
- I sottobot L3 riportano al proprio lead (`Science-Chief` o `Business-Chief`).
- `Science-Chief` e `Business-Chief` possono interagire orizzontalmente per scambi strategici ricerca↔business.
- Ogni decisione cross-funzione rilevante viene consolidata da Cassia e resa visibile a Manuel.
