# Science-Chief MEMORY

## Persistent Operating Directives

### 1) Real-time outbox ping protocol (mandatory)
Whenever SC publishes any new file in outbox, immediately ping Cassia with:
1. file path(s)
2. checkpoint tag (C1/C2/C3/C4)
3. one-line summary
No delay.

### 1-bis) PDF delivery in chat (Manuel directive)
- Every time SC finishes a milestone report and compiles final PDF(s), SC must send the PDF files directly in chat to Manuel.
- Sending only file paths is not sufficient unless explicitly requested.
- This applies to all future report closures.

### 1-ter) Mandatory path appendix for figures/tables (Manuel directive)
- Whenever a report contains figures and/or tables, add at the end a dedicated appendix section listing the exact source paths for all included figures and tables.
- Path appendix is mandatory for reproducibility and navigation.

### 1-quater) Push-triggered SC review (Manuel directive)
- SC final review/report starts on Specialist completion sentinel:
  `outbox/CPF_DONE_<task>_<date>.md`.
- This sentinel is the primary trigger; periodic polling is fallback only.

### 2) Mandatory 5-block reporting standard (SC -> Cassia)
All technical summaries must be punctual, precise, scientifically rigorous, and always include:
1. method/procedure
2. key results
3. limitations/problems
4. confidence level
5. next actions

### 2-bis) Milestone paper-style reporting (Manuel directive)
- For every Specialist milestone, SC must read all Specialist deliverables carefully.
- SC must reorganize and synthesize results into a paper-style file.
- Canonical destination: `outbox/Reports/`.
- Hard format: milestone report as `.tex` (single document with text + figures + tables), plus compiled `.pdf`.
- Naming rule: `.tex` and `.pdf` must include delivery name + date.
- Source folders per milestone are mandatory:
  - `Reports/<delivery_name_date>/figures/`
  - `Reports/<delivery_name_date>/tables/`
- Language rule: highly accurate and scientific, but also basic and fully explanatory.
- Writing format standard: manuscript-style continuous scientific prose (not bullet-only reporting), with explicit narrative interpretation of each figure/table in the Results and Discussion sections.
- Mandatory data-description block in every report:
  1) what the data represent,
  2) where they come from,
  3) why we extracted them (research question),
  4) how extraction was done (registry interaction, with contract addresses),
  5) full schema explanation (columns/fields linked back to registry events).
- One file per milestone, with clear scientific schema:
  1) Title/Scope
  2) Data & Methods
  3) Results (with figure/table pointers)
  4) Robustness & Limitations
  5) Scientific Interpretation (SC-only)
  6) Decision (GO/HOLD/KILL)
  7) Next Actions

### 3) ERC8004 reporting chain (default)
ERC8004-Specialist writes detailed technical updates in specialist outbox ->
SC reads/reviews and produces compact decision-grade summary ->
Cassia reports to Manuel ->
direct deep-dive with specific bot only on explicit Manuel request.

### 4) SC outbox style rule (Manuel directive)
SC outbox files must contain only SC-extracted synthesis and evaluation:
- concise summary of what SC extracted,
- SC critical assessment,
- GO/HOLD/KILL decision,
- navigation pointers to specialist outputs (essential only),
- next actions.
Do not replicate specialist deep technical detail in SC outbox. Deep details remain specialist-only on demand.

### 4) Workspace workflow convention (mandatory for ERC8004 stream)
- `inbox/` = incoming tasks only.
- `working/` = active technical workbench only.
- `outbox/` = decision-ready final deliverables only.
- `logs/` = operational trace and supervision notes.

Specialist working standard accepted by Manuel:
- `working/src/` stable code
- `working/runs/` run-scoped execution
- `working/data/raw|processed`
- `working/analysis/notebooks|scripts`
- `working/results/figures|tables|summaries`
- Promote only validated outputs from `working/` to `outbox/`.

### 5) `src/` promotion governance (SC approval required)
`ERC8004-Specialist` cannot self-promote code to `working/src/` without SC approval.

### 6) Role boundary hard rule (Manuel override)
- SC = capo scientifico e unico owner dell'interpretazione finale.
- Specialist = execution layer (code + figures + technical artifacts).
- Nessuna conclusione scientifica esterna senza validazione SC.
- In caso di delivery non consegnata: escalation immediata con SLA rinegoziato e tracciato.

Approval principles (SC must verify all):
1. **Reusability**: code used/planned for multiple runs, not one-off.
2. **Stability**: no ad-hoc hacks; deterministic behavior on current datasets.
3. **Interface clarity**: explicit inputs/outputs/parameters.
4. **Minimum documentation**: short usage note + purpose.
5. **Evidence**: at least one successful run log referencing the code.
6. **Non-regression**: promotion does not break existing workflow.

Process:
- Specialist proposes (path + reason + evidence).
- SC approves/rejects explicitly.
- Decision recorded in logs (reason + timestamp + affected files).

### 7) Pipeline permanente richiesto da Manuel (SC↔Specialist)
- SC fa la parte di ragionamento/scelta scientifica e genera task produttivi puntuali.
- Specialist esegue e produce solo artifact (codice Python + immagini/tabelle + output), senza discussioni non richieste.
- Dopo consegna Specialist, SC legge i file e produce il report finale.
- Post-report: housekeeping obbligatorio (inbox done -> archive, outbox storico -> archive) per mantenere outbox lean.
- Nei report SC usare riferimenti ai path finali in archivio, non path temporanei pre-spostamento.
- Policy universale (tutti i task): fast-delivery misurabile, no status senza artifact, handoff template unico, archive immediato post-CPF.

