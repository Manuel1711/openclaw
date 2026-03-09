#!/usr/bin/env python3
"""
Collect ERC-8004 Identity + Reputation registry events on multiple chains and export to CSV.

Features:
- Multi-chain loop (Ethereum, Polygon, Base, Arbitrum, Avalanche, BNB)
- Auto-detect contract deployment block (binary search using eth_getCode)
- Retry/backoff on HTTP 429 (rate limit)
- Auto-split getLogs ranges when provider returns >10,000 results
- Per-chain output folders + per-chain manifest + global manifest
"""

import os
import json
import time
import csv
from dataclasses import dataclass
from typing import Dict, Any, List, Optional

import pandas as pd
from dotenv import load_dotenv
from requests.exceptions import HTTPError
from web3 import Web3
from web3._utils.events import get_event_data

# POA middleware (Polygon/BSC/Avalanche often need it)
from web3.middleware import geth_poa_middleware

load_dotenv()

# -----------------------
# Minimal ABIs (events only)
# -----------------------
IDENTITY_EVENTS_ABI = [
    # Registered(agentId, agentURI, owner)
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "internalType": "uint256", "name": "agentId", "type": "uint256"},
            {"indexed": False, "internalType": "string", "name": "agentURI", "type": "string"},
            {"indexed": True, "internalType": "address", "name": "owner", "type": "address"},
        ],
        "name": "Registered",
        "type": "event",
    },
    # MetadataSet(agentId, keyHash, metadataKey, metadataValue)
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "internalType": "uint256", "name": "agentId", "type": "uint256"},
            {"indexed": True, "internalType": "bytes32", "name": "keyHash", "type": "bytes32"},
            {"indexed": False, "internalType": "string", "name": "metadataKey", "type": "string"},
            {"indexed": False, "internalType": "bytes", "name": "metadataValue", "type": "bytes"},
        ],
        "name": "MetadataSet",
        "type": "event",
    },
    # ERC721 Transfer
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "internalType": "address", "name": "from", "type": "address"},
            {"indexed": True, "internalType": "address", "name": "to", "type": "address"},
            {"indexed": True, "internalType": "uint256", "name": "tokenId", "type": "uint256"},
        ],
        "name": "Transfer",
        "type": "event",
    },
]

REPUTATION_EVENTS_ABI = [
    # NewFeedback(...)
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "internalType": "uint256", "name": "agentId", "type": "uint256"},
            {"indexed": True, "internalType": "address", "name": "clientAddress", "type": "address"},
            {"indexed": False, "internalType": "uint64", "name": "feedbackIndex", "type": "uint64"},
            {"indexed": False, "internalType": "int128", "name": "value", "type": "int128"},
            {"indexed": False, "internalType": "uint8", "name": "valueDecimals", "type": "uint8"},
            {"indexed": True, "internalType": "string", "name": "indexedTag1", "type": "string"},
            {"indexed": False, "internalType": "string", "name": "tag1", "type": "string"},
            {"indexed": False, "internalType": "string", "name": "tag2", "type": "string"},
            {"indexed": False, "internalType": "string", "name": "endpoint", "type": "string"},
            {"indexed": False, "internalType": "string", "name": "feedbackURI", "type": "string"},
            {"indexed": False, "internalType": "bytes32", "name": "feedbackHash", "type": "bytes32"},
        ],
        "name": "NewFeedback",
        "type": "event",
    },
    # FeedbackRevoked(agentId, clientAddress, feedbackIndex)
    {
        "anonymous": False,
        "inputs": [
            {"indexed": True, "internalType": "uint256", "name": "agentId", "type": "uint256"},
            {"indexed": True, "internalType": "address", "name": "clientAddress", "type": "address"},
            {"indexed": False, "internalType": "uint64", "name": "feedbackIndex", "type": "uint64"},
        ],
        "name": "FeedbackRevoked",
        "type": "event",
    },
]

# -----------------------
# Config from env
# -----------------------
IDENTITY_REGISTRY = os.getenv("IDENTITY_REGISTRY", "").strip()
REPUTATION_REGISTRY = os.getenv("REPUTATION_REGISTRY", "").strip()

FROM_BLOCK = os.getenv("FROM_BLOCK", "0").strip()
TO_BLOCK = os.getenv("TO_BLOCK", "latest").strip()

OUT_DIR = os.getenv("OUT_DIR", "./erc8004_out").strip()
CHUNK_SIZE_DEFAULT = int(os.getenv("CHUNK_SIZE", "5000"))

if not (IDENTITY_REGISTRY and REPUTATION_REGISTRY):
    raise SystemExit("Missing registry addresses: IDENTITY_REGISTRY and/or REPUTATION_REGISTRY")

os.makedirs(OUT_DIR, exist_ok=True)

# -----------------------
# Chain list
# -----------------------
CHAINS = [
    # name, chainId, rpc env var, needs_poa_middleware
    ("ethereum", 1, "RPC_URL_ETHEREUM", False),
    ("polygon", 137, "RPC_URL_POLYGON", True),
    ("base", 8453, "RPC_URL_BASE", False),
    ("arbitrum", 42161, "RPC_URL_ARBITRUM", False),
    ("avalanche", 43114, "RPC_URL_AVALANCHE", True),
    ("bnb", 56, "RPC_URL_BNB", True),
]

# -----------------------
# Helpers
# -----------------------
@dataclass
class EventSpec:
    name: str
    abi: Dict[str, Any]
    address: str

def is_rate_limit_error(e: Exception) -> bool:
    if isinstance(e, HTTPError) and getattr(e, "response", None) is not None:
        return e.response.status_code == 429
    s = str(e)
    return "429" in s or "Too Many Requests" in s

def is_too_many_results_error(e: Exception) -> bool:
    s = str(e)
    return "more than 10000 results" in s or "query returned more than 10000 results" in s

def resolve_block(w3: Web3, x: str) -> int:
    if x == "latest":
        return w3.eth.block_number
    return int(x)

def checksum(w3: Web3, addr: str) -> str:
    return w3.to_checksum_address(addr)

def event_topic(w3: Web3, abi_event: Dict[str, Any]) -> str:
    types = ",".join([i["type"] for i in abi_event["inputs"]])
    sig = f"{abi_event['name']}({types})"
    return w3.keccak(text=sig).hex()

def fetch_logs_range(
    w3: Web3,
    address: str,
    topic0: str,
    start: int,
    end: int,
    max_retries: int = 8,
    base_sleep: float = 0.6
) -> List[Dict[str, Any]]:
    """
    Fetch logs for a block range.
    - Retries on 429 with exponential backoff.
    - Splits range recursively when provider refuses due to >10,000 results.
    """
    if start > end:
        return []

    attempt = 0
    while True:
        try:
            return w3.eth.get_logs({
                "fromBlock": start,
                "toBlock": end,
                "address": address,
                "topics": [topic0],
            })
        except Exception as e:
            if is_too_many_results_error(e):
                if start == end:
                    raise RuntimeError(f"Single block {start} exceeds provider log limit for {address}.") from e
                mid = (start + end) // 2
                left = fetch_logs_range(w3, address, topic0, start, mid, max_retries=max_retries, base_sleep=base_sleep)
                right = fetch_logs_range(w3, address, topic0, mid + 1, end, max_retries=max_retries, base_sleep=base_sleep)
                return left + right

            attempt += 1
            if attempt > max_retries or not is_rate_limit_error(e):
                raise
            sleep_s = base_sleep * (2 ** (attempt - 1))
            print(f"429 rate limit on get_logs({start}-{end}). Sleeping {sleep_s:.1f}s then retry...")
            time.sleep(sleep_s)

def find_deploy_block(w3: Web3, addr: str, latest: int) -> int:
    """
    Binary-search the first block where code at addr is non-empty.
    """
    code_latest = w3.eth.get_code(addr, block_identifier=latest)
    if code_latest in (b"", b"\x00"):
        raise RuntimeError(f"No contract code at {addr} on latest block {latest}.")

    lo, hi = 0, latest
    while lo < hi:
        mid = (lo + hi) // 2
        code = w3.eth.get_code(addr, block_identifier=mid)
        if code in (b"", b"\x00"):
            lo = mid + 1
        else:
            hi = mid
    return lo

def decode_logs(w3: Web3, raw_logs: List[Dict[str, Any]], abi_event: Dict[str, Any]) -> List[Dict[str, Any]]:
    decoded = []
    for log in raw_logs:
        try:
            evt = get_event_data(w3.codec, abi_event, log)
            row = {
                "blockNumber": log["blockNumber"],
                "transactionHash": log["transactionHash"].hex(),
                "logIndex": log["logIndex"],
                "address": log["address"],
                "event": abi_event["name"],
            }
            for k, v in evt["args"].items():
                if isinstance(v, (bytes, bytearray)):
                    row[k] = "0x" + bytes(v).hex()
                else:
                    row[k] = v
            decoded.append(row)
        except Exception as e:
            decoded.append({
                "blockNumber": log.get("blockNumber"),
                "transactionHash": log.get("transactionHash").hex() if log.get("transactionHash") else None,
                "logIndex": log.get("logIndex"),
                "address": log.get("address"),
                "event": abi_event["name"],
                "decodeError": str(e),
                "data": log.get("data"),
                "topics": [t.hex() if hasattr(t, "hex") else str(t) for t in log.get("topics", [])],
            })
    return decoded

def run_event_collection(
    w3: Web3,
    spec: EventSpec,
    start_block: int,
    end_block: int,
    chunk_size: int
) -> pd.DataFrame:
    t0 = event_topic(w3, spec.abi)
    rows: List[Dict[str, Any]] = []

    cur = start_block
    while cur <= end_block:
        b = min(end_block, cur + chunk_size - 1)
        raw = fetch_logs_range(w3, spec.address, t0, cur, b)
        rows.extend(decode_logs(w3, raw, spec.abi))
        print(f"[{spec.name}] blocks {cur}-{b}: {len(raw)} logs (chunk={chunk_size})")
        cur = b + 1
        time.sleep(0.05)

    if rows:
        return pd.DataFrame(rows).sort_values(["blockNumber", "logIndex"], ignore_index=True)
    return pd.DataFrame()

def build_w3(rpc_url: str, inject_poa: bool) -> Web3:
    w3 = Web3(Web3.HTTPProvider(rpc_url, request_kwargs={"timeout": 60}))
    if not w3.is_connected():
        raise RuntimeError(f"Cannot connect to RPC: {rpc_url}")
    if inject_poa:
        # must be early in middleware stack
        w3.middleware_onion.inject(geth_poa_middleware, layer=0)
    return w3


def safe_to_csv(df: pd.DataFrame, out_path: str) -> None:
    """
    Robust CSV writer for on-chain event data.
    Handles commas/quotes/newlines in string fields.
    """
    df.to_csv(
        out_path,
        index=False,
        quoting=csv.QUOTE_ALL,
        quotechar='"',
        escapechar='\\',
        lineterminator='\n',
    )

# -----------------------
# Main multi-chain runner
# -----------------------
def run_for_chain(name: str, expected_chain_id: int, rpc_env: str, inject_poa: bool) -> Optional[Dict[str, Any]]:
    rpc_url = os.getenv(rpc_env, "").strip()
    if not rpc_url:
        print(f"Skipping {name}: missing {rpc_env} in env.")
        return None

    print("\n" + "=" * 80)
    print(f"Chain: {name} (expected chainId={expected_chain_id})")
    print("=" * 80)

    w3 = build_w3(rpc_url, inject_poa=inject_poa)

    actual_chain_id = w3.eth.chain_id
    if actual_chain_id != expected_chain_id:
        raise RuntimeError(f"{name}: RPC chainId mismatch. expected {expected_chain_id}, got {actual_chain_id}")

    identity = checksum(w3, IDENTITY_REGISTRY)
    reputation = checksum(w3, REPUTATION_REGISTRY)

    to_block = resolve_block(w3, TO_BLOCK)
    from_block_user = resolve_block(w3, FROM_BLOCK)

    if from_block_user > to_block:
        raise RuntimeError(f"{name}: FROM_BLOCK ({from_block_user}) > TO_BLOCK ({to_block})")

    # output folder per chain
    chain_out = os.path.join(OUT_DIR, f"{name}_{actual_chain_id}")
    os.makedirs(chain_out, exist_ok=True)

    print(f"RPC: {rpc_url[:60]}{'...' if len(rpc_url) > 60 else ''}")
    print(f"Latest block: {to_block}")
    print("Detecting deployment blocks (binary search via eth_getCode)...")

    id_deploy = find_deploy_block(w3, identity, to_block)
    rep_deploy = find_deploy_block(w3, reputation, to_block)

    from_block_identity = max(from_block_user, id_deploy)
    from_block_reputation = max(from_block_user, rep_deploy)

    print(f"Identity deploy block ~ {id_deploy}. Using FROM_BLOCK={from_block_identity}")
    print(f"Reputation deploy block ~ {rep_deploy}. Using FROM_BLOCK={from_block_reputation}")

    event_specs = [
        ("identity_registered", IDENTITY_EVENTS_ABI[0], identity, from_block_identity),
        ("identity_metadataset", IDENTITY_EVENTS_ABI[1], identity, from_block_identity),
        ("identity_transfer", IDENTITY_EVENTS_ABI[2], identity, from_block_identity),
        ("reputation_newfeedback", REPUTATION_EVENTS_ABI[0], reputation, from_block_reputation),
        ("reputation_feedbackrevoked", REPUTATION_EVENTS_ABI[1], reputation, from_block_reputation),
    ]

    manifest = {
        "chainName": name,
        "chainId": actual_chain_id,
        "rpc": rpc_url[:40] + ("..." if len(rpc_url) > 40 else ""),
        "identityRegistry": identity,
        "reputationRegistry": reputation,
        "fromBlockRequested": from_block_user,
        "toBlock": to_block,
        "identityDeployBlock": id_deploy,
        "reputationDeployBlock": rep_deploy,
        "chunkSizeDefault": CHUNK_SIZE_DEFAULT,
        "files": {},
    }

    for (evt_name, abi, addr, start_blk) in event_specs:
        spec = EventSpec(evt_name, abi, addr)
        df = run_event_collection(w3, spec, start_blk, to_block, chunk_size=CHUNK_SIZE_DEFAULT)

        out_path = os.path.join(chain_out, f"{evt_name}.csv")
        safe_to_csv(df, out_path)
        manifest["files"][evt_name] = out_path
        print(f"Saved {len(df)} rows -> {out_path}")

    with open(os.path.join(chain_out, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    print(f"Done chain {name}. Output dir: {chain_out}")
    return manifest

def main() -> None:
    all_manifests: List[Dict[str, Any]] = []
    for (name, cid, rpc_env, poa) in CHAINS:
        try:
            m = run_for_chain(name, cid, rpc_env, poa)
            if m:
                all_manifests.append(m)
        except Exception as e:
            print(f"ERROR on {name}: {e}")

    out_all = {
        "generatedAt": int(time.time()),
        "outDir": OUT_DIR,
        "chains": all_manifests,
    }
    with open(os.path.join(OUT_DIR, "manifest_all.json"), "w", encoding="utf-8") as f:
        json.dump(out_all, f, indent=2)

    print("\nAll done.")
    print(f"Global manifest: {os.path.join(OUT_DIR, 'manifest_all.json')}")

if __name__ == "__main__":
    main()