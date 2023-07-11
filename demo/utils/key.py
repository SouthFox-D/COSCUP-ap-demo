#!/usr/bin/env python3
"""process Key."""

import sys

from pathlib import Path
from Crypto.PublicKey import RSA
from demo.config import KEY_PATH


def get_pubkey_as_pem(key_path: Path) -> str:
    """Exporting public key from private key file."""
    text = key_path.read_text()
    return RSA.import_key(text).public_key().export_key("PEM").decode("utf-8")


def gen_key():
    """Generate key."""
    if KEY_PATH.exists():
        print("is existing!")
        sys.exit(2)
    else:
        k = RSA.generate(2048)
        privkey_pem = k.exportKey("PEM").decode("utf-8")
        KEY_PATH.write_text(privkey_pem)
