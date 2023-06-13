from flask import Request, abort
from demo.httpsig import HttpSignature


def inbox_prechecker(
        request: Request,
) -> bool:
    try:
        payload = request.headers
        parsec_signature = HttpSignature.parse_signature(
            payload["signature"]
        )
        print(parsec_signature)
    except KeyError:
        abort(401, "Missing signature key!")

    return True
