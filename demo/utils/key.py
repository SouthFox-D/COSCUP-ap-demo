#!/usr/bin/env python3
"""process Key."""
from pathlib import Path
from Crypto.PublicKey import RSA
from demo.config import KEY_PATH


def get_pubkey_as_pem(key_path: Path) -> str:
    """Exporting public key from private key file."""
    text = key_path.read_text()
    return RSA.import_key(text).public_key().export_key("PEM").decode("utf-8")
