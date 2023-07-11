"""Request checker"""
import json

from flask import Request, abort
from demo.httpsig import HttpSignature, SignedData
from demo.actor import fetch_actor


def inbox_prechecker(
        request: Request,
) -> bool:
    """Inbox request prechecker"""
    payload = request.headers
    ap_body = request.data
    try:
        parsed_signature = HttpSignature.parse_signature(
            payload["signature"]
        )
    except KeyError:
        abort(401, "Missing signature key!")

    actor_id = request.get_json()["actor"]
    actor = fetch_actor(actor_id)

    try:
        pub_key = actor["publicKey"]["publicKeyPem"]
    except json.JSONDecodeError as exc:
        raise ValueError from exc
    except KeyError as exc:
        print("actore gone?")
        raise KeyError from exc

    sigdate = SignedData(
        method = request.method,
        path = request.path,
        signed_list = parsed_signature["headers"],
        body_digest = HttpSignature.calculation_digest(ap_body),
        headers = request.headers,
    )

    is_verify = HttpSignature.verify_signature(
        HttpSignature.build_signature_string(sigdate),
        parsed_signature["signature"],
        pub_key,
    )

    return is_verify
