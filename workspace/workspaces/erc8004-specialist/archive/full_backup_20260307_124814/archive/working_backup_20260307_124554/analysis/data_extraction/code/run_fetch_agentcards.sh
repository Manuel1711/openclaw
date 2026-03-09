#!/usr/bin/env bash

set -e

########################################
# CONFIG
########################################

# Percorso del CSV che hai già
export IDENTITY_REGISTERED_CSV="../../../data/latest/raw/ethereum_1/identity_registered.csv"

# Output files
export OUT_JSONL="../../../data/enriched/latest/ethereum_1/identity_agentcard.jsonl"
export OUT_FLAT="../../../data/enriched/latest/ethereum_1/identity_agentcard_flat.csv"

# Gateway IPFS (puoi cambiarlo)
export IPFS_GATEWAY="https://ipfs.io/ipfs/"

# Timeout HTTP
export HTTP_TIMEOUT=30
export MAX_OFFCHAIN_BYTES=5000000

########################################
# RUN
########################################

echo "=== Fetching ERC-8004 agent cards from identity_registered.csv ==="
python3 fetch_agentcards_ethereum.py
echo "=== DONE ==="