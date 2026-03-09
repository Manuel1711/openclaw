# OUTBOX_PING_PROTOCOL

Effective: 2026-03-07 10:15 GMT+1
Status: MANDATORY

## Rule
Whenever Business-Chief (or any Business-Chief subbot) publishes any **new file** in `outbox/`, send an immediate completion ping to **Cassia** including:

1. File path(s)
2. Milestone tag
3. One-line summary

## Ping format (standard)
- Paths: <file1>, <file2>, ...
- Milestone: <Mx / D3 / D7 / D10 / D14 / ADHOC>
- Summary: <single line>
- Reporting block (mandatory standard):
  1) Method/Procedure
  2) Key Results
  3) Limitations/Problems
  4) Confidence Level
  5) Next Actions

## SLA
- Send ping immediately after file write completion (no batching delay).

## Scope
- Applies to Business-Chief + all delegated subbots under Business-Chief.
