#!/usr/bin/env python3
import os, json, time, base64, re
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

IN_CSV = os.getenv("IDENTITY_REGISTERED_CSV", "identity_registered.csv")
OUT_JSONL = os.getenv("OUT_JSONL", "identity_agentcard.jsonl")
OUT_FLAT = os.getenv("OUT_FLAT", "identity_agentcard_flat.csv")

IPFS_GATEWAY = os.getenv("IPFS_GATEWAY", "https://ipfs.io/ipfs/").rstrip("/") + "/"
HTTP_TIMEOUT = int(os.getenv("HTTP_TIMEOUT", "30"))
MAX_BYTES = int(os.getenv("MAX_OFFCHAIN_BYTES", "5000000"))

def normalize_uri(uri: str) -> str:
    if uri.startswith("ipfs://"):
        return IPFS_GATEWAY + uri[len("ipfs://"):].lstrip("/")
    return uri

def is_data_uri(uri: str) -> bool:
    return uri.startswith("data:")

def decode_data_uri(uri: str):
    m = re.match(r"data:([^;,]+)?(;base64)?,(.*)$", uri, flags=re.IGNORECASE | re.DOTALL)
    if not m:
        raise ValueError("Invalid data URI")
    mime = m.group(1) or "text/plain"
    is_b64 = m.group(2) is not None
    data_part = m.group(3) or ""
    if is_b64:
        return base64.b64decode(data_part), mime
    return data_part.encode("utf-8", errors="replace"), mime

def fetch_json_from_uri(uri: str):
    if not uri or not isinstance(uri, str):
        return None, {"error": "empty uri"}

    rec = {"uri": uri, "resolvedUri": None, "status": None, "contentType": None, "bytes": None, "error": None}

    try:
        if is_data_uri(uri):
            payload, mime = decode_data_uri(uri)
            rec["resolvedUri"] = "data:"
            rec["status"] = 200
            rec["contentType"] = mime
            rec["bytes"] = len(payload)
            if len(payload) > MAX_BYTES:
                rec["error"] = f"too large: {len(payload)}"
                return None, rec
            return json.loads(payload.decode("utf-8", errors="replace")), rec

        url = normalize_uri(uri)
        rec["resolvedUri"] = url
        if not (url.startswith("http://") or url.startswith("https://")):
            rec["error"] = f"unsupported scheme: {url[:20]}"
            return None, rec

        r = requests.get(url, timeout=HTTP_TIMEOUT, headers={"User-Agent": "erc8004-agentcard-fetch/1.0"})
        rec["status"] = r.status_code
        rec["contentType"] = r.headers.get("Content-Type")
        content = r.content or b""
        rec["bytes"] = len(content)

        if len(content) > MAX_BYTES:
            rec["error"] = f"too large: {len(content)}"
            return None, rec
        if r.status_code != 200:
            rec["error"] = f"http {r.status_code}"
            return None, rec

        return r.json(), rec

    except Exception as e:
        rec["error"] = f"{type(e).__name__}: {e}"
        return None, rec

def flatten_agentcard(agentId: int, card: dict) -> dict:
    # flatten minimo e robusto
    out = {
        "agentId": agentId,
        "type": card.get("type"),
        "name": card.get("name"),
        "description": card.get("description"),
        "image": card.get("image"),
        "active": card.get("active"),
        "x402Support": card.get("x402Support"),
        "supportedTrust": ",".join(card.get("supportedTrust", []) or []),
    }
    # services: prova a estrarre service wallet se presente
    services = card.get("services") or []
    wallet = None
    for s in services:
        if isinstance(s, dict) and s.get("name") == "wallet":
            wallet = s.get("endpoint")
            break
    out["service_wallet_endpoint"] = wallet

    # registrations: salva come stringa
    regs = card.get("registrations") or []
    out["registrations"] = json.dumps(regs, ensure_ascii=False)

    return out

def main():
    df = pd.read_csv(IN_CSV)
    if "agentId" not in df.columns or "agentURI" not in df.columns:
        raise SystemExit("Il CSV deve contenere colonne agentId e agentURI")

    df = df.dropna(subset=["agentId", "agentURI"]).copy()
    # Dedup per agentId tenendo l’ultimo agentURI (se ci sono più Registered)
    df = df.sort_values(["agentId", "blockNumber", "logIndex"], ascending=True)
    df = df.groupby("agentId").tail(1)

    jsonl_rows = []
    flat_rows = []

    for _, r in df.iterrows():
        agentId = int(r["agentId"])
        uri = str(r["agentURI"])

        card, meta = fetch_json_from_uri(uri)
        row = {
            "agentId": agentId,
            "agentURI": uri,
            "fetchedAt": int(time.time()),
            "fetchMeta": meta,
            "card": card,
        }
        jsonl_rows.append(row)

        if isinstance(card, dict):
            flat_rows.append(flatten_agentcard(agentId, card))

        if agentId % 100 == 0:
            print(f"Processed agentId={agentId}")

    with open(OUT_JSONL, "w", encoding="utf-8") as f:
        for r in jsonl_rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    pd.DataFrame(flat_rows).to_csv(OUT_FLAT, index=False)
    print(f"Saved: {OUT_JSONL}")
    print(f"Saved: {OUT_FLAT}")

if __name__ == "__main__":
    main()