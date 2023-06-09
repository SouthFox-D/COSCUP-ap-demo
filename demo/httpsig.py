#!/usr/bin/env python3
"""
Verify and build HTTP signatures
"""
import base64

from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA


class HttpSignature:
    """
    calculation and verification of HTTP signatures
    """
    @classmethod
    def calculation_digest(
            cls,
            body : bytes,
            algorithm : str ="sha-256"
    ) -> str:
        """
        Calculates the digest header value for a given HTTP body
        """
        if "sha-256" == algorithm:
            body_digest = SHA256.new()
            body_digest.update(body)
            return "SHA-256=" + \
                base64.b64encode(body_digest.digest()
                                 ).decode("utf-8")

        raise ValueError(f"No support algorithm {algorithm}")

    @classmethod
    def verify_signature(
            cls,
            signature_string : str,
            signature : bytes,
            pubkey,
    ) -> bool:
        """
        Verify signatur that returns bool
        """
        pubkey = RSA.importKey(pubkey)
        signer = PKCS1_v1_5.new(pubkey)
        digest = SHA256.new()
        digest.update(signature_string.encode("utf-8"))
        return signer.verify(digest, signature)


    @classmethod
    def parse_signature(
            cls,
            signature : str
    ) -> dict:
        """
        Parse signature string in headers
        """
        detail = {}
        for item in signature.split(','):
            name, value = item.split('=', 1)
            value = value.strip('"')
            detail[name.lower()] = value
        signature_details = {
            "headers": detail["headers"].split(),
            "signature": base64.b64decode(detail["signature"]),
            "algorithm": detail["algorithm"],
            "keyid": detail["keyid"],
        }
        return signature_details

    @classmethod
    def build_signature_string(
            cls,
            method : str,
            path : str,
            signed_headers : list,
            body_digest : str | None,
            headers,
    ) -> str:
        """
        Build signature string
        """
        signed_string = []
        for signed_header in signed_headers:
            if signed_header == "(request-target)":
                signed_string.append("(request-target): "
                                     + method.lower() + ' ' + path)
            elif signed_header == "digest" and body_digest:
                signed_string.append("digest: " + body_digest)
            else:
                signed_string.append(signed_header + ": "
                                     + headers[signed_header])

        return "\n".join(signed_string)
