#!/usr/bin/env python3
"""Test App index"""

def test_index_page(client):
    """Test index path"""
    response = client.get("/")
    assert b"Hello Fediverse!" in response.data
