#!/usr/bin/env python3
"""ActivityPub Actor"""
import demo.activitypub as ap


def fetch_actor(
        actor_url: str,
) -> dict:
    """Fetch actor"""
    ap_object = ap.fetch(actor_url)
    return ap_object
