#!/usr/bin/env python3
"""Build test fixture"""

import pytest
from app import app as flask_app


@pytest.fixture(name="app")
def fixture_app():
    """Build flask app"""
    yield flask_app


@pytest.fixture
def client(app):
    """Build test client"""
    return app.test_client()
