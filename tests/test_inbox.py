#!/usr/bin/env python3
"""Test inbox route."""

def test_inbox_no_signature_key(client):
    """Test inbox"""
    response = client.post("/inbox",
                           data={"name": "Test"})
    assert response.status_code == 401
