#!/usr/bin/env python3

def test_request_example(client):
    response = client.get("/")
    assert b"Hello Fediverse!" in response.data
