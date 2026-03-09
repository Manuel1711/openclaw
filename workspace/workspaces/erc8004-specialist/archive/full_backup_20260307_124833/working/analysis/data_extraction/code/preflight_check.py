#!/usr/bin/env python3
import os
import sys
from pathlib import Path
from datetime import datetime

BASE = Path('/home/manuel/.openclaw/workspace/workspaces/erc8004-specialist')
CODE = BASE / 'working/analysis/data_extraction/code'
CFG_ENV = BASE / 'working/analysis/data_extraction/config/.env'
DATA = BASE / 'working/data'
RUNLOGS = BASE / 'runlogs'
LOCK = BASE / '.run_active.lock'

required_paths = [
    CODE / 'collect_erc8004_events.py',
    CFG_ENV,
    DATA / 'raw',
    DATA / 'latest',
    RUNLOGS,
]

missing = [str(p) for p in required_paths if not p.exists()]
if missing:
    print('PREFLIGHT_FAIL: missing paths:')
    for m in missing:
        print(f' - {m}')
    sys.exit(1)

# load env (without printing values)
for line in CFG_ENV.read_text(encoding='utf-8').splitlines():
    s = line.strip()
    if not s or s.startswith('#') or '=' not in s:
        continue
    k, v = s.split('=', 1)
    os.environ.setdefault(k.strip(), v.strip())

required_env = ['IDENTITY_REGISTRY', 'REPUTATION_REGISTRY', 'RPC_URL_ETHEREUM']
missing_env = [k for k in required_env if not os.getenv(k)]
if missing_env:
    print('PREFLIGHT_FAIL: missing required env keys:')
    for k in missing_env:
        print(f' - {k}')
    sys.exit(2)

# lock status (informational guard)
if LOCK.exists():
    print(f'PREFLIGHT_FAIL: active run lock present: {LOCK}')
    sys.exit(3)

# writeability checks
try:
    test = RUNLOGS / '.preflight_write_test'
    test.write_text('ok', encoding='utf-8')
    test.unlink()
except Exception as e:
    print(f'PREFLIGHT_FAIL: runlogs not writable: {e}')
    sys.exit(4)

print('PREFLIGHT_OK')
print(f'timestamp={datetime.now().isoformat(timespec="seconds")}')
print('paths=OK env=OK lock=FREE write=OK')
