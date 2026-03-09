# SC_SUPERVISION_KPI

KPI per misurare qualità di supervisione (non solo output tecnico).

## KPI core
1. **First-pass acceptance rate**
   - % deliverable specialist accettati al primo review
2. **Review turnaround time**
   - Tempo medio da outbox specialist a decisione SC
3. **Recurring bug elimination**
   - # bug ricorrenti risolti definitivamente / periodo
4. **Learning extraction rate**
   - # lezioni trasferibili documentate / settimana
5. **Cross-context transfer**
   - # regole applicate con successo in contesti diversi
6. **Decision quality mix**
   - Distribuzione GO/HOLD/KILL e outcome successivo

## Target iniziali (v1)
- First-pass acceptance >= 70%
- Review turnaround <= 6h su task caldi
- >= 3 lesson trasferibili/settimana
- 0 retry storm / 0 duplicate canonical sessions

## Reporting cadence
- Daily: mini stato KPI critici
- Weekly: review completa + update playbook
