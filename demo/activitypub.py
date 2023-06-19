#!/usr/bin/env python3
"""ActivityPub settings, fetch & post"""
import httpx
from demo import config


def fetch(
        url: str,
) -> dict:
    """Fetch url and return json"""
    print(f"fetch {url}")

    with httpx.Client() as client:
        resp = client.get(
            url,
            headers={
                "User-Agent": config.USER_AGENT,
                "Accept": config.AP_CONTENT_TYPE,
            }
        )

    return resp.json()
