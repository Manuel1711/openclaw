# Company Control Center

Cartella centrale di governo operativo gestita da Cassia.

## Sottocartelle
- `tasks/` → task ufficiali assegnati ai bot lead
- `reports/` → report consolidati da Cassia verso Manuel
- `decisions/` → decision records operativi (oltre al log in MEMORY.md)
- `THREAD_ORCHESTRATION_PLAYBOOK.md` → protocollo operativo thread-bound (spawn order, restart discipline, cleanup stale)

## Processo
1. Cassia crea task in `tasks/`
2. Bot eseguono nei loro workspace dedicati
3. Bot consegnano in `outbox/`
4. Cassia valida e pubblica sintesi in `reports/`
