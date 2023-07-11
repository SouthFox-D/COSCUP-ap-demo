#!/usr/bin/env python3
"""Something misc."""
import sys
import click

from Crypto.PublicKey import RSA
from demo import config


@click.command()
def gen_key():
    """Generate key."""
    if config.KEY_PATH.exists():
        print("Key is existing!")
        sys.exit(2)
    else:
        k = RSA.generate(2048)
        privkey_pem = k.exportKey("PEM").decode("utf-8")
        config.KEY_PATH.write_text(privkey_pem)
        print("Done!")


if __name__ == "__main__":
    gen_key()
