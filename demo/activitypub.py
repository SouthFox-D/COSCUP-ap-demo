#!/usr/bin/env python3
"""ActivityPub settings, fetch & post"""
import httpx
from demo import config
from demo.utils.key import get_pubkey_as_pem


AS_CTX = "https://www.w3.org/ns/activitystreams"
AS_PUBLIC = "https://www.w3.org/ns/activitystreams#Public"

AS_EXTENDED_CTX = [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1",
    {
        # AS ext
        "Hashtag": "as:Hashtag",
        "sensitive": "as:sensitive",
        "manuallyApprovesFollowers": "as:manuallyApprovesFollowers",
        "alsoKnownAs": {"@id": "as:alsoKnownAs", "@type": "@id"},
        "movedTo": {"@id": "as:movedTo", "@type": "@id"},
        # toot
        "toot": "http://joinmastodon.org/ns#",
        "featured": {"@id": "toot:featured", "@type": "@id"},
        "Emoji": "toot:Emoji",
        "blurhash": "toot:blurhash",
        "votersCount": "toot:votersCount",
    },
]

ME = {
    "@context": AS_EXTENDED_CTX,
    "type": "Person",
    "id": config.ID,
    "following": config.BASE_URL + "/following",
    "followers": config.BASE_URL + "/followers",
    "featured": config.BASE_URL + "/featured",
    "inbox": config.BASE_URL + "/inbox",
    "outbox": config.BASE_URL + "/outbox",
    "preferredUsername": config.USERNAME,
    "name": config.NICKNAME,
    "summary": config.ACTOR_SUMMARY,
    "endpoints": {
        "sharedInbox": config.BASE_URL + "/inbox",
    },
    "url": config.ID + "/",  # the path is important for Mastodon compat
    "manuallyApprovesFollowers": False,
    "attachment": [],
    "icon": {
        "mediaType": "image/png",
        "type": "Image",
        "url": config.AVATAR_URL,
    },
    "publicKey": {
        "id": f"{config.ID}#main-key",
        "owner": config.ID,
        "publicKeyPem": get_pubkey_as_pem(config.KEY_PATH),
    },
    "tag": [] # TODO tag support
}


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
