#!/usr/bin/env python3
"""Test App nodeinfo"""


def test_wellknow_nodeinfo(mocker, client):
    """Test app well-known nodeinfo ath."""
    mocker.patch("demo.config.BASE_URL", "foo")
    response = client.get("/.well-known/nodeinfo")
    assert response.json["links"][0]["href"] == "foo/nodeinfo/2.0"


def test_nodeinfo(client):
    """Test app nodeinfo."""
    response = client.get("/nodeinfo/2.0")
    assert response.json["software"]["name"] == "COSCUP-demo"
