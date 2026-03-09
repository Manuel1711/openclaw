# MVP_ERC8004_REBUILD_WORKING_2026-03-09

## Scope
Rebuilt ERC8004 dApp MVP and continuous indexer with canonical location only under `working/`.

## Canonical path
`/home/manuel/.openclaw/workspace/workspaces/ai-agent-specialist/working/erc8004-dapp-mvp`

## Delivered
- Pages: `index.html`, `agents.html`, `agent.html`
- Frontend: `assets/app.js`, `assets/styles.css`
- Snapshot data: `data/identity_registry.snapshot.json`, `data/feedback_registry.snapshot.json`, `data/agents.snapshot.json`
- Build pipeline: `scripts/build-snapshot.mjs`
- Continuous loop: `scripts/indexer-loop.mjs`, `scripts/run-indexer.sh`, `.env.example`
- Docs: `README.md`

## Validation
- Snapshot build executed successfully.
- Indexer script syntax check passed.

## Run
```bash
cd /home/manuel/.openclaw/workspace/workspaces/ai-agent-specialist/working/erc8004-dapp-mvp
node scripts/build-snapshot.mjs
python3 -m http.server 5173
```

Continuous mode:
```bash
cp .env.example .env
# set ETH_RPC_URL
./scripts/run-indexer.sh
```
