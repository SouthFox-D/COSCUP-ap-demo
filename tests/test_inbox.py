#!/usr/bin/env python3
"""Test inbox route."""


def test_inbox_no_signature_key(client):
    """Test inbox"""
    response = client.post("/inbox",
                           data={"name": "Test"})
    assert response.status_code == 401


def test_inbox_signature_verify():
    from demo.httpsig import HttpSignature

    sig_str = """(request-target): post /inbox
user-agent: Fediverse Application
host: 127.0.0.1:5000
date: Tue, 22 Feb 2022 00:00:00 GMT
digest: SHA-256=pYx72lX8cxrG48M5a2YUZu1XsbfdI6bDm2QBnY3/ABo=
content-type: application/activity+json"""
    sig_header = 'keyId="http://127.0.0.1:8000#main-key",algorithm="rsa-sha256",headers="(request-target) user-agent host date digest content-type",signature="MxSPaNM2S1BnWlMVe0tPaTj4Z8nBSXHu5hvaQfN+Qo+LFVC8T/H8pLvE1DLxAE6IXyRg5xTkams9DS+O7GjEKotHoJuQxtpT5LzNzgliX3xyHd39Jy0jr2JOJmnlAPnUUeQDab3fkEWUkQROhcnL6rGOAGTasuie6Fhy+rNTcVh4HwkXt9uj321sa7kd0cWpsgtxzQyQ/2NRpfgxM9bEZCzddUVIIH1xng57GUiknkaDLhvn4OXWAgwh421i2AATB8eOGuOvR+LNmDofkK6HzWqru7W5cwzCOifCulJPAEN6rAhKOPbP76vKbaPlWcmsEgEOl8RLMjK2YjyWPupSCg=='
    sig_header = HttpSignature.parse_signature(sig_header)
    pub_key = """-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxTsTLCVt+jGSaVO6c+iW\nqOXsO45vB31twWzpDYg0yWcwX6u3sjc3ZyfmzJrmD8/x0xqBEpt2e9eUWzXsbOej\nmG8lBo0z5a7FLbui+MWH2ZwIPdjtbV/dhsWREfhBw5QAuPWM2dOmyJzyI1WOIfiy\n9bOO8ZYdMeBx/D8fPDk3LRHF6l5RmzQmCkcQdF1zAI4d4HmxIoUnhc9CsFBMLxb6\nI6TSswT+GAWF5jM11Yva5Fm8aaV444vk7wobG17g2BLCr2qmRQb7KT0vvVCoakUV\nTNE56Bh6aTEa/64xT6+vuX/Vk7IauetI9z0FlR8n2I1VONTi37DgAJUhMljDe+Z4\nwwIDAQAB\n-----END PUBLIC KEY-----"""

    is_verify = HttpSignature.verify_signature(
        sig_str,
        sig_header["signature"],
        pub_key,
    )

    assert is_verify == True
