# ROUND-2 (BLINDATA) — Acceptance Criteria vincolanti

Tema: robustezza interpretativa tag1/NA.
Obiettivo: ridurre ambiguità su `NA_unmapped` e quantificare stabilità semantica.

## Deliverable obbligatori
D1) `outbox/normalization_map_v1.csv`
D2) `outbox/na_partition_audit.csv`
D3) `outbox/sensitivity_v1_v2_report.md` (con metriche)
D4) `outbox/delta_rank_A_vs_B.csv` + plot (`.pdf` preferito; `.png` ammesso intermedio)

## Criteri di accettazione numerici (vincolanti)
A1) Partizione NA disgiunta e chiusa:
- `raw_missing + parse_error + unmapped = totale_NA`
- errore consentito: **0**

A2) Copertura mapping v1 e v2:
- riportare `%` + `N` assoluti

A3) Rank stability top-k (k=10):
- riportare `overlap@10`
- riportare `Kendall` e/o `Spearman`

A4) Delta quote top-tag tra scenario:
- A = NA incluso
- B = NA escluso
- tabella completa per top-tag

A5) Tracciabilità numeri:
- ogni numero deve avere path sorgente esplicito

## SLA
- checkpoint iniziale entro 10 min
- chiusura round entro 30 min salvo blocker esplicito

## Formato risposta
1) Method
2) Results
3) Problems/Limitations
4) Confidence
5) Next Actions

+ indicare decisione proposta GO/HOLD su uso semantico `tag1` in report esterni.
