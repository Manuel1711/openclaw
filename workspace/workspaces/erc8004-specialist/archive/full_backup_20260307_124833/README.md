# ERC8004-Specialist Workspace

Workspace operativo per il filone ERC-8004.

## Obiettivo
Costruire una base tecnico-scientifica solida (teoria + evidenza) su ERC-8004 e trasformarla in output riusabili (paper, note, piani sperimentali, materiali business-facing).

## Struttura
- `inbox/` task in ingresso
- `working/` analisi in corso
- `outbox/` deliverable pronti
- `logs/` decisioni e stato

## Fonte principale attuale
- Progetto Overleaf: `ERC8004` (main.tex)

## Reporting protocol (default corrente)
1. ERC8004-Specialist scrive aggiornamenti dettagliati in `outbox/`
2. Science-Chief legge/revisiona
3. Science-Chief invia sintesi concisa dei principal results a Cassia
4. Cassia riporta a Manuel
5. Deep-dive diretto con bot specifico solo su richiesta esplicita di Manuel

## Regole operative vincolanti (Manuel)
- **Prima di qualsiasi modifica su Overleaf, chiedere SEMPRE permesso esplicito a Manuel.**
- Consentito senza permesso: lettura, analisi, preparazione bozze in locale.
- Non consentito senza permesso: edit file, compile finalizzate a cambi strutturali, rename, delete, upload su Overleaf.
- **Quando Manuel parla con lo Specialist, la risposta deve essere tecnica e dettagliata**: includere file coinvolti, comandi/pipeline, motivazioni, output, errori e limiti (no solo sintesi alta).

## Struttura operativa v3 (attiva)
- `inbox/`, `outbox/`, `logs/` invariati (protocollo)
- `working/data/` dati operativi (`raw`, `enriched`, `analytics`, `latest`)
- `analysis/` area analisi (risultati, note, figure PDF)
- `pipeline/extraction/` con `code/`, `config/`, `docs/`
- `analysis/results/` output analitici e figure finali (PDF)
- `runlogs/` log runtime completi
- `archive/` storico

