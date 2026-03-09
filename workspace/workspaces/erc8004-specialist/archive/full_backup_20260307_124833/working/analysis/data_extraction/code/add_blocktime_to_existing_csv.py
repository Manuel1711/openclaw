#!/usr/bin/env python3
import os
import time
import pandas as pd
from web3 import Web3
from dotenv import load_dotenv

# -----------------------
# CONFIG
# -----------------------
DATA_DIR = "/home/manuel/Documents/AI_agents/erc8004-data/out/ethereum_1"
RPC_ENV_VAR = "RPC_URL_ETHEREUM"   # deve essere nel tuo .env
OVERWRITE = True                  # se False crea file *_with_time.csv

# Progress / robustness
PRINT_EVERY = 100                 # stampa progresso ogni N blocchi
SAVE_CACHE_EVERY = 500            # salva cache ogni N blocchi (per non perdere lavoro)
SAVE_CACHE_AFTER_EACH_FILE = True # salva cache anche a fine file
MAX_RETRIES = 8                   # retry su errori (incl. rate limit)
BASE_SLEEP = 0.6                  # backoff base

load_dotenv()

rpc_url = os.getenv(RPC_ENV_VAR, "").strip()
if not rpc_url:
    raise SystemExit(f"Missing {RPC_ENV_VAR} in .env")

w3 = Web3(Web3.HTTPProvider(rpc_url, request_kwargs={"timeout": 60}))
if not w3.is_connected():
    raise RuntimeError("RPC not connected")

# -----------------------
# Cache blocchi
# -----------------------
cache_path = os.path.join(DATA_DIR, "block_times_cache.csv")

def load_cache(path: str) -> dict:
    if os.path.exists(path) and os.path.getsize(path) > 0:
        try:
            cdf = pd.read_csv(path)
            if {"blockNumber", "blockTime"}.issubset(cdf.columns):
                return {int(b): int(t) for b, t in zip(cdf["blockNumber"], cdf["blockTime"])}
        except pd.errors.EmptyDataError:
            pass
    return {}

def save_cache(path: str, cache: dict) -> None:
    cdf = pd.DataFrame(
        sorted(cache.items(), key=lambda x: x[0]),
        columns=["blockNumber", "blockTime"]
    )
    cdf.to_csv(path, index=False)

def is_rate_limit_error(e: Exception) -> bool:
    s = str(e).lower()
    return ("429" in s) or ("too many requests" in s) or ("rate limit" in s)

def get_block_timestamp(block_number: int) -> int:
    attempt = 0
    while True:
        try:
            blk = w3.eth.get_block(int(block_number))
            return int(blk["timestamp"])
        except Exception as e:
            attempt += 1
            if attempt > MAX_RETRIES:
                raise
            sleep_s = BASE_SLEEP * (2 ** (attempt - 1))
            if is_rate_limit_error(e):
                print(f"    rate limit on block {block_number} (retry {attempt}/{MAX_RETRIES}), sleeping {sleep_s:.1f}s")
            else:
                print(f"    error on block {block_number}: {e} (retry {attempt}/{MAX_RETRIES}), sleeping {sleep_s:.1f}s")
            time.sleep(sleep_s)

block_cache = load_cache(cache_path)
print(f"Loaded cache: {len(block_cache)} block timestamps")

# -----------------------
# Process all CSV with blockNumber
# -----------------------
files = sorted([f for f in os.listdir(DATA_DIR) if f.endswith(".csv")])

for fname in files:
    path = os.path.join(DATA_DIR, fname)

    # Skip empty (0 bytes) files
    if os.path.getsize(path) == 0:
        print(f"Skipping {fname}: empty file (0 bytes).")
        continue

    # Read CSV safely
    try:
        df = pd.read_csv(path)
    except pd.errors.EmptyDataError:
        print(f"Skipping {fname}: pandas EmptyDataError (no columns).")
        continue

    if "blockNumber" not in df.columns:
        # Not an event file
        continue

    print(f"\nProcessing {fname}")

    df["blockNumber"] = pd.to_numeric(df["blockNumber"], errors="coerce").astype("Int64")
    unique_blocks = df["blockNumber"].dropna().astype(int).unique().tolist()
    unique_blocks.sort()

    missing_blocks = [b for b in unique_blocks if b not in block_cache]
    print(f"  unique blocks: {len(unique_blocks)} | missing in cache: {len(missing_blocks)}")

    # Fetch missing block timestamps with progress + periodic cache save
    for i, b in enumerate(missing_blocks, start=1):
        block_cache[int(b)] = get_block_timestamp(int(b))

        if (i % PRINT_EVERY) == 0 or i == len(missing_blocks):
            print(f"  fetched {i}/{len(missing_blocks)} missing block timestamps")

        if (i % SAVE_CACHE_EVERY) == 0:
            save_cache(cache_path, block_cache)
            print(f"  cache checkpoint saved ({len(block_cache)} blocks) -> {cache_path}")

    # Add time columns
    df["blockTime"] = df["blockNumber"].astype(int).map(block_cache)
    df["blockDateUTC"] = pd.to_datetime(df["blockTime"], unit="s", utc=True).dt.date.astype(str)

    if OVERWRITE:
        df.to_csv(path, index=False)
        print(f"  wrote (overwrite) -> {path}")
    else:
        new_path = path.replace(".csv", "_with_time.csv")
        df.to_csv(new_path, index=False)
        print(f"  wrote -> {new_path}")

    if SAVE_CACHE_AFTER_EACH_FILE:
        save_cache(cache_path, block_cache)
        print(f"  cache saved after file ({len(block_cache)} blocks) -> {cache_path}")

# Final cache save
save_cache(cache_path, block_cache)

print("\nDone.")
print(f"Block cache saved to {cache_path} ({len(block_cache)} blocks)")